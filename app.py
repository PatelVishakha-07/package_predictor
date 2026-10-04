import pickle
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/", methods=["POST", "GET"])
def home():
    result, error = None, None
    if request.method == "POST":
        try:
            cgpa = float(request.form["cgpa"])
            if not 0 <= cgpa <= 10:
                raise ValueError

            pred = model.predict(pd.DataFrame({"cgpa":[cgpa]}))[0]
            result = round(max(float(pred.ravel()[0]), 0), 2)

        except ValueError:
            error = "Please enter a CGPA between 0 and 10."
    return render_template("index.html", result=result, error = error)

if __name__ == "__main__":
    app.run(debug=True)