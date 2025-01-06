from models import User, Message, db
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta
import random
from flask import Flask

# Création d'une nouvelle instance Flask pour la production
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prod_guestbook.db'
db.init_app(app)

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
        },
        {
            'title': 'Superbe organisation',
            'content': 'Tout a été pensé dans les moindres détails. Une organisation irréprochable!'
        },
        {
            'title': 'Équipe au top',
            'content': 'Une équipe dynamique et professionnelle qui sait recevoir. Bravo à tous!'
        },
        {
            'title': 'Expérience inoubliable',
            'content': 'Ces moments resteront gravés dans nos mémoires. Merci pour tout!'
        },
        {
            'title': 'Accueil chaleureux',
            'content': 'Nous avons été reçus comme des rois. L\'accueil était parfait.'
        },
        {
            'title': 'Prestations exceptionnelles',
            'content': 'La qualité des prestations était au rendez-vous. Une expérience à renouveler!'
        },
        {
            'title': 'Soirée magique',
            'content': 'Une soirée qui restera dans les annales. Tout était magique!'
        },
        {
            'title': 'Recommandation sincère',
            'content': 'Je recommande sans hésitation. Une valeur sûre!'
        },
        {
            'title': 'Personnel attentionné',
            'content': 'Le personnel était aux petits soins. Un service irréprochable!'
        },
        {
            'title': 'Ambiance extraordinaire',
            'content': 'L\'ambiance était au rendez-vous. Un moment de partage exceptionnel!'
        },
        {
            'title': 'Satisfaction totale',
            'content': 'Rien à redire, tout était parfait de A à Z. Bravo!'
        },
        {
            'title': 'Merci infiniment',
            'content': 'Un grand merci pour ces moments de bonheur partagés.'
        },
        {
            'title': 'Événement réussi',
            'content': 'Un événement parfaitement réussi qui laissera de beaux souvenirs.'
        },
        {
            'title': 'Qualité premium',
            'content': 'Des prestations de grande qualité qui méritent d\'être soulignées.'
        },
        {
            'title': 'Ravie de l\'expérience',
            'content': 'Une expérience enrichissante et pleine de surprises. À refaire!'
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