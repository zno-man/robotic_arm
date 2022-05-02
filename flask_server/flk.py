#!/usr/bin/env python3
import time
from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS #pip install -U flask-cors 


lnk1 = 0
lnk2 = 0
lnk3 = 0
state = 0
ch_t1 = 0
ch_t2 = 0
ch_t3 = 0
ch_t4 = 0

lo1 = [50,0,50] #pick up 
lo2 = [100 , 50 , 0] #collection 
lo3 = [-100 ,50 , 0] #deposit

def write_data():
    global state,ch_t1,ch_t2,ch_t3,ch_t4,lo1,lo2,lo3
    f = open("communication.txt","w")
    lst = []
    val1 = state
    val2 = 0
    val3 = 0
    val4 = 0
    val5 = 0
    val6 = 0
    val7 = 0
    val8 = 0 
    val9 = 0
    val10 = 0

    if state == 1:
        val2 = lo1[0]
        val3 = lo1[1]
        val4 = lo1[2]
        val5 = lo2[0]
        val6 = lo2[1]        
        val7 = lo2[2]
        val8 = lo3[0]
        val9 = lo3[1]
        val10 = lo3[2]



    elif state == 8:
        val2 = ch_t1
        val3 = ch_t2
        val4 = ch_t3
        val5 = ch_t4
    print([val1,val2,val3,val4,val5,val6,val7,val8,val9,val10])
    for i in [val1,val2,val3,val4,val5,val6,val7,val8,val9,val10]:
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

app = Flask(__name__,template_folder='templates')
CORS(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    global lnk1,lnk2,lnk3,state

    if request.method == 'POST':
        if request.form.get('1') == 'Configure':
            print("config")
            state = 1
            return redirect(url_for('my_form'))

            
        elif  request.form.get('2') == 'Pickup Location':
            state = 2
            set_data()
        elif  request.form.get('3') == 'Collection Location':
            state = 3 
            set_data()
        elif  request.form.get('4') == 'Deposit Location':
            state = 4
            set_data()
        elif  request.form.get('5') == 'Pickup Operation':
            state = 5
            set_data()
        elif  request.form.get('6') == 'Collection Operation':
            state = 6
            set_data()
        elif  request.form.get('7') == 'Deposit Operation':
            state = 7
            set_data()

        elif  request.form.get('8') == 'Adjust Angles':
            state = 8
            return redirect(url_for('adjust'))
            
        elif  request.form.get('9') == 'Previous Tip Location  ':
            state = 9
            set_data()
                      
        else:
            pass # unknown

    elif request.method == 'GET':
        return render_template('index.html', form='form')
    
    return render_template("index.html")


@app.route('/configu')
def my_form():
    return render_template('my-form.html')

@app.route('/configu', methods=['POST'])
def my_form_post():
    global lo1,lo2,lo3
    
    x1 = float(request.form['x1'])
    y1 = float(request.form['y1'])
    z1 = float(request.form['z1'])
    
    x2 = float(request.form['x2'])
    y2 = float(request.form['y2'])
    z2 = float(request.form['z2'])
    
    x3 = float(request.form['x3'])
    y3 = float(request.form['y3'])
    z3 = float(request.form['z3'])
    lo1 = [x1,y1,z1]
    lo2 = [x2,y2,z2]
    lo3 = [x3,y3,z3]
    
    print(x1,y1,z1," ",x2,y2,z2," ",x3,y3,z3)
    set_data()
    return redirect(url_for('index'))



@app.route("/adjust", methods=['GET', 'POST'])
def adjust():
    global ch_t1,ch_t2,ch_t3,ch_t4

    if request.method == 'POST':
        if request.form.get('-1') == '-':
            ch_t1 = -1
        elif  request.form.get('+1') == '+':
            ch_t1 = +1
        elif  request.form.get('-2') == '-':
            ch_t2 = -1
        elif  request.form.get('+2') == '+':
            ch_t2 = +1
        elif  request.form.get('-3') == '-':
            ch_t3 = -1
        elif  request.form.get('+3') == '+':
            ch_t3 = +1
        elif  request.form.get('-4') == '-':
            ch_t4 = -1
        elif  request.form.get('+4') == '+':
            ch_t4 = +1
        elif  request.form.get('5') == 'back':
            return redirect(url_for('index'))
        
    elif request.method == 'GET':
        return render_template('adjust.html', form='form')
    

    set_data()
    ch_t1 = 0
    ch_t2 = 0
    ch_t3 = 0
    ch_t4 = 0
    return render_template("adjust.html")




# @app.route("/slider")

# def helloSlider():
#     return '''
# <html>
 
# <body>
 
 
# <div class="slidecontainer">
#   <input type="range" min="1" max="100" value="50" class="slider" id="myRange">
#   <p>Value: <span id="demo"></span></p>
# </div>
 
# <script>
# var slider = document.getElementById("myRange");
# var output = document.getElementById("demo");
# output.innerHTML = slider.value;
 
# slider.oninput = function() {
#   output.innerHTML = this.value;
# }
 
 
# </script>
 
# </body>
# </html>
# '''


if __name__ == "__main__":
    app.run(debug=True)
