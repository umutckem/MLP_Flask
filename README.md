# Öğrenci Performans Tahmini (MLP_Flask)

Ad Soyad: Umutcan Kemahlı
Okul No: 2212721050

Bu küçük proje, makine öğrenmesi modeli kullanarak bir öğrencinin performans skorunu tahmin eden Flask tabanlı bir web uygulamasıdır. Proje, bir Jupyter Notebook içinde veri temizleme ve model eğitimi adımlarını içerir ve eğitilmiş model `model.pkl` dosyası olarak kaydedilip `app.py` tarafından yüklenir.

**Özeti**
- Web arayüzü: `templates/index.html` — kullanıcıdan özellikleri alan ve tahmini gösteren şık bir form.
- Sunucu: `app.py` — Flask uygulaması; `GET /` ile formu gösterir, `POST /predict` ile tahmin yapar.
- Model: `model.pkl` — `app.py` tarafından yüklenen eğitilmiş model (repo içinde yoksa kullanıcı eğitmelidir).
- Eğitim adımları: `Uygulama_3.ipynb` — veri temizleme (imputation), özellik mühendisliği ve model eğitimi adımları içerir.

**Gereksinimler**
- Python 3.8+ (tercihen 3.8-3.11)
- Paketler (örnek): `flask`, `numpy`, `pandas`, `scikit-learn`, `statsmodels` (Notebook için), `joblib` veya `pickle` (pickle standart kütüphanedir)

Hızlı yükleme örneği (PowerShell):

```powershell
python -m pip install --upgrade pip
python -m pip install flask numpy pandas scikit-learn statsmodels
```

**Kurulum ve Çalıştırma**
1. Çalışma dizinine gidin (örnek):

```powershell
cd "C:\Users\Windows\Desktop\MLP_Flask"
```

2. Eğer henüz oluşturulmadıysa, `model.pkl` dosyasını hazırlayın:
   - `Uygulama_3.ipynb` içindeki eğitim hücrelerini kullanarak modeli eğitin ve pickle (`pickle.dump`) ile `model.pkl` adıyla proje köküne kaydedin.
   - Alternatif olarak, kendi eğitilmiş modelinizi `model.pkl` adıyla aynı klasöre koyun.

3. Flask uygulamasını çalıştırın:

```powershell
python app.py
```

Varsayılan olarak uygulama `http://127.0.0.1:5000/` adresinde çalışacaktır.

**Kullanım**
- Tarayıcıda `http://127.0.0.1:5000/` adresini açın.
- Formu doldurun:
  - `Çalışılan Saat` (`Hours Studied`) — sayısal
  - `Önceki Not Ortalaması` (`Previous Scores`) — sayısal
  - `Ekstraküriküler Etkinlik` (`Extracurricular Activities`) — 1 (var) veya 0 (yok)
  - `Uyku Süresi` (`Sleep Hours`) — sayısal
  - `Çözülen Örnek Soru Sayısı` (`Sample Question Papers Practiced`) — sayısal
- Gönderince `index.html` içinde `result` alanında tahmin gösterilir.

**Model Girdi Sıralaması**
- `app.py` içindeki model çağrısı şu biçimi bekler: `np.array([[1, Hours, Prev, Extra, Sleep, Papers]])`.
  - Burada ilk eleman sabit `1` (intercept/constant) olarak eklenmiştir. Eğer modelinizi eğitirken intercept dahil farklı bir sıra kullandıysanız, `app.py` dosyasını buna göre güncelleyin.

**Dosya Açıklamaları**
- `app.py` — Flask sunucusu ve tahmin endpoint'i.
- `templates/index.html` — kullanıcı arayüzü (form + sonuç gösterimi). Stil ve düzen HTML içinde inline CSS ile tanımlanmıştır.
- `Uygulama_3.ipynb` — veriyi temizleme, eksik değerleri doldurma, model eğitimi ve kaydetme adımlarını içeren notebook.
- `model.pkl` — eğitilmiş model dosyası (gerekli, repo içinde yoksa oluşturulmalıdır).

**Hata Ayıklama / Notlar**
- `ModuleNotFoundError` veya eksik paket hatası alırsanız gereken paketleri yükleyin.
- `FileNotFoundError: model.pkl` hatası alırsanız model dosyasının proje kökünde olduğundan emin olun.
- Modelin beklediği özellik sırası ile `app.py` içindeki giriş sırasının uyumlu olması önemlidir.


# Ekran Görüntüsü index.html

<img width="1898" height="901" alt="Ekran görüntüsü 2025-12-07 194131" src="https://github.com/user-attachments/assets/a97c6aa0-de22-4242-9912-c50233bb2111" />
