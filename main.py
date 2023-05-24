import streamlit as st
import pandas as pd
import numpy as np
from tab2 import fine_tuning, few_shot_learning
from tab3 import test_form, challenge_form

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
    test_form()
    challenge_form()

tab1, tab2, tab3 = st.tabs(["LLM qu'est-ce que c'est", "LLM comment s'en servir", "Le challenge"])
with tab1:
   main_tab1()

with tab2:
   main_tab2()

with tab3:
   main_tab3()
