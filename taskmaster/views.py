from flask import render_template, request, redirect
from werkzeug.utils import redirect
from taskmaster import app, db
from taskmaster.models import Todo
from taskmaster.forms import LoginForm, SignupForm
from flask_login import login_required, current_user, login_user, logout_user

@app.route('/', methods=["GET", "POST"])
@login_required
def index():
    if request.method == "POST":
        try:
            task = Todo(name=request.form['name'])
            db.session.add(task)
            db.session.commit()
        except:
            return "Could not add task"
    tasks = Todo.query.order_by(Todo.created).all()
    return render_template('index.html', tasks=tasks)

@app.route('/register', methods=["GET", "POST"])
def register():
    form = SignupForm()
    return render_template("register.html", form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("login.html", form=form)

@app.route('/delete/<int:id>')
@login_required
def delete(id):
    task = Todo.query.filter_by(id=id).first()
    try:
        db.session.delete(task)
        db.session.commit()
        return redirect('/')
    except:
        return "Cannot Delete Record"

@app.route('/update/<int:id>', methods=["GET", "POST"])
@login_required
def update(id):
    task = Todo.query.filter_by(id=id).first()
    if request.method == "POST":
        task.name = request.form['name']
        db.session.commit()
        return redirect('/')
    return render_template('update.html', task=task)