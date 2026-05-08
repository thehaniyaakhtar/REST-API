from flask import Flask
app = Flask(__name__)
# FLask creates a web apps
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique = True, nullable = False)
    description = db.Column(db.String(120))
    
with app.app_context():
    db.create_all()

@app.route('/')
# when user visits /, Flask runs this function
def index():
    return 'Hello!'
# Flask runs index()
# index() returns "Hello!"
# Browser displays it

@app.route('/drinks')
# runs on http://127.0.0.1:5000/drinks
def get_drinks():
    drinks = Drink.query.all()
    
    output = []
    for drink in drinks:
        drink_data = {'name':drink.name,
                      'description': drink.description}
        output.append(drink_data)
        
    return {"drinks": output}