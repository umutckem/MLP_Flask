from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Model ve kolonları yükle
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("model_columns.pkl", "rb") as f:
    model_columns = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        # Kullanıcıdan gelen veriler
        age = int(request.form["age"])
        bmi = float(request.form["bmi"])
        children = int(request.form["children"])
        sex = request.form["sex"]
        smoker = request.form["smoker"]
        region = request.form["region"]

        # Boş dataframe (model kolonlarına göre)
        input_df = pd.DataFrame(0, index=[0], columns=model_columns)

        # Sayısal değerler
        input_df["age"] = age
        input_df["bmi"] = bmi
        input_df["children"] = children

        # One-Hot Encoding eşleştirmesi
        if f"sex_{sex}" in input_df.columns:
            input_df[f"sex_{sex}"] = 1

        if f"smoker_{smoker}" in input_df.columns:
            input_df[f"smoker_{smoker}"] = 1

        if f"region_{region}" in input_df.columns:
            input_df[f"region_{region}"] = 1

        # Tahmin
        prediction = model.predict(input_df)[0]

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
