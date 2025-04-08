import os
from dotenv import load_dotenv

# Chargement des variables d'environnement depuis le fichier .env
load_dotenv()

class Config:
    """Configuration de base pour l'application Flask"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'une-cle-secrete-difficile-a-deviner'
    
    # Ajoutez d'autres configurations ici selon vos besoins
    # Par exemple, configuration d'une base de données:
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///kindergarten.db'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configuration d'email
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')

class DevelopmentConfig(Config):
    """Configuration pour l'environnement de développement"""
    DEBUG = True

class ProductionConfig(Config):
    """Configuration pour l'environnement de production"""
    DEBUG = False

# Configuration à utiliser selon l'environnement
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}