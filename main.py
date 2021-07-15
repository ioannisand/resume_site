from flask import Flask, render_template, redirect, url_for, request, send_from_directory
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_ckeditor import CKEditor, CKEditorField
from smtplib import SMTP
import os
from dotenv import load_dotenv
import gunicorn

# to use .env file for environment variables
load_dotenv()

#Initializing app and connecting to bootstrap and ckeditop
app = Flask(__name__)

app.secret_key = os.getenv("secretkey")
app.config['UPLOAD_FOLDER'] = 'static'
ckeditor = CKEditor(app)
Bootstrap(app)

#dummy email creds
korompos = os.getenv("korobos")
password = os.getenv("password")





class ContactForm(FlaskForm):
    name = StringField("Name:", validators=[DataRequired()])
    email = StringField("Email:", validators=[DataRequired(), Email()])
    message = CKEditorField("Message:", validators=[DataRequired()])
    submit = SubmitField("Send", validators=[DataRequired()])


@app.route('/')
def homepage():
    return render_template("index.html")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    # forma = ContactForm()
    #
    # if forma.validate_on_submit():
    #     client_name = forma.name.data
    #     client_email = forma.email.data
    #     message = forma.message.data
    #     connection = SMTP("smtp.mailgun.org")
    #     connection.starttls()
    #     print(korompos, password)
    #     connection.login(korompos, password)
    #     connection.sendmail(from_addr=korompos,
    #         to_addrs="andreadakis.ioa@gmail.com",
    #         msg=f"Subject:{client_email}\n\nYou have a message from your website, {client_name} sent you the following message {message}")
    #     return redirect(url_for("homepage"))
    return render_template("contact.html")

@app.route('/view_cv')
def view_cv():
    return send_from_directory('static', path='files/ioannis-andreadakis-cv.pdf')


if __name__ == '__main__':
    app.run()