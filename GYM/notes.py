from flask import (
    Blueprint, flash, request, render_template, redirect, url_for, g, Response
)
from GYM.auth import login_required
from GYM.db import get_db

bp = Blueprint('notes', __name__)

@bp.route('/notes/<day>/<int:id>', methods=('GET', 'POST'))
@login_required
def user_notes(day, id):
    db = get_db()
    
    # Get all notes for the user on the specified day
    note = db.execute(
        """SELECT u.id AS user_id, n.*
        FROM user u
        JOIN notes n ON u.id = n.user_id
        WHERE u.id = ? AND n.day = ?""",
        (id, day)
    ).fetchall()

    # Organize notes in a dictionary by position
    note_dict = {note['position']: note for note in note}

    numbers = range(1, 11)

    days_allowed = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')

    if day not in days_allowed:
        return redirect(url_for('auth.login'))

    if id != g.user["id"]:
        return redirect(url_for('auth.login'))

    if request.method == "POST":
        error = None
        
        # Iterate through numbers 1-10 to check and save the workout details
        for number in numbers:
            exercise = request.form.get(f"exercise_{number}")
            sets = request.form.get(f"sets_{number}")
            kg = request.form.get(f"kg_{number}")
            notes_text = request.form.get(f"notes_{number}")

            # Check if there is an existing note for this exercise
            existing_note = db.execute(
                "SELECT * FROM notes WHERE user_id = ? AND day = ? AND position = ?",
                (id, day, number)
            ).fetchone()

            # If the note doesn't exist, insert it
            if existing_note is None:
                db.execute(
                    "INSERT INTO notes (user_id, day, position, exercise, sets, kg, notes) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?)", 
                    (id, day, number, exercise, sets, kg, notes_text)
                )

            # If the note exists, update it
            else:
                db.execute(
                    """
                    UPDATE notes
                    SET exercise = ?, 
                    sets = ?, 
                    kg = ?, 
                    notes = ?
                    WHERE user_id = ? AND day = ? AND position = ?
                    """,
                    (exercise, sets, kg, notes_text, id, day, number)
                )
            db.commit()

        # If there is an error, flash the message
        if error is not None:
            flash(error)
        
        else:
            response = redirect(url_for('notes.user_notes', day=day, id=id))
            response.cache_control.no_cache = True
            return response

    return render_template("notes.html", note_dict=note_dict, numbers=numbers, day=day)
