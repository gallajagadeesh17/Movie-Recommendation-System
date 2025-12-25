from flask import Flask, render_template, request
from model import recommend

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    movies = []
    selected_mood = None

    if request.method == "POST":
        selected_mood = request.form.get("mood")
        country = request.form.get("country")
        language = request.form.get("language")

        movies = recommend(selected_mood, country, language)

    return render_template(
        "index.html",
        movies=movies,
        selected_mood=selected_mood
    )

# ✅ THIS MUST BE OUTSIDE THE FUNCTION
if __name__ == "__main__":
    app.run()
