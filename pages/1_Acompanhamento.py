import streamlit as st
import numpy as np
import gspread as gs
import pandas as pd

st.title('Acompanhamento')

# Cria uma conexão com a api do google cloud, esse json precisa ser de uma service account
# aprendi aqui https://stackoverflow.com/questions/43004904/accessing-gae-log-files-using-google-cloud-logging-python
gc = gs.service_account(filename='ServiceAccount.json')

#passando o link da planilha
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/12jdMAui9TTkRGSWJOmonNkBJZpK2iEf_4WQ-Oz02MEY/edit?usp=sharing')
#passando o nome da folha da planilha
ws = sh.worksheet('Form responses 1')
df = pd.DataFrame(ws.get_values())
df.columns = list(df.iloc[0]) #usa a primeira linha como nome das colunas
df = df[1:] #usa só da segunda linha pra frente
df.index-=1 #importante -> vou dar um shift pra trás no index, pra não começar com 1, e sim com 0
df.drop([''], inplace=True, axis=1)
df.dropna(inplace=True,axis=1) #deleta colunas vazias
column_headers = list(df.columns.values) #faz uma lista com nome das colunas
coluna=['Timestamp', 'Nome', 'Categoria', 'TipoInvest', 'Captação', 'PipeInvest', 'Status', 'TipoBank', 'ValorBank', 'Abertura', 'NumeroConta', 'Comentário', 'PipeBank', 'DataReuniao', 'Tarefa', 'DataTarefa']
dictColuna=dict(zip(column_headers,coluna)) #criando um dicionario que vai ser usado para renomear as colunas
df.rename(columns=dictColuna, inplace=True) #renomear colunas usando dicionário
column_headers = list(df.columns.values)
column_headers[2]='Categoria' #mudando uma coluna que ficou repetida, manualmente
column_headers[3]='TipoInvest' #mudando uma coluna que ficou repetida, manualmente
df.columns=list(column_headers)
df["Captação total"]= df[['Captação', 'ValorBank']].sum(axis=1) #criando nova coluna somando as captações de invest e banking
df.drop(['Captação','ValorBank'], inplace=True, axis=1) #deletando as colunas que já foram usadas

df["Tipo"]= df[['TipoInvest', 'TipoBank']].sum(axis=1)
df.drop(['TipoInvest','TipoBank'], inplace=True, axis=1)

for x in range(len(df)):
    if not bool(df['Tipo'][x]):
        df.loc[x]['Tipo']=df.loc[x]['Categoria']

st.write('Acompanhe a seguir a tabela com os eventos gerados')
st.write(df)
#Total Captado
df['Captação total'] = pd.to_numeric(df['Captação total'])
CaptacaoTotal= df['Captação total'].sum()
st.write('A captação total é de ', CaptacaoTotal)
#numero de prospecções
num_prospec= df['Categoria'].str.contains('Prospecção', na=False).sum()
st.write('Foram realizadas ', num_prospec, ' prospecções.')
#Contas Abertas
num_abertura= df['Abertura'].str.contains('Sim', na=False).sum()
st.write('Foram abertas',num_abertura, 'contas')

#comentarios
dfComent=df[['Nome','Comentário']] #separando só em cliente e comentário
dfComent=dfComent.replace(r'^\s*$', np.nan, regex=True) #substituindo espaço por NA
dfComent=dfComent.dropna() # tirando os NA
st.write('Acompanhe os eventos que possuem comentários')
st.write(dfComent)
