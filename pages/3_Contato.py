import streamlit as st

st.title('Contato')

st.write('Renan Carneiro')
st.write('32 999189393')
st.write('renan.carneiro@okuscapital.com')

with st.container():
    st.write("---")
    
    # Center the header
    st.header("<div style='text-align: center;'>Me envie um email!</div>", unsafe_allow_html=True)
    st.write('##')

    contact_form = """
    <style>
        .contact-form {
            max-width: 400px;
            margin: auto;
            padding: 20px;
            background-color: #f4f4f4;
            border-radius: 10px;
        }
        .form-input {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .form-textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .form-button {
            width: 100%;
            padding: 10px;
            background-color: #007BFF;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>

    <div class="contact-form">
        <form action="https://formsubmit.co/renan.carneiro@okuscapital.com" method="POST">
            <input class="form-input" type="hidden" name="_captcha" value="false">
            <input class="form-input" type="text" name="name" placeholder="Seu nome" required>
            <input class="form-input" type="email" name="email" placeholder="Seu email" required>
            <textarea class="form-textarea" name="message" placeholder="Sua mensagem" required></textarea>
            <button class="form-button" type="submit">Enviar</button>
        </form>
    </div>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
