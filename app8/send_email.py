from email.mime.text import MIMEText
import smtplib


def send_email(email, height, average, count):
    from_email = "iztekermiek@gmail.com"
    from_password = "Thefor132"
    to_email = email

    subject = "Height data"
    message = "Hello! Your registered height is <strong>%s</strong>. :) \nAverage height is <strong>%s</strong> out of <strong>%s</strong>  people. " % (height, average, count)

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)