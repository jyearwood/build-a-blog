from flask import Flask, request, redirect,render_template, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import cgi
import os

app = Flask(__name__)
app.config['DEBUG']= True
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://build-a-blog:buildablog@localhost:3307/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db= SQLAlchemy(app)


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(120))
    body = db.Column(db.Text)

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
    thisid = request.args.get("id")
    if thisid:
        blog = Blog.query.filter_by(id=thisid).first()
        return render_template("blogpost.html", blog=blog)
    else:
        blogs = Blog.query.order_by(Blog.id.desc()).all()
        return render_template("blog.html", blogs = blogs)


@app.route("/validate", methods=["POST", "GET"])
def validate():
    blogtitle = request.form["blogtitle"]
    blogtitle_error = ""
    blogbody = request.form["blogbody"]
    blogbody_error = ""

    if blogtitle == "":
        blogtitle_error = "Please enter a blog title"
        return render_template("newpost.html", blogtitle=blogtitle, blogbody=blogbody, blogtitle_error = blogtitle_error, blogbody_error = blogbody_error)

    if blogbody == "":
        blogbody_error = "Please make an entry"
        return render_template("newpost.html", blogtitle=blogtitle, blogbody=blogbody, blogtitle_error = blogtitle_error, blogbody_error = blogbody_error)

    elif request.method == "POST":
        newpost = Blog(blogtitle, blogbody)
        db.session.add(newpost)
        db.session.flush()
        db.session.commit()

    currentid = newpost.id
    return redirect("/blog?id={0}".format(currentid))



if __name__ == '__main__':
    app.run()