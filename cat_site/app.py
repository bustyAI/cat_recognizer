from flask import Flask, render_template, url_for, request
import torch
import pickle

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")

def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    img = request.form["cat"]

    return render_template("index.html", pred_text=f"Hello")

if __name__ == "__main__":
    app.run()
