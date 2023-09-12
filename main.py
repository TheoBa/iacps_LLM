import streamlit as st
import pandas as pd
import numpy as np
from tab2 import fine_tuning, few_shot_learning
from tab3 import test_form, challenge_form, challenge_description1, challenge_description2

# SETTING PAGE CONFIG TO WIDE MODE
st.set_page_config(page_icon="⚙️", page_title="L'IA c'est pas sorcier : Challenge FSL", layout="wide")

st.title("L'IA c'est pas sorcier: ")
st.subheader("Voyage au pays des Large Language Models (LLM)")        


def main_sidebar():
    with st.sidebar:
        st.header("Qui sommes nous ?")
        st.image("data/theo_benjamin.png")
        st.markdown("“Salut ! Nous c'est Benjamin et Théo. On est tous les deux data-scientists chez LittleBigCode et mordu d'IA.”")
        st.markdown("**LittleBigCode** (**LBC** pour les intimes 😉) c'est un laboratoire de conseil en Intelligence Artificielle. On accompagne nos clients dans l'exploitation de leurs données, de la collecte à l'industrialisation de modèles mathématiques d'IA en passant par la mise en place de service structurés Cloud ainsi que la co-construction des cas d'usages.")
        st.markdown("Au dela des missions de conseils, nous développons également nos propres solution en interne. L'apprentissage étant au étant au coeur des valeurs de **LBC**, nous encourageons nos consultants à développer leur expertise via d'autres activités comme la participation à des challenges Kaggle, à des conférences, à passer des certifications cloud ou encore à écrire des articles.")
        st.markdown("La production de **l'IA c'est pas sorcier** fait parti de ces initiatives que nous soutenons")
        st.image("data/benjamin.png")
        st.markdown("**Benjamin**: “Ce qui me plait c'est de défrichier des nouveaux sujets. De comprendre en détail et me former sur le fonctionnement des dernières technologies de l'état de l'art en IA.”")
        st.image("data/theo.jpg")
        st.markdown("**Théo**: “Ce qui me plait c'est de bidouiller, de manipuler ces technologies et de créer des petites applications. Mais ce qui me plait plus encore c'est de transmettre, de faire découvrir ce que j'ai compris à mes collègues, mes amis, ma famille.”")

def main_tab1():
    st.markdown("Les visuels et rappels ci-dessous sont issus de la vidéo : (n'hésitez pas à faire un tour avant)")
    st.video('https://www.youtube.com/watch?v=izlcj0PEaPw') 


def main_tab2():
    st.markdown('Comment adapter un LLM à performer sur une tâche spécifique ?')
    st.subheader("Le fine-tuning")
    fine_tuning()
    st.subheader("Le few shot learning")
    few_shot_learning()


def main_tab3():
    challenge_description1()
    url_hf = "https://huggingface.co"
    url_token = "https://huggingface.co/settings/tokens"
    st.markdown("Pour participer au challenge vous aurez besoin d'un compte [HuggingFace](%s)" % url_hf)
    st.markdown("Il vous faudra créer un [token en lecture](%s) (READ)" % url_token)
    test_form()
    challenge_description2()
    challenge_form()

main_sidebar()
tab1, tab2, tab3 = st.tabs(["LLM qu'est-ce que c'est", "LLM comment s'en servir", "Le challenge"])
with tab1:
   main_tab1()

with tab2:
   main_tab2()

with tab3:
   main_tab3()
