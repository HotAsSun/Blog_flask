import secrets 
import os 
from PIL import Image
from flask import render_template  , url_for , flash , redirect ,request
from flaskblog.forms import RegistrationForm , LoginForm , UpdateAccountForm
from flaskblog.models import User , Post
from flaskblog import app , db , bcrypt 
from flask_login import login_user , current_user , logout_user , login_required 



posts = [
    {
        "author": "Alice Johnson",
        "title": "The Future of AI",
        "content": "Artificial Intelligence is rapidly evolving and changing industries.",
        "time_posted": "2025-09-27 10:15:00"
    },
    {
        "author": "Bob Smith",
        "title": "Healthy Living Tips",
        "content": "Eating more vegetables and regular exercise improves your lifestyle.",
        "time_posted": "2025-09-27 11:30:00"
    },
    {
        "author": "Charlie Brown",
        "title": "Traveling on a Budget",
        "content": "You can explore amazing destinations without breaking the bank.",
        "time_posted": "2025-09-27 12:45:00"
    },
    {
        "author": "Diana Prince",
        "title": "Cybersecurity Basics",
        "content": "Protect your online accounts with strong passwords and 2FA.",
        "time_posted": "2025-09-27 14:05:00"
    },
    {
        "author": "Ethan Hunt",
        "title": "Top 5 Coding Practices",
        "content": "Writing clean, maintainable code is as important as solving problems.",
        "time_posted": "2025-09-27 15:20:00"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts,title="home")


@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods = ["GET", "POST"])
def register():
    if current_user.is_authenticated:
        flash("your already registered" , 'danger')
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username = form.username.data , email = form.email.data , password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created succesfully for {form.username.data}","success")
        return redirect(url_for('login'))
    
    return render_template('register.html',form=form,title="register")


@app.route("/login",methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        flash("your already loged in " , 'danger')
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            next_page = request.args.get("next")

            return redirect(next_page) if next_page else  redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
             
            
    return render_template('login.html',form=form,title="login")

@app.route("/logout")
def logout():
    logout_user()
    flash(f"you are logged out of yuor account", 'success')
    return redirect(url_for("home"))



def save_picture(from_picture):
    random_hex = secrets.token_hex(8)
    _ , f_etc = os.path.splitext(from_picture.filename)
    picture_fn = random_hex + f_etc
    picture_path = os.path.join(app.root_path,'static/profile_pics',picture_fn)

    output = (125,125)

    i = Image.open(from_picture)
    i.thumbnail(output)

    i.save(picture_path)
   
    return picture_fn

@app.route("/account",methods=['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_url = picture_file

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("your account has been updated" , 'success')
        return redirect(url_for("account"))
    elif  request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email

    image_file = url_for("static",filename = 'profile_pics/' + current_user.image_url)
    return render_template('account.html',title = 'account', image_file=image_file , form = form)

 
