from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return "<h1>Hi!</h1>"

@app.route('/home')
def home():
  return render_template('home.html', aktiva_lapa = 'home')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact')
def contacts():
  return render_template('contact.html', phone = 12345678)
if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 5420, threaded = True, debug = True)

# push github un reģistrēties heroku.com
# ctrl + f5 reloado cache