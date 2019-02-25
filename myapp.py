from flask import Flask, request
from test import main
from train import train_me
import urllib

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/check/", methods=['POST'])
def check_url():
    url = request.form.get("url")
    urllib.urlretrieve(url, "markup.txt")
    return main(url)
    
@app.route("/train/", methods=['GET'])
def train_model():
    return train_me()
    
if __name__ == "__main__":
    app.run(debug=True)