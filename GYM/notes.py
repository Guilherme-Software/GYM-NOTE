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
        'SELECT * FROM user WHERE id = ?', (id,)
    ).fetchone()

    numbers = range(1, 11)

    if request.method == "POST":
        error = None
        
        for number in numbers:
            x = [f"exercise_{number}"]
            y = [f"kg_{number}"]
            z = [f"notes_{number}"]
            if (x, y, z) is None:
                error = "Put the workout"
                break

            if error:
                flash(error)





    return render_template("notes.html", note=note, numbers=numbers)
