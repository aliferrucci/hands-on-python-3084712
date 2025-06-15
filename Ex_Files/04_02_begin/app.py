import csv
from flask import Flask, render_template, jsonify


app = Flask(__name__)

with open("laureates.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)


@app.route("/")
def index():
    # template found in templates/index.html
    # render_template will render the HTML file (index.html)
    # it will call the laureates endpoint
    # which will return the laureates data in JSON format
    # and pass it to the template
    return render_template("index.html")


@app.route("/laureates/")
def laureate():
    return jsonify(laureates)


app.run(debug=True)
