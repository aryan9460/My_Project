import requests
from flask import Flask,render_template
from flask_sqlalchemy import sqlalchemy
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("weather.html")
if __name__=="__main__":
    app.run(host="localhost",port=80,debug=True)
