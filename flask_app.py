from flask import Flask
from flask import Flask, render_template

app=Flask(__name__)

if __name__ =='_main_':
    app.run(port=5000,debug=True)
    
@app.route('/')
def home ():
    return "<p>Hello world!</p>"

@app.route('/')
def home (basic_Flask_code):
    return "<p>Test run!</p>"