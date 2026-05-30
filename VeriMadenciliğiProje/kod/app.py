import streamlit as st
import joblib
import numpy as np

# Arka planda duran (backend) eğitilmiş modelimizi çağırıyoruz
model = joblib.load('churn_model.pkl')

st.set_page_config(page_title="Müşteri Kayıp Tahmin Paneli", layout="centered")

st.title("📊 Telekom Müşteri Kayıp (Churn) Tahmin Sistemi")
st.markdown("Bu panel, Telco veri seti üzerinde eğitilmiş **Lojistik Regresyon** modeli ile çalışmaktadır. Müşterinin sistemden çıkma (churn) riskini hesaplar.")
st.divider()

st.subheader("Müşteri Bilgilerini Giriniz")

# Arayüzdeki veri giriş kutuları (Frontend)
tenure = st.number_input("Müşteri kaç aydır sistemimize kayıtlı? (Tenure)", min_value=0, max_value=100, value=12)
aylik_ucret = st.number_input("Aylık Fatura Tutarı ($)", min_value=0.0, value=50.0)
toplam_ucret = st.number_input("Toplam Harcama ($)", min_value=0.0, value=600.0)

# Tahmin Butonu
if st.button("Riski Hesapla", use_container_width=True):
    # Girilen verileri modelin anlayacağı diziye çevir
    veri = np.array([[tenure, aylik_ucret, toplam_ucret]])
    
    # Modelden tahmini ve olasılık yüzdesini al
    tahmin = model.predict(veri)
    olasilik = model.predict_proba(veri)[0][1] # Churn olma (1) ihtimali
    
    st.divider()
    
    # Sonucu ekrana yazdır
    if tahmin[0] == 1:
        st.error(f"⚠️ **YÜKSEK RİSK:** Bu müşterinin aboneliğini iptal etme ihtimali **%{olasilik*100:.1f}**. Özel promosyon veya indirim sunulması tavsiye edilir!")
    else:
        st.success(f"✅ **GÜVENLİ:** Müşterinin sistemde kalma ihtimali yüksek. (Risk Oranı: **%{olasilik*100:.1f}**)")