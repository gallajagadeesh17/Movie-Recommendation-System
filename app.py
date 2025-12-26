from flask import Flask, render_template, request
from model import recommend

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    movies = []
    mood = None

    if request.method == "POST":
        mood = request.form.get("mood")
        country = request.form.get("country")
        language = request.form.get("language")

        movies = recommend(mood, country, language)

    return render_template(
        "index.html",
        movies=movies,
        selected_mood=mood
    )

if __name__ == "__main__":
    app.run(debug=True)
