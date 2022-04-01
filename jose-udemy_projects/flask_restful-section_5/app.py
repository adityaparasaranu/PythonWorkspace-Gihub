from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from item import Item, Items

app = Flask(__name__)
app.secret_key = "aditya"
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<name>')
api.add_resource(Items, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
