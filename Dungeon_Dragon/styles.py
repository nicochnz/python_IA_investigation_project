# styles.py - Styles CSS pour le thème fantasy D&D

RETRO_FANTASY_CSS = """
<style>
    /* Thème rétro fantasy avec ambiance médiévale */
    .stApp {
        background: linear-gradient(135deg, #1a0f0a 0%, #2d1b13 25%, #3d2817 50%, #2d1b13 75%, #1a0f0a 100%);
        background-image: 
            radial-gradient(circle at 20% 50%, rgba(255, 215, 0, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(255, 140, 0, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 40% 80%, rgba(255, 69, 0, 0.1) 0%, transparent 50%);
        color: #f4e4bc;
        font-family: 'Cinzel', 'Times New Roman', serif;
    }
    
    /* Effet de parchemin vieilli */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
            repeating-linear-gradient(
                0deg,
                transparent,
                transparent 2px,
                rgba(139, 69, 19, 0.03) 2px,
                rgba(139, 69, 19, 0.03) 4px
            );
        pointer-events: none;
        z-index: 1000;
    }
    
    /* Titre principal style médiéval */
    .main-title {
        color: #ffd700;
        font-family: 'Cinzel', 'Times New Roman', serif;
        font-size: 3.5rem;
        font-weight: bold;
        text-align: center;
        text-shadow: 
            2px 2px 0px #8b4513,
            4px 4px 0px #654321,
            0 0 20px rgba(255, 215, 0, 0.5);
        margin-bottom: 2rem;
        border: 3px solid #ffd700;
        border-radius: 15px;
        padding: 1.5rem;
        background: linear-gradient(45deg, rgba(139, 69, 19, 0.3), rgba(160, 82, 45, 0.2));
        box-shadow: 
            0 0 30px rgba(255, 215, 0, 0.4),
            inset 0 0 20px rgba(255, 215, 0, 0.1);
        position: relative;
    }
    
    /* Effet de relief sur le titre */
    .main-title::before {
        content: '';
        position: absolute;
        top: -3px;
        left: -3px;
        right: -3px;
        bottom: -3px;
        background: linear-gradient(45deg, #8b4513, #654321);
        border-radius: 18px;
        z-index: -1;
    }
    
    /* Sous-titres style médiéval */
    h1, h2, h3 {
        color: #ffd700 !important;
        font-family: 'Cinzel', 'Times New Roman', serif;
        text-shadow: 1px 1px 2px #8b4513;
        border-bottom: 2px solid #ffd700;
        padding-bottom: 0.5rem;
        position: relative;
    }
    
    /* Texte principal */
    .stMarkdown {
        color: #f4e4bc !important;
        font-family: 'Cinzel', 'Times New Roman', serif;
        line-height: 1.6;
    }
    
    /* Boutons style médiéval */
    .stButton > button {
        background: linear-gradient(45deg, #8b4513, #a0522d);
        color: #ffd700;
        border: 2px solid #ffd700;
        border-radius: 8px;
        padding: 0.7rem 1.5rem;
        font-family: 'Cinzel', 'Times New Roman', serif;
        font-weight: bold;
        font-size: 1.1rem;
        box-shadow: 
            0 4px 8px rgba(0, 0, 0, 0.3),
            0 0 15px rgba(255, 215, 0, 0.2);
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 215, 0, 0.2), transparent);
        transition: left 0.5s;
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }
    
    .stButton > button:hover {
        background: linear-gradient(45deg, #a0522d, #cd853f);
        box-shadow: 
            0 6px 12px rgba(0, 0, 0, 0.4),
            0 0 25px rgba(255, 215, 0, 0.4);
        transform: translateY(-2px);
    }
    
    /* Métriques style parchemin */
    .metric-container {
        background: linear-gradient(135deg, rgba(139, 69, 19, 0.4), rgba(160, 82, 45, 0.3));
        border: 2px solid #ffd700;
        border-radius: 12px;
        padding: 1.2rem;
        margin: 0.5rem;
        box-shadow: 
            0 4px 8px rgba(0, 0, 0, 0.3),
            inset 0 0 10px rgba(255, 215, 0, 0.1);
        font-family: 'Cinzel', 'Times New Roman', serif;
        position: relative;
    }
    
    .metric-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: 
            radial-gradient(circle at 20% 20%, rgba(255, 215, 0, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 80%, rgba(255, 140, 0, 0.1) 0%, transparent 50%);
        border-radius: 10px;
        pointer-events: none;
    }
    
    /* Expanders style médiéval */
    .streamlit-expanderHeader {
        background: linear-gradient(45deg, rgba(139, 69, 19, 0.6), rgba(160, 82, 45, 0.4));
        color: #ffd700 !important;
        border: 2px solid #ffd700;
        border-radius: 8px;
        font-family: 'Cinzel', 'Times New Roman', serif;
        font-weight: bold;
        font-size: 1.1rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    /* Zone de texte style parchemin */
    .stTextInput > div > div > input {
        background: rgba(139, 69, 19, 0.3);
        color: #f4e4bc;
        border: 2px solid #ffd700;
        border-radius: 8px;
        font-family: 'Cinzel', 'Times New Roman', serif;
        box-shadow: 
            0 0 10px rgba(255, 215, 0, 0.2),
            inset 0 0 5px rgba(0, 0, 0, 0.2);
    }
    
    /* Selectbox style médiéval */
    .stSelectbox > div > div {
        background: rgba(139, 69, 19, 0.3);
        color: #f4e4bc;
        border: 2px solid #ffd700;
        border-radius: 8px;
        font-family: 'Cinzel', 'Times New Roman', serif;
        box-shadow: 
            0 0 10px rgba(255, 215, 0, 0.2),
            inset 0 0 5px rgba(0, 0, 0, 0.2);
    }
    
    /* Spinner style doré */
    .stSpinner {
        color: #ffd700 !important;
    }
    
    /* Messages d'historique style parchemin */
    .history-message {
        background: linear-gradient(135deg, rgba(139, 69, 19, 0.3), rgba(160, 82, 45, 0.2));
        border-left: 4px solid #ffd700;
        padding: 1.2rem;
        margin: 1rem 0;
        border-radius: 0 12px 12px 0;
        box-shadow: 
            0 2px 8px rgba(0, 0, 0, 0.3),
            inset 0 0 10px rgba(255, 215, 0, 0.1);
        font-family: 'Cinzel', 'Times New Roman', serif;
        border: 1px solid rgba(255, 215, 0, 0.3);
        position: relative;
    }
    
    .history-message::before {
        content: '📜';
        position: absolute;
        top: 0.5rem;
        right: 0.5rem;
        font-size: 1.2rem;
        opacity: 0.6;
    }
    
    /* Inventaire style coffre */
    .inventory-item {
        background: linear-gradient(135deg, rgba(139, 69, 19, 0.4), rgba(160, 82, 45, 0.3));
        border: 1px solid #ffd700;
        border-radius: 6px;
        padding: 0.7rem;
        margin: 0.25rem 0;
        font-family: 'Cinzel', 'Times New Roman', serif;
        box-shadow: 
            0 2px 4px rgba(0, 0, 0, 0.3),
            inset 0 0 5px rgba(255, 215, 0, 0.1);
        position: relative;
    }
    
    .inventory-item::before {
        content: '💰';
        margin-right: 0.5rem;
    }
    
    /* Effet de pulsation dorée */
    .metric-container:hover {
        animation: goldenPulse 2s ease-in-out infinite;
    }
    
    @keyframes goldenPulse {
        0% { 
            box-shadow: 
                0 4px 8px rgba(0, 0, 0, 0.3),
                inset 0 0 10px rgba(255, 215, 0, 0.1),
                0 0 15px rgba(255, 215, 0, 0.2);
        }
        50% { 
            box-shadow: 
                0 4px 8px rgba(0, 0, 0, 0.3),
                inset 0 0 10px rgba(255, 215, 0, 0.1),
                0 0 25px rgba(255, 215, 0, 0.4);
        }
        100% { 
            box-shadow: 
                0 4px 8px rgba(0, 0, 0, 0.3),
                inset 0 0 10px rgba(255, 215, 0, 0.1),
                0 0 15px rgba(255, 215, 0, 0.2);
        }
    }
    
    /* Effet de brillance sur les boutons */
    .stButton > button:active {
        transform: translateY(1px);
        box-shadow: 
            0 2px 4px rgba(0, 0, 0, 0.3),
            0 0 10px rgba(255, 215, 0, 0.3);
    }
</style>
"""

def apply_retro_fantasy_theme():
    """Applique le thème rétro fantasy au jeu"""
    import streamlit as st
    st.markdown(RETRO_FANTASY_CSS, unsafe_allow_html=True)

def create_title():
    """Crée le titre principal stylisé style médiéval"""
    import streamlit as st
    st.markdown('<h1 class="main-title">🏰 CHRONIQUES DE DONJONS & DRAGONS 🏰</h1>', unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; font-size: 1.3rem; color: #f4e4bc; margin-bottom: 2rem; font-family: 'Cinzel', 'Times New Roman', serif;">
        ✨ Bienvenue dans un monde de magie et d'aventure ! ✨<br>
        Choisissez votre héros et plongez dans une quête épique.
    </div>
    """, unsafe_allow_html=True)

def create_stats_display(pv, mana, gold):
    """Crée l'affichage des statistiques style médiéval"""
    import streamlit as st
    st.markdown("### ⚔️ Statistiques de votre héros")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div class="metric-container">
            <h4 style="color: #ff6b6b; margin: 0; font-family: 'Cinzel', 'Times New Roman', serif;">💖 Points de Vie</h4>
            <h2 style="color: #ffd700; margin: 0; font-family: 'Cinzel', 'Times New Roman', serif;">{pv}</h2>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="metric-container">
            <h4 style="color: #4ecdc4; margin: 0; font-family: 'Cinzel', 'Times New Roman', serif;">✨ Mana</h4>
            <h2 style="color: #ffd700; margin: 0; font-family: 'Cinzel', 'Times New Roman', serif;">{mana}</h2>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="metric-container">
            <h4 style="color: #ffe66d; margin: 0; font-family: 'Cinzel', 'Times New Roman', serif;">💰 Pièces d'Or</h4>
            <h2 style="color: #ffd700; margin: 0; font-family: 'Cinzel', 'Times New Roman', serif;">{gold}</h2>
        </div>
        """, unsafe_allow_html=True)

def create_history_display(messages):
    """Crée l'affichage de l'historique style médiéval"""
    import streamlit as st
    st.markdown("### 📖 Chroniques de votre aventure")
    for message in messages:
        st.markdown(f"""
        <div class="history-message">
            {message}
        </div>
        """, unsafe_allow_html=True)

def create_inventory_display(inventory):
    """Crée l'affichage de l'inventaire style médiéval"""
    import streamlit as st
    if inventory:
        st.markdown("### 🎒 Inventaire")
        for item in inventory:
            st.markdown(f"""
            <div class="inventory-item">
                ✨ {item}
            </div>
            """, unsafe_allow_html=True)
