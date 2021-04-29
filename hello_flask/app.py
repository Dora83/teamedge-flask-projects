from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return '<h1>About</h1><p>some other content</p>'


@app.route('/api/v1/album', meathods = ['GET'])
def album_json():
    album_info = os.path.join(app.static_folder, 'hello_flask', 'album.json')
    with open(album_info, 'r') as json_data:
        json_info = json.load(json_data)
        return jsonify(json_info)k


@app.route('/nasa')
def nasa_image():
    today = str(date.today)
    response = request.get('https://api.nasa.gov/planetary/apod?api_key=wjlnR0Xw9B5Sh3WEIJa9kmVd368hNMiUIGahGPi&date=' + today)

    data = response.json()

    return render_template('nasa.html',data=data)

if __name__ == '__main__':
    app.run(debug=True, host ='0.0.0.0')