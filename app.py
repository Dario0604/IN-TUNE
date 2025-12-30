from flask import Flask, render_template, request, redirect, url_for
import random
from songs import mood_songs

app = Flask(__name__)

def get_random_songs(mood, limit=5):
    return random.sample(mood_songs[mood], k=min(limit, len(mood_songs[mood])))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/results", methods=["POST"])
def results():
    mood = request.form.get("mood")

    if mood == "happy":
        return redirect(url_for("happy"))
    elif mood == "reflective":
        return redirect(url_for("reflective"))
    elif mood == "energetic":
        return redirect(url_for("energetic"))
    elif mood == "chill":
        return redirect(url_for("chill"))

    return redirect("/")


@app.route("/happy")
def happy():
    songs = get_random_songs("happy")
    return render_template("happy.html", songs=songs)


@app.route("/reflective")
def reflective():
    songs = get_random_songs("reflective")
    return render_template("reflective.html", songs=songs)


@app.route("/energetic")
def energetic():
    songs = get_random_songs("energetic")
    return render_template("energetic.html", songs=songs)


@app.route("/chill")
def chill():
    songs = get_random_songs("chill")
    return render_template("chill.html", songs=songs)


if __name__ == "__main__":
    app.run()
