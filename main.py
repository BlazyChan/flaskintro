from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  #return "<h1>Hi!</h1>"
  return render_template('chat.html') # lai testētu lapu vieglāk... parāda home page
@app.route('/home')
def home():
  return render_template('home.html', aktiva_lapa = 'home')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact')
def contacts():
  return render_template('contact.html', phone = 12345678)

@app.route('/params')
def params():
  args = request.args
  for key, value in args.item():
    print(f"{key}:{value}")
  return args

@app.route('/params_table')
def params_table():
  args = request.args
  return render_template('params_table.html', args = args)

@app.route('/chat')
def chat():
  return render_template('chat.html')

@app.route('/post_req', methods = ['POST'])
def post_req():
  return request.args

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 5000, threaded = True, debug = True)
# push github un reģistrēties heroku.com
# ctrl + f5 reloado cache