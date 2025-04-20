import os
from dotenv import load_dotenv
from flask import render_template, request, redirect, url_for
from flask import Flask

load_dotenv()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY= os.getenv('SECRET_KEY'),
        DATABASE=os.path.join(app.instance_path, 'GYM.sqlite'),
    )
    
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    with app.app_context():
        try:
            from .db import init_db
            init_db()
        except Exception as e:
            print("Error initizaling the db.")

    # go to login page
    @app.route("/")
    def home():
        return redirect(url_for('auth.login'))

    # db init
    from . import db
    db.init_app(app)

    # authentication page (login/register)
    from . import auth
    app.register_blueprint(auth.bp)
    
    # workouts page
    from . import workouts
    app.register_blueprint(workouts.bp)

    # notes page
    from . import notes
    app.register_blueprint(notes.bp)

    # APP
    return app

app = create_app()
