import streamlit as st

st.write("<center>Insira abaixo os dados.</center>", unsafe_allow_html=True )
formulario="""
        <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSeBZoiGYHM5PL6rxBkHfX6AuFzFdccv1F9iruUpeMaHGYLDFA/viewform?embedded=true" width="100%" height="820" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
        """

st.markdown(formulario, unsafe_allow_html=True)