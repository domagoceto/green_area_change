🌿 Yeşil Alan Değişim Analizi ve Tahmini

Bu proje, 2016 - 2024 yılları arasında seçilen bir şehir ve ilçenin yeşil alan değişimini analiz etmeyi ve gelecek yıllardaki tahmini değişiklikleri hesaplamayı amaçlamaktadır. Google Earth Engine (GEE), Sentinel-2 uydu görüntüleri, Python, Flask ve XGBoost algoritması kullanılarak geliştirilmiştir.

![Ekran görüntüsü 2025-02-03 133834](https://github.com/user-attachments/assets/9ffad71c-28ad-401e-b90d-c9ea545edee1)

🚀 Proje Özeti
Projemiz, seçilen şehir ve ilçedeki yeşil alan değişimini analiz ederek aşağıdaki hedefleri gerçekleştirmektedir:

Google Earth Engine (GEE) ve Sentinel-2 uydu görüntüleri kullanarak yeşil alanların belirlenmesi
2016 - 2024 yılları arasındaki yeşil alan değişiminin hesaplanması
XGBoost makine öğrenme algoritması ile gelecek yıllardaki yeşil alan değişiminin tahmin edilmesi
Kullanıcı dostu bir arayüz sağlayarak şehir ve ilçe bazında yeşil alan değişiminin görselleştirilmesi

📌 Kullanılan Teknolojiler
Teknoloji	Kullanım Amacı
Python	Veri işleme ve modelleme
Google Earth Engine (GEE)	Uydu görüntüleri ile analiz
Sentinel-2	Yeşil alan tespiti için uydu görüntüleri
Flask	Web arayüzü geliştirme
XGBoost	Yeşil alan değişim tahmini
Pandas, NumPy, Geopandas	Veri işleme ve analiz
Matplotlib, Seaborn	Görselleştirme

![Ekran görüntüsü 2025-02-03 134033](https://github.com/user-attachments/assets/0882a74e-5105-4cc7-8257-20756eccf957)

📊 Proje İşleyişi

1️⃣ Veri Toplama ve Ön İşleme
Google Earth Engine (GEE) üzerinden Sentinel-2 uydu görüntüleri alınır.
NDVI (Normalized Difference Vegetation Index) hesaplanarak yeşil alanlar belirlenir.
İlgili şehir ve ilçeye ait yeşil alan verileri 2016-2024 yılları arasında toplanır.
2️⃣ Yeşil Alan Değişiminin Hesaplanması
Yıllara göre ortalama NDVI değerleri ve toplam yeşil alan hektar cinsinden hesaplanır.
Değişimler şehir ve ilçe bazında görselleştirilir.
3️⃣ Makine Öğrenmesi ile Gelecek Tahmini
XGBoost algoritması kullanılarak gelecek yıllardaki yeşil alan değişimi tahmin edilir.
Model, geçmiş verilerden öğrenerek olası kayıp veya kazanımları öngörür.
4️⃣ Web Arayüzü ile Kullanıcı Etkileşimi
Flask tabanlı bir web arayüzü geliştirilmiştir.
Kullanıcılar şehir ve ilçeyi seçerek değişim analizini görebilir.
Gelecek yıllara yönelik tahmin sonuçları görselleştirilir.

![Ekran görüntüsü 2025-02-03 134108](https://github.com/user-attachments/assets/1c12125a-2be6-4022-bdd6-d265d49ff69d)

Geliştirme Süreci
✅ Google Earth Engine API ile Sentinel-2 görüntülerinin işlenmesi
✅ NDVI hesaplanarak yeşil alan tespiti
✅ GEE'den elde edilen verilerle veri setinin oluşturulması
✅ XGBoost algoritması ile tahmin modeli eğitilmesi
✅ Flask tabanlı web arayüzünün oluşturulması
✅ Veri görselleştirme ve analizlerin yapılması

📩 İletişim


