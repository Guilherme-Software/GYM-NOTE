from flask import (
    Blueprint, flash, g, request, render_template, url_for, redirect
)

from GYM.auth import login_required
from GYM.db import get_db

bp = Blueprint('workouts', __name__)


@bp.route('/workouts/<int:id>', methods=('GET', 'POST'))
@login_required
def user_workouts(id):
    db = get_db()
    workout = db.execute(
        'SELECT * FROM user WHERE id = ?', (id,)
    ).fetchone()

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    if request.method == 'POST':
        for day in days:
            work = request.form[F'workout_{day.lower()}']
            db = get_db()
            error = None

            if not work:
                error = "Name of the Workout is required"

            if error is None:
                try:
                    db.execute(
                        "SELECT id"
                        "FROM user"
                        "JOIN workout"
                        "ON user.id = workout.id"
                        "iNSERT INTO workout(workout_({ day }) VALUES (?)",
                        (work,)
                    )
                    db.commit() 
                except db.IntegrityError:
                    error = "something went wrong!"
                else:
                    return redirect(url_for('notes.user_notes', id=user['id']))

            flash(error)

    return render_template("workouts.html", days=days)