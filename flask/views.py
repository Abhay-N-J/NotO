from math import remainder
from flask import Blueprint,render_template
from flask_login import login_user,login_required,logout_user,current_user


views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("welcome_page.html")

@views.route('/abc')
# @login_required
def abc():
    return render_template("ABC.html")

@views.route('/review')
# @login_required
def review():
    return render_template("student_feedback.html")

@views.route('/forum')
# @login_required
def forum():
    return render_template("t.html")

@views.route('/quiz')
# @login_required
def quiz():
    return render_template('quiz.html')


