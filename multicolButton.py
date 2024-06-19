import streamlit as st

# Création d'une session state pour suivre quelles images doivent être affichées
if 'show_cicd' not in st.session_state:
    st.session_state['show_cicd'] = False


def toggle_cicd():
    st.session_state['show_cicd'] = not st.session_state['show_cicd']



# Création des boutons et association avec les fonctions
st.button("Afficher/Masquer le processus CI/CD", on_click=toggle_cicd)



# Affichage des images en fonction de l'état des boutons
if st.session_state['show_cicd']:
    st.image("CICD_process.png", caption="Processus CI/CD")

# --------------------------------

if 'show_accuracy' not in st.session_state:
    st.session_state['show_accuracy'] = False
    
def toggle_accuracy():
    st.session_state['show_accuracy'] = not st.session_state['show_accuracy']
    
st.button("Afficher/Masquer la courbe d'accuracy", on_click=toggle_accuracy)

if st.session_state['show_accuracy']:
    st.image("courbe_accuracy.png", caption="Courbe d'accuracy")
    
