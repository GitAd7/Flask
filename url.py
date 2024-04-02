## Building URL Dynamically

from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome To The Home Page"

@app.route('/pass/<int:score>')
def success(score):
    return "The Person has allocated a score of "+ str(score)+ "\n Congrats! You have Passed this Module and Can Move on to Next Module"

@app.route('/fail/<int:score>')
def fail(score):
    return "The Person has allocated a score of "+ str(score)+ "\n Sorry! You didn't make it this time but you have one more chance left to compelete the Module. Best of Luck!"

@app.route('/result/<int:marks>')
def result(marks):
    result = ""
    if marks >= 50:
        result = "pass"
    else:
        result = "fail"
    return redirect(url_for(result, score=marks))

if __name__ == '__main__':
    app.run(debug=True)