# My message
from flask import Flask, render_template, g
import sqlite3

def open_db():
    if 'db' not in g:
        g.db = sqlite3.connect("blog.db")
    return g.db

def close_db():
    db = g.pop('db', None)
    if db is not None:
        db.close()

app = Flask(__name__)

def index():
    db = open_db()
    results = db.execute("SELECT * FROM users").fetchall()
    return render_template("index.html", data = results)

app.add_url_rule("/", "index", index)
