from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    
    x1 = request.form['x1']
    y1 = request.form['y1']
    z1 = request.form['z1']
    
    x2 = request.form['x2']
    y2 = request.form['y2']
    z2 = request.form['z2']
    
    x3 = request.form['x3']
    y3 = request.form['y3']
    z3 = request.form['z3']
    
    return x1+y1+z1+" "+x2+y2+z2+" "+x3+y3+z3
