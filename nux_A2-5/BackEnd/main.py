from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index() :
    return render_template('index.html')

@app.route('/input')
def input() :
    return render_template('input.html')

@app.route('/result',methods=['POST'])
def result():
    profile_pics  = request.form.getlist('profile_pic[]')
    names = request.form.getlist('name[]')
    role = request.form.getlist('Role[]')
    student_numbers = request.form.getlist('StudentNumber[]')
    department = request.form.getlist('Department[]')
    emails = request.form.getlist("email[]")
    genders = request.form.getlist('gender[]')
    foods   = request.form.getlist('favorite_food[]')
    Languages = request.form.getlist('Languages[]')
    dreams = request.form.getlist('Dream[]')
    phonenumber = request.form.getlist('Phonenumber[]')
    MBTI = request.form.getlist('MBTI[]')
    return render_template('result.html',
                          students=zip(
                            names, role, student_numbers, department,
                            phonenumber, emails, genders, foods,
                            MBTI, dreams, Languages, profile_pics
                           ))    

@app.route('/contact')
def contact_info():
    return render_template('contact.html')

app.run(debug=1,host='0.0.0.0',port=5000)