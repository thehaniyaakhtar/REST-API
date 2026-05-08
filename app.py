from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request
app = Flask(__name__)
# FLask creates a web apps

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

# GET data by ID with parameter
# http://127.0.0.1:5000/drinks/1
@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return {"name": drink.name, "description": drink.description}

# content type in inspect is application json, unlike on an actual webpage

# POST a new record
@app.route('/drinks', methods=['POST'])
def add_drink():
    drink = Drink(name = request.json['name'],
                  description = request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id':drink.id}

# delete drink
@app.route('/drinks/<id>', methods = ['DELETE'])
def delete_drink(id):
    drink = Drink.query.get(id)
    if drink is None:
        return {"error": "not found"}
    db.session.delete(drink)
    db.session.commit()
    return {"message": "deleted"}

'''
constructing API routes:
@app.route(/url/<id>, method = [HTTP Method])
def function():
    drink = data needed/ requirements
    
    interact with database:
    db.session.add()
    db.session.delete()
    db.session.commit()
    
    return respose:
    return {"message": "response"}
'''
