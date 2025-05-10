from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def input() :
    return render_template('input.html')

@app.route('/result',methods=['POST','GET'])
def result() :
    if(request.method=='POST'):
        result = dict()
        result['Name'] = request.form.get('name')
        result['StuedentNumber'] = request.form.get('StudentNumber')
        result['Gender'] = request.form.get('Gender')
        result['Major'] = request.form.get('Major')
        result['Languages'] = request.form.getlist('Languages')
        result['Languages'] = ', '.join(result['Languages'])
    return render_template('result.html', result=result)
    
app.run(debug=1)