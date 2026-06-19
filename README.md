# TP 5 – Modules Python

## Objectif

Ce TP explore la création, l'organisation et l'utilisation des modules Python dans un projet structuré en packages. On y aborde également les imports relatifs, la gestion des exports avec `__all__`, ainsi que l'utilisation d'un module externe (`requests`) pour effectuer des requêtes HTTP et interroger l'API OpenWeatherMap.

---

## Structure du projet

```
mon_projet/
├── __init__.py
├── main.py
├── main2.py
├── main3.py
├── meteo_main.py
├── requirements.txt
├── maths/
│   ├── __init__.py
│   ├── operations.py
│   └── statistiques.py
├── utils/
│   ├── __init__.py
│   └── string_utils.py
└── captures/
```

---

## Installation

### 1. (Optionnel) Créer un environnement virtuel

```bash
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## Exécution

Depuis le dossier **parent** de `mon_projet/` :

```bash
# main.py : opérations, statistiques, chaînes, requête HTTP
python mon_projet/main.py

# main2.py : import relatif + somme des carrés
python -m mon_projet.main2

# main3.py : test de __all__
python mon_projet/main3.py

# meteo_main.py : météo en temps réel via OpenWeatherMap
python mon_projet/meteo_main.py
```

---

## Captures d'écran

Les captures d'exécution sont disponibles dans le dossier `captures/`.
