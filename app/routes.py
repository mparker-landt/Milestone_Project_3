from urllib.parse import urlsplit
from flask import render_template, request, redirect, url_for, flash, jsonify
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
def add_project():
    """Path for editing a User Profile page."""
    if request.method == "POST":
        project = Project(
            title=request.form.get("project_title"),
            description=request.form.get("project_description")
        )
        db.session.add(project)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("project_add.html")


@app.route("/project_edit/<int:project_id>", methods=["GET", "POST"])
def edit_project(project_id):
    """Path for editing a User Profile page."""
    project = Project.query.get_or_404(project_id)
    if request.method == "POST":
        project.title = request.form.get("project_title")
        project.description = request.form.get("project_description")
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("project_edit.html", project=project)


@app.route("/delete_project/<int:project_id>")
def delete_project(project_id):
    """Path for deleting a project from the database. Redirects to homepage."""
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/requirements/<int:project_id>")
def requirements(project_id):
    """Path for Requirements Page. Displays project requirements in a table."""
    projects = list(Project.query.order_by(Project.id).all())
    # primarys = list(Primary.query.order_by(Primary.id).all())
    primarys = Primary.query.filter_by(project_id=Primary.project_id).all()
    return render_template(
        "requirements.html", projects=projects, primarys=primarys, project_id=project_id
    )


@app.route("/primary_reqs", methods=["POST"])
def primary_reqs():
    """To be filled."""
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
        return redirect(url_for("requirements"))
    return render_template(url_for("requirements"), projects=projects)


@app.route("/delete_primary/<int:primary_id>")
def delete_primary(primary_id):
    """Path for deleting a requirement from the database. Redirects to Project Requirements page."""
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
