from pathlib import Path

import pandas as pd

ROOT_DIR = Path(__file__).resolve().parent.parent

ARQUIVO_ENTRADA = ROOT_DIR / "data" / "credit_risk_dataset.csv"
ARQUIVO_SAIDA = ROOT_DIR / "data" / "dataset_traduzido.csv"


def traduzir_dataset():

    df = pd.read_csv(ARQUIVO_ENTRADA)

    novos_nomes = {
        "person_age": "idade",
        "person_income": "renda_anual",
        "person_home_ownership": "tipo_moradia",
        "person_emp_length": "tempo_emprego",
        "loan_intent": "finalidade_emprestimo",
        "loan_grade": "classe_emprestimo",
        "loan_amnt": "valor_emprestimo",
        "loan_int_rate": "taxa_juros",
        "loan_status": "inadimplente",
        "loan_percent_income": "percentual_renda",
        "cb_person_default_on_file": "historico_inadimplencia",
        "cb_person_cred_hist_length": "tempo_historico_credito"
    }

    df.rename(columns=novos_nomes, inplace=True)

    
    df["tipo_moradia"] = df["tipo_moradia"].replace({
        "RENT": "Alugada",
        "OWN": "Própria",
        "MORTGAGE": "Financiada",
        "OTHER": "Outra"
    })

    
    df["finalidade_emprestimo"] = df["finalidade_emprestimo"].replace({
        "EDUCATION": "Educação",
        "MEDICAL": "Saúde",
        "VENTURE": "Empreendedorismo",
        "PERSONAL": "Pessoal",
        "HOMEIMPROVEMENT": "Reforma residencial",
        "DEBTCONSOLIDATION": "Consolidação de dívidas"
    })

    
    df["historico_inadimplencia"] = df["historico_inadimplencia"].replace({
        "Y": "Sim",
        "N": "Não"
    })

   
    df.to_csv(
        ARQUIVO_SAIDA,
        index=False,
        encoding="utf-8-sig"
    )


if __name__ == "__main__":
    traduzir_dataset()