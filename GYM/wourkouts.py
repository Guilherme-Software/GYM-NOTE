from flask import (
    Blueprint, flash, g, request, render_template, url_for, redirect
)
from werkzeug.exceptions import abort

from GYM.auth import login_required
from GYM.db import get_db
from markupsafe import escape

bp = Blueprint('wourkouts', __name__)


@bp.route('/workouts/<int:id>', methods=('GET', 'POST'))
@login_required
def user_wourkouts(id):
    db = get_db()
    wourkout = db.execute(
        'SELECT * FROM user WHERE id = ?', (id,)
    ).fetchone()
    return render_template("wourkouts.html", wourkout=wourkout)