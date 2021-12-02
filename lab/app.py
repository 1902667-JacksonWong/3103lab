from logging import Handler
from flask import Flask, request, render_template
from flask.json import jsonify
import json
import time
from datetime import datetime



app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    
	print('he')
    # if request.method == "POST":
    #     return f"Request Recieved"




if __name__ == '__main__':
    app.run(debug=True, host='3.19.61.215', port=5000)