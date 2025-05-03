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
        result['Email'] = request.form.get('Full-email')
        # result['language'] = request.form.getlist('languages')
        # result['languages'] = ','.join(result['languages'])
        # return render_template('result.html',result=result)
    return render_template('result.html', result=result)
    
app.run(debug=1)