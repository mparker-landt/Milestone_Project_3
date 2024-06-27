from flask import render_template
from app import app, db


@app.errorhandler(404)
def not_found_error(error):
    """Path for HTTP Status Code 404 - Not found."""
    return render_template('errorpage_404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    """Path for HTTP Status Code 500 - Internal server error."""
    db.session.rollback()
    return render_template('errorpage_500.html'), 500