import streamlit as st
import pandas as pd
import numpy as np
from utils import get_challenge_output, send_simple_message
from tab2 import fine_tuning, few_shot_learning

# SETTING PAGE CONFIG TO WIDE MODE
st.set_page_config(page_icon="⚙️", page_title="L'IA c'est pas soricer : Challenge FSL", layout="wide")

st.title("L'IA c'est pas soricer: ")
st.subheader("Voyage au pays des Large Language Models (LLM)")        


def main_tab1():
    st.markdown("Les visuels et rappels ci-dessous sont issus de la vidéo : [Il faudra penser à insérer le lien vers la bonne vidéo], n'hésitez pas à faire un tour avant")
    st.video('https://www.youtube.com/watch?v=89KrwcGCwZ8&t=2s') 

def main_tab2():
    st.markdown('Comment adapter un LLM à performer sur une tâche spécifique ?')
    st.subheader("Le fine-tuning")
    fine_tuning()
    st.subheader("Le few shot learning")
    few_shot_learning()


def main_tab3():
    st.header("L'analyse de sentiment")
    with st.form(key='prompt FSL'):
        st.markdown('Récupérez votre token HuggingFace ici: https://huggingface.co/settings/tokens')
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
    with st.form(key='Submit your model to the challenge', clear_on_submit=True):
        contact_pseudo = st.text_input(label="Pseudo")
        contact_mail = st.text_input(label="Email")
        submitted_model = st.text_area(label="Copy paste your prompt here")
        submit_FSL_model = st.form_submit_button(label='Soumettre ma participation au challenge !')
    if submit_FSL_model:
        send_simple_message(contact_pseudo, contact_mail, submitted_model)

tab1, tab2, tab3 = st.tabs(["LLM qu'est-ce que c'est", "LLM comment s'en servir", "Le challenge"])
with tab1:
   main_tab1()

with tab2:
   main_tab2()

with tab3:
   main_tab3()
