from app import app, db
from models import Teacher, Class, BlogPost
from datetime import datetime, date
import random

def seed_database():
    """Initialise la base de données avec des données de démonstration"""
    
    # Vérifier si des données existent déjà
    if Teacher.query.first():
        print("La base de données contient déjà des données. Opération annulée.")
        return
    
    print("Initialisation de la base de données...")
    
    # Créer des enseignants
    teachers = [
        {
            'name': 'Sarah Johnson',
            'position': 'Professeur en chef',
            'description': 'Sarah a plus de 15 ans d\'expérience dans l\'éducation préscolaire avec une formation spécialisée en développement de la petite enfance.',
            'image': 'team-1.jpg',
            'email': 'sarah.johnson@example.com',
            'phone': '+33 6 12 34 56 78',
            'facebook': 'facebook.com/sarahjohnson',
            'twitter': 'twitter.com/sarahjohnson',
            'instagram': 'instagram.com/sarahjohnson'
        },
        {
            'name': 'Marc Dubois',
            'position': 'Professeur d\'art',
            'description': 'Marc est spécialisé dans l\'enseignement des arts créatifs aux jeunes enfants, favorisant l\'expression et la créativité.',
            'image': 'team-2.jpg',
            'email': 'marc.dubois@example.com',
            'phone': '+33 6 23 45 67 89',
            'facebook': 'facebook.com/marcdubois',
            'twitter': 'twitter.com/marcdubois',
            'instagram': 'instagram.com/marcdubois'
        },
        {
            'name': 'Emma Garcia',
            'position': 'Professeur de musique',
            'description': 'Emma apporte la joie de la musique aux enfants avec une approche ludique et éducative du rythme et de la mélodie.',
            'image': 'team-3.jpg',
            'email': 'emma.garcia@example.com',
            'phone': '+33 6 34 56 78 90',
            'facebook': 'facebook.com/emmagarcia',
            'twitter': 'twitter.com/emmagarcia',
            'instagram': 'instagram.com/emmagarcia'
        },
        {
            'name': 'Thomas Martin',
            'position': 'Professeur d\'activités physiques',
            'description': 'Thomas aide les enfants à développer leurs capacités motrices et leur coordination par des jeux et des activités sportives adaptées.',
            'image': 'team-4.jpg',
            'email': 'thomas.martin@example.com',
            'phone': '+33 6 45 67 89 01',
            'facebook': 'facebook.com/thomasmartin',
            'twitter': 'twitter.com/thomasmartin',
            'instagram': 'instagram.com/thomasmartin'
        }
    ]
    
    teacher_objects = []
    for teacher_data in teachers:
        teacher = Teacher(**teacher_data)
        db.session.add(teacher)
        teacher_objects.append(teacher)
    
    # Créer des classes
    classes = [
        {
            'name': 'Classe des Petits Explorateurs',
            'description': 'Cette classe stimule la curiosité naturelle des enfants à travers des activités d\'exploration et de découverte.',
            'age_group': '3-4 ans',
            'capacity': 15,
            'time_start': '09:00',
            'time_end': '11:30',
            'days': 'Lundi, Mercredi, Vendredi',
            'price': 150.00,
            'image': 'class-1.jpg',
            'teacher_id': 1
        },
        {
            'name': 'Atelier d\'Art Créatif',
            'description': 'Un atelier où les enfants peuvent exprimer leur créativité par la peinture, le dessin et d\'autres formes d\'art.',
            'age_group': '4-5 ans',
            'capacity': 12,
            'time_start': '14:00',
            'time_end': '16:00',
            'days': 'Mardi, Jeudi',
            'price': 120.00,
            'image': 'class-2.jpg',
            'teacher_id': 2
        },
        {
            'name': 'Éveil Musical',
            'description': 'Les enfants découvrent le monde de la musique à travers le chant, le rythme et l\'exploration d\'instruments simples.',
            'age_group': '3-5 ans',
            'capacity': 10,
            'time_start': '10:00',
            'time_end': '11:30',
            'days': 'Mercredi, Samedi',
            'price': 130.00,
            'image': 'class-3.jpg',
            'teacher_id': 3
        },
        {
            'name': 'Jeux et Mouvement',
            'description': 'Une classe active où les enfants développent leurs capacités motrices par des jeux, des sports et des activités physiques adaptées.',
            'age_group': '4-6 ans',
            'capacity': 15,
            'time_start': '15:00',
            'time_end': '16:30',
            'days': 'Lundi, Vendredi',
            'price': 140.00,
            'image': 'class-1.jpg',
            'teacher_id': 4
        }
    ]
    
    for class_data in classes:
        class_obj = Class(**class_data)
        db.session.add(class_obj)
    
    # Créer des articles de blog
    blog_posts = [
        {
            'title': 'L\'importance du jeu dans le développement de l\'enfant',
            'content': 'Le jeu est essentiel au développement sain des enfants. Il permet non seulement de s\'amuser, mais aussi d\'acquérir des compétences fondamentales...',
            'image': 'blog-1.jpg',
            'author_id': 1,
            'category': 'Développement'
        },
        {
            'title': 'Activités artistiques pour stimuler la créativité',
            'content': 'L\'art joue un rôle crucial dans le développement de l\'enfant. Voici quelques activités artistiques simples que vous pouvez faire à la maison...',
            'image': 'blog-2.jpg',
            'author_id': 2,
            'category': 'Créativité'
        },
        {
            'title': 'Les bienfaits de la musique pour les jeunes enfants',
            'content': 'La musique a des effets remarquables sur le développement cognitif des enfants. Des études montrent que l\'exposition précoce à la musique...',
            'image': 'blog-3.jpg',
            'author_id': 3,
            'category': 'Musique'
        }
    ]
    
    for post_data in blog_posts:
        post = BlogPost(**post_data)
        db.session.add(post)
    
    # Valider les changements
    db.session.commit()
    print("Base de données initialisée avec succès!")

if __name__ == '__main__':
    with app.app_context():
        # Créer les tables
        db.create_all()
        # Remplir avec des données de démo
        seed_database()