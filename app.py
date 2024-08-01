import os
from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
from utils.db import session, User
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

load_dotenv()
UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app.config['SECRET_KEY'] = "rvgkt3delm2bty4io3flejn2k;3kmoij[40t3rfl2jn4ek1;]"

@app.route('/hi', methods=['GET'])
def hi():
    return 'Hello, World!'

@app.route('/home', methods=['GET'])
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
    

@app.route('/fileupload', methods=['GET'])
def files():
    return render_template('fileupload.html')

@app.route('/fileupload', methods=['POST'])
def fileupload():
    if request.method == 'POST':
        
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('hi'))
        
        if file and not allowed_file(file.filename):
            flash('Invalid file type')
            return "Invalid file type"