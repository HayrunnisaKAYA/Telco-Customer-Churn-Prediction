import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

print("Model eğitiliyor ve arayüz için kaydediliyor...")

# 1. Temizlediğimiz veriyi yükle
df = pd.read_csv('Telco_Churn_Temiz.csv')

# 2. Arayüzün basit olması için sadece en önemli 3 kolonu seçiyoruz
X = df[['tenure', 'MonthlyCharges', 'TotalCharges']]

# 3. Churn kolonundaki Yes/No değerlerini makinenin anlaması için 1 ve 0'a çeviriyoruz
y = df['Churn'].map({'Yes': 1, 'No': 0})

# 4. Modeli eğit
model = LogisticRegression()
model.fit(X, y)

# 5. Eğitilmiş modeli Streamlit'in kullanması için diske kaydet
joblib.dump(model, 'churn_model.pkl')

print("Harika! 'churn_model.pkl' dosyası başarıyla oluşturuldu.")