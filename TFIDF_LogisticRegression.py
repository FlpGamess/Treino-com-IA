import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import re


def normalize(text):
    text = re.sub(r'\bpt\b', 'porta', text)
    text = re.sub(r'\btras\b', 'traseira', text)
    return text

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'[^a-zA-Z ]', '', text)
    return text



# carregar base limpa
df = pd.read_csv(r"E:\programação python\treino IA\complaints\clean.csv")

# remover vazios (garantia)
df = df.dropna(subset=["Consumer complaint narrative", "Product"])

counts = df['Product'].value_counts()

valid_classes = counts[counts >= 50].index

df = df[df['Product'].isin(valid_classes)]

df["Consumer complaint narrative"] = df["Consumer complaint narrative"].apply(clean_text)


# definir X e y
X = df["Consumer complaint narrative"]
y = df["Product"]


# dividir treino/teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# TF-IDF
vectorizer = TfidfVectorizer(
    ngram_range=(1,2),   # palavras + combinações
    min_df=2,
    max_df=0.9,
    max_features=5000
)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# modelo
model = LogisticRegression(
    C=2,
    max_iter=1000,
    class_weight='balanced'
)

model.fit(X_train_tfidf, y_train)

# prever
y_pred = model.predict(X_test_tfidf)

# métricas
print("Acurácia:", accuracy_score(y_test, y_pred))
print("\nRelatório:\n", classification_report(y_test, y_pred))

'''
import pandas as pd

# carregar dataset
df = pd.read_csv(r"E:\programação python\treino IA\complaints\complaints.csv")
print(df.columns)

# selecionar colunas importantes
df = df[["Consumer complaint narrative", "Product"]]

df["Consumer complaint narrative"] = df["Consumer complaint narrative"].str.lower()

# remover linhas sem texto
df = df.dropna()

# reduzir tamanho (ex: 5000 linhas)
df = df.sample(5000)

# salvar limpo
df.to_csv("clean.csv", index=False)

print("terminado")'''

