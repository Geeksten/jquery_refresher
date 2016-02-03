from flask import Flask, request, render_template, redirect, flash
import os
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = 'ABC'

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def homepage():
    """This is the homepage"""
    # give the user the home:
    return render_template("jquery_intro.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)