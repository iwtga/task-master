from flask import render_template, request, redirect, flash
from flask.helpers import url_for
from taskmaster import app, db
from taskmaster.models import Todo, User
from taskmaster.forms import LoginForm, SignupForm, TaskForm, UpdateForm
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/', methods=["GET", "POST"])
@login_required
def index():
    form = TaskForm()
    if form.validate_on_submit():
        try:
            task = Todo(name=form.name.data, owner=current_user)
            db.session.add(task)
            db.session.commit()
            flash("Task Added Successfully", category="info")
            return redirect(url_for("index"))
        except Exception as e:
            print(e)
            flash("Could Not Add Task!", category="error")
            return redirect(url_for('index'))
    page = request.args.get("page", 1, int)
    tasks = Todo.query.filter_by(owner=current_user).paginate(per_page=10, page=page)
    username = current_user.username
    return render_template('index.html', tasks=tasks, username=username, form=form)

@app.route('/register', methods=["GET", "POST"])
def register():
    form = SignupForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        hashed_password = generate_password_hash(form.password.data)
        if not User.query.filter_by(email=email).first():
            if not User.query.filter_by(username=username).first():
                try:
                    user = User(email=email, username=username, password=hashed_password)
                    db.session.add(user)
                    db.session.commit()
                    flash("User Registered Successfully! You can log in now!", category="info")
                    return redirect(url_for('login'))
                except Exception as e:
                    print(e)
                    flash("Something went wrong, while adding user!", category="error")
            else:
                flash("Username Already Taken!", category="error")
        else:
            flash("Email Already Taken!", category="error")
    return render_template("register.html", form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                next = request.args.get('next')
                flash("User Logged in successfully!", category="info")
                return redirect(next or url_for('index'))
        flash("Username or Password Incorrect", category="error")
    return render_template("login.html", form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out successfully", category="info")
    return redirect(url_for('login'))

@app.route('/delete/<int:id>')
@login_required
def delete(id):
    task = Todo.query.filter_by(id=id).first()
    try:
        db.session.delete(task)
        db.session.commit()
        flash("Task Deleted Successfully!", category="info")
    except Exception as e:
        print(e)
        flash("Cannot Delete Task!", category="error")
    return redirect(url_for("index"))

@app.route('/update/<int:id>', methods=["GET", "POST"])
@login_required
def update(id):
    form = UpdateForm()
    task = Todo.query.filter_by(id=id).first()
    if form.validate_on_submit():
        task.name = form.name.data
        try:
            db.session.commit()
            flash("Task Updated Successfully!")
            return redirect(url_for('index'))
        except Exception as e:
            print(e)
            flash("Could not update Task!")
    return render_template('update.html', task=task, form=form)