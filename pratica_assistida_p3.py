import pandas as pd
#carregando a base

link1 = 'dataset_boston.csv'

data = pd.read_csv(link1)
#convertendo type da coluna RM

data['RM'] = data['RM'].astype(float)
#removendo colunas irrelevantes

data = data.drop(columns=['TOWN', 'TRACT', 'LON', 'LAT', 'ZN', 'AGE', 'RAD', 'DIS', 'TAX'])
#salvando

data.to_csv('data.csv', index=False)
#criando arquivo csv