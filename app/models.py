from app import db, login
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin



class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True,unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True,unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    about_me: so.Mapped[Optional[str]] = so.mapped_column(sa.String(140))
    job_title: so.Mapped[Optional[str]] = so.mapped_column(sa.String(50))
    job_description: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))

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