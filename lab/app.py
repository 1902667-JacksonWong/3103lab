from logging import Handler
from flask import Flask, request, render_template
from flask.json import jsonify
import json
import time
from datetime import datetime

# for sql db
import pymysql as sql
# import datetime

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    

    if request.method == "POST":
        
        return f"Request Recieved"




if __name__ == '__main__':
    app.run(debug=True, host=file[3], port=file[4])
    # app.run(debug=True, host='0.0.0.0', port=5000)