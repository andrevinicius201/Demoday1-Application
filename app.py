from flask import Flask, render_template,escape, request, flash, redirect,url_for, jsonify, session 
from flask import Response,send_file
from waitress import serve
import os
import socket
import redis

app = Flask(__name__)

#app.secret_key = os.environ.get('SECRET_KEY', default=None)
app.secret_key = 'eufheufe'

import rds_db as db

#REDIS_URL = os.environ.get('REDIS_URL')
REDIS_URL = 'redis://demoday-001.jr2xop.0001.use1.cache.amazonaws.com:6379'
store = redis.Redis.from_url(REDIS_URL)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(app.secret_key)
        session['username'] = request.form['username']
        return redirect('/')
    return '''<form method="post"> <input type=text name=username> <input type=submit value=Login> '''



@app.route('/')
def index():
    #host = flask.Flask.request.host
    host = socket.gethostname()
    if 'username' in session:
        username = escape(session['username'])
        visits = store.hincrby(username, 'visits', 1)
        store.expire(username, 3600)
        print("logged in as {0}. Visits count: {1}".format(username, visits))
        details = db.get_details()
        headings = ("ID", "Nome", "Preço", "Comentário", "Descrição")
        return render_template("index.html", headings=headings, data=details, user=username, visit_count=visits, hostname=host)
    return "You are not logged in!"
@app.route('/insert',methods = ['post'])
def insert():
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        gender = request.form['optradio']
        comment = request.form['comment']
        db.insert_details(name,email,comment,gender)
        details = db.get_details()
        print(details)
        for detail in details:
            var = detail
        #return render_template('index.html',var=var)
        return redirect('/')

@app.route("/delete/<string:id>", methods = ['post'])
def delete(id):
       db.delete(id) 
       details = db.get_details() 
       headings = ("Id", "Nome", "Preço", "Descrição", "Comentãrio") 
       #return render_template('index.html', headings=headings, data=details)
       return redirect('/')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

if __name__ == "__main__":
    
    serve(app, host='0.0.0.0', port=80)
