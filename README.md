
**BLM308 VERİ MADENCİLİĞİ FİNAL PROJESİ
Proje Başlığı: Telekom Müşteri Kaybı (Churn) Tahmini ve Web Arayüzü
Dönem: Bahar 2026

TAKIM ÜYELERİ VE ROLLERİ:
1. Fatma Nur Atagün - 231041022 -> Veri ve Model Mühendisi
2. Hayrunnisa Kaya - 231041047 -> Değerlendirme ve Raporlama

KLASÖR YAPISI VE İÇERİKLERİ:
📁 veri/
   - WA_Fn-UseC_-Telco-Customer-Churn.csv (Kaggle'dan alınan orijinal raw veri)
   - Telco_Churn_Temiz.csv (Python ile ön işlemeden geçirilmiş temiz veri)

📁 kod/
   - on_isleme.py: Orijinal verideki gizli boşlukları ve eksikleri temizleyen script.
   - model.py: Weka sonuçlarını doğrulamak için Python'da yazılan model.
   - xai_analizi.py: Modelin kararlarını açıklamak için SHAP kullanan analiz scripti.
   - shap_grafigi.png: SHAP analizi sonucunda üretilen görsel.
   - model_kaydet.py: Web arayüzü için Lojistik Regresyon modelini diske kaydeden script.
   - app.py: Streamlit ile geliştirilen Müşteri Risk Paneli web arayüzü.
   - churn_model.pkl: Eğitilmiş ML model dosyası.
   - lojistik_model.model: Weka'dan export edilen şampiyon model dosyası.
   - weka_sonuclar_*.txt: Weka algoritmalarının (J48, NaiveBayes, Logistic, RandomForest) sonuç ve hata analizi (Confusion Matrix) çıktıları.

📄 rapor.docx
   - CRISP-DM süreçlerini, analizleri, metrikleri ve iş değeri yorumlarını içeren final raporu.


**PROJEYİ (WEB ARAYÜZÜNÜ) ÇALIŞTIRMA TALİMATLARI:


Projeye eklenen "Açık Uçlu Bonus" kapsamında, eğitilen model bir web arayüzüne (Streamlit) entegre edilmiştir. Uygulamayı ayağa kaldırmak için:

1. Terminal veya Komut İstemcisini (cmd) açın.
2. "kod" klasörünün dizinine gidin.
3. Gerekli kütüphanelerin yüklü olduğundan emin olun:
   > pip install pandas scikit-learn streamlit joblib shap matplotlib
4. Web arayüzünü başlatmak için şu komutu çalıştırın:
   > streamlit run app.py
5. Tarayıcınızda açılan panel üzerinden müşteri değerlerini girerek anlık Churn riski hesaplayabilirsiniz.
   
