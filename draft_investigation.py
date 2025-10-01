import random
from ollama import chat, ChatResponse

suspects = [
    {"name": "Aedan", "description": "Il travaille dans la cybersécurité, calme et observateur."},
    {"name": "Nico", "description": "Il est Développeur web, assez nerveux et parle vite."},
    {"name": "Mattéo", "description": "Il est étudiant en infrastructure, timide, réservé et mystérieux."},
    {"name": "Lisa", "description": "Elle est comptable, détendue mais parfois mystérieuse."},
    {"name": "Laura", "description": "Elle est coach de fitness, très froide et directe."}
]

culprit = random.choice(suspects)

print("Bienvenue dans l'enquête interactive !")
print("Il y a 5 suspects :")
for s in suspects:
    print(f"{s['name']}: {s['description']}")
print("\nPose des questions directement aux suspects pour découvrir le coupable !")
print("⚠️ Vous avez deux essais maximum pour accuser.\n")

messages = [
    {"role": "system", "content": f"Tu es un jeu d'enquête. Voici les suspects : {suspects}. L'un d'eux est coupable : {culprit['name']}. \
Réponds toujours dans le rôle du suspect interrogé, en restant fidèle à sa personnalité. \
Ne révèle jamais directement le coupable. L'utilisateur a le droit d'accuser au maximum deux fois."}
]

erreurs = 0
max_erreurs = 2

while True:
    question = input("👮 Ta question (ou 'accuser [nom]' pour désigner un suspect): ")
    
    if question.lower().startswith("accuser"):
        accused_name = question.split(" ", 1)[1]

        if accused_name.lower() == culprit["name"].lower():
            print(f"✅ Bravo ! {accused_name} était bien le coupable ! 🎉")
            break
        else:
            erreurs += 1
            if erreurs >= max_erreurs:
                print(f"❌ Mauvais choix... {accused_name} est innocent.")
                print(f"💀 Vous avez utilisé vos {max_erreurs} essais. Le vrai coupable était {culprit['name']}.")
                break
            else:
                print(f"❌ Mauvais choix... {accused_name} est innocent. Il vous reste {max_erreurs - erreurs} essai(s).")
        continue

    messages.append({"role": "user", "content": question})
    response: ChatResponse = chat(model="gemma3", messages=messages)
    answer = response["message"]["content"]
    print(f"💬 Réponse du suspect : {answer}")
    messages.append({"role": "assistant", "content": answer})
