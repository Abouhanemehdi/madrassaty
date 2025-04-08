from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    """Formulaire de contact"""
    name = StringField('Nom', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Sujet', validators=[DataRequired(), Length(min=2, max=100)])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=10, max=1000)])
    submit = SubmitField('Envoyer')

# Vous pouvez ajouter d'autres formulaires selon vos besoins
# Par exemple, un formulaire d'inscription, de demande d'information, etc.