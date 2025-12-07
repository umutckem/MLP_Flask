from flask import Flask, render_template, request
import pickle
import numpy as np

# Flask uygulamasını başlatıyoruz
app = Flask(__name__)

# ----------------------------
# 1) Eğitilmiş modeli yükleme
# ----------------------------
# model.pkl dosyasını aynı klasörde olmalı
model = pickle.load(open("model.pkl", "rb"))


# ----------------------------
# 2) Ana sayfa (form)
# ----------------------------
@app.route("/")
def index():
    return render_template("index.html")


# ----------------------------
# 3) Tahmin işlemi
# ----------------------------
@app.route("/predict", methods=["POST"])
def predict():
    Hours = float(request.form["Hours Studied"])
    Prev = float(request.form["Previous Scores"])
    Extra = float(request.form["Extracurricular Activities"])
    Sleep = float(request.form["Sleep Hours"])
    Papers = float(request.form["Sample Question Papers Practiced"])

    # MODELIN BEKLEDİĞİ SIRAYA GÖRE 6 FEATURE
    # İlk özellik: const = 1
    input_data = np.array([[1, Hours, Prev, Extra, Sleep, Papers]])

    prediction = model.predict(input_data)[0]

    return render_template(
        "index.html",
        result=f"Tahmin Edilen Performans Skoru: {round(prediction, 2)}"
    )



# ----------------------------
# 4) Uygulamayı çalıştırma
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)
