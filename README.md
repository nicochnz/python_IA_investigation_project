# Projet enquête_ollama

Ce projet est une application Python utilisant **Ollama** pour créer un LLM (Large Language Model) d'enquête policière.  
L'interface utilisateur est réalisée avec **Streamlit**.

## Installation des dépendances

Après avoir cloné le repository, installez les dépendances nécessaires :

```bash
pip install -r requirements.txt
```

**Ou installation manuelle :**
```bash
pip install streamlit
pip install ollama
pip install requests
pip install beautifulsoup4
```

### Dépendances requises

- **streamlit** : Framework pour créer des applications web interactives
- **ollama** : Bibliothèque Python pour interagir avec Ollama (modèles IA locaux)
- **requests** : Pour effectuer des requêtes HTTP (utilisé dans le module scrapping)
- **beautifulsoup4** : Pour le parsing HTML (utilisé dans le module scrapping)
**installation manuelle :**
```bash
pip install streamlit
pip install ollama
pip install requests
pip install beautifulsoup4
## Prérequis

- Python 3.7 ou supérieur
- Ollama installé et configuré sur votre machine (pour utiliser les modèles IA locaux)

## Lancer l'application

### Méthode 1 (recommandée) :
```bash
python -m streamlit run app.py
```

### Méthode 2 :
```bash
streamlit run app.py
```

