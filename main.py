# REST = Representational State Transfer
# API = Application Programming Interface
# fancy way to say:
# "how 2 pieces of software communicate w each other"

# apps can be written in different languages
# REST APIs allow these different applications to communicate over the web

# usually follows a client-server architecture
# client sends requests
# server sends responses

# data is commonly sent using JSON

# APIs expose endpoints
# endpoint = URL where requests are made
# eg:
# frontend -> backend -> database

# frontend should NOT directly access the database
# only the backend should talk to the db

# why?
# modularity:
# multiple frontends (web app, mobile app, etc.)
# can use the same backend

# security:
# prevents direct public access to sensitive db operations/data

# backend controls:
# what data can be accessed
# who can access it
# what operations are allowed

# API endpoints act like controlled public interfaces
# GET
# retrieve/fetch data from server
# POST
# create new data on server
# DELETE
# remove data from server
# PUT
# update/replace existing data (idempotent)
# usually replaces the entire resource

# idempotent means:
# sending the same request multiple times
# gives the same final result

# example:
# updating user id=5 w same data repeatedly
# still results in the same updated user

# POST is NOT idempotent
# sending same POST request multiple times
# may create multiple new records

# PATCH
# partially update existing data
# useful when only changing small portions of data

# CREATE -> POST
# READ   -> GET
# UPDATE -> PUT / PATCH
# DELETE -> DELETE

import requests
import json

response = requests.get("https://api.stackexchange.com/2.3/questions?site=stackoverflow")

print(response.json())
print(response.json()['items'])

# consuming an API for questions with 0 answers
for data in response.json()['items']:
    if data['answer_count'] == 0:
        print(data['title'])
        print(data['link'])
    else:
        print('skipped')
    print()

