import os
import sys
import subprocess
import random
import string
import shutil
from pathlib import Path

def print_color(text, color_code):
    """Imprime du texte en couleur dans le terminal"""
    print(f"\033[{color_code}m{text}\033[0m")

def print_success(text):
    """Imprime un message de succès en vert"""
    print_color(text, 92)

def print_info(text):
    """Imprime un message d'info en bleu"""
    print_color(text, 94)

def print_warning(text):
    """Imprime un avertissement en jaune"""
    print_color(text, 93)

def print_error(text):
    """Imprime une erreur en rouge"""
    print_color(text, 91)

def generate_secret_key(length=24):
    """Génère une clé secrète aléatoire"""
    chars = string.ascii_letters + string.digits + '!@#$%^&*()_-+=<>?'
    return ''.join(random.choice(chars) for _ in range(length))

def create_env_file():
    """Crée un fichier .env avec les variables d'environn