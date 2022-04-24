from traceback import print_tb
from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']

    processed_text = text.upper()
    print(processed_text)
    return processed_text
    
    
