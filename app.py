from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/itzC9")
def profile_itzc9():
    return render_template("profile.html",
        username="itzC9",
        tag="ug_32",
        about="itzC9 is a Roblox Coder since 2022. Once an exploiter, now an Exploiter Destroyer. Proud CEO of Velonix-Studio.",
        bg="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGZmZTVnaGd2bTU2dzhvdW5uYW00dmJmNm1kaDB5eTh2Z2JtazdyNiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/11JTxkrmq4bGE0/giphy.gif"
    )

@app.route("/mariii")
def profile_mari():
    return render_template("profile.html",
        username="Mari",
        tag="mariii.xx",
        about=".",
        bg="https://media.giphy.com/media/2xPPMjGclT7YsV6cL7/giphy.gif"
    )

@app.route("/good")
def profile_good():
    return render_template("profile.html",
        username="good",
        tag="goodgamerYTbro",
        about="Script engineer. Whisper in the Lua shadows. Master of silent tools and trusted hand of the crew.",
        bg="https://media.giphy.com/media/l0HlQ7LRalGq4fXvC/giphy.gif"
    )

@app.route("/Blaze")
def profile_blaze():
    return render_template("profile.html",
        username="Blaze",
        tag="echo_blaze",
        about=".",
        bg="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3lpOHZpaWJ5Z2V0aHZia3kxY3d2ZXp4bnJ3Yjk3NzR5Nm5waHFkaCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/1fGcRY5kYW4UGsn2kG/giphy.gif"
    )

if __name__ == "__main__":
    app.run(debug=False)
