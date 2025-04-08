from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask import send_from_directory
import os
from dotenv import load_dotenv
from datetime import datetime

# Import des formulaires et modèles
from forms import ContactForm
from models import db, Teacher, Class, Parent, Child, Enrollment, BlogPost, Contact

# Charger les variables d'environnement
load_dotenv()

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'une-cle-secrete-difficile-a-deviner'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///kindergarten.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static/img/uploads')
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# S'assurer que le dossier d'upload existe
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialiser la base de données
db.init_app(app)

# Fonction utilitaire pour vérifier l'extension des fichiers
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Remplacez cette partie dans app.py
# @app.before_first_request
# def create_tables():
#     """Crée les tables de la base de données avant la première requête"""
#     db.create_all()

# Par ceci:
with app.app_context():
    db.create_all()  # Crée les tables au démarrage de l'application

# Routes pour les pages principales
@app.route('/')
def index():
    # Récupérer quelques données pour la page d'accueil
    teachers = Teacher.query.limit(4).all()
    classes = Class.query.limit(3).all()
    return render_template('index.html', teachers=teachers, classes=classes)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    page = request.args.get('page', 1, type=int)
    posts = BlogPost.query.order_by(BlogPost.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('blog.html', posts=posts)

@app.route('/blog/<int:post_id>')
def blog_single(post_id):
    post = BlogPost.query.get_or_404(post_id)
    return render_template('single.html', post=post)

@app.route('/class')
def class_page():
    classes = Class.query.all()
    return render_template('class.html', classes=classes)

@app.route('/class/<int:class_id>')
def class_detail(class_id):
    class_obj = Class.query.get_or_404(class_id)
    return render_template('class_detail.html', class_obj=class_obj)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        new_contact = Contact(
            name=form.name.data,
            email=form.email.data,
            subject=form.subject.data,
            message=form.message.data
        )
        db.session.add(new_contact)
        db.session.commit()
        flash('Votre message a été envoyé avec succès!', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html', form=form)

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/team')
def team():
    teachers = Teacher.query.all()
    return render_template('team.html', teachers=teachers)

@app.route('/team/<int:teacher_id>')
def teacher_detail(teacher_id):
    teacher = Teacher.query.get_or_404(teacher_id)
    return render_template('teacher_detail.html', teacher=teacher)

# Routes pour l'inscription
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Code pour l'inscription des parents
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Code pour la connexion des parents
    return render_template('login.html')

@app.route('/logout')
def logout():
    # Code pour la déconnexion
    return redirect(url_for('index'))

@app.route('/profile')
def profile():
    # Code pour afficher et modifier le profil
    return render_template('profile.html')

@app.route('/enroll/<int:class_id>', methods=['GET', 'POST'])
def enroll(class_id):
    # Code pour l'inscription à un cours
    return render_template('enroll.html')

# Gestionnaires d'erreurs personnalisés
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static', 'img'),
                              'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/lib/<path:filename>')
def lib_files(filename):
    return send_from_directory(os.path.join(app.root_path, 'static', 'lib'), filename)

@app.route('/mail/<path:filename>')
def mail_files(filename):
    return send_from_directory('mail', filename)



if __name__ == '__main__':
    app.run(debug=True)