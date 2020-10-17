from scrape_mars import scrape
from flask import Flask,redirect,jsonify,render_template
from flask_pymongo import PyMongo 

app = Flask(__name__)
mongo = PyMongo(app, uri = 'mongodb://localhost:27017/mars_db')

@app.route('/')
def index():
    return render_template('index.html')









if __name__=='__main__':
    app.run()