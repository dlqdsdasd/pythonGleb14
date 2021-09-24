from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///result.db'
db = SQLAlchemy(app)

@app.route('/news')
def index():
    return render_template('index.html')


app.run(host='127.0.0.1', debug=True)