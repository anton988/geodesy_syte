from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class CallbackForm(FlaskForm):
    name = StringField('Имя', [
        validators.InputRequired(message="Поле обязательно для заполнения"),
        validators.Length(min=2, max=50)
    ])
    phone = StringField('Телефон', [
        validators.InputRequired(),
        validators.Regexp(r'^\+?[1-9]\d{1,14}$', message="Некорректный номер телефона")
    ])
    message = TextAreaField('Сообщение', [
        validators.InputRequired(),
        validators.Length(max=500)
    ])