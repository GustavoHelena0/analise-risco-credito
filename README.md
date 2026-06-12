# Análise de Risco de Crédito | Machine Learning + IA

Projeto desenvolvido para estimar a probabilidade de inadimplência de clientes utilizando Machine Learning e gerar uma análise textual do perfil com auxílio de IA.

## Funcionalidades

* Predição da probabilidade de inadimplência
* Classificação do risco em baixo, moderado ou alto
* Interface interativa desenvolvida com Streamlit
* Geração automática de uma análise do perfil do cliente
* Avaliação em tempo real a partir das informações fornecidas

## Variáveis Utilizadas

* Idade
* Renda anual
* Tipo de moradia
* Tempo de emprego
* Finalidade do empréstimo
* Classe do empréstimo
* Valor solicitado
* Taxa de juros
* Percentual da renda comprometida
* Histórico de inadimplência
* Tempo de histórico de crédito

## Como Executar

1. Clone o repositório:

```txt
git clone https://github.com/seu-usuario/analise-risco-credito.git
```

2. Instale as dependências:

```txt
pip install -r requirements.txt
```

3. Crie um arquivo `.env` contendo sua chave da OpenAI:

```txt
OPENAI_API_KEY=sua_chave
```

4. Execute a aplicação:

```txt
python -m streamlit run app/ui.py
```

## Ferramentas Utilizadas

* Python
* Pandas
* Scikit-Learn
* XGBoost
* Streamlit
* LangChain
* OpenAI API
* Joblib

## Classificação de Risco

O sistema classifica os clientes em:

* Baixo risco
* Risco moderado
* Alto risco

A classificação considera a previsão do modelo e a probabilidade estimada de inadimplência.

## Estrutura do Projeto

```txt
analise-risco-credito/

├── app/
│   └── ui.py
│
├── data/
│   ├── credit_risk_dataset.csv
│   └── dataset_traduzido.csv
│
├── ml/
│   ├── predict.py
│   ├── explanation.py
│   ├── risk_utils.py
│   ├── modelo_risco_credito.pkl
│   └── preprocessor.pkl
│
├── scripts/
│   ├── tradutor.py
│   ├── treinamento_modelo.py
│   └── avaliacao_modelo.py
│
├── requirements.txt
└── README.md
```

## Aprendizados

Durante o desenvolvimento deste projeto, foram praticados conceitos relacionados a:

* Pré-processamento de dados
* Treinamento e avaliação de modelos de Machine Learning
* Desenvolvimento de aplicações com Streamlit
* Integração com modelos de linguagem
* Organização de projetos para portfólio

## Próximos Passos

* Adicionar gráficos com métricas do modelo
* Testar outros algoritmos de classificação
* Permitir a análise de múltiplos clientes por meio de arquivos CSV

## Autor

Gustavo Locatelli Helena

🔗 https://www.linkedin.com/in/gustavo-locatelli-helena-9967b224b/
