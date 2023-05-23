import streamlit as st

def fine_tuning():
    st.markdown("L'une des principale caractéristique d'un LLM est sa capacité à comprendre le contexte et à générer des réponses cohérentes et pertinentes sur la base des données fournies. Cela lui permet d'effectuer diverses tâches, telles que:\n- Répondre à des questions\n- Générer du texte\n- Résumer un texte\n- Traduire du texte")
    st.markdown("Le fine-tuning d'un LLM consiste à ajuster et à adapter ce modèle pré-entraîné afin qu'il exécute des tâches spécifiques plus efficacement. Le processus implique généralement un entraînement supplémentaire du modèle sur un dataset plus petit et ciblé qui est pertinent pour la tâche souhaité.")
    st.image("data/fine_tuning1.png")
    st.markdown("L’intérêt du fine-tuning en Machine Learning est multiple :\n-	**La mutualisation des coûts**, c’est particulièrement le cas dans les LLM. Partir d’un modèle très performant sans avoir à assumer la phase excessivement couteuse d’entrainement initiale.\n-	**La customisation**. Le fine-tuning permet d’augmenter très spécifiquement la performance de notre modèle sur une tâche ciblée. Attention, cela entraîne souvent une perte de généralisation sur les autres cas d’usage (perte de performance).\n-	**Pallier le manque de données labellisées** pour la tâche spécifique ciblée. En effet la phase de fine-tuning nécessite une quantité de donnée plus raisonnable que la phase d’entrainement.")
    st.markdown("En ML, il existe plusieurs façon de fine-tuner ses modèles avec leurs avantages et inconvénients :\n- **Le Transfer-Learning** : Consiste à initialiser l’entrainement d’un nouveau modèle à partir des poids d’un modèle existant. \n- **Le Task-specific Fine-tuning** : On utilise un dataset spécifique à la tâche souhaitée lors du fine-tuning. On cherche alors uniquement la performance sur une tâche spécifique au détriment de la généralisation du modèle. Cette méthode requière de la donnée spécifique, souvent difficile à obtenir. \n- **Le Multi-task Learning** : Le modèle pré-entraîné est affiné sur plusieurs tâches simultanément. Cette approche permet au modèle d'apprendre et d'exploiter les représentations partagées entre les différentes tâches, ce qui conduit à une meilleure généralisation et à de meilleures performances.")


def few_shot_learning():
    st.markdown("**Le Few-Shot Learning** est une autre méthode de fine-tuning de modèle de ML. Elle tire parti au maximum de la généralisation des Large Language Model.")
    st.markdown("On ne fournit que quelques exemples au modèle - de l’ordre de 3 ou 4 - avant de lui demander la tâche que l’on souhaite qu’il réalise. Cette méthode possède l'énorme avantage de nécessité très peu de données d’entrainement. Si peu qu’on peu même s’affranchir de la phase de réentrainement en lui fournissant les exemples labelisés dans la même requête que la tâche souhaitée. En d'autre terme on n'a même pas besoin d'instancier un nouveau modèle. On interroge directement le modèle LLM général mais d'une manière particulière. C'est ça qui nous intéresse ici : créer un modèle spécialisé dans l'analyse sentimentale à partir d'un LLM open source !")