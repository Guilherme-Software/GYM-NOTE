from flask import (
    Blueprint, flash, g, request, render_template, url_for, redirect
)
from werkzeug.exceptions import abort

from GYM.auth import login_required
from GYM.db import get_db

bp = Blueprint('notes', __name__)

@bp.route('/notes')
@login_required
def notes():
    return render_template("notes.html")
