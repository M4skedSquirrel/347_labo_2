from app import app, db
from models import User, Message
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta
import random

def add_prod_data():
    # Création des utilisateurs
    users = {
        'admin@example.com': {'password': 'adminPass123', 'role': 'admin', 'name': 'Administrator'},
        'manager@example.com': {'password': 'managerPass123', 'role': 'admin', 'name': 'Manager'},
        'john.doe@example.com': {'password': 'userPass123', 'role': 'user', 'name': 'John Doe'},
        'emma.smith@example.com': {'password': 'userPass123', 'role': 'user', 'name': 'Emma Smith'},
        'michael.brown@example.com': {'password': 'userPass123', 'role': 'user', 'name': 'Michael Brown'},
        'sarah.wilson@example.com': {'password': 'userPass123', 'role': 'user', 'name': 'Sarah Wilson'},
        'david.miller@example.com': {'password': 'userPass123', 'role': 'user', 'name': 'David Miller'},
        'lisa.anderson@example.com': {'password': 'userPass123', 'role': 'user', 'name': 'Lisa Anderson'},
        'james.taylor@example.com': {'password': 'userPass123', 'role': 'user', 'name': 'James Taylor'},
        'emily.thomas@example.com': {'password': 'userPass123', 'role': 'user', 'name': 'Emily Thomas'}
    }

    created_users = {}
    for username, data in users.items():
        user = User.query.filter_by(username=username).first()
        if not user:
            user = User(
                username=username,
                password=generate_password_hash(data['password']),
                role=data['role']
            )
            db.session.add(user)
            db.session.commit()
            print(f"Compte {data['role']} ({data['name']}) créé avec succès!")
        created_users[username] = user

    # Messages possibles pour plus de variété
    message_templates = [
        {
            'title': 'Excellente expérience client',
            'content': 'Le service était impeccable et le personnel très attentionné. Je recommande vivement!'
        },
        {
            'title': 'Merci pour cette soirée',
            'content': 'Une ambiance fantastique et une organisation parfaite. Nous avons passé un moment inoubliable.'
        },
        {
            'title': 'Service exceptionnel',
            'content': 'Je tiens à souligner le professionnalisme de l\'équipe. Tout était parfait du début à la fin.'
        },
        {
            'title': 'Très satisfait',
            'content': 'Une prestation de haute qualité qui a dépassé nos attentes. Merci à toute l\'équipe!'
        },
        {
            'title': 'Belle découverte',
            'content': 'Quelle agréable surprise! Nous reviendrons certainement.'
        },
        {
            'title': 'Moment mémorable',
            'content': 'Un grand merci pour cette expérience unique. Tout était parfaitement orchestré.'
        }
    ]

    # Création des messages si la table est vide
    if Message.query.count() == 0:
        # Date de base pour les messages (30 jours avant aujourd'hui)
        base_date = datetime.now() - timedelta(days=30)
        
        for i in range(30):
            # Sélection aléatoire d'un utilisateur et d'un message template
            user = random.choice(list(created_users.values()))
            template = random.choice(message_templates)
            
            # Création d'une date aléatoire dans les 30 derniers jours
            random_days = random.randint(0, 30)
            message_date = base_date + timedelta(days=random_days)
            
            # Personnalisation du message
            message = Message(
                title=f"{template['title']} #{i+1}",
                content=f"{template['content']} [Message créé le {message_date.strftime('%d/%m/%Y')}]",
                author=user,
                created_at=message_date
            )
            db.session.add(message)
        
        db.session.commit()
        print("30 messages de production créés avec succès!")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        add_prod_data() 