from socket import gethostname
from os import getenv
from flask import Flask, render_template,redirect, request, json, jsonify,make_response
app = Flask(__name__)
import os
from flask_mysqldb import MySQL
import random
import json
import time



app.config['MYSQL_HOST'] = 'us-cdbr-iron-east-01.cleardb.net'
app.config['MYSQL_USER'] = 'ba899f3b32b533'
app.config['MYSQL_PASSWORD'] = 'cd7a8319'
app.config['MYSQL_DB'] = 'ad_752a490146a72e0'

mysql = MySQL(app)


@app.route("/service")
def hello():
    vcap_services = getenv('VCAP_SERVICES')
    return jsonify({'message': 'hello world', 'hostname': gethostname(), 'services-bind': json.loads(vcap_services)}), 200

@app.route('/')
def index2():
    return render_template('details.html')

@app.route('/res', methods=['GET', 'POST'])
def index1():
    print("hello")
    b=()
    if request.method == "POST":
        details = request.form
        roll = details['roll']
        cur = mysql.connection.cursor()
        #cur.execute("INSERT INTO myusers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        cur.execute("select * from student where idstudent=%s",(roll,))
        b=cur.fetchall()
        print("something")
        mysql.connection.commit()
        cur.close()

    if(len(b)> 0):
        return render_template('details.html',name = str(b[0][1]), branch = str(b[0][2]), year = str(b[0][3]), cgpa = str(b[0][4]))
    else :
        return render_template('details.html',name = " null", branch = "null", year = "null", cgpa = "null")


@app.route('/form')
def index3():
    return render_template('index.html')

@app.route('/usr', methods=['GET', 'POST'])
def index():
    print("user")
    if request.method == "POST":
        details = request.form
        idno = details['fid']
        lastName = details['lname']
        branch = details['lbranch']
        year = details['lyear']
        cgpa = details['lcgpa']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO student(idstudent, name, year,branch,CGPA) VALUES (%s, %s, %s, %s, %s)", (idno, lastName,year,branch,cgpa))
        mysql.connection.commit()
        cur.close()
        return render_template('details.html')
    return render_template('index.html')



@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

@app.route('/graph')
def index5():
    return render_template('graph.html')

@app.route('/data', methods=["GET", "POST"])
def data():
    data = [time.time() * 1000, random.random() * 100]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response
  
port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
