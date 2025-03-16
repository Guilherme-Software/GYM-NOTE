from flask import (
    Blueprint, flash, g, request, render_template, url_for, redirect
)

from GYM.auth import login_required
from GYM.db import get_db

bp = Blueprint('Notes', __name__)