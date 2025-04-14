<<<<<<< HEAD
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
            a = [f"exercise_{number}"]
            b = [f"sets_{number}"]
            c = [f"kg_{number}"]
            d = [f"notes_{number}"]
            value = (a, b, c, d)
            if value is None:
                error = f"Name of the {a, b, c, d} is required to continue."
                break
            
            if error:
                flash(error)

            else:
            #see if gonna insert or update
                search = db.execute(
                    "SELECT * from notes WHERE user_id = ?",
                    (id,)
                ).fetchone()

            

        


        





    return render_template("notes.html", note=note, numbers=numbers)
=======
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
        'SELECT * FROM user WHERE id = ?',
        (id,)
    ).fetchone()

    numbers = range(1, 11)

    if request.method == "POST":
        error = None
        
        for number in numbers:
            x = [f"exercise_{number}"]
            y = [f"kg_{number}"]
            z = [f"notes_{number}"]

        #see if gonna insert or update
        search = db.execute(
            "SELECT * from notes WHERE id = ?",
            (id,)
        ).fetchone()

        


        





    return render_template("notes.html", note=note, numbers=numbers)
>>>>>>> 43d1475e80626c81c539e548dce0b0f7a9df358c
