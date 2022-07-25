#from turtle import title
from flask import render_template
from l7challenge_flask import routes, app
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title='Home')

@app.route("/widgets")
def widgets():
    return render_template("widgets.html", title='Widgets')

@app.route("/benford")
def benford():
    return render_template("benford.html", title="Benford's Law")

@app.route("/stack_traces")
def stack_traces():
    return render_template("stack_traces.html", title='Python Stack Traces')

