import pymysql.cursors

import click
from flask import current_app, g
import pymysql.cursors

# get db
def get_db():
    if 'db' not in g:
        g.db = pymysql.connect(
            host = current_app.config['DB_HOST'],
            user = current_app.config['DB_USER'],
            password = current_app.config['DB_PASSWORD'],
            database = current_app.config['DB_NAME'],
            port = current_app.config['DB_PORT'],
            cursorclass=pymysql.cursors.DictCursor
        )
    return g.db

# close db
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


# init db
def init_db():
    db = get_db()
    with db.cursor() as cursor:
        with current_app.open_resource('schema.sql') as f:
            sql_commands = f.read().decode('utf8')
            for command in sql_commands.split(';'):
                command = command.strip()
                if command:
                    cursor.execute(command)


# command to create db
@click.command('init-db')
def init_db_command():
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
