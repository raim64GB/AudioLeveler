import os
from flask import Flask, flash, redirect, render_template, request, session, abort

template_dir = os.path.abspath('../templates')

app = Flask(__name__, template_folder=template_dir)

@app.route("/")
def index():
    return render_template(
        'index.html')

@app.route("/login")
def login():
    return render_template(
        'login.html')

@app.route("/set_volume", methods=["POST"])
def setVolume():
    volume = request.form["volumeSet"]
    return volume


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)