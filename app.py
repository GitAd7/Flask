from flask import Flask
## WSGI App
app = Flask(__name__)

## Decorator with a function which automatically get triggers
@app.route('/')
def Welcome():
    return "Welcome To The Home Page"

@app.route('/people')
def Amigo():
    return "Welcome To The Home Page. Fam!"

if __name__ == '__main__':
    app.run(debug=True)