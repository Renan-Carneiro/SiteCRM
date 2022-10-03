import streamlit as st
import requests

from streamlit_lottie import st_lottie



st.set_page_config(page_title='Okus CRM' , page_icon='✔' , layout='wide')
st.sidebar.success("Selecione uma página acima.")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


#asset
lottie_animation = load_lottieurl('https://assets9.lottiefiles.com/packages/lf20_zu3z8n5o.json')

#Header
with st.container():

    st.title('Bem vindo ao CRM da Okus 💵')
    st.title('Esse é o protótipo de um CRM para ser utilizado pelos assessores')
    st.subheader('Criado por Renan Carneiro')
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('Quem somos nós')
        st.write(
            """
            Somos um escritório de assessoria de investimentos, com sede em Poços de Caldas - MG
            """
        )
        st.write('[Website](https://www.okuscapital.com/)')
    with right_column:
        st_lottie(lottie_animation,height=300,key='finance')