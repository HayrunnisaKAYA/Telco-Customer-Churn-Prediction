import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

print("Veri yükleniyor ve model eğitiliyor, lütfen bekleyin...")

# 1. Temizlenmiş veriyi yükle
df = pd.read_csv('Telco_Churn_Temiz.csv')

# 2. X (Özellikler) ve y (Hedef değişken) olarak ayır
X = df.drop('Churn', axis=1)
y = df['Churn']

# 3. Kategorik (yazı tipli) verileri makinenin anlayacağı sayısala çevir (One-Hot Encoding)
X = pd.get_dummies(X, drop_first=True)

# 4. Modeli tanımla (Adım sayısını 3000'e çıkardık ki uyarı vermesin)
model = LogisticRegression(max_iter=3000)

# 5. 10-Fold Cross Validation (Çapraz Doğrulama) ile Accuracy hesapla
skorlar = cross_val_score(model, X, y, cv=10, scoring='accuracy')

# 6. Sonucu ekrana yazdır
print(f"Python Lojistik Regresyon Doğruluk Oranı: %{skorlar.mean() * 100:.2f}")