from flask import Flask, request , jsonify
from flask_sqlalchemy import SQLAlchemy


 
app = Flask(__name__)
db=SQLAlchemy(app) 

app.config.from_pyfile('config/config.ini')

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@localhost:5432/user'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True