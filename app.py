

import sqlalchemy

#pip install Flask-MySQLdb
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL

import json


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'k2pdcy98kpcsweia.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'yp4h3nbpaqgm9z8c'
app.config['MYSQL_PASSWORD'] = 'z0s17ip96lnvhlwg'
app.config['MYSQL_DB'] = 'xznsdf2fik8wnexq'

mysql = MySQL(app)


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")
    
@app.route("/sunburst")
def sunburst():
    """Return Sunburst Page"""
    return render_template("sunburst.html")

@app.route("/dogdata")
def dog_data():
    """Return the Breed Data."""
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM doggy_data')
    row_headers = [x[0] for x in cur.description]
    rv=cur.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))
    return jsonify(json_data)


if __name__ == "__main__":
    app.run()
