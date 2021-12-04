
from flask import Flask

from wsgiref import simple_server # used to serve the application on a server and we can utilize this

from flask import Flask, session, request, Response, jsonify



import atexit
import uuid
import os
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return "Flask app is running and test is deployed successfully"

port = int(os.getenv("PORT", 5001))

if __name__ == "__main__":
    host = '0.0.0.0'
    #app.run()
    httpd = simple_server.make_server(host=host, port=port, app=app) #httpd is used to run the system on threads
    #httpd = simple_server.make_server(host='127.0.0.1', port=5000, app=app)
    # print("Serving on %s %d" % (host, port))
    httpd.serve_forever() #http deamon is used to run the system on threads