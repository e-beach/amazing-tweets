from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    topic = StringField('topic', [validators.Length(min=2, max=25)])
    