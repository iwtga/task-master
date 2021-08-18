from flask import render_template, request
from taskmaster import app, db
from taskmaster.models import Todo

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = Todo(name=request.form['name'])
        db.session.add(task)
        db.session.commit()
    tasks = Todo.query.order_by(Todo.created).all()
    return render_template('index.html', tasks=tasks)