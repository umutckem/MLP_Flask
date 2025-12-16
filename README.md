# Çoklu Doğrusal Regresyon ve Flask GUI Uygulaması

## 👤 Öğrenci Bilgileri
- **Ad Soyad:** Umutcan Kemahlı
- **Okul Numarası:** 2212721050
- **GitHub Repo:** https://github.com/umutckem/MLP_Flask

---

## 📌 Proje Tanımı
Bu projede, seçilen bir veri seti üzerinde **Çoklu Doğrusal Regresyon (Multiple Linear Regression)** modeli oluşturulmuş ve elde edilen tahmin modeli **Flask tabanlı bir web arayüzü** ile kullanıcıya sunulmuştur.

Proje kapsamında veri ön işleme, öznitelik seçimi, eksik veri analizi, kategorik veri kodlama, Backward Elimination yöntemi, model değerlendirme metrikleri ve Flask arayüz geliştirme adımları eksiksiz şekilde uygulanmıştır.

---

## 📊 Kullanılan Veri Seti
**Medical Insurance Cost Dataset**

Veri seti, bireylerin demografik ve sağlık bilgilerine göre sigorta maliyetlerini içermektedir.

### Kullanılan Değişkenler:
- **age:** Yaş
- **bmi:** Vücut Kitle İndeksi
- **children:** Çocuk sayısı
- **sex:** Cinsiyet
- **smoker:** Sigara kullanımı
- **region:** Bölge
- **charges:** Sigorta ücreti (hedef değişken)

---

## ⚙️ Veri Ön İşleme Aşamaları

### 🔹 Öznitelik Seçimi
Modelde kullanılacak öznitelikler seçilmiş, gereksiz ve modele katkı sağlamayan değişkenler veri setinden çıkarılmıştır. Toplam öznitelik sayısı maksimum 10 olacak şekilde sınırlandırılmıştır.

### 🔹 Kayıp Veri Analizi
Veri setinde başlangıçta eksik değer bulunmadığından, gerçek hayat senaryosunu simüle etmek amacıyla rastgele seçilen 20 hücrede eksik veri oluşturulmuştur.

- Sayısal değişkenlerde eksik değerler **medyan (median)** yöntemi ile doldurulmuştur.
- Kategorik değişkenlerde eksik değerler **mod (mode)** yöntemi ile doldurulmuştur.

Bu yöntemler, veri setinin genel dağılımını korumak amacıyla tercih edilmiştir.

### 🔹 Kategorik Verilerin Kodlanması
Sayısal olmayan değişkenler, modele uygun hale getirilmesi için **One-Hot Encoding** yöntemi ile kodlanmıştır.  
`drop_first=True` parametresi kullanılarak çoklu doğrusal bağlantı (dummy variable trap) problemi önlenmiştir.

---

## 🔍 Backward Elimination
İstatistiksel olarak anlamsız değişkenleri belirlemek amacıyla **Backward Elimination** yöntemi uygulanmıştır.

- Tüm özniteliklerle model kurulmuş
- p-value değerleri incelenmiş
- p-value > 0.05 olan değişkenler birer birer modelden çıkarılmıştır
- Sadece istatistiksel olarak anlamlı değişkenlerden oluşan nihai model elde edilmiştir

---

## 📈 Model Kurulumu ve Değerlendirme

Model olarak **Çoklu Doğrusal Regresyon** kullanılmıştır.  
Veri seti %80 eğitim, %20 test olacak şekilde ayrılmıştır.

### Kullanılan Değerlendirme Metrikleri:
- **R² (R Kare)**
- **MAE (Mean Absolute Error)**
- **MSE (Mean Squared Error)**

Elde edilen sonuçlar, modelin sigorta maliyetlerini tahmin etmede başarılı bir performans sergilediğini göstermektedir.

---

## 🌐 Flask Web Uygulaması
Eğitilen model `.pkl` formatında kaydedilmiş ve Flask tabanlı bir web arayüzü ile kullanıcıya sunulmuştur.

Web arayüzü üzerinden:
- Kullanıcıdan model giriş değişkenleri alınmakta
- Girilen değerlere göre tahmini sigorta ücreti hesaplanmakta
- Sonuç ekranda görüntülenmektedir

---

## 📁 Proje Dosya Yapısı

```text
MLP_Flask/
│
├── app.py
├── model.pkl
├── model_columns.pkl
├── insurance_filled.csv
│
├── static/
│   └── gorsel.jpg 
├── templates/
│   └── index.html
│
└── README.md


## Poje Görselleri

<img width="1916" height="911" alt="Ekran görüntüsü 2025-12-16 122916" src="https://github.com/user-attachments/assets/06f5c13e-2f34-47ce-857e-9574ecea625a" />

<img width="1919" height="907" alt="Ekran görüntüsü 2025-12-16 122923" src="https://github.com/user-attachments/assets/43c6da84-edde-44dd-95f2-a865f7490e62" />
