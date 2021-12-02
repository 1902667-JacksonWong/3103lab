from logging import Handler
from flask import Flask, request, render_template
from flask.json import jsonify
import json
import time
from datetime import datetime



app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    # if request.method == "GET":
    #     return f"Request Recieved"
     
    if request.method == "POST":
        input1 = request.form['search']
        print('hello')
        print(input1)
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 80)
    #app.run(debug=True, host='0.0.0.0', port = 8080)