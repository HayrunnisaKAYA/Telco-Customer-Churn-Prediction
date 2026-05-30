import pandas as pd

# 1. Veriyi yükle (Dosya adının doğru olduğundan emin ol)
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

# 2. TotalCharges sütununu sayısal (numeric) tipe zorla.
# errors='coerce' parametresi, boşluk veya harf görürse onu anında NaN (eksik veri) yapar.
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# 3. Eksik verileri (henüz 0 aylık olan yeni müşterileri) 0 ile doldur
df['TotalCharges'] = df['TotalCharges'].fillna(0)

# Gereksiz kimlik sütununu modelin kafasını karıştırmaması için atalım
df = df.drop('customerID', axis=1)

# 4. Temizlenmiş veriyi yeni bir CSV olarak kaydet
df.to_csv('Telco_Churn_Temiz.csv', index=False)

print("Veri başarıyla temizlendi ve 'Telco_Churn_Temiz.csv' olarak kaydedildi!")