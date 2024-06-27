from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import sqlalchemy as sa
from app import app, db
from app.forms import LoginForm, RegistrationForm, EditProfileForm
from app.models import Project, Test, Primary, Secondary, User
from flask_login import current_user, login_user, logout_user, login_required
from urllib.parse import urlsplit


@app.route('/')
@app.route('/index')
def index():
    """Path for Homepage/Dashboard. Displays available projects in a grid pattern."""
    projects = list(Project.query.order_by(Project.id).all())
    return render_template('index.html', projects=projects)


@app.route("/add_project", methods=["GET", "POST"])
@login_required
def add_project():
    """Path for adding a project to the database. Redirects to homepage."""
    if request.method == "POST":
        project = Project(
            title=request.form.get("title"),
            description=request.form.get("description")
        )
        db.session.add(project)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template(url_for("index"))


@app.route("/edit_project/<int:project_id>", methods=["GET", "POST"])
def edit_project(project_id):
    """Path for editing a project in the database. Redirects to homepage."""
    project = Project.query.get_or_404(project_id)
    if request.method == "POST":
        project = Project(
            title=request.form.get("title"),
            description=request.form.get("description")
        )
        db.session.commit()
        return redirect(url_for("index"))
    return render_template(url_for("index"), project=project)


@app.route("/delete_project/<int:project_id>")
def delete_project(project_id):
    """Path for deleting a project from the database. Redirects to homepage."""
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/project_reqs/<int:project_id>")
def project_reqs(project_id):
    """Path for Requirements Page. Displays project requirements in a table."""
    projects = list(Project.query.order_by(Project.id).all())
    # primarys = list(Primary.query.order_by(Primary.id).all())
    primarys = Primary.query.filter_by(project_id=Primary.project_id).all()
    secondarys = list(Secondary.query.order_by(Secondary.id).all())
    return render_template("project_reqs.html", projects=projects, primarys=primarys, project_id=project_id)


@app.route("/primary_reqs", methods=["POST"])
def primary_reqs():
    project_id = request.form.get('project_id')
    primarys = Primary.query.filter_by(project_id=project_id).all()
    primarys_list = [p.serialize() for p in primarys]  # assuming you have a serialize method
    return jsonify({'primarys': primarys_list})


@app.route("/add_primary", methods=["GET", "POST"])
def add_primary():
    """Path for adding a requirement to the database. Redirects to Project Requirements page."""
    projects = list(Project.query.order_by(Project.title).all())
    if request.method == "POST":
        primary = Primary(
            description=request.form.get("description"),
            acceptance_rationale=request.form.get("acceptance_rationale"),
            project_id=request.form.get("project_id")
        )
        db.session.add(primary)
        db.session.commit()
        return redirect(url_for("project_reqs"))
    return render_template(url_for("project_reqs"), projects=projects)


@app.route("/delete_primary/<int:primary_id>")
def delete_primary(primary_id):
    """Path for deleting a requirement from the database. Redirects to Project Requirements page."""
    primary = Primary.query.get_or_404(primary_id)
    db.session.delete(primary)
    db.session.commit()
    return redirect(url_for("project_reqs"))


@app.route("/test_reports")
def test_reports():
    """Path for Tests Page. Displays available test of a specifically chosen project in a grid pattern."""
    projects = list(Project.query.order_by(Project.id).all())
    tests = list(Test.query.order_by(Test.id).all())
    return render_template("test_reports.html", projects=projects, tests=tests)


@app.route("/add_test", methods=["GET", "POST"])
def add_test():
    """Path for adding a test report to the database. Redirects to Test Reports page."""
    projects = list(Project.query.order_by(Project.title).all())
    if request.method == "POST":
        test = Test(
            description=request.form.get("description"),
            test_date=request.form.get("test_date"),
            reporter=bool(True if request.form.get("reporter") else False),
            report=request.form.get("report"),
            project_id=request.form.get("project_id")
        )
        db.session.add(test)
        db.session.commit()
        return redirect(url_for("test_reports"))
    return render_template(url_for("test_reports"), projects=projects)


@app.route("/delete_test/<int:test_id>")
def delete_test(test_id):
    """Path for deleting a test report from the database. Redirects to Test Reports page."""
    test = Test.query.get_or_404(test_id)
    db.session.delete(test)
    db.session.commit()
    return redirect(url_for("test_reports"))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Path for login page for a user."""
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('user_login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    """Path to logout for a user."""
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Path for user to register to use the site."""
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('user_register.html', title='Register', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    """Path for User Profile page."""
    user = db.first_or_404(sa.select(User).where(User.username == username))
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user_profile.html', user=user, posts=posts)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    """Path for editing a User Profile page."""
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        current_user.job_title = form.job_title.data
        current_user.job_description = form.job_description.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
        form.job_title.data = current_user.job_title
        form.job_description.data = current_user.job_description
    return render_template('user_editprofile.html', title='Edit Profile', form=form)
