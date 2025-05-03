from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index() :
    return render_template('app_index.html')

@app.route('/input')
def input():
    return render_template('app_input.html')

@app.route('/result',methods=['POST'])
def result() :
    names = request.form.getlist('name[]')
    student_number = request.form.getlist('StudentNumber[]')
    return render_template('app_result.html',students=zip(names,student_number))

@app.route('/contact')
def contact_info() :
    return render_template('app_contact.html')

if __name__=='__main__' :
    app.run(debug=True)