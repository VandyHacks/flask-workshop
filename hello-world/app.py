'''
1. Hello World:

This simply serves a "Hello, World!" string message.
'''


from flask import Flask

# initialize the flask app
app = Flask(__name__)

# at the root default route, just serve a string as HTML
@app.route('/')
def hello_world():
    return 'Hello, World!'

# enables running from command line `flask run`
if __name__ == '__main__':
    app.run()