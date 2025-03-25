from flask import (
    Blueprint, flash, g, request, render_template, url_for, redirect
)
from werkzeug.exceptions import abort

from GYM.auth import login_required
from GYM.db import get_db
from markupsafe import escape

bp = Blueprint('workouts', __name__)


@bp.route('/workouts/<int:id>', methods=('GET', 'POST'))
@login_required
def user_workouts(id):
    db = get_db()
    workout = db.execute(
        'SELECT * FROM user WHERE id = ?', (id,)
    ).fetchone()

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return render_template("workouts.html", workout=workout, days=days)