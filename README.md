# Gestionnaire de Modules et Integration API

Ce projet est une application pratique visant à renforcer la structuration d'applications Python. Il illustre l'organisation du code en packages, la gestion rigoureuse des imports et l'utilisation d'APIs externes.

## Objectifs du projet

- Structuration : Creation et organisation de packages et sous-packages.
- Gestion des imports : Maitrise des imports absolus, relatifs et controle de l'espace de noms via __all__.
- Integration d'API : Utilisation de la librairie requests pour la communication HTTP avec OpenWeatherMap.
- Gestion des dependances : Configuration d'un fichier requirements.txt pour la portabilite du projet.

## Structure du projet

TD5-Python/
├── maths/            # Package dedie aux operations mathematiques
├── utils/            # Package utilitaire pour la manipulation de donnees
├── main.py           # Point d'entree principal de l'application
├── meteo_main.py     # Script de consultation d'informations meteorologiques
├── requirements.txt  # Liste des dependances techniques
└── ...

## Installation

1. Cloner le depot :
   git clone https://github.com/Vinsmoke-Fatou/TD5-Python.git
   cd TD5-Python

2. Creer et activer un environnement virtuel :
   python -m venv venv
   source venv/bin/activate

3. Installer les dependances :
   pip install -r requirements.txt

## Utilisation

Le projet permet d'executer differentes logiques selon le fichier cible :

- Pour lancer le programme principal :
  python main.py

- Pour tester la recuperation de donnees meteo :
  python meteo_main.py

## Technologies utilisees

- Python 3.x
- Requests (gestion des requetes HTTP)
- OpenWeatherMap API

---
Projet realise dans le cadre du cursus de genie logiciel.
