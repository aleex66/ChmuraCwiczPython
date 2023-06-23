from flask import Flask
from jinja2 import Template
from flask_mail import Mail, Message
from flask import request
from flask import render_template
from flask import abort, url_for, make_response

app = Flask(__name__)
'''
mail = Mail(app)
template = Template('Hello {{ name }}!')
template.render(name='Aleex S')
app.config['MAIL_SERVER'] = 'sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'da3bed477b6fa7'
app.config['MAIL_PASSWORD'] = 'cc0f75eed05411'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route("/")
def index():
    msg = Message('Hello', sender='da3bed477b6fa7', recipients=['olisia.olcia@gmail.com'])
    msg.body = "Hello Flask message sent from Flask-Mail. Odbiór żołnierzu."
    msg.html = "<b>Hey </b>sending <a href='https://google.com'>Flask app</a>, ldk if it works"
    mail.send(msg)
    return "Sent!"
'''

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/gallery')
def gallery():
    return render_template("gallery.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/aboutme')
def aboutme():
    return render_template("aboutme.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8169)
