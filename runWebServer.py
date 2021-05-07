from flask import Flask, render_template

app = Flask(__name__)

#--------------------------------------------------------------------------------
# Menu principal de opciones
#--------------------------------------------------------------------------------
@app.route('/')
def index():
    return render_template('index.html')

#--------------------------------------------------------------------------------
# Opción hello
#--------------------------------------------------------------------------------
@app.route("/hello/")
def hello():
    return render_template('hello.html')
    #return 'Hello, World!'

#--------------------------------------------------------------------------------
# Main Routine
#--------------------------------------------------------------------------------
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True, threaded=True) 
