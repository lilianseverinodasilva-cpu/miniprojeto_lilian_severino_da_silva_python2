# Projeto de Análise de Dados de Varejo

Este repositório contém um projeto completo de Ciência de Dados, realizado como parte da avaliação do curso de Análise de Dados com Python, ofertado pelo programa SCTec, que é uma parceria entre a SCTI e Senai SC.
Este projeto está focado no pipeline de **Engenharia, Limpeza e Análise Exploratória de Dados (EDA)** de uma base de dados de transações de varejo (contendo originalmente mais de 830 mil linhas), retirada no Kaggle: https://www.kaggle.com/datasets/namespaiva/base-varejo/data. 
O principal objetivo foi tratar inconsistências críticas ocultas no banco de dados estruturado e extrair inteligência de negócio sobre o comportamento dos consumidores.

## Estrutura do Repositório

* `limpeza.ipynb`: Notebook focado no processo de ETL, tratamento de nulos, inconsistências e validação de tipos.
* `analise.ipynb`: Notebook com a análise exploratória de dados, cruzamentos estatísticos (`crosstab`), Feature Engineering e geração de gráficos estruturados para negócio.
* `utils.py`: Scripts auxiliares contendo funções personalizadas para varredura e padronização dos dados.
* `data/`: Diretório contendo as bases de dados (Raw/Bruta e Limpa).

---

## Tecnologias e Ferramentas Utilizadas

* **Linguagem:** Python
* **Manipulação de Dados:** Pandas, NumPy
* **Estatística Computacional:** SciPy (análise de Z-Score)
* **Visualização de Dados:** Matplotlib, Seaborn

---

## Etapas Críticas de Tratamento e Qualidade de Dados (ETL)

O projeto identificou e resolveu armadilhas clássicas que costumam quebrar relatórios automatizados:

1. **Tratamento de Falsos Nulos:** Identificação de strings de texto textuais como `"#N/D"` e `"NaN"` mascaradas como dados reais, convertidas e tratadas de forma vetorial.
2. **Validação de Identificadores:** Investigação estatística da coluna `id_compra` (identificada como `int64`). A validação garantiu que a coluna preservava a integridade de "carrinhos fechados" e orientou o uso de agregações estritas por contagem (`count`/`size`), blindando o projeto contra erros matemáticos em tabelas dinâmicas.
3. **Filtragem de Escopo:** Redução e consolidação da base final para **730.219 linhas** distribuídas em 11 colunas de alta integridade, mapeando exatamente **18.471 compras únicas**.
4. **A coluna data:** Esta coluna estava em formato string e não datetime. A conversão foi feita para melhor análise futura. Também foi criada uma coluna data_br, em string, para a visualização dos dados em formato universal.
5. **Outliers:** Não havia dados considerados outliers, mesmo após a criação, por Feature Engineering, da coluna itens_por_compra. Usou-se o método IQR e Z-score, que retornaram valor 0. O capping, então, nem vou aplicado.
---


## Insights de Negócio e Análise Exploratória

### 1. Perfil Demográfico (Gênero vs. Estado Civil)
Utilizando técnicas de normalização por linha (`pd.crosstab(normalize='index')`), foi possível extrair a composição exata de homens e mulheres dentro de cada status civil, convertendo dados absolutos em proporções ideais para campanhas de marketing direcionadas. De forma geral, as mulheres representaram uma fatia maior nas compras, em todas as categorias.

### 2. Volumetria de Vendas por Categoria
Geração de gráficos de barras horizontais e verticais customizados sob as diretrizes de *Data Storytelling*, limpando ruídos visuais (como remoção de bordas e grades excessivas) e exibindo o ranking real de compras por categoria do produto.

[Vendas por Categoria (Total de Compras Únicas)]
(https://github.com/lilianseverinodasilva-cpu/miniprojeto_lilian_severino_da_silva_python2/blob/main/graficos/Vendas%20por%20Categoria%20(Total%20de%20Compras%20%C3%9Anicas).png)

### 3. Relação classe social e montante de compras
Criou-se um gráfico de barras para mostrar a relação entre as classes sociais (A, B, C) e o montante de compras. A classe B é a que mais gerou compras, tendo mais que o dobro de valor da classe C. A classe A gerou pouco valor aos dados. Isto mostra que estratégias de marketing deveriam/devem focar no público da classe B.

[Quantidade de Registros por Classe Social]
(https://github.com/lilianseverinodasilva-cpu/miniprojeto_lilian_severino_da_silva_python2/blob/main/graficos/Quantidade%20de%20Registros%20por%20Classe%20Social.png)
---

Feito por Lilian Severino da Silva
