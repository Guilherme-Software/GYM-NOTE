from functools import wraps

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from GYM.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form["nameform"]
        email = request.form["emailform"]
        password = request.form["passwordform"]
        db = get_db()
        error = None
        
        if not name:
            error = "Name is required."
        elif not email:
            error = "E-mail is required."
        elif not password:
            error = "Password is required."

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user(name, email, password) VALUES (?, ?, ?);",
                    (name, email, generate_password_hash(password)),
                )
                db.commit()

            except db.IntegrityError:
                error = f"E-mail {email} is already registered."
            else:
                try:
                    db.execute(
                    "INSERT INTO workout(email) VALUES (?);",
                    (email,),
                )
                    db.commit()
                    return redirect(url_for("auth.login"))
                except Exception as E:
                    print("something went wrong: {E}")

        flash(error)

    return render_template('auth/register.html')


@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        email = request.form["emailform"]
        password = request.form["passwordform"]
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE email = ?', (email,)
        ).fetchone()

        if user is None:
            error = "Incorrect email."
        elif not check_password_hash(user['password'], password):
            error = "Incorrect password."

        if error is None:
            session.clear()
            session["user_id"] = user["id"]
            return redirect(url_for("workouts.user_workouts", id=user['id']))
        
        flash(error)

    return render_template("/auth/login.html")


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")
    if user_id is None:
        g.user = None   
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))


def login_required(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    return wrapped


#FAZER UM SESSION CLEAR DPS
