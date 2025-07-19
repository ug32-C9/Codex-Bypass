from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/itzC9")
def profile_itzc9():
    return render_template("profile.html", username="itzC9", tag="ug_32", about="itzC9 is Roblox Coder back in 2022. Used to exploit games. But now back – not as an exploiter, but as Exploiter Destroyer. Proud CEO of Velonix-Studio!", avatar="itzC9.jpg")

@app.route("/Mari")
def profile_mari():
    return render_template("profile.html", username="Mari", tag="mari", about=".", avatar="mari.jpg")

@app.route("/good")
def profile_good():
    return render_template("profile.html", username="good", tag="goodgamerYTbro", about="Script developer and helper. Working on Velonix Scripts.", avatar="good.jpg")

@app.route("/Blaze")
def profile_blaze():
    return render_template("profile.html", username="Blaze", tag="echo_blaze", about="Web Developer, Loves Gay Person and Lua scripts.", avatar="blaze.jpg")

if __name__ == "__main__":
    app.run(debug=False)
