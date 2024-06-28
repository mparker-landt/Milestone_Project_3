from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login


class User(UserMixin, db.Model):
    """Schema for a User."""
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True,unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True,unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    about_me: so.Mapped[Optional[str]] = so.mapped_column(sa.String(140))
    job_title: so.Mapped[Optional[str]] = so.mapped_column(sa.String(50))
    job_description: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    def __repr__(self): # __repr__ to represent itself in the form of a string
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    """Loads user detail to remember login."""
    return db.session.get(User, int(id))


class Project(db.Model):
    """Schema for the Project model."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(25), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    primary_reqs = db.relationship("Primary", backref="project", cascade="all, delete", lazy=True)

    def __repr__(self):
        return self.title


class Primary(db.Model):
    """Schema for the Primary Reqs model."""
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    acceptance_rationale = db.Column(db.Text, default=False, nullable=False)
    project_id = db.Column(
        db.Integer, db.ForeignKey("project.id", ondelete="CASCADE"), nullable=False
    )

    def __repr__(self):
        return self.id
