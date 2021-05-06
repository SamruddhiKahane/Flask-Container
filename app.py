# flask_web/app.py

from flask import Flask
from flask import render_template

app = Flask(__name__)     #create instance of flask 

@app.route('/')          #URL sholud trigger function
def webapp():
	return "Hey, this is Samruddhi's very first web app!!"


@app.route('/blog')
def hello():
	return render_template('CaaS.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')