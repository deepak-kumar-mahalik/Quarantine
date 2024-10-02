from flask_mysqldb import MySQL
from flask import Flask, render_template,request

app=Flask(__name__)

app.config['MYSQL_USER']='root'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_PASSWORD']='chiku@123'
#app.config['MYSQL_DB']='mine'

dp=MySQL(app)

@app.route('/')
def dub():
    return render_template('Q_Home.html')

@app.route('/a')
def dy():
    return render_template('QHOM.html')

@app.route('/b')
def sya():
    return render_template('Availability.html')

@app.route('/c')
def so():
    return render_template('Book_now.html')

@app.route('/d')
def ji():
    return render_template('Facilities.html')

@app.route('/e')
def sun():
    return render_template('FAQ.html')

@app.route('/f')
def aj():
    return render_template('CON.html')

@app.route('/g')
def au():
    return render_template('Introduction.html')

@app.route('/h')
def gu():
    return render_template('Servicess.html')

@app.route('/i')
def wt():
    return render_template('Announ.html')

@app.route('/j')
def jk():
    return render_template('Facility.html')

@app.route('/k')
def bj():
    return render_template('Update.html')

@app.route('/l')
def duch():
    return render_template('Meal.html')

@app.route('/m')
def gok():
    return render_template('Health.html')

@app.route('/n')
def al():
    return render_template('Facilityy.html')

#@app.route('/')
#def fun():
 #   conn=dp.connection.cursor()
  #  conn.execute("create database mine")
   # conn.close()
    #return "database created successfully"

app.run(debug=True,port=367802)