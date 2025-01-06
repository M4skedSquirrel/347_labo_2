from app import app, db
from models import User, Message
from werkzeug.security import generate_password_hash

def add_dev_data():
    # Création des utilisateurs s'ils n'existent pas
    users = {
        'admin@test.ch': {'password': 'admin', 'role': 'admin'},
        'user1@test.ch': {'password': 'user1', 'role': 'user'},
        'user2@test.ch': {'password': 'user2', 'role': 'user'}
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
            print(f"Compte {data['role']} ({username}) créé avec succès!")
        created_users[username] = user

    # Création des messages fictifs si la table est vide
    if Message.query.count() == 0:
        fake_messages = [
            {
                'title': 'Bienvenue sur le livre d\'or!',
                'content': 'C\'est un plaisir de partager ce moment avec vous tous.',
                'author': created_users['admin@test.ch']
            },
            {
                'title': 'Super événement',
                'content': 'Je tenais à remercier toute l\'équipe pour cette organisation parfaite.',
                'author': created_users['user1@test.ch']
            },
            {
                'title': 'Message de remerciement',
                'content': 'Un grand merci à tous les participants. C\'était une journée mémorable!',
                'author': created_users['user2@test.ch']
            },
            {
                'title': 'Félicitations',
                'content': 'Excellente initiative, continuez comme ça!',
                'author': created_users['user1@test.ch']
            },
            {
                'title': 'Impressionnant',
                'content': 'Je suis vraiment impressionné par la qualité de l\'événement. À refaire!',
                'author': created_users['admin@test.ch']
            },
            {
                'title': 'Retour positif',
                'content': 'Une expérience enrichissante et des rencontres formidables.',
                'author': created_users['user2@test.ch']
            },
            {
                'title': 'Merci pour tout',
                'content': 'Un grand bravo aux organisateurs pour leur travail remarquable.',
                'author': created_users['user1@test.ch']
            },
            {
                'title': 'Excellent moment',
                'content': 'Je garde un excellent souvenir de cette journée.',
                'author': created_users['admin@test.ch']
            },
            {
                'title': 'À refaire',
                'content': 'Vivement la prochaine édition, on sera là!',
                'author': created_users['user2@test.ch']
            },
            {
                'title': 'Bravo à tous',
                'content': 'Une organisation au top et une ambiance extraordinaire.',
                'author': created_users['user1@test.ch']
            }
        ]

        for msg in fake_messages:
            message = Message(
                title=msg['title'],
                content=msg['content'],
                author=msg['author']
            )
            db.session.add(message)
        
        db.session.commit()
        print("10 messages fictifs créés avec succès!")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        add_dev_data() 