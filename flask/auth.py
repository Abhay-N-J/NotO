from flask import Blueprint,render_template,request,flash,redirect,url_for
from __init__ import db
from models import User,Note
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user,login_required,logout_user,current_user


auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        passwd = request.form.get('passwd')
        print("hello")

        user = User.query.filter_by(name=name).first()
        print(user.passwd)
        if user:
            if check_password_hash(user.passwd,passwd):
                flash('Logged in Successfully',category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again',category='error')
        else:
            flash('User name does not exist',category='error')
    return render_template('login.html', user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method =='POST':
        name = request.form.get('name')
        email = request.form.get('email')
        passwd = request.form.get('password')

        user = User.query.filter_by(name=name).first()
        if user:
            flash('Email already exists',category='error')
            return redirect(url_for('auth.login'))
        if len(name) < 2:
            flash('Name is too small',category='error')
        elif len(passwd) <8:
            flash('Password is too small',category='error')
        else:
            new_user = User(email=email,name=name,passwd=generate_password_hash(passwd,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created',category='success')
            return redirect(url_for('views.home'))
        
    return render_template("sign-up.html")

