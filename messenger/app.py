'''
3. Messenger application

This serves static files from /static and /template directories
'''

# note we need to import several functions from Flask
from flask import Flask, request, render_template, json
app = Flask(__name__)


messages = []

# NOTE: Flask defaults to serving HTML out of /templates, static files (JS/CSS) out of /static

# at the root route, serve an html page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")

    # now add this part
    elif request.method == 'POST':
        obj = json.loads(request.data)
        print(obj)
        messages.append((obj['message'], obj['name']))
        response = app.response_class(
                response='Success.',
                status=200
        )
        return response


# returns messages
@app.route('/messages', methods=['GET'])
def api():
    response = app.response_class(
        response=json.dumps(messages),
        status=200,
        mimetype='application/json'
    )
    return response

# enables running from command line `flask run`
if __name__ == '__main__':
    app.run()