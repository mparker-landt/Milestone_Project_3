from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from app import app, db
from app.models import Project, Test, Primary, Secondary


# Path for Homepage/Dashboard. Displays available projects in a grid pattern
@app.route('/')
@app.route('/index')
def index():
    projects = list(Project.query.order_by(Project.id).all())
    return render_template('index.html', projects=projects)

@app.route("/add_project", methods=["GET", "POST"])
def add_project():
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
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for("index"))


#####################################################################################################################


# Path for project Requirements Page. 
# Displays primary and related secondary requirements of a specifically chosen project 
# Displays in a table pattern
@app.route("/project_reqs")
def project_reqs():
    projects = list(Project.query.order_by(Project.id).all())
    primarys = list(Primary.query.order_by(Primary.id).all())
    secondarys = list(Secondary.query.order_by(Secondary.id).all())
    return render_template("project_reqs.html", projects=projects, primarys=primarys, secondarys=secondarys)

@app.route("/add_primary", methods=["GET", "POST"])
def add_primary():
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
    primary = Primary.query.get_or_404(primary_id)
    db.session.delete(primary)
    db.session.commit()
    return redirect(url_for("project_reqs"))


#####################################################################################################################


# Path for Tests Page. Displays available test of a specifically chosen project in a grid pattern
@app.route("/test_reports")
def test_reports():
    projects = list(Project.query.order_by(Project.id).all())
    tests = list(Test.query.order_by(Test.id).all())
    return render_template("test_reports.html", projects=projects, tests=tests)

@app.route("/add_test", methods=["GET", "POST"])
def add_test():
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
    test = Test.query.get_or_404(test_id)
    db.session.delete(test)
    db.session.commit()
    return redirect(url_for("test_reports"))


