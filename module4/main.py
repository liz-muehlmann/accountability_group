# Data analysis and visualization module
# use pandas, maploblib, plotly

# learn how to build api
# use html

# this step builds the webframe
from flask import Flask, render_template

app = Flask("Website")

# each web page should be in templates folder
# images should be in static folder

@app.route("/home")         # the @ symbol means it's a decorator
def home():
    return render_template("tutorial.html")
@app.route("/about/")
def about():
    return render_template("about.html")

app.run(debug=True)