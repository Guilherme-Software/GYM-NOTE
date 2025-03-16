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
    
    @app.route("/")
    def home():
        return redirect(url_for('auth.login'))

    @app.route("/notes", methods=['GET'])
    def note():
        return render_template("notes.html")


    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import notes
    app.register_blueprint(notes.bp)
    app.add_url_rule("/note", endpoint='notes')

    return app
