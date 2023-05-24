import streamlit as st
from utils import get_challenge_output, send_simple_message


def test_form():
    with st.form(key='prompt FSL'):
        API_TOKEN = st.text_input(label="HF_API_TOKEN")
        HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}
        API_URL = "https://api-inference.huggingface.co/models/EleutherAI/gpt-neo-2.7B"
        prompt = st.text_area(label='Your prompt', value='''Task to perform\nexample1\nsol1\n###\nexample2\nsol2\n###\nexample3\nsol3\n###\ntest''')
        parameters = {
            "max_new_tokens": 1,
            "temperature": .5,
            "end_sequence": "###"
            }
        submit_FSL_test = st.form_submit_button(label='Test this setup')
    if submit_FSL_test:
        st.markdown(get_challenge_output(API_URL, HEADERS, prompt, parameters))


def challenge_form():
    with st.form(key='Submit your model to the challenge', clear_on_submit=True):
        contact_pseudo = st.text_input(label="Pseudo")
        contact_mail = st.text_input(label="Email")
        submitted_model = st.text_area(label="Copy paste your prompt here")
        submit_FSL_model = st.form_submit_button(label='Soumettre ma participation au challenge !')
    if submit_FSL_model:
        send_simple_message(contact_pseudo, contact_mail, submitted_model)