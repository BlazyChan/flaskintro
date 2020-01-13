from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return "<h1>Hi!</h1>"

@app.route('/home')
def home():
  return "<h1><a href=https://flaskintro.xxblazyxx.repl.co/about>My home</a></h1>"

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contacts')
def contacts():
  return render_template('contact.html')

app.run(host = '0.0.0.0', port = 8020)

# push github un reģistrēties heroku.com