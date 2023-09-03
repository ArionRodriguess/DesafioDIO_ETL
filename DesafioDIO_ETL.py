import pandas as pd 

# Leitura do Arquivo CSV
df = pd.read_csv('SDW2023DESAFIO.csv')
print(df)

# Verifica se há valores null no dataset
num_na = df.isna().sum()
print(num_na)

# Irei extrair a moda da coluna Quantidade para posteriormente preencher os valores null
moda = df['Quantidade'].value_counts().index[0]
print(moda)

# Preenchendo os valores null com a Moda
df['Quantidade'].fillna(value = moda , inplace = True)
nums_na = df.isna().sum()

# Criando uma nova coluna para armazenar o Ano

df['ID_Pedido'].str.split('-').str[1]
df['Ano'] = df['ID_Pedido'].str.split('-').str[1]

# Criando um novo DataFrame para filtrar apenas no segmento Home Office na região West e acima do Ano de 2015

df2 = df[(df.Segmento == 'Home Office') & (df.Regiao == 'West') & (df.Ano >= '2015')]
print(df2)

# Checando os valores mínimos e maximos da coluna Valor_Venda no DataFrame 2

ValorVenda = df2.Valor_Venda.describe()
print(ValorVenda)

# Criando um novo DataFrame filtrando os valores de venda entre 500 e 20000 baseado no Df 2
df3 = df2.query('500 < Valor_Venda < 20000')
df3.Valor_Venda.describe()

print(df3)

# Criando o novo arquivo CSV com o processo de ETL realizado
df3.to_csv('SDW_NOVO.csv')





