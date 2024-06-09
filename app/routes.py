from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from app import app, db
from app.models import Project #, Primary_Req, Secondary_Req, Test


# HOME
# NEW TASK
# CATOGERIES


# Connect to the database
# conn = psycopg2.connect(database="flask_db", user="postgres", password="rootuser", host="localhost", port="5432")

# create a cursor
# cur = conn.cursor()

# if you already have any table or not id doesnt matter this
# will create a products table for you.
# cur.execute( '''CREATE TABLE IF NOT EXISTS products (id serial PRIMARY KEY, name varchar(100), price float);''')

# Insert some data into the table
# cur.execute( '''INSERT INTO products (name, price) VALUES ('Apple', 1.99), ('Orange', 0.99), ('Banana', 0.59);''')

# commit the changes
# conn.commit()

# close the cursor and connection
# cur.close()
# conn.close()


# Path for Homepage/Dashboard. Displays available projects in a grid pattern
@app.route('/')
@app.route('/index')
def index():
    # Connect to the database 
    # conn = psycopg2.connect(database="flask_db", user="postgres", password="rootuser", host="localhost", port="5432")
  
    # create a cursor 
    # cur = conn.cursor()
  
    # Select all products from the table 
    # cur.execute('''SELECT * FROM products''')
  
    # Fetch the data 
    # data = cur.fetchall()
  
    # close the cursor and connection 
    # cur.close()
    # conn.close()
  
    # projects = list(Project.query.order_by(Project.id).all())
    return render_template('index.html')

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


# Path for project Requirements Page. 
# Displays primary and related secondary requirements of a specifically chosen project 
# Displays in a table pattern
@app.route("/project_reqs")
def project_reqs():
    return render_template("project_reqs.html")

# Path for Tests Page. Displays available test of a specifically chosen project in a grid pattern
@app.route("/test_reports")
def test_reports():
    return render_template("test_reports.html")


@app.route("/delete_project/<int:project_id>")
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for("/"))


# @app.route('/create', methods=['POST'])
# def create():
#     conn = psycopg2.connect(database="flask_db", user="postgres", password="rootuser", host="localhost", port="5432")
#     cur = conn.cursor()
  
#     # Get the data from the form
#     name = request.form['name']
#     price = request.form['price']
  
#     # Insert the data into the table
#     cur.execute( '''INSERT INTO products (name, price) VALUES (%s, %s)''', (name, price))
  
#     # commit the changes
#     conn.commit()
  
#     # close the cursor and connection
#     cur.close()
#     conn.close()
  
#     return redirect(url_for('index'))

# @app.route('/update', methods=['POST']) 
# def update(): 
#     conn = psycopg2.connect(database="flask_db", user="postgres", password="rootuser", host="localhost", port="5432") 
#     cur = conn.cursor() 
  
#     # Get the data from the form 
#     name = request.form['name'] 
#     price = request.form['price'] 
#     id = request.form['id'] 
  
#     # Update the data in the table 
#     cur.execute( '''UPDATE products SET name=%s,price=%s WHERE id=%s''', (name, price, id)) 
  
#     # commit the changes 
#     conn.commit() 
#     return redirect(url_for('index')) 

# @app.route('/delete', methods=['POST'])
# def delete():
#     conn = psycopg2.connect(database="flask_db", user="postgres", password="rootuser", host="localhost", port="5432")
#     cur = conn.cursor()
  
#     # Get the data from the form
#     id = request.form['id']
  
#     # Delete the data from the table
#     cur.execute('''DELETE FROM products WHERE id=%s''', (id,))
  
#     # commit the changes
#     conn.commit()
  
#     # close the cursor and connection
#     cur.close()
#     conn.close()
  
#     return redirect(url_for('index'))


