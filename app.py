from flask import Flask, render_template, request, jsonify
from utils.db import session, User

app = Flask(__name__)

app.config['SECRET_KEY'] = "rvgkt3delm2bty4io3flejn2k;3kmoij[40t3rfl2jn4ek1;]"

@app.route('/hi', methods=['GET'])
def hi():
    return 'Hello, World!'

@app.route('/', methods=['GET'])
def get_users():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/login/', methods=['POST'])
def login_post():
    if request.method=='POST':
        email = request.form.get('email')
        password = request.form.get('password')
        return f"Email: {email}, Password: {password}"

@app.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():
    if request.method=='POST':
        email = request.form.get('email')
        password = request.form.get('password')
        return f"Email: {email}, Password: {password}"
    
