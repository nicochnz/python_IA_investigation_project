import streamlit as st
import random
from ollama import chat, ChatResponse

st.title("Salle d'interrogatoire")

suspects = [
    {"name": "Aedan", "description": "Cybersécurité, calme et observateur."},
    {"name": "Nico", "description": "Développeur web, nerveux et parle vite."},
    {"name": "Mattéo", "description": "Étudiant en infra, timide et mystérieux."},
    {"name": "Lisa", "description": "Comptable, détendue mais mystérieuse."},
    {"name": "Laura", "description": "Coach fitness, très froide et directe."}
]
# ICI --> st.session_state est un dictionnaire qui garde des données entre les interactions C'est à dire que Streamlit recharge complètement le script à chaque action  Si on ne sauvegarde pas l’état quelque part, toutes les variables Python normales sont réinitialisées à chaque interaction.
if "culprit" not in st.session_state:
    st.session_state.culprit = random.choice(suspects)
    st.session_state.erreurs = 0
    st.session_state.messages = [
        {"role": "system", "content": f"Tu es un jeu d'enquête. Voici les suspects : {suspects}. \
L'un d'eux est coupable : {st.session_state.culprit['name']}. Réponds toujours dans le rôle du suspect interrogé, \
en restant fidèle à sa personnalité. Ne révèle jamais directement le coupable."}
    ]
    st.session_state.history = []
#st.subheader c'est un sous titre de streamlite && st.write("---") = ligne de séparation visuelle
st.subheader("Suspects :")
for s in suspects:
    st.write(f"**{s['name']}**: {s['description']}")

st.write("---")

question = st.text_input("Pose ta question ou accuse un suspect (ex: accuser Alice) :")

if st.button("Envoyer"):
    if question.lower().startswith("accuser"):
        accused_name = question.split(" ", 1)[1]

        if accused_name.lower() == st.session_state.culprit["name"].lower():
            st.success(f"✅ Bravo ! {accused_name} était bien le coupable ! 🎉")
            st.session_state.history.append(f"Tu as accusé {accused_name} ✅ Correct !")
        else:
            st.session_state.erreurs += 1
            if st.session_state.erreurs >= 2:
                st.error(f"❌ Mauvais choix... {accused_name} est innocent. 🕵️‍♂️ Fin du jeu ! Le coupable était {st.session_state.culprit['name']}.")
                st.session_state.history.append(f"Tu as accusé {accused_name} ❌ Plus d'essais !")
            else:
                st.warning(f"❌ Mauvais choix... {accused_name} est innocent. Il te reste 1 essai.")
                st.session_state.history.append(f"Tu as accusé {accused_name} ❌ 1 essai restant")
    else:
        # Ajouter la question au chat
        st.session_state.messages.append({"role": "user", "content": question})
        response: ChatResponse = chat(model="gemma3", messages=st.session_state.messages)
        answer = response["message"]["content"]
        st.session_state.history.append(f"💬 Question: {question}\n💬 Réponse: {answer}")
        st.session_state.messages.append({"role": "assistant", "content": answer})

# --- Affichage de l'historique ---
st.subheader("Historique")
for msg in st.session_state.history:
    st.markdown(msg)
