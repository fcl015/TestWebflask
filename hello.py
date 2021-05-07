from flask import Flask

app = Flask(__name__)

@app.route("/hello/")
def hello():
    return 'Hola Mundo!'

if __name__ == "__main__":
   #Run web server
   app.run(host='192.4.68.5', port=8000, debug=True, threaded=True) 
