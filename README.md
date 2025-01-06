# Livre d'Or - Application Flask

## 1. Structure du Projet

### Arborescence
```bash

livre_dor/
├── instance/
│   ├── dev_guestbook.db    # Base de données de développement
│   └── prod_guestbook.db   # Base de données de production
├── templates/
│   ├── index.html         # Page principale
│   ├── login.html         # Page de connexion
│   └── register.html      # Page d'inscription
├── app.py                 # Application principale
├── models.py             # Modèles de données
├── addDataDevDb.py       # Script de données de dev
├── addDataProdDb.py      # Script de données de prod
├── Dockerfile           # Configuration Docker
├── docker-compose.yml   # Configuration Docker Compose
└── requirements.txt     # Dépendances

```

### 1.1 Fonctionnalités
- Authentification utilisateur (login/register/logout)
- Gestion des rôles (admin/user)
- CRUD des messages du livre d'or
- Auto-login en développement (apres une première connexion lors de l'installation)
- Séparation dev/prod

### 1.2 Installation et Exécution

**Prérequis**
- Docker
- Docker Compose

**Lancement en développement**
``` bash
# Construction et démarrage
docker-compose up web-dev

# Initialisation de la base de données (dans un autre terminal)
docker-compose exec web-dev python addDataDevDb.py
```

**Lancement en production**
``` bash
# Construction et démarrage
docker-compose up web-prod

# Initialisation de la base de données (dans un autre terminal)
docker-compose exec web-prod python addDataProdDb.py
```

### 1.3 Architecture Générale

**Technologies**
- Frontend : HTML, Jinja2 Templates
- Backend : Python Flask
- Base de données : SQLite
- ORM : SQLAlchemy
- Authentification : Flask-Login

**Architecture Docker**
- Base commune : python:3.9-slim
- Conteneur dev : 
  - Port 5000
  - Auto-login admin
  - Debug activé
- Conteneur prod :
  - Port 5001
  - Pas d'auto-login
  - Debug désactivé

### 1.4 Environnements

**Développement**
- URL : http://localhost:5000
- Auto-login avec admin@test.ch
- Mode debug activé
- Base de données : dev_guestbook.db
- 3 utilisateurs de test
- 10 messages de test

**Production**
- URL : http://localhost:5001
- Pas d'auto-login
- Mode debug désactivé
- Base de données : prod_guestbook.db
- 10 utilisateurs réalistes
- 30 messages de démonstration

**Vérification des environnements**
``` bash
# Vérifier l'environnement de dev
curl http://localhost:5000  # Devrait montrer une session admin active

# Vérifier l'environnement de prod
curl http://localhost:5001  # Devrait demander une connexion
```