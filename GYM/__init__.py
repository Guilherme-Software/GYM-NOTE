<<<<<<< HEAD
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

    #A PP
    return app
=======
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

    #A PP
    return app
>>>>>>> 43d1475e80626c81c539e548dce0b0f7a9df358c
