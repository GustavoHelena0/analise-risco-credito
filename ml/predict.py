from pathlib import Path

import joblib
import pandas as pd

ROOT_DIR = Path(__file__).resolve().parent.parent

MODELO_PATH = ROOT_DIR / "ml" / "modelo_risco_credito.pkl"
PREPROCESSADOR_PATH = ROOT_DIR / "ml" / "preprocessor.pkl"

modelo = joblib.load(MODELO_PATH)
preprocessador = joblib.load(PREPROCESSADOR_PATH)

def predict_risk(cliente):

    entrada = pd.DataFrame([cliente])

    entrada_transformada = preprocessador.transform(
        entrada
    )

    predicao = modelo.predict(
        entrada_transformada
    )[0]

    probabilidade = modelo.predict_proba(
        entrada_transformada
    )[0][1]

    return {
        "predicao": int(predicao),
        "probabilidade": float(probabilidade)
    }