# Projet enquête_ollama

Ce projet est une application Python utilisant **Ollama** pour créer un LLM (Large Language Model) d'enquête policière.  
L'interface utilisateur est réalisée avec **Streamlit**.

## Installation des dépendances

Après avoir cloné le repository, installez les dépendances nécessaires :

```bash
pip install -r requirements.txt
```

### Dépendances requises

- **streamlit** : Framework pour créer des applications web interactives
- **ollama** : Bibliothèque Python pour interagir avec Ollama (modèles IA locaux)
- **requests** : Pour effectuer des requêtes HTTP (utilisé dans le module scrapping)
- **beautifulsoup4** : Pour le parsing HTML (utilisé dans le module scrapping)

## Prérequis

- Python 3.7 ou supérieur
- Ollama installé et configuré sur votre machine (pour utiliser les modèles IA locaux)

## Lancer l'application

```
streamlit run app.py
```

Cela ouvrira l'interface utilisateur dans votre navigateur.