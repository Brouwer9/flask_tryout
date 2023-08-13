from flask import Flask
from flask import Flask, render_template

app=Flask(__name__)

if __name__ =='_main_':
    app.run(port=5000,debug=True)

@app.route('/')
def home ():
    return "<p>Hello World</p>"

@app.route('/basicFlaskcode')
def basicFlaskcode ():
    return "<p>test</p>"