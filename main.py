from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def hello_world():
    name = request.args.get('name')
    message = request.args.get('message')

    return '''<h1>Hello {}!</h1>
              <h2>{}!<h2>'''.format(name, message)
