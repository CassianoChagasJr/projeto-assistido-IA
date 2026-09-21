# Previsão de valores de imóveis

Data App desenvolvido com Streamlit para explorar o conjunto de dados Boston House Prices e estimar o valor de imóveis usando aprendizado de máquina.

## Funcionalidades

- Visualização dos primeiros registros e seleção de atributos.
- Histograma da distribuição dos preços (`MEDV`) com filtro por faixa de valores.
- Predição interativa a partir de características do imóvel informadas pelo usuário.

## Tecnologias

- **Python 3**
- **Pandas**: leitura e preparação dos dados.
- **Scikit-learn**: treinamento do `RandomForestRegressor`.
- **Plotly Express**: geração do histograma.
- **Streamlit**: interface web interativa.

## Estrutura do projeto

```text
.
├── app.py                    # Aplicação Streamlit e modelo de regressão
├── pratica_assistida_p3.py   # Preparação do dataset original
├── data.csv                  # Dataset usado pela aplicação
├── dataset_boston.csv        # Dataset original
├── requirements.txt          # Dependências Python
└── LICENSE                   # Licença MIT
```

O modelo prevê `MEDV` usando os atributos `CRIM`, `INDUS`, `CHAS`, `NOX`, `RM` e `PTRATIO`.

## Como executar localmente

### 1. Clone o repositório e entre na pasta

```bash
git clone <URL_DO_REPOSITORIO>
cd projeto-assistido-IA
```

### 2. Crie e ative um ambiente virtual

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Instale as dependências

```bash
python -m pip install -r requirements.txt
```

### 4. Inicie a aplicação

```bash
streamlit run app.py
```

O Streamlit exibirá a URL local no terminal, normalmente `http://localhost:8501`.

## Regenerar o dataset tratado

O arquivo `data.csv` já está incluído e pode ser usado diretamente. Para recriá-lo a partir do dataset original, execute:

```bash
python pratica_assistida_p3.py
```

Esse script remove colunas não utilizadas, converte `RM` para `float` e salva o resultado em `data.csv`.

## Licença

Este projeto está disponível sob a [Licença MIT](LICENSE).