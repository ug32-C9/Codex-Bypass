from flask import Flask, render_template

app = Flask(name)

@app.route("/") def index(): return render_template("index.html")

@app.route("/itzC9") def profile_itzc9(): return render_template("profile.html", username="itzC9", tag="ug_32", about="That one girl, restored my life.", bg="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGZmZTVnaGd2bTU2dzhvdW5uYW00dmJmNm1kaDB5eTh2Z2JtazdyNiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/11JTxkrmq4bGE0/giphy.gif", avatar="static/itzc9.jpg" )

@app.route("/mariii") def profile_mari(): return render_template("profile.html", username="Mari", tag="mariii.xx", about="", bg="https://media.giphy.com/media/2xPPMjGclT7YsV6cL7/giphy.gif", avatar="static/mari.jpg" )

@app.route("/good") def profile_good(): return render_template("profile.html", username="good", tag="goodgamerYTbro", about="They built walls? > We forged a KEY THAT BITES BACK. > Paste it.  > Feel the lock scream. > Click it. > Hear reality CRACK. > RISE through the rubble— > not user… > GOD of the ghost-light. > Velonix Bupass: > Where firewalls go to DIE. > Your world.", bg="https://media.giphy.com/media/l0HlQ7LRalGq4fXvC/giphy.gif", avatar="static/good.jpg" )

@app.route("/Blaze") def profile_blaze(): return render_template("profile.html", username="Blaze", tag="echo_blaze", about=".", bg="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3lpOHZpaWJ5Z2V0aHZia3kxY3d2ZXp4bnJ3Yjk3NzR5Nm5waHFkaCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/1fGcRY5kYW4UGsn2kG/giphy.gif", avatar="static/blaze.jpg" )

if name == "main": app.run(debug=False)

