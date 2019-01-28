#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "kmeiklejohn"
__version__ = "0.1.0"


from flask import Flask, render_template
from tinydb import TinyDB, Query, where
from jinja2 import Template
import random

app = Flask(__name__)
db = TinyDB('db.json')
Recipes = Query()

def init_db():
    """returns all the content of the database"""
    return db.all()
    

@app.route('/')
@app.route('/index')
def index():
    """Starts flask and sets up the html template"""
    one_recipe = random_query()
    return render_template('index.html', title="Recipe", recipe=one_recipe)

def random_query():
    """Returns a random recipe from the databases"""
    db_list = db.search(where("name").any(Recipes))
    random_item = random.sample(db_list,1)
    print(random_item[0])
    return random_item[0]

def main():
    """ Main entry point of the app """
    if not db:
        init_db()
    random_query()
    index()
    print("serving on localhost:5000")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
