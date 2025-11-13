
import streamlit as st
import random
from ollama import chat, ChatResponse
from characters import get_welcome_message

def initialize_game_state():
    """Initialise l'état du jeu"""
    if "game_initialized" not in st.session_state:
        st.session_state.game_initialized = False
        st.session_state.selected_character = None
        st.session_state.current_scene = "character_selection"
        st.session_state.game_history = []
        st.session_state.player_stats = {"PV": 100, "Mana": 50, "Pièces d'or": 50}
        st.session_state.inventory = []
        st.session_state.scene_count = 0

def initialize_ai_messages(character):
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "system",
                "content": (
                    f"Tu es un Maître de Donjon D&D. Classe: {character['name']} - {character['description']}\n"
                    f"Stats: {character['stats']}\n"
                    f"Capacités: {character['special_abilities']}\n"
                    f"Stats actuels: {st.session_state.player_stats}\n"
                    f"Scène: {st.session_state.scene_count}\n\n"
                    "RÈGLES:\n"
                    "- Histoire immersive D&D adaptée à la classe\n"
                    "- OBLIGATOIRE: Termine chaque réponse par exactement 3 choix numérotés au format '1. [choix]', '2. [choix]', '3. [choix]'\n"
                    "- Les choix influencent l'histoire et les stats\n"
                    "- Utilise les capacités spéciales du personnage\n"
                    "- Varie: combat, énigmes, exploration, social\n"
                    "- Combats réduisent PV, sorts consomment Mana\n"
                    "- Succès rapportent or/objets\n"
                    "- Minimum 5-7 scènes\n"
                    "- Univers fantasy médiéval\n"
                    "- IMPORTANT: Chaque réponse doit se terminer par 3 choix clairement numérotés"
                )
            }
        ]
        
        welcome_message = get_welcome_message(character['name'])
        st.session_state.game_history.append(welcome_message)
        st.session_state.messages.append({"role": "assistant", "content": welcome_message})

def process_player_choice(selected_choice):

    player_action = f"Le joueur choisit : {selected_choice}"
    st.session_state.messages.append({"role": "user", "content": player_action})
    
    try:
        with st.spinner("🎲 Le Maître de Donjon réfléchit..."):
            response: ChatResponse = chat(model="phi3:mini", messages=st.session_state.messages)
        ai_response = response["message"]["content"]
        
        st.session_state.game_history.append(ai_response)
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
        st.session_state.scene_count += 1
        
        update_player_stats(ai_response)
        
        return True
        
    except Exception as e:
        st.error(f"Erreur lors de la génération de la réponse : {e}")
        return False

def update_player_stats(ai_response):
    """Met à jour les stats du joueur basées sur la réponse IA"""
    response_lower = ai_response.lower()
    
    if "blessé" in response_lower or "dégâts" in response_lower or "attaque" in response_lower:
        damage = random.randint(5, 15)
        st.session_state.player_stats["PV"] = max(0, st.session_state.player_stats["PV"] - damage)
    
    # Consommation de mana
    if "sort" in response_lower or "magie" in response_lower or "incantation" in response_lower:
        mana_cost = random.randint(3, 8)
        st.session_state.player_stats["Mana"] = max(0, st.session_state.player_stats["Mana"] - mana_cost)
    
    # Gain d'or
    if "trésor" in response_lower or "or" in response_lower or "pièces" in response_lower:
        gold_gain = random.randint(10, 30)
        st.session_state.player_stats["Pièces d'or"] += gold_gain
    
    # Nouvel objet (seulement si explicitement mentionné)
    if ("trouve" in response_lower and ("objet" in response_lower or "équipement" in response_lower or "arme" in response_lower or "armure" in response_lower)) or "récupère" in response_lower:
        new_item = f"Objet mystérieux (scène {st.session_state.scene_count})"
        st.session_state.inventory.append(new_item)

def check_game_over():
    """Vérifie si le jeu est terminé"""
    if st.session_state.player_stats["PV"] <= 0:
        st.error("💀 Votre personnage est mort ! L'aventure se termine ici...")
        return True
    return False

def reset_game():
    """Remet à zéro le jeu"""
    st.session_state.game_initialized = False
    st.session_state.current_scene = "character_selection"
    st.rerun()

def extract_choices_from_message(message):
    """Extrait les choix numérotés d'un message"""
    choices = []
    lines = message.split('\n')
    for line in lines:
        line = line.strip()
        # Cherche différents formats de choix
        if (line.startswith(('1.', '2.', '3.', '4.', '5.')) or 
            line.startswith(('1)', '2)', '3)', '4)', '5)')) or
            line.startswith(('1-', '2-', '3-', '4-', '5-')) or
            line.startswith(('1 ', '2 ', '3 ', '4 ', '5 '))):
            choices.append(line)
    return choices
