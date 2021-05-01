from flask import Flask, render_template, request, redirect, url_for, current_app as app
from sense_emu import SenseHat
from time import sleep
import sqlite3

sense = SenseHat



@app.route('/')
def index():
    return render_template('index.html')

@app.route('add', methods=['POST'])
def add():
    task = request.form['task']
    deadline = request.form['deadline']
    conn = sqlite3.connect('./static/data/tasks.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO tasks (task, date) VALUES((?), (?), (?))", (task, deadline))
    conn.commit()
    conn.close()

#@app.route('delete')
#def delete():

#@app.route('edit')
#def edit():

#@app.route('complete')
#def complete():

#@app.route('reminder')
#def reminder():

#@app.route('completed')
#def completed():

#@app.route('confirmation')
#def confirmation():

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
