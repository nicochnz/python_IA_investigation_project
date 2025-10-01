# draft_dungeon.py - Jeu D&D principal (version refactorisée)

import streamlit as st
from characters import character_classes
from styles import apply_retro_fantasy_theme, create_title, create_stats_display, create_history_display, create_inventory_display
from game_logic import (
    initialize_game_state, initialize_ai_messages, process_player_choice, 
    check_game_over, reset_game, extract_choices_from_message
)

# Configuration de la page
st.set_page_config(
    page_title="🏰 Aventures D&D",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Application du thème rétro fantasy
apply_retro_fantasy_theme()
create_title()

# Initialisation du jeu
initialize_game_state()

# === SÉLECTION DE PERSONNAGE ===
if st.session_state.current_scene == "character_selection":
    st.subheader("🎭 Choisissez votre héros :")
    
    for i, char_class in enumerate(character_classes):
        with st.expander(f"**{char_class['name']}** - {char_class['description']}"):
            st.write(f"**Armes :** {char_class['weapon']}")
            st.write(f"**Armure :** {char_class['armor']}")
            st.write("**Statistiques :**")
            for stat, value in char_class['stats'].items():
                st.write(f"  • {stat}: {value}")
            st.write("**Capacités spéciales :**")
            for ability in char_class['special_abilities']:
                st.write(f"  • {ability}")
            
            if st.button(f"Choisir {char_class['name']}", key=f"select_{i}"):
                st.session_state.selected_character = char_class
                st.session_state.current_scene = "game_start"
                st.session_state.game_initialized = True
                st.rerun()

# === JEU PRINCIPAL ===
if st.session_state.current_scene == "game_start":
    character = st.session_state.selected_character
    
    st.subheader(f"🎮 Aventure de {character['name']}")
    
    # Affichage des stats stylisées
    create_stats_display(
        st.session_state.player_stats["PV"],
        st.session_state.player_stats["Mana"],
        st.session_state.player_stats["Pièces d'or"]
    )
    
    st.write("---")
    
    # Initialisation des messages IA
    initialize_ai_messages(character)
    
    # Affichage de l'historique stylisé
    create_history_display(st.session_state.game_history)
    
    st.write("---")
    
    # Interface de choix
    st.subheader("🎯 Vos choix")
    
    # Détection des choix dans le dernier message
    last_message = st.session_state.game_history[-1] if st.session_state.game_history else ""
    choices = extract_choices_from_message(last_message)
    
    if choices:
        selected_choice = st.selectbox(
            "Choisissez votre action :",
            choices,
            key=f"choice_{st.session_state.scene_count}"
        )
        
        if st.button("🎲 Lancer l'action", key=f"action_{st.session_state.scene_count}"):
            if process_player_choice(selected_choice):
                if check_game_over():
                    if st.button("🔄 Recommencer"):
                        reset_game()
                else:
                    st.rerun()
    
    # Bouton pour recommencer
    if st.button("🔄 Recommencer l'aventure"):
        reset_game()

# === AFFICHAGE DE L'INVENTAIRE ===
if st.session_state.game_initialized and st.session_state.inventory:
    create_inventory_display(st.session_state.inventory)
