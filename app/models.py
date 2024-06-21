from app import db
# from flask_login import UserMixin


# schema for the Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(25), unique=True, nullable=False) # Unique = Can't be used again / nullable = Can't be left empty
    description = db.Column(db.Text, nullable=False)
    primary_reqs = db.relationship("Primary", backref="project", cascade="all, delete", lazy=True)
    tests = db.relationship("Test", backref="project", cascade="all, delete", lazy=True)

    def __repr__(self):
        return self.title

# schema for the Primary Reqs model
class Primary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    acceptance_rationale = db.Column(db.Text, default=False, nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey("project.id", ondelete="CASCADE"), nullable=False)
    secondary_reqs = db.relationship("Secondary", backref="primary", cascade="all, delete", lazy=True)

    def __repr__(self):
        return self.id

# schema for the Secondary Reqs model
class Secondary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    need = db.Column(db.Text, default=False, nullable=False)
    acceptance_criteria = db.Column(db.Text, nullable=False)
    changed = db.Column(db.Text, nullable=False)
    tested = db.Column(db.Boolean, nullable=False)
    primary_req_id = db.Column(db.Integer, db.ForeignKey("primary.id", ondelete="CASCADE"), nullable=False)
    # test = db.relationship("Test", backref="primary_req", cascade="all, delete", lazy=True)

    def __repr__(self):
        return self.id

# schema for the Test model
class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    test_date = db.Column(db.Date, nullable=False)
    reporter = db.Column(db.Text, nullable=False)
    report = db.Column(db.Text, nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey("project.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return "#{0} - Description: {1} | Date: {2}".format(
            self.id, self.description, self.test_date
        )

# __repr__ to represent itself in the form of a string