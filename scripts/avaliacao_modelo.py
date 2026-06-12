from pathlib import Path

import joblib
import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report
)
from sklearn.model_selection import train_test_split


ROOT_DIR = Path(__file__).resolve().parent.parent

ARQUIVO_DADOS = ROOT_DIR / "data" / "dataset_traduzido.csv"

MODELO_PATH = ROOT_DIR / "ml" / "modelo_risco_credito.pkl"
PREPROCESSADOR_PATH = ROOT_DIR / "ml" / "preprocessor.pkl"


df = pd.read_csv(ARQUIVO_DADOS)

X = df.drop(columns=["inadimplente"])
y = df["inadimplente"]

preprocessador = joblib.load(PREPROCESSADOR_PATH)

X_transformado = preprocessador.transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_transformado,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

modelo = joblib.load(MODELO_PATH)

y_pred = modelo.predict(X_test)
y_prob = modelo.predict_proba(X_test)[:, 1]

print("\nMétricas do modelo")
print("-" * 40)

print(f"Accuracy : {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred):.4f}")
print(f"Recall   : {recall_score(y_test, y_pred):.4f}")
print(f"F1-score : {f1_score(y_test, y_pred):.4f}")
print(f"ROC-AUC  : {roc_auc_score(y_test, y_prob):.4f}")

print("\nMatriz de confusão")
print(confusion_matrix(y_test, y_pred))

print("\nRelatório de classificação")
print(classification_report(y_test, y_pred))