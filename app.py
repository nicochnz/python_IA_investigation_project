import streamlit as st
import random
from ollama import chat, ChatResponse

st.title("Salle d'interrogatoire")
st.write(f"Un cri a retenti dans la vieille demeure abandonnée, isolée au bout d'une ruelle sombre. Quand la police arrive, une scène macabre se dévoile : un meurtre vient d'être commis. Cinq personnes, présentes sur les lieux, sont immédiatement retenues comme suspects. Tous se connaissent vaguement… mais leurs relations semblent plus complexes qu'il n'y paraît.")


suspects = [
    {"name": "Aedan", "description": " Expert en cybersécurité, calme et observateur. Il analyse chaque détail et parle peu, mais semble toujours remarquer ce que les autres voudraient cacher."},
    {"name": "Nico", "description": "Développeur web, nerveux et bavard. Il parle vite, trop vite, comme s'il voulait noyer ses interlocuteurs sous un flot de mots. Certains disent qu'il se trahit souvent lui-même."},
    {"name": "Mattéo", "description": "Étudiant en infrastructures, discret et réservé. On le décrit comme timide, mais son silence cache une aura étrange, presque inquiétante."},
    {"name": "Lisa", "description": "Comptable, détendue en apparence. Mais derrière son sourire, il y a une part d'ombre : elle sait très bien dissimuler ses véritables intentions."},
    {"name": "Laura", "description": " Coach fitness, froide et directe. Elle dit toujours les choses sans détour, mais son ton glacial rend difficile de savoir si elle dit toute la vérité."}
]
# ICI --> st.session_state est un dictionnaire qui garde des données entre les interactions C'est à dire que Streamlit recharge complètement le script à chaque action  Si on ne sauvegarde pas l’état quelque part, toutes les variables Python normales sont réinitialisées à chaque interaction.
if "culprit" not in st.session_state:
    st.session_state.culprit = random.choice(suspects)
    st.session_state.erreurs = 0
    st.session_state.messages = [
        {
            "role": "system",
            "content": (
            "Voici le contexte : Un cri a retenti dans la vieille demeure abandonnée, isolée au bout d'une ruelle sombre. "
            "Quand la police arrive, une scène macabre se dévoile : un meurtre vient d'être commis. "
            "Cinq personnes, présentes sur les lieux, sont immédiatement retenues comme suspects. "
            "Tous se connaissent vaguement… mais leurs relations semblent plus complexes qu'il n'y paraît.\n\n"
            "Suspects : "
            f"{suspects}. L'un d'eux est coupable : {st.session_state.culprit['name']}.\n\n"
            "RÈGLES IMPORTANTES :\n"
            "- CONTEXTE : Vous êtes un SUSPECT arrêté dans une VIEILLE DEMEURE ABANDONNÉE où un MEURTRE vient d'avoir lieu\n"
            "- Vous êtes interrogé par la POLICE - vous êtes SUSPECT, pas enquêteur !\n"
            "- Tu dois identifier quel suspect est interrogé selon le contexte de la question\n"
            "- Réponds UNIQUEMENT dans le rôle de ce suspect spécifique\n"
            "- Respecte STRICTEMENT la personnalité et la profession de ce suspect\n"
            "- Laura = Coach fitness (froide, directe, parle de sport/fitness)\n"
            "- Aedan = Expert cybersécurité (calme, observateur, parle de tech/sécurité)\n"
            "- Nico = Développeur web (nerveux, bavard, parle de code/développement)\n"
            "- Mattéo = Étudiant infrastructures (discret, réservé, parle d'études/infrastructure)\n"
            "- Lisa = Comptable (détendue, souriante, parle de comptabilité/finances)\n"
            "- Ne mélange JAMAIS les professions ou personnalités\n"
            "- Vous êtes SUSPECTS - répondez comme des personnes arrêtées et interrogées\n"
            "- Montrez du stress, de la nervosité, de la défensive selon votre personnalité\n"
            "- Si on te demande pourquoi tu es ici, explique ta présence sur les lieux du crime\n"
            "- Ne proposez JAMAIS d'aider la police - vous êtes suspects, pas alliés !\n"
            "- Garde en mémoire les réponses précédentes pour rester cohérent\n"
            "- Ne révèle jamais directement le coupable, mais glisse des indices subtils\n"
            "- Si accusé, reste dans le caractère du suspect (défensif, mystérieux, etc.)\n"
            "- Chaque réponse doit être crédible selon la personnalité du suspect ET le contexte de crime"
            )
        }
    ]
    st.session_state.history = []
#st.subheader c'est un sous titre de streamlite && st.write("---") = ligne de séparation visuelle
st.subheader("Suspects :")
for s in suspects:
    st.write(f"**{s['name']}**: {s['description']}")

st.write("---")

question = st.text_input("Pose ta question à l'un des suspect ou accuse en un (ex: accuser Alice) :")
st.write("Cliquez sur le bouton `Envoyer` pour soumettre votre question")

if st.button("Envoyer"):
    if question.lower().startswith("accuser"):
        accused_name = question.split(" ", 1)[1]

        if accused_name.lower() == st.session_state.culprit["name"].lower():
            st.success(f"Bravo ! {accused_name} était bien le coupable !")
            st.session_state.history.append(f"Tu as accusé {accused_name} Correct !")
        else:
            st.session_state.erreurs += 1
            if st.session_state.erreurs >= 2:
                st.error(f"Mauvais choix... {accused_name} est innocent. Fin du jeu ! Le coupable était {st.session_state.culprit['name']}.")
                st.session_state.history.append(f"Tu as accusé {accused_name} Plus d'essais !")
            else:
                st.warning(f"Mauvais choix... {accused_name} est innocent. Il te reste 1 essai.")
    else:
        # ICI --> On identifie quel suspect est interrogé 
        questioned_suspect = None
        for suspect in suspects:
            if suspect["name"].lower() in question.lower():
                questioned_suspect = suspect
                break
            
            # ICI --> Ajoute le contexte du suspect interrogé à la question
        if questioned_suspect:
            contextual_question = f"Question posée à {questioned_suspect['name']} ({questioned_suspect['description']}): {question}"
        else:
            contextual_question = f"Question générale: {question}"
        
        st.session_state.messages.append({"role": "user", "content": contextual_question})
        response: ChatResponse = chat(model="gemma3", messages=st.session_state.messages)
        answer = response["message"]["content"]
        st.session_state.history.append(f"💬 Question: {question}\n💬 Réponse: {answer}")
        st.session_state.messages.append({"role": "assistant", "content": answer})

st.subheader("Historique")
for msg in st.session_state.history:
    st.markdown(msg)
