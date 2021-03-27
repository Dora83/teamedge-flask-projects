from flask import Flask, redirect, url_for, request, render_template
from sense_hat import SenseHat

sense = SenseHat()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('form.html')

@app.route('/success/<name>',methods = ['POST', 'GET'])
def success(name):
    sense.show_message(name)
    return 'Thank you! Your message was: %s' % name 
 

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['fname']
        return redirect(url_for('success',name = user))
    else:
        user = request.args.get('fname')
        return redirect(url_for('success', name = user))
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')