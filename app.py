import os
from flask import Flask, render_template, request, jsonify, flash, redirect, url_for, make_response
from utils.db import session, User
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
from utils.db import session, create_user, login_user
from utils.db import patient_info
load_dotenv()
UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app.config['SECRET_KEY'] = "rvgkt3delm2bty4io3flejn2k;3kmoij[40t3rfl2jn4ek1;]"




@app.route('/app/<string:mode>', methods=['GET'])
def appfunc(mode):
    return render_template(f'{mode}.html')

@app.route('/home', methods=['GET'])
def home():
   return render_template('index.html')
    

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/login/', methods=['POST'])
def login_post():
    if request.method=='POST':
        email = request.form.get('email')
        password = request.form.get('password')
        res = login_user(session, email, password)
        print(res)
        if res['message']['status']==200:
            resp = make_response("setting session cookie")
            resp.set_cookie('session', res['session']["user"])
            return redirect(url_for('appfunc'))
        else:
            return redirect(url_for('login'))

@app.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():
    if request.method=='POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        res = create_user(session, email, password)
        print(res)
        if res['message']['status']==200:
            resp = make_response("setting session cookie")
            resp.set_cookie('session', res['session']["user"])
            return redirect(url_for('profile'))

        else:
            return redirect(url_for('signup'))

@app.route('/', methods=['GET'])
def index():
    if request.cookies.get('session'):
        return redirect(url_for('appfunc'))
    else:
        return redirect(url_for('home'))
    
@app.route('/logout', methods=['GET'])
def logout():
    resp = make_response("deleting session cookie")
    resp.delete_cookie('session')
    return redirect(url_for('login'))

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
            
            return redirect(url_for('profile'))
        
        if file and not allowed_file(file.filename):
            flash('Invalid file type')
            return "Invalid file type"
        
@app.route('/app/profileupdate', methods=['GET'])
def updateprofile():
    return render_template('profileupdate.html')

@app.route('/app/profileupdate', methods=['POST'])
def profileupdate():
    if request.method=='POST':
        name = request.form.get('name')
        age = request.form.get('age')
        blood_type = request.form.get('blood_type')
        allergies = request.form.get('allergies')
        weight = request.form.get('weight')
        height = request.form.get('height')
        user_id = request.cookies.get('session')
        res = patient_info(session, name, age, blood_type, allergies, weight, height, user_id)
        print(res)
        

@app.route('/app/profile', methods=['GET'])
def profile():
    return render_template('profile.html')


@app.route("/callambu", methods=["POST"])
def call_ambu():
    return render_template("callambu.html")

@app.route("/hospitalregistry", methods=["GET"])
def hospital_registry():
    return render_template("hospitalregistry.html")

@app.route("/hospitalregistry", methods=["POST"])
def hospital_reistry():
    if request.method=="POST":
        location = request.form.get("location")
        phone_number = request.form.get("phone_number")
        name = request.form.get("name")

        print(res)
        return redirect(url_for('profile'))
    
@app.route("/icu", methods=["GET"])
def icu():
    return render_template("icu.html")

@app.route("/app/ambulance/patients", methods=["GET"])
def ambulance_patients():
    return render_template("patients.html")