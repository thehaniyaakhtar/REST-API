# representational state transfer application programming interface
# fance way to say how 2 pieces of software communicate w one another

# 2 softwares in diff languages
# REST API allows these different applications to communicate
# one way, always a server and a client
# uses JSON
# and endpoint, where the request is made
# REST communicates over the web

# eg: backend software, communicates with a database
# u dont want to give direct access to the database
# thus, diff api endpoints are exposed

# a backend module, database, frontend module
# the frontend module shouldnt have direct access to db, only backend
# this maintaines modularity where multiple frontend modules can be connected to the be, maintains sync
# security, if fe can directly access fe, all data can be accessed/ compromised
# u can specifically make only certain parts of the interface public, which can be used as api 

# http methods
# GET retrieve data
# POST write (new) data to the server
# DELETE 
# PUT Update/Replace data (Idempotent)
# - u need to identify what data needs to replaced
# - designed to give the same data over the same request
# - in POST, even if the same ID is requested, a new record in the table is created
# PATCH in large data, helps u change small portions of data
# CRUD

# 