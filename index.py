# -*- coding: utf-8 -*-

from __future__ import with_statement
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, _app_ctx_stack
import os
app = Flask(__name__)

# configuration
DATABASE = os.path.join(app.root_path, 'summer2014courses.db')
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'


# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)




def init_db():
    import LoadDatabase
    LoadDatabase.load_database()




def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    top = _app_ctx_stack.top
    if not hasattr(top, 'sqlite_db'):
        sqlite_db = sqlite3.connect(app.config['DATABASE'])
        sqlite_db.row_factory = sqlite3.Row
        top.sqlite_db = sqlite_db


    return top.sqlite_db




@app.teardown_appcontext
def close_db_connection(exception):
    """Closes the database again at the end of the request."""
    top = _app_ctx_stack.top
    if hasattr(top, 'sqlite_db'):
        top.sqlite_db.close()


@app.route('/Assignments')
def show_assignments():
    db = get_db()
    sql = '''SELECT * FROM {0} ORDER BY date'''.format("Assignments")
    cur = db.execute(sql)
    entries = cur.fetchall()
    return render_template('show_assignments.html',entries=entries)

@app.route('/Tests')
def show_tests():
    db = get_db()
    sql = '''SELECT * FROM {0} ORDER BY date'''.format("Tests")
    cur = db.execute(sql)
    entries = cur.fetchall()
    return render_template('show_tests.html',entries=entries)

@app.route('/Readings')
def show_readings():
    db = get_db()
    sql = '''SELECT * FROM {0} ORDER BY date'''.format("Readings")
    cur = db.execute(sql)
    entries = cur.fetchall()
    return render_template('show_readings.html',entries=entries)




if __name__ == '__main__':
    #init_db()
    app.run()
