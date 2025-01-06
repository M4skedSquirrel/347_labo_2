from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Message
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'votre_clé_secrète'

# Utiliser la DB de prod ou dev selon l'environnement
if os.environ.get('FLASK_ENV') == 'production':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prod_guestbook.db'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dev_guestbook.db'

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    messages = Message.query.order_by(Message.created_at.desc()).all()
    return render_template('index.html', messages=messages)

@app.route('/message/new', methods=['GET', 'POST'])
@login_required
def new_message():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        message = Message(title=title, content=content, author=current_user)
        db.session.add(message)
        db.session.commit()
        flash('Message ajouté avec succès!')
        return redirect(url_for('index'))
    return render_template('new_message.html')

@app.route('/message/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_message(id):
    message = Message.query.get_or_404(id)
    if current_user.role != 'admin' and message.user_id != current_user.id:
        flash('Non autorisé')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        message.title = request.form.get('title')
        message.content = request.form.get('content')
        db.session.commit()
        flash('Message modifié avec succès!')
        return redirect(url_for('index'))
    return render_template('edit_message.html', message=message)

@app.route('/message/<int:id>/delete')
@login_required
def delete_message(id):
    message = Message.query.get_or_404(id)
    if current_user.role != 'admin' and message.user_id != current_user.id:
        flash('Non autorisé')
        return redirect(url_for('index'))
    
    db.session.delete(message)
    db.session.commit()
    flash('Message supprimé avec succès!')
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        if user:
            flash('Nom d\'utilisateur déjà pris')
            return redirect(url_for('register'))
        
        new_user = User(
            username=username,
            password=generate_password_hash(password),
            role='user'
        )
        db.session.add(new_user)
        db.session.commit()
        
        flash('Inscription réussie!')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Connexion réussie!')
            return redirect(url_for('index'))
        
        flash('Nom d\'utilisateur ou mot de passe incorrect')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Vous êtes déconnecté')
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True) 