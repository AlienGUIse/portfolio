import smtplib
from email.message import EmailMessage
import cgi, cgitb


# Get data from form
form = cgi.FieldStorage()

# assign data
name = form.getvalue('name')
email = form.getvalue('email')
content = form.getvalue('subject')
SENDER = 'awsallen.wang@gmail.com'
MYEMAIL = 'pcboy0715@gmail.com'

msg = EmailMessage()
msg['Subject'] = 'Email from My Portfolio'
msg['From'] = 'awsallen.wang@gmail.com'
msg['To'] = 'pcboy0715@gmail.com'
msg.set_content('This is a test email')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    smtp.login('awsallen.wang@gmail.com', 'password')

    smtp.send_message(msg)
