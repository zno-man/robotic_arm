from flask import Flask #pip install flask (or) sudo apt install python3-flask
from flask_cors import CORS #pip install -U flask-cors 
 
app = Flask(__name__)
CORS(app)
 
 
@app.route("/")
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
