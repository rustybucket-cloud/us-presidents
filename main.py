from flask import Flask, render_template
import requests
import json
import os
app = Flask(__name__)

key = os.environ.get("API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/presidents/<name>')
def president(name):
    data = getPresidentInfo(name)
    return render_template('president.html', name=name.replace("_", " "), in_office=data["in_office"], img=data["photo_img"], order=data["order"])

def getPresidentInfo(name):
    url = f"https://wikiapi.p.rapidapi.com/api/v1/wiki/biography/president/us/info/{name}"
    querystring = {"lan":"en"}
    headers = {
        "X-RapidAPI-Host": "wikiapi.p.rapidapi.com",
        "X-RapidAPI-Key": key
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    return data

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')