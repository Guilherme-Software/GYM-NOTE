from functools import wraps

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from GYM.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


# Register user Page
@bp.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form["nameform"]
        email = request.form["emailform"]
        password = request.form["passwordform"]
        confirm = request.form["confirmform"]
        db = get_db()
        error = None
        
        # possible errors
        if not name:
            error = "Name is required."
            
        elif not email:
            error = "E-mail is required."

        elif not password:
            error = "Password is required."

        elif confirm != password:
            error = "Passwords isn't the same."

        # Insert into db forms of the user.
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
                return redirect(url_for("auth.login"))


        flash(error)

    return render_template('auth/register.html')


# Login user Page.
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
        
        # erros
        if user is None:
            error = "Incorrect email."
        elif not check_password_hash(user['password'], password):
            error = "Incorrect password."

        # if error is None Log in user.
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


# logout user (not used)
@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))

# Usser login is required.
def login_required(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    return wrapped
