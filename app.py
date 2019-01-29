from flask import Flask,request,render_template,url_for
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/<username>')
def user(username):
   return render_template('user.html',username=username)

@app.route('/browser')
def browser():
   user_agent = request.headers.get('User-Agent')
   return '你的浏览器是{}'.format(user_agent)

@app.route('/url')
def url():
   return str(url_for('user',username='Loner',_external=True))

class NameForm(FlaskForm):
   name = StringField('姓名?',validators=[DataRequired()])
   submit = SubmitField('submit')

@app.route('/form')
def form_index():
   name = None
   form = NameForm()
   
   