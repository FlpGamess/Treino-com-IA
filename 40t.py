import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

# carregar dados
df = pd.read_csv("falhas.csv")

X = df["descricao"]
y = df["codigo"]

# dividir treino/teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression(max_iter=1000))
])

# treinar
model.fit(X_train, y_train)

# prever
pred = model.predict(X_test)

print(classification_report(y_test, pred))
