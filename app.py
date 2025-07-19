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
        about="That one girl, restored my life.",
        avatar="https://cdn.discordapp.com/attachments/1387996706074792016/1396123221685833798/mari.jpg",
        bg="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGZmZTVnaGd2bTU2dzhvdW5uYW00dmJmNm1kaDB5eTh2Z2JtazdyNiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/11JTxkrmq4bGE0/giphy.gif"
    )

@app.route("/mariii.xx")
def profile_mari():
    return render_template("profile.html",
        username="Mari",
        tag="mariii.xx",
        about="The love hate relantionship I have with quroot is insane like tell me why it tastes so good but I can’t even bite it or my teeth will break",
        avatar="https://cdn.discordapp.com/attachments/1387996706074792016/1396123221685833798/mari.jpg",
        bg="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGZmZTVnaGd2bTU2dzhvdW5uYW00dmJmNm1kaDB5eTh2Z2JtazdyNiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/11JTxkrmq4bGE0/giphy.gif"
    )

@app.route("/Good")
def profile_good():
    return render_template("profile.html",
        username="good",
        tag="goodgamerYTbro",
        about="Script developer and silent system builder. Good is reliable, focused, and thrives in the chaos of code.",
        avatar="https://cdn.discordapp.com/attachments/1387996706074792016/1396123221685833798/mari.jpg",
        bg="https://media.giphy.com/media/l0HlQ7LRalGq4fXvC/giphy.gif"
    )

@app.route("/Blaze")
def profile_blaze():
    return render_template("profile.html",
        username="Blaze",
        tag="echo_blaze",
        about="",
        avatar="https://cdn.discordapp.com/attachments/1387996706074792016/1396123221685833798/mari.jpg",
        bg="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3lpOHZpaWJ5Z2V0aHZia3kxY3d2ZXp4bnJ3Yjk3NzR5Nm5waHFkaCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/1fGcRY5kYW4UGsn2kG/giphy.gif"
    )

if __name__ == "__main__":
    app.run(debug=False)
