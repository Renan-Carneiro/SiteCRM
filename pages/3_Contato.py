import streamlit as st

st.title('Contato')

st.write('Renan Carneiro')
st.write('32 999189393')
st.write('renan.carneiro@okuscapital.com')

with st.container():
        st.write("---")
        st.header("Me envie um email!")
        st.write('##')

        contact_form = """
        <form action="https://formsubmit.co/renan.carneiro@okuscapital.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Seu nome" required>
            <input type="email" name="email" placeholder="Seu email" required>
            <textarea name="message" placeholder="Sua mensagem" required></textarea>
            <button type="submit">Enviar</button>
        </form>
        """
        left_column,right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()