#!/usr/bin/env python3
import time
from flask import Flask, render_template, request
from flask_cors import CORS #pip install -U flask-cors 

lnk1 = 0
lnk2 = 0
lnk3 = 0
state = 0

def write_data():
    global state,lnk1,lnk2,lnk3
    f = open("communication.txt","w")
    lst = []
    for i in [state,lnk1,lnk2,lnk3]:
        f.write(str(i))
        f.write("\n")
    f.close()

def set_data():
    complete = False
    while not complete :
        try:
            write_data()
        except:
            pass
        else:
            complete = True
    print("setting data")

app = Flask(__name__,template_folder='/home/jayee/Desktop/project/prototyping stuff/templates')
CORS(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    global lnk1,lnk2,lnk3,state

    if request.method == 'POST':
        if request.form.get('1') == 'config':
            lnk1 = 0
            lnk2 = 0
            lnk3 = 0
            state = 1
            set_data()
            
        elif  request.form.get('2') == 'pickup location':
            lnk1 = 90
            lnk2 = 90
            lnk3 = 90
            state = 2
            set_data()
        elif  request.form.get('3') == 'collection location':
            lnk1 = 90
            lnk2 = 90
            lnk3 = 90
            state = 3 
            set_data()
        elif  request.form.get('4') == 'deposit location':
            lnk1 = 90
            lnk2 = 90
            lnk3 = 90
            state = 4
            set_data()
        elif  request.form.get('5') == 'pickup operation':
            lnk1 = 90
            lnk2 = 90
            lnk3 = 90
            state = 5
            set_data()
        elif  request.form.get('6') == 'collection operation':
            lnk1 = 90
            lnk2 = 90
            lnk3 = 90
            state = 6
            set_data()
        elif  request.form.get('7') == 'deposit operation':
            lnk1 = 90
            lnk2 = 90
            lnk3 = 90
            state = 7
            set_data()
            
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('index.html', form='form')
    
    return render_template("index.html")

@app.route("/slider")

def helloSlider():
    return '''
<html>
 
<body>
 
 
<div class="slidecontainer">
  <input type="range" min="1" max="100" value="50" class="slider" id="myRange">
  <p>Value: <span id="demo"></span></p>
</div>
 
<script>
var slider = document.getElementById("myRange");
var output = document.getElementById("demo");
output.innerHTML = slider.value;
 
slider.oninput = function() {
  output.innerHTML = this.value;
}
 
 
</script>
 
</body>
</html>
'''


if __name__ == "__main__":
    app.run(debug=True)
