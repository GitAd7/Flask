## Integrating HTML with FLASK
## HTTP vers like GET and POST

from flask import Flask, redirect, url_for, render_template,request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pass/<int:score>')
def success(score):
    res = ""
    if score>= 50:
        res = "Pass"
    else:
        res = "Fail"
    return render_template('results.html', result=res)

@app.route('/fail/<int:score>')
def fail(score):
    es = ""
    if score>= 50:
        res = "Pass"
    else:
        res = "Fail"
    return render_template('results.html', result=res)

@app.route('/result/<int:marks>')
def result(marks):
    result = ""
    if marks >= 50:
        result = "pass"
    else:
        result = "fail"
    return redirect(url_for(result, score=marks))

## HTML PAge for Checking Result
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        analogy = float(request.form['analogy'])
        datascience = float(request.form['datascience'])
        total_score = (science+maths+analogy+datascience)/4
    res = ""
    if total_score>= 50:
        res="success"
    else:
        res="fail"
    return redirect(url_for(res, score=total_score))
    


if __name__ == '__main__':
    app.run(debug=True)