from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

# Load pickle
with open("recommender.pkl", "rb") as f:
    data = pickle.load(f)

cosine_sim = data['cosine_sim']
movie_titles = data['movie_titles']

# Recommendation function
def recommend(movie_title):
    if movie_title not in movie_titles:
        return ["Movie not found."]
    idx = movie_titles.index(movie_title)
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_indices = [i[0] for i in sim_scores[1:11]]
    return [movie_titles[i] for i in top_indices]

@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = []
    if request.method == "POST":
        movie = request.form["movie"]
        recommendations = recommend(movie)
    return render_template("index.html", recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
