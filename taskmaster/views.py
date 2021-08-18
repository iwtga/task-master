from flask import render_template
from taskmaster import app

@app.route('/')
def index():
    return "Hello"