from flask import json, Flask, render_template, current_app as app
import requests

app = Flask(__name__)


@app.route('/holidays')
def holiday_data():

    response = requests.get("https://holidays.abstractapi.com/v1/?api_key=d6862ba0773844959ecc6f8a5114eb49&country=US&year=2020&month=12&day=25") 
    data = response.json()

    return render_template('holiday.html',data=data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')