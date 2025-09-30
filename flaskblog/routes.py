from flask import render_template  , url_for , flash , redirect 
from flaskblog.forms import RegistrationForm , LoginForm
from flaskblog.models import User , Post
from flaskblog import app 



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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created succesfully for {form.username.data}","success")
        return redirect(url_for('home'))
    return render_template('register.html',form=form,title="register")


@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html',form=form,title="login")


