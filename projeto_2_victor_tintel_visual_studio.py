import pandas            as pd
import streamlit         as st
import seaborn           as sns
import matplotlib.pyplot as plt
from PIL                 import Image

# Set no tema do seaborn para melhorar o visual dos plots
custom_params = {"axes.spines.right": False, "axes.spines.top": False}
sns.set_theme(style="ticks", rc=custom_params)

st.set_page_config(
     page_title="Previsão de Renda",
     page_icon="C:\\Users\\victo\\OneDrive\\Área de Trabalho\\Ciências de Dados\\5 - Desenvolvimento Modelos com Pandas e Python\\Módulo 16 - Métodos de análise\\PROJETO 2\\pacote-de-dinheiro-11551050258raiuc7rsi5.png",
     layout="wide",
     initial_sidebar_state='expanded'
)

# Função para filtrar baseado na multiseleção de categorias
@st.cache(allow_output_mutation=True)
def multiselect_filter(relatorio, col, selecionados):
    if 'all' in selecionados:
        return relatorio
    else:
        return relatorio[relatorio[col].isin(selecionados)].reset_index(drop=True)

# Função para ler os dados
@st.cache(show_spinner= True, allow_output_mutation=True)
def load_data(file_data):
    try:
        return pd.read_csv(file_data, sep=';')
    except:
        return pd.read_excel(file_data)

    
# Título principal da aplicação
st.write('# Análise exploratória da previsão de renda')


def new_func():
    renda = pd.read_csv("C:\\Users\\victo\\Downloads\\input\\previsao_de_renda.csv")
    return renda

# Apresenta a imagem na barra lateral da aplicação
image = Image.open("C:\\Users\\victo\\OneDrive\\Área de Trabalho\\Ciências de Dados\\5 - Desenvolvimento Modelos com Pandas e Python\\Módulo 16 - Métodos de análise\\PROJETO 2\\pacote-de-dinheiro-11551050258raiuc7rsi5.png")
st.sidebar.image(image)

renda = new_func()

# Botão para carregar arquivo na aplicação
st.sidebar.write("## Suba o arquivo")
data_file_1 = st.sidebar.file_uploader("Relatórios de Renda", type = ['csv','xlsx'])

#plots
fig, ax = plt.subplots(8,1,figsize=(10,30))
renda[['posse_de_imovel','renda']].plot(kind='hist', ax=ax[0])

st.write('## Gráficos ao longo do tempo')

sns.lineplot(x='data_ref',y='renda', hue='posse_de_imovel',data=renda, ax=ax[1])
ax[1].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='posse_de_veiculo',data=renda, ax=ax[2])
ax[2].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='qtd_filhos',data=renda, ax=ax[3])
ax[3].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='tipo_renda',data=renda, ax=ax[4])
ax[4].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='educacao',data=renda, ax=ax[5])
ax[5].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='estado_civil',data=renda, ax=ax[6])
ax[6].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='tipo_residencia',data=renda, ax=ax[7])
ax[7].tick_params(axis='x', rotation=45)
sns.despine()
st.pyplot(plt)

st.write('## Gráficos bivariada:')

fig, ax = plt.subplots(7,1,figsize=(10,30))


sns.barplot(x='posse_de_imovel',y='renda',data=renda, ax=ax[0])
sns.barplot(x='posse_de_veiculo',y='renda',data=renda, ax=ax[1])
sns.barplot(x='qtd_filhos',y='renda',data=renda, ax=ax[2])
sns.barplot(x='tipo_renda',y='renda',data=renda, ax=ax[3])
sns.barplot(x='educacao',y='renda',data=renda, ax=ax[4])
sns.barplot(x='estado_civil',y='renda',data=renda, ax=ax[5])
sns.barplot(x='tipo_residencia',y='renda',data=renda, ax=ax[6])
sns.despine()
st.pyplot(plt)





