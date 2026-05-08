# instructions to connect to db
# python3 (global), python
# make connection to the database in the code to reference it 
# from app import db
'''
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy

create tables:
with app.app_context():
    db.create_all()
'''

'''
>>> with app.app_context():
...     drink = Drink(
...         name="Grape Soda",
...         description="tastes like grape"
...     )
...     db.session.add(drink)
...     db.session.commit()
... 

>>> with app.app_context():
...     drinks = Drink.query.all()
...     print(drinks)
... 
[<Drink 1>]
'''
'''
# 1. ADDING DATA TO THE DATABASE

with app.app_context():
    db.session.add(
        Drink(name="Cherry", description="")
    )
    db.session.commit()

# app.app_context()
# activates the Flask app context so DB operations work

# db.session.add(...)
# stages/adds the object to the database session

# db.session.commit()
# permanently saves changes to the database
'''

'''
# 2. READING DATA FROM THE DATABASE

with app.app_context():
    drinks = Drink.query.all()

    for drink in drinks:
        print(drink.name, "-", drink.description)

# Drink.query.all()
# fetches all rows from the Drink table
'''