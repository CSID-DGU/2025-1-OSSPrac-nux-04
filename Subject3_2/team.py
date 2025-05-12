from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index() :
    return render_template('index.html')

@app.route('/input')
def input() :
    return render_template('input.html')

@app.route('/result',methods=['POST'])
def result():
    names = request.form.getlist('name[]')
    role = request.form.getlist('Role[]')
    student_numbers = request.form.getlist('StudentNumber[]')
    department = request.form.getlist('Department[]')
    emails = request.form.getlist("email[]")
    genders = request.form.getlist('gender[]')
    foods   = request.form.getlist('favorite_food[]')
    dreams = request.form.getlist('Dream[]')
    phonenumber = request.form.getlist('Phonenumber[]')
    MBTI = request.form.getlist('MBTI[]')
    return render_template('result.html',students=zip(names,role,student_numbers,department,phonenumber,emails,genders,foods,MBTI,dreams))    


@app.route('/contact')
def contact_info():
    return render_template('contact.html')

app.run(debug=1)