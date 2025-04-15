from flask import (
    Blueprint, flash, g, request, render_template, url_for, redirect
)
from werkzeug.exceptions import abort
from GYM.auth import login_required
from GYM.db import get_db
from markupsafe import escape

bp = Blueprint('notes', __name__)


@bp.route('/notes/<day>/<int:id>', methods=('GET', 'POST'))
@login_required
def user_notes(day, id):
    db = get_db()
    note = db.execute(
            """SELECT u.id AS user_id, n.*
            FROM user u
            JOIN notes n ON u.id = n.user_id
            WHERE u.id = ?""",
        (id,)
    ).fetchone()

    numbers = range(1, 11)

    if request.method == "POST":
    
        error = None
        
        #errors
        for number in numbers:

            exercise = request.form.get(f"exercise_{number}")
            sets = request.form.get(f"sets_{number}")
            kg = request.form.get(f"kg_{number}")
            notes = request.form.get(f"notes_{number}")

            if not exercise:
                error = f"Name of the {exercise} is required to continue."
                break
            
            if error:
                flash(error)

            else:
            #see if gonna insert or update
                search = db.execute(
                    "SELECT * from notes WHERE user_id = ?",
                    (id,)
                ).fetchone()

                if search is None:
                    db.execute(
                        "INSERT INTO notes (user_id, exercise, sets, kg, notes)"
                        "VALUES( ?, ?, ?, ?, ?)",
                        (id, exercise, sets, kg, notes)
                    )
                    db.commit()

                else:
                    db.execute(
                        """
                        UPDATE notes
                            SET exercise = ?,
                            sets = ?,
                            kg = ?,
                            notes = ?
                        WHERE user_id = ?
                        """,
                        (exercise, sets, kg, notes, id)
                    )
                    db.commit()


    return render_template("notes.html", note=note, numbers=numbers)