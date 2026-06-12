import streamlit as st
from dotenv import load_dotenv

from ml.predict import predict_risk
from ml.explanation import gerar_explicacao
from ml.risk_utils import classificar_risco

load_dotenv()

st.set_page_config(
    page_title="Análise de Risco de Crédito",
    layout="wide"
)

st.title("Análise de Risco de Crédito")

with st.form("formulario_credito"):

    col1, col2 = st.columns(2)

    with col1:

        nome_cliente = st.text_input(
            "Nome do cliente",
            placeholder="Nome completo"
        )

        idade = st.number_input(
            "Idade",
            min_value=18,
            max_value=100,
            value=30
        )

        renda_anual = st.number_input(
            "Renda anual",
            min_value=0,
            value=50000
        )

        tipo_moradia = st.selectbox(
            "Tipo de moradia",
            [
                "Alugada",
                "Própria",
                "Financiada",
                "Outra"
            ]
        )

        tempo_emprego = st.number_input(
            "Tempo de emprego (anos)",
            min_value=0,
            value=5
        )

        finalidade_emprestimo = st.selectbox(
            "Finalidade do empréstimo",
            [
                "Educação",
                "Saúde",
                "Empreendedorismo",
                "Pessoal",
                "Reforma residencial",
                "Consolidação de dívidas"
            ]
        )

    with col2:

        classe_emprestimo = st.selectbox(
            "Classe do empréstimo",
            [
                "A",
                "B",
                "C",
                "D",
                "E",
                "F",
                "G"
            ]
        )

        valor_emprestimo = st.number_input(
            "Valor do empréstimo",
            min_value=0,
            value=10000
        )

        taxa_juros = st.number_input(
            "Taxa de juros (%)",
            min_value=0.0,
            value=12.0
        )

        percentual_renda = st.number_input(
            "Percentual da renda comprometida",
            min_value=0.0,
            max_value=1.0,
            value=0.25
        )

        historico_inadimplencia = st.selectbox(
            "Possui histórico de inadimplência?",
            [
                "Sim",
                "Não"
            ]
        )

        tempo_historico_credito = st.number_input(
            "Histórico de crédito (anos)",
            min_value=0,
            value=5
        )

    
    analisar = st.form_submit_button(
    "Realizar Análise de Risco",
    use_container_width=True
    )

if analisar:

    cliente = {
        "idade": idade,
        "renda_anual": renda_anual,
        "tipo_moradia": tipo_moradia,
        "tempo_emprego": tempo_emprego,
        "finalidade_emprestimo": finalidade_emprestimo,
        "classe_emprestimo": classe_emprestimo,
        "valor_emprestimo": valor_emprestimo,
        "taxa_juros": taxa_juros,
        "percentual_renda": percentual_renda,
        "historico_inadimplencia": historico_inadimplencia,
        "tempo_historico_credito": tempo_historico_credito
    }

    resultado = predict_risk(cliente)

    predicao = resultado["predicao"]
    probabilidade = resultado["probabilidade"]

    nome_exibicao = (
        nome_cliente.strip()
        if nome_cliente.strip()
        else "Cliente"
    )

    st.divider()

    st.subheader(
        f"Resultado da Análise do Cliente - {nome_exibicao}"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Probabilidade de inadimplência",
            f"{probabilidade:.2%}"
        )

    with col2:

        classificacao = classificar_risco(
            predicao,
            probabilidade
        )

        if classificacao == "alto":

            st.error(
                "Alto Risco de Inadimplência"
            )

        elif classificacao == "moderado":

            st.warning(
                "Risco Moderado de Inadimplência"
            )

        else:

            st.success(
                "Baixo Risco de Inadimplência"
            )

    st.divider()

    with st.spinner(
        "Gerando análise do perfil..."
    ):

        explicacao = gerar_explicacao(
            cliente,
            probabilidade
        )


    st.markdown(explicacao)