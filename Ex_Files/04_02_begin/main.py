from distutils.log import debug
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hell():
  return "Hello, World!"

app.run(debug=True)