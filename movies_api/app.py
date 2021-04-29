from flask import Flask, render_template, jsonify, json
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return '<h1>About</h1><p>some other content</p>'


@app.route('/api/v1/album', methods=['GET'])
def album_json():
    album_info = os.path.join(app.static_folder, 'data', 'album.json')
    with open(album_info, 'r') as json_data:
        json_info = json.load(json_data)
    return jsonify(json_info)


@app.route('/api/v1/movies', methods=['GET'])
def movies_json():
    movies_info = os.path.join(app.static_folder, 'data', 'movies.json')
    with open(movies_info, 'r') as json_data:
        json_info = json.load(json_data)
    return jsonify(json_info)
    return render_template('index.html')

@app.route('/api/v1/movies/clean')
def movies_clean():
    results = []
    movies_info = os.path.join(app.static_folder, 'data', 'movies.json')
    with open(movies_info, 'r') as json_data:
        json_info = json.load(json_data)
    for movie in json_info: 






    

#@app.route('//')
#def index():
 #   return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host ='0.0.0.0')