from flask import render_template, request, redirect, flash
from flask.helpers import url_for
from taskmaster import app, db
from taskmaster.models import Todo, User
from taskmaster.forms import LoginForm, SignupForm
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

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
    username = current_user.username
    return render_template('index.html', tasks=tasks, username=username)

@app.route('/register', methods=["GET", "POST"])
def register():
    form = SignupForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.username.data
        hashed_password = generate_password_hash(form.password.data)
        if not User.query.filter_by(email=email).first():
            if not User.query.filter_by(username=username).first():
                try:
                    user = User(email=email, username=username, password=hashed_password)
                    db.session.add(user)
                    db.session.commit()
                    flash("User Registered Successfully! You can log in now!")
                    return redirect(url_for('login'))
                except:
                    flash("Something went wrong, while adding user!")
            else:
                flash("Username Already Taken!")
        else:
            flash("Email Already Taken!")
    return render_template("register.html", form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.passworc, form.password.data):
                login_user(user, remember=form.remember.data)
                next = request.args.get('next')
                return redirect(next or url_for('index'))
        flash("Username or Password Incorrect")
    return render_template("login.html", form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

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