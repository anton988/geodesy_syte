import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
from flask_mail import Mail, Message

from forms import CallbackForm

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

app.config.update(
    MAIL_SERVER=os.getenv('MAIL_SERVER'),
    MAIL_PORT=os.getenv('MAIL_PORT'),
    MAIL_USE_SSL=os.getenv('MAIL_USE_SSL'),
    MAIL_USERNAME=os.getenv('MAIL_USERNAME'),
    MAIL_PASSWORD=os.getenv('MAIL_PASSWORD')
)

mail = Mail(app)

# Контактные данные (можно менять)
CONTACT_INFO = {
    "phone": "+7 (916) 098-55-20",
    "email": "titkovantonandreevich@yandex.ru",
    "work_hours": "Пн-Пт: 9:00-21:00"
}

@app.route('/')
def home():
    return render_template('index.html', contact=CONTACT_INFO)


@app.route('/about')
def about():
    return render_template('about.html', contact=CONTACT_INFO)


@app.route('/price')
def price():
    return render_template('price.html', contact=CONTACT_INFO)


@app.route('/faq')
def faq():
    return render_template('faq.html', contact=CONTACT_INFO)


@app.route('/callback', methods=['POST'])
def callback():
    form = CallbackForm(request.form)
    if form.validate():
        try:
            msg = Message(
                subject="Новая заявка",
                sender=app.config['MAIL_USERNAME'],
                recipients=["your-business-email@example.com"]
            )
            msg.body = f"""
            Имя: {form.name.data}
            Телефон: {form.phone.data}
            Сообщение: {form.message.data}
            """
            mail.send(msg)
            return render_template('success.html')
        except Exception as e:
            app.logger.error(f"Ошибка отправки: {str(e)}")
            return render_template('error.html'), 500
    else:
        return render_template('error.html', errors=form.errors), 400

if __name__ == '__main__':
    app.run(debug=False)
