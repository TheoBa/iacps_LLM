import streamlit as st
from utils import get_challenge_output, send_simple_message


def test_form():
    with st.form(key='prompt FSL'):
        st.subheader("Formulaire de test")
        st.markdown("En anglais et en respectant le template ci-dessous:\n- Renseignez votre token HF\n- Décrivez précisément la tâche que vous souhaitez que le modèle apprenne et exécute\n- Donnez autant d'exemples que nécessaire en veillant à bien ajouter les caractères de séparation “###”\n- Ajouter enfin une phrase _test_ avant de lancer le test\n Si votre token est valide: vous pourrez observez le résultat")
        API_TOKEN = st.text_input(label="HF_API_TOKEN", type="password")
        HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}
        API_URL = "https://api-inference.huggingface.co/models/EleutherAI/gpt-neo-2.7B"
        prompt = st.text_area(label='Your prompt', value='''Task to perform\nexample1\nsol1\n###\nexample2\nsol2\n###\nexample3\nsol3\n###\ntest''', height=280)
        prompt += "\n"
        parameters = {
            "max_new_tokens": 1,
            "temperature": .1,
            "end_sequence": "###"
            }
        submit_FSL_test = st.form_submit_button(label='Tester mon prompt sur un test custom')
    if submit_FSL_test:
        st.markdown(get_challenge_output(API_URL, HEADERS, prompt, parameters))


def challenge_description1():
    st.markdown("## Challenge:\nProposer un setup de prompt pour performer des tâches **d'analyse sentimental** sur des objets d'avis AMAZON au moyen de GPT Neo. On souhaite que le modèle classifie des phrases selon 2 labels: is the review 'positive' or 'negative'")
    st.markdown("Exemples:\n 1. “This is the worst book.”: negative\n2. “The best soundtrack ever to anything.”: positive, \n3. “Pop psychology at its worst.”: negative\n4. “Amazing!”: positive\n5. “Stuning even for the non-gamer.”: positive\n6. “Fuzzy around the edges.”: negative")	


def challenge_description2():
    st.markdown("## **Evaluation:**\nVos prompts seront soumis à un data-set de 100 évaluations.")
    st.markdown("Rentre en ligne de compte:")
    st.latex(r'''
    \begin{cases}
    n_{ok} \text{: le nombre de bonnes réponses} \\
    l_{desc} \text{: la longueur de la description de la tâche à réaliser (plus elle est longue, moins vous scorez de point)} \\
    n_{ex} \text{: le nombre d'exemple, moins vous fournirez d'exemple, plus vous scorerez de points par bonnes réponse}
    \end{cases}''')
    st.markdown("Le score final sera calculé de la manière suivante:")
    st.latex(r'''Score = min(\frac{200}{l_{desc}}, 10) + n_{ok} * (1,3 - \frac{n_{ex}}{10})''')


def challenge_form():
    st.markdown("**Attention**, une seule participation par email sera accepté (la première soumission)")
    with st.expander("Formulaire de soumission au challenge"):
        with st.form(key='Submit your model to the challenge', clear_on_submit=True):
            st.subheader("Formulaire de soumission de votre prompt au challenge")
            contact_pseudo = st.text_input(label="Pseudo")
            contact_mail = st.text_input(label="Email")
            submitted_model = st.text_area(label="Copiez votre prompt ici en retirant la phrase test (dernière ligne)")
            submit_FSL_model = st.form_submit_button(label='Soumettre ma participation au challenge !')
        if submit_FSL_model:
            send_simple_message(contact_pseudo, contact_mail, submitted_model)
