#author: Cheri Chen
import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://xxx:xxx@xxx:3306/"

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)


# each table in the database needs a class to be created for it
# identify all columns by name and data type
class City(db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    countrycode = db.Column(db.String, db.ForeignKey('country.code'))
    district = db.Column(db.String)
   

class Country(db.Model):
    __tablename__ = 'country'
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    continent = db.Column(db.String)
    gnp = db.Column(db.Float)
    
    
@app.route('/home',methods=['POST','GET'])
def home():
    if request.method=='POST':
        if request.values['send'] == 'send':
            cname = request.form["city"]
            icity = City.query.filter(City.name==cname)
            return render_template('home-1.html', city = icity)
    return render_template('home.html')    
 
@app.route('/overlay',methods=['POST','GET'])
def overlay():
    return render_template('overlay.html') 


if __name__ == "__main__":
    app.run(host='0.0.0.0',port='5000)
