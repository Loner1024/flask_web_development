from flask import Flask,request
app = Flask(__name__)

@app.route('/')
def index():
   return '<h1>Hello,Flask!</h1>'

@app.route('/<username>')
def user(username):
   return '<h1>Hello,{}!</h1>'.format(username)

@app.route('/browser')
def browser():
   user_agent = request.headers.get('User-Agent')
   return '你的浏览器是{}'.format(user_agent)