from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
import os

uri = 'postgres://ozqqhdmuqezsca:a220c425e3f1a1ab567bdfb15625642cd33f3ca924a3846352923f45bf39d6ba@ec2-3-208-50-226.compute-1.amazonaws.com:5432/d4p1h3ane0mls4'

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = uri

db = SQLAlchemy(app)

Base = declarative_base()

class User(Base):
    __tablename__ = "pansydb"
    iD = Column(Integer, primary_key=True)
    user_name = Column(String)
    age = Column(String)

@app.route("/login")
def login():
    try:
        result = request.args.get('result')
    except:
        result = -1
    return '{"Result": "'+str(result)+'", "Key":"165ED175E107494580D47E4F89C6907C" }'

@app.route("/")
def hello():

    # engine = create_engine('postgres://ozqqhdmuqezsca:a220c425e3f1a1ab567bdfb15625642cd33f3ca924a3846352923f45bf39d6ba@ec2-3-208-50-226.compute-1.amazonaws.com:5432/d4p1h3ane0mls4')  
    
    # df = pd.read_sql(sql='select * from pansydb;', con=engine)

    t = text("select * from pansydb")

    df = ""

    for r in db.session.execute(t):
        df = df + r["user_name"] + ", "

    return render_template('index.html', name=df)

@app.route("/send", methods=["GET"])
def get_method():
    name = "GET!!!"
    return render_template('index.html', name=name)

@app.route("/send", methods=["POST"])
def post_method():
    # インサートする
    iD = request.form['id']
    age = request.form['age']
    name = request.form['name']
    
    t = text("insert into pansydb (id, user_name, age) values ("+ iD +", '"+ name +"', '" + age + "')")

    db.session.execute(t)
    db.session.commit()

    return render_template('index.html', name="OK")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)