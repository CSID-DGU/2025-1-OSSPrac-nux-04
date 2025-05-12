from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index() :
    return render_template('index.html')

@app.route('/input')
def input() :
    return render_template('input.html')

names = ['조바이든','육','신','정']
dic = {}

for name in names :
    fname = f'images/{name}.webp'
    dic[name] = fname
    
print(dic)

@app.route('/result',methods=['POST'])
def result():
    names = request.form.getlist('name[]')
    student_numbers = request.form.getlist('StudentNumber[]')
    emails = request.form.getlist("email[]")
    dreams = request.form.getlist('Dream[]')
    
    return render_template('result.html',students=zip(names,student_numbers,emails,dreams),img = dic)

@app.route('/contact')
def contact_info():
    return render_template('contact.html')

app.run(debug=1)