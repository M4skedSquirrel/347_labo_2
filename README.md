# Livre d'Or - Application Flask

## Structure du Projet

```bash

livre_dor/
├── instance/
│   ├── dev.db        # Base de données de développement
│   └── prod.db       # Base de données de production
├── static/
│   └── style.css     # Styles CSS de l'application
├── templates/
│   ├── base.html     # Template de base
│   ├── index.html    # Page principale
│   ├── login.html    # Page de connexion
│   └── register.html # Page d'inscription
├── .env              # Variables d'environnement
├── .gitignore        # Fichiers ignorés par Git
├── app.py           # Application principale
├── config.py        # Configuration de l'application
└── requirements.txt  # Dépendances du projet

```

## Configuration

### Environnement de Développement
```bash
export FLASK_ENV=development
```

### Environnement de Production
```bash
export FLASK_ENV=production
```

## Bases de Données

### Base de données de développement (dev.db)

#### Utilisateurs
1. **Admin**
   - Email: admin@test.ch
   - Password: admin
   - Role: admin

2. **User1**
   - Email: user1@test.ch
   - Password: user1
   - Role: user

3. **User2**
   - Email: user2@test.ch
   - Password: user2
   - Role: user

#### Messages de test
- Messages de bienvenue de l'admin
  - "Bienvenue sur le Livre d'Or"
  - "Règles de modération"

- Messages de User1
  - "Premier message"
  - "Super initiative"

- Messages de User2
  - "Bonjour à tous"
  - "Question"
  - "Merci pour les réponses"

### Base de données de production (prod.db)

#### Utilisateurs
1. **Admin Principal**
   - Email: admin@production.ch
   - Password: admin_secure_2024
   - Role: admin

2. **Moderateur**
   - Email: mod@production.ch
   - Password: mod_2024
   - Role: admin

3. **Jean Dupont**
   - Email: jean@example.com
   - Password: user123
   - Role: user

4. **Marie Martin**
   - Email: marie@example.com
   - Password: user456
   - Role: user

5. **Pierre Durant**
   - Email: pierre@example.com
   - Password: user789
   - Role: user

#### Messages
1. **Admin Principal**
   - "Annonce Importante" (01/01/2024)
   - "Mise à jour" (01/02/2024)
   - "Événement à venir" (01/03/2024)

2. **Moderateur**
   - "Règlement" (02/01/2024)
   - "Maintenance prévue" (10/02/2024)
   - "Rappel" (05/03/2024)

3. **Jean Dupont**
   - "Premier Retour" (03/01/2024)
   - "Retour d'expérience" (05/02/2024)

4. **Marie Martin**
   - "Question Technique" (04/01/2024)
   - "Remerciements" (15/02/2024)

5. **Pierre Durant**
   - "Suggestion" (05/01/2024)
   - "Idée" (20/02/2024)

## Fonctionnalités

- Système d'authentification complet
- Gestion des rôles (admin/user)
- CRUD des messages
- Interface responsive
- Messages flash pour les notifications
- Protection des routes
- Séparation dev/prod

## Installation

1. Créer un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
```

2. Installer les dépendances :
```bash
pip install -r requirements.txt
```

3. Configurer l'environnement :
```bash
# Développement
export FLASK_ENV=development

# Production
export FLASK_ENV=production
```

4. Lancer l'application :
```bash
python app.py
```

## Notes
- Les mots de passe de production doivent être changés lors du déploiement
- Les fichiers de base de données sont ignorés par Git
- L'environnement de développement inclut des données de test
- L'environnement de production contient des données réalistes


## Création des bases de données

### Base de données de développement
1. Lancer l'environnement de développement (Linux/MacOS):
   ```bash
   export FLASK_ENV=development
   ```

   ou 

1. Lancer l'environnement de développement (Windows):
   ```bash
   set FLASK_ENV=development
   ```
2. Exécuter le script de création :
   ```bash
   python addDataDevDb.py
   ```
3. Vérifie la création des comptes de test et messages

### Base de données de production
1. Lancer l'environnement de production (Linux/MacOS):
   ```bash
   export FLASK_ENV=production
   ```

   ou

1. Lancer l'environnement de production (Windows):
   ```bash
   set FLASK_ENV=production
   ```

2. Exécuter le script de création :
   ```bash
   python addDataProdDb.py
   ```
3. Vérifie la création des comptes utilisateurs et messages de démonstration
4. Changer les mots de passe par défaut des comptes admin