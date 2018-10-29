'''
2. Static Files:

This serves static files from /static and /template directories
'''

# note we need to import several functions from Flask
from flask import Flask, request, render_template
app = Flask(__name__)


# NOTE: Flask defaults to serving HTML out of /templates, static files (JS/CSS) out of /static

# at the root route, serve an html page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")

# enables running from command line `flask run`
if __name__ == '__main__':
    app.run()