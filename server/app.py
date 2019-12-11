import os
from flask import Flask
#from flask_migrate import flask_migrate
from flask_cors import flask_cors

#def create_app():
#    flask_app = Flask(__name__)
#    return flask_app

#app = create_app()
#CORS(app)

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"
    
if __name__ == "__main__":
    app.run(debug=True)

