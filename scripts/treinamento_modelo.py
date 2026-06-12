from pathlib import Path
import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from xgboost import XGBClassifier

ROOT_DIR = Path(__file__).resolve().parent.parent

ARQUIVO_DADOS = ROOT_DIR / "data" / "dataset_traduzido.csv"

MODELO_PATH = ROOT_DIR / "ml" / "modelo_risco_credito.pkl"
PREPROCESSADOR_PATH = ROOT_DIR / "ml" / "preprocessor.pkl"
FEATURE_NAMES_PATH = ROOT_DIR / "ml" / "feature_names.pkl"

df = pd.read_csv(ARQUIVO_DADOS)
y = df["inadimplente"]
X = df.drop(columns=["inadimplente"])

colunas_categoricas = [
    "tipo_moradia",
    "finalidade_emprestimo",
    "classe_emprestimo",
    "historico_inadimplencia"
]

preprocessador = ColumnTransformer(
    transformers=[
        (
            "categoricas",
            OneHotEncoder(handle_unknown="ignore"),
            colunas_categoricas
        )
    ],
    remainder="passthrough"
)

X_transformado = preprocessador.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_transformado,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

modelo = XGBClassifier(
    random_state=42
)

modelo.fit(
    X_train,
    y_train
)

joblib.dump(
    modelo,
    MODELO_PATH
)

joblib.dump(
    preprocessador,
    PREPROCESSADOR_PATH
)

feature_names = preprocessador.get_feature_names_out()

joblib.dump(
    feature_names,
    FEATURE_NAMES_PATH
)

print("Treinamento concluído com sucesso.")
print(f"Modelo salvo em: {MODELO_PATH}")
print(f"Preprocessador salvo em: {PREPROCESSADOR_PATH}")
print(f"Features salvas em: {FEATURE_NAMES_PATH}")