from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

modelo_ia = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3
)


def gerar_explicacao(cliente, probabilidade):

    prompt = f"""
Você é um analista de crédito de uma instituição financeira.

Analise o perfil abaixo:

Idade: {cliente['idade']} anos
Renda anual: R$ {cliente['renda_anual']:,.2f}
Tipo de moradia: {cliente['tipo_moradia']}
Tempo de emprego: {cliente['tempo_emprego']} anos
Finalidade do empréstimo: {cliente['finalidade_emprestimo']}
Classe do empréstimo: {cliente['classe_emprestimo']}
Valor do empréstimo: R$ {cliente['valor_emprestimo']:,.2f}
Taxa de juros: {cliente['taxa_juros']}%
Percentual da renda comprometida: {cliente['percentual_renda']:.0%}
Histórico de inadimplência: {cliente['historico_inadimplencia']}
Histórico de crédito: {cliente['tempo_historico_credito']} anos

Probabilidade de inadimplência estimada: {probabilidade:.2%}

Escreva uma análise em português do Brasil contendo:

## Resumo Executivo

## Principais Fatores de Risco

## Pontos Positivos

## Recomendação Bancária

## Conclusão Final

Retorne a resposta em Markdown.
Separe cada seção por uma linha em branco.
Escreva parágrafos curtos e objetivos.
Utilize linguagem profissional.
Não use listas.
Não invente informações.
"""
    
    resposta = modelo_ia.invoke(prompt)

    return resposta.content