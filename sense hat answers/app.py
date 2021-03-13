from flask import Flask, redirect, url_for, request, render_template
from sense_emu import SenseHat

sense = SenseHat()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('form.html')

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['fname']
        return redirect(url_for('success',name = user))
    else:
        user = request.args.get('fname')
        return redirect(url_for('success', name = user))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
