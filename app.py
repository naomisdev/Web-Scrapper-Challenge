from scrape_mars import scrape
from flask import Flask,redirect,jsonify,render_template
from flask_pymongo import PyMongo 

app = Flask(__name__)
mongo = PyMongo(app, uri = 'mongodb://localhost:27017/mars_db')

@app.route('/')
def index():
    mars = mongo.db.mars.find_one()
    return render_template('index.html', mars = mars)



@app.route("/scrape")
def scraper():
    mars = mongo.db.mars
    mars_data = scrape()
    mars.update({}, mars_data, upsert=True)
    return redirect("/", code=302)







if __name__=='__main__':
    app.run()