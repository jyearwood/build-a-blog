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


class Task(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    def __init__(self,name):
        slef.name = name 


if __name__=='__main__':
    app.run()