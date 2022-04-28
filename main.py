from flask import Flask, redirect, render_template, url_for, request, flash
from flask_bootstrap import Bootstrap
from projects import all_projects
from forms import ContactForm
import dotenv
import os
import datetime
import smtplib

dotenv.load_dotenv()
MY_WEBSITE_EMAIL = os.environ.get("MY_WEBSITE_EMAIL")
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
Bootstrap(app)


@app.route('/')
def home():
    return render_template("index.html", projects=all_projects, year=datetime.date.today().year)


@app.route('/contact-me', methods=["POST", "GET"])
def contact_me():
    form = ContactForm()
    if form.validate_on_submit():
        print("Form validated")
        print(form.name.data)
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(MY_WEBSITE_EMAIL, MY_PASSWORD)
            print("email logged in")
            connection.sendmail(
                from_addr=MY_WEBSITE_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject: Contact from Website\n\n"
                    f"Someone wants to contact you!\n"
                    f"Name: {form.name.data}\n"
                    f"Company: {form.company.data}\n"
                    f"Email Address: {form.email.data}\n"
                    f"Phone Number: {form.phone_number.data}\n"
                    f"Message: {form.message.data}")
        flash("Message has been sent, I'll get back to you asap.")
        return redirect(url_for('contact_me'))
    return render_template("contact_me.html", year=datetime.date.today().year, form=form)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
