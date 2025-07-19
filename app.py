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
        about="She restored me.",
        avatar="itzC9.jpg"
    )

@app.route("/mariii.xx")
def profile_mari():
    return render_template("profile.html",
        username="Mari",
        tag="mariii.xx",
        about="The love hate relantionship I have with quroot is insane like tell me why it tastes so good but I can’t even bite it or my teeth will break",
        avatar="mari.jpg"
    )

@app.route("/Good")
def profile_good():
    return render_template("profile.html",
        username="good",
        tag="goodgamerYTbro",
        about="Script developer and silent system builder. Good is reliable, focused, and thrives in the chaos of code.",
        avatar="good.jpg"
    )

@app.route("/Blaze")
def profile_blaze():
    return render_template("profile.html",
        username="Blaze",
        tag="echo_blaze",
        about="",
        avatar="blaze.jpg"
    )

if __name__ == "__main__":
    app.run(debug=False)
