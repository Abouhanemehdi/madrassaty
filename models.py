from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Teacher(db.Model):
    """Modèle pour les enseignants"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    image = db.Column(db.String(100), default='default.jpg')
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    facebook = db.Column(db.String(100))
    twitter = db.Column(db.String(100))
    instagram = db.Column(db.String(100))
    classes = db.relationship('Class', backref='teacher', lazy=True)
    
    def __repr__(self):
        return f"Teacher('{self.name}', '{self.position}')"

class Class(db.Model):
    """Modèle pour les cours/classes"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    age_group = db.Column(db.String(50), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    time_start = db.Column(db.String(10), nullable=False)
    time_end = db.Column(db.String(10), nullable=False)
    days = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(100), default='default.jpg')
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False)
    enrollments = db.relationship('Enrollment', backref='class', lazy=True)
    
    def __repr__(self):
        return f"Class('{self.name}', '{self.age_group}')"

class Parent(db.Model):
    """Modèle pour les parents"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    children = db.relationship('Child', backref='parent', lazy=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f"Parent('{self.name}', '{self.email}')"

class Child(db.Model):
    """Modèle pour les enfants"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    allergies = db.Column(db.Text)
    special_needs = db.Column(db.Text)
    parent_id = db.Column(db.Integer, db.ForeignKey('parent.id'), nullable=False)
    enrollments = db.relationship('Enrollment', backref='child', lazy=True)
    
    def __repr__(self):
        return f"Child('{self.name}', '{self.dob}')"

class Enrollment(db.Model):
    """Modèle pour les inscriptions"""
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'), nullable=False)
    child_id = db.Column(db.Integer, db.ForeignKey('child.id'), nullable=False)
    enrollment_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='pending')  # pending, confirmed, cancelled
    
    def __repr__(self):
        return f"Enrollment(Class: '{self.class_id}', Child: '{self.child_id}')"

class BlogPost(db.Model):
    """Modèle pour les articles de blog"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    image = db.Column(db.String(100), default='default.jpg')
    author_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False)
    author = db.relationship('Teacher', backref='posts')
    category = db.Column(db.String(50), nullable=False)
    
    def __repr__(self):
        return f"BlogPost('{self.title}', '{self.date_posted}')"

class Contact(db.Model):
    """Modèle pour les messages de contact"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    date_sent = db.Column(db.DateTime, default=datetime.utcnow)
    is_read = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f"Contact('{self.name}', '{self.subject}', '{self.date_sent}')"