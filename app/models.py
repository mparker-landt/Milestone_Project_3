from app import db


class Project(db.Model):
    # schema for the Project model
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(25), unique=True, nullable=False) # Unique = Can't be used again / nullable = Can't be left empty
    description = db.Column(db.Text, nullable=False)
    # primary_req = db.relationship("Primary_Req", backref="category", cascade="all, delete", lazy=True)
    # tests = db.relationship("Test", backref="project", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self #.title


# class Primary_Req(db.Model):
#     # schema for the Primary Reqs model
#     id = db.Column(db.Integer, primary_key=True)
#     description = db.Column(db.Text, nullable=False)
#     acceptance_rationale = db.Column(db.Text, default=False, nullable=False)
#     secondary_req = db.relationship("Secondary_Req", backref="project", cascade="all, delete", lazy=True)

#     def __repr__(self):
#         # __repr__ to represent itself in the form of a string
#         return self.id


# class Secondary_Req(db.Model):
#     # schema for the Secondary Reqs model
#     id = db.Column(db.Integer, primary_key=True)
#     description = db.Column(db.Text, nullable=False)
#     need = db.Column(db.Text, default=False, nullable=False)
#     acceptance_criteria = db.Column(db.Text, nullable=False)
#     changed = db.Column(db.Text, nullable=False)
#     tested = db.Column(db.Boolean, nullable=False)
#     test = db.relationship("Test", backref="primary_req", cascade="all, delete", lazy=True)

#     def __repr__(self):
#         # __repr__ to represent itself in the form of a string
#         return self.id


# class Test(db.Model):
#     # schema for the Test model
#     id = db.Column(db.Integer, primary_key=True)
#     description = db.Column(db.Text, nullable=False)
#     test_date = db.Column(db.Date, nullable=False)
#     reporter = db.Column(db.Text, nullable=False)
#     report = db.Column(db.Text, nullable=False)
#     category_id = db.Column(db.Integer, db.ForeignKey("project.id", ondelete="CASCADE"), nullable=False)

#     def __repr__(self):
#         # __repr__ to represent itself in the form of a string
#         return "#{0} - Description: {1} | Date: {2}".format(
#             self.id, self.description, self.test_date
#         )

