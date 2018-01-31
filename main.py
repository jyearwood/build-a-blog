from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import cgi
import os

app = Flask(__name__)
app.config['DEBUG']= True
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://build-a-blog:buildablog@localhost:3307/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True


db = SQLAlchemy(app)


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(120))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime(), default=datetime.utcnow, index=True)

    def __init__(self, title, body):
        self.title = title
        self.body = body


@app.route("/", methods = ["POST", "GET"])
def index():
    blogs = Blog.query.order_by(Blog.id.desc()).all()
    return render_template("blog.html", blogs = blogs)


@app.route("/newpost", methods = ["POST", "GET"])
def newpost():
    return render_template("newpost.html")

@app.route("/blog", methods = ["POST", "GET"])
def blog():


@app.route("/validate", methods=["POST", "GET"])
def validate():



if __name__ == '__main__':
app.run()