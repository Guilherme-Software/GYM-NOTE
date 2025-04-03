from flask import (
    Blueprint, flash, g, request, render_template, url_for, redirect, session
)

from GYM.auth import login_required
from GYM.db import get_db

bp = Blueprint('workouts', __name__)


@bp.route('/workouts/<int:id>', methods=('GET', 'POST'))
@login_required
def user_workouts(id):
    db = get_db()
    workout = db.execute(
        """SELECT u.id AS user_id, w.*
            FROM user u
            JOIN workout w ON u.id = w.id
            WHERE u.id = ?""",
        (id,)
    ).fetchone()

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    if request.method == 'POST':
        for day in days:
            work = request.form[f'workout_{day.lower()}']
            error = None

            if not work:
                error = "Name of the Workout is required"
            
            if error is not None:
                flash(error)

            else:
                db = get_db()
                db.execute(
                    "iNSERT INTO workout (id, workout_monday, workout_tuesday, workout_wednesday, workout_thursday, workout_friday, workout_saturday, workout_sunday)"
                    "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    (id),
                    request.form.get('workout_monday'),
                    request.form.get('workout_tuesday'),
                    request.form.get('workout_wednesday'),
                    request.form.get('workout_thursday'),
                    request.form.get('workout_friday'),
                    request.form.get('workout_saturday'),
                    request.form.get('workout_sunday')
                )
                    )
                db.commit()
                return redirect(url_for('notes.user_notes', id=workout["user_id"]))

            flash(error)

    return render_template("workouts.html", days=days, workout=workout)