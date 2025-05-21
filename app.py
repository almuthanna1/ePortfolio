from flask import Flask, render_template, send_from_directory, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')

# Routes for your HTML pages
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index')
def home1():
    return render_template('index.html')

@app.route('/about-me')
def about():
    return render_template('about-me.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/filesmagic')
def filesmagic():
    return render_template('filesmagic.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/contactme', methods=['POST'])
def contactme():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    sender_email = "amshihab99@gmail.com"
    receiver_email = "amshihab99@gmail.com"
    app_password = "lmswtnxoacpvedow"

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = receiver_email
    msg['Subject'] = f"New message from {name}"

    body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(email, receiver_email, msg.as_string())
        server.quit()
        return "✅ Message sent successfully!", 200
    except Exception as e:
        print("Email failed:", e)
        return "❌ Failed to send message. Please try again later.", 500

# Serve the resume file (from /static/files/)
@app.route('/files/<filename>')
def download_file(filename):
    return send_from_directory('static/files', filename)

if __name__ == '__main__':
    app.run(debug=True)
