from flask import Flask
from jinja2 import Template
from flask_mail import Mail, Message
from flask import request
from flask import render_template
from flask import abort, url_for, make_response

app = Flask(__name__)
'''ail = Mail(app)
template = Template('Hello {{ name }}!')
template.render(name='Aleex S')
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] ='bombelekhurrdurr@gmail.com'
app.config['MAIL_PASSWORD'] = 'zaq1@WSX'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
    msg = Message('Hello', sender = 'bombelekhurrdurr@gmail.com', recipients = ['olisia.olcia@gmail.com'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return "Sent"
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
