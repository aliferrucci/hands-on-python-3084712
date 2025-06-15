from flask import Flask

app = Flask(__name__)

# To make this method a route in Flask use decorator
# This is the base route defined by "/"
@app.route("/")
def hello():
  return "Hello, World!"

# Running flask application
app.run(debug=True)
