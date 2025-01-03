from django.shortcuts import render, redirect
import ssl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Create your views here.
def sendEmail(data):
    # Replace with your email details
    sender_email = "neldsonportfolio@gmail.com"
    receiver_email = "neldson1406122@gmail.com"
    password = "fgrn ckun gjym lcad"  # It's better to use app password for security

    # Set up the MIME
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "New Email From Django App (your portfolio website)"

    context = ssl.create_default_context()

    # Add email body
    body = data
    message.attach(MIMEText(body, "plain"))

    # Set up the SMTP server and send email
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465 ,context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
    except Exception as e:
        print(f"Error sending email: {e}")

def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mesaaage = request.POST['Message']
        data = "Here is an update from your Portfolio Website\n\nName: {}\nEmail: {}\nMessage: {}".format(name, email, mesaaage)
        sendEmail(data)
        return redirect('polls:home')
    return render(request, 'home.html')