from flask import Flask

app = Flask(__name__)

@app.route("/hello/")
def hello():
    return 'Hello, World!'

if __name__ == "__main__":
   #Run web server
   app.run(host='0.0.0.0', port=80, debug=True, threaded=True) 