import json
from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    # Load news data from the saved JSON file
    with open('news.json', 'r') as f:
        newslist = json.load(f)

    return render_template('index.html', newslist=newslist)

if __name__ == '__main__':
    app.run(debug=True)
