from urllib.parse import urlsplit
from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import Project, Primary, User


@app.route('/')
@app.route('/index')
def index():
    """Path for Homepage/Dashboard. Displays available projects in a grid pattern."""
    projects = list(Project.query.order_by(Project.id).all())
    project_id = 0
    return render_template('index.html', projects=projects, project_id=project_id)


@app.route("/project_add", methods=["GET", "POST"])
@login_required
def add_project():
    """Path for adding a Project page. Redirects to homepage."""
    if request.method == "POST":
        project = Project(
            title=request.form.get("project_title"),
            description=request.form.get("project_description")
        )
        db.session.add(project)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("project-add.html")


@app.route("/project_edit/<int:project_id>", methods=["GET", "POST"])
@login_required
def edit_project(project_id):
    """Path for editing a User Profile page. Redirects to homepage."""
    project = Project.query.get_or_404(project_id)
    if request.method == "POST":
        project.title = request.form.get("project_title")
        project.description = request.form.get("project_description")
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("project-edit.html", project=project)


@app.route("/delete_project/<int:project_id>")
@login_required
def delete_project(project_id):
    """Path for deleting a project from the database. Redirects to homepage."""
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/requirements")
def requirements():
    """Path for Requirements Page. Displays project requirements in a table."""
    projects = list(Project.query.order_by(Project.id).all())
    primarys = list(Primary.query.order_by(Primary.id).all())
    return render_template(
        "requirements.html", projects=projects, primarys=primarys)


@app.route("/primary_add", methods=["GET", "POST"])
@login_required
def add_requirement():
    """Path for adding a Requirement page."""
    projects = list(Project.query.order_by(Project.id).all())
    if request.method == "POST":
        primary = Primary(
            description=request.form.get("req_description"),
            acceptance_rationale=request.form.get("req_acceptance_rationale"),
            project_id=request.form.get("req_project")
        )
        db.session.add(primary)
        db.session.commit()
        return redirect(url_for("requirements"))
    return render_template("requirements-add.html", projects=projects)


@app.route("/primary_edit/<int:primary_id>", methods=["GET", "POST"])
@login_required
def edit_requirement(primary_id):
    """Path for editing a Requirement page."""
    projects = list(Project.query.order_by(Project.id).all())
    primary = Primary.query.get_or_404(primary_id)
    if request.method == "POST":
        primary.description = request.form.get("req_description")
        primary.acceptance_rationale = request.form.get("req_acceptance_rationale")
        primary.project_id = request.form.get("req_project")
        db.session.commit()
        return redirect(url_for("requirements"))
    return render_template("requirements-edit.html", primary=primary, projects=projects)


@app.route("/delete_primary/<int:primary_id>")
@login_required
def delete_primary(primary_id):
    """Path for deleting a requirement from the database."""
    primary = Primary.query.get_or_404(primary_id)
    db.session.delete(primary)
    db.session.commit()
    return redirect(url_for("requirements"))


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
    return render_template('user-login.html', title='Sign In', form=form)


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
    return render_template('user-register.html', title='Register', form=form)
