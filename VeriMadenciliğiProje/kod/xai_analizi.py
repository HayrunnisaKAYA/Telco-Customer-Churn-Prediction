import pandas as pd
import shap
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

print("XAI (SHAP) Analizi başlatılıyor...")

# 1. Veriyi Hazırla
df = pd.read_csv('Telco_Churn_Temiz.csv')
X = df.drop('Churn', axis=1)
y = df['Churn'].map({'Yes': 1, 'No': 0})
X = pd.get_dummies(X, drop_first=True)

# İŞTE SİHİRLİ DOKUNUŞ BURADA: True/False (boolean) olan tüm kolonları kesin olarak sayıya (float) çeviriyoruz!
X = X.astype(float)

# 2. Veriyi Böl ve Modeli Eğit
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression(max_iter=3000)
model.fit(X_train, y_train)

# 3. SHAP Açıklayıcısını Kur
explainer = shap.LinearExplainer(model, X_train)

print("SHAP değerleri hesaplanıyor...")
shap_values = explainer.shap_values(X_test)

# 4. SHAP Özet Grafiğini Çizdir ve Kaydet
plt.figure(figsize=(10, 6))
shap.summary_plot(shap_values, X_test, show=False)
plt.title("SHAP Ozet Grafigi: Churn Kararini Etkileyen Faktorler")
plt.tight_layout()
plt.savefig("shap_grafigi.png", dpi=300)
print("Başarılı! 'shap_grafigi.png' dosyası klasöre kaydedildi.")