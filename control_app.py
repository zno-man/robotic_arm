from flask import Flask, render_template, request
from flask_cors import CORS #pip install -U flask-cors 

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action1') == 'VALUE1':
            pass # do something
        elif  request.form.get('action2') == 'VALUE2':
            pass # do something else
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
