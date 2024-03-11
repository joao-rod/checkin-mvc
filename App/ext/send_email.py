"""Imports"""
import smtplib
import email.message
from flask import render_template


def send_email(user, markings):
    """Disparo de emails sobre carga horária completa"""
    body = render_template('template_email.html', user=user, markings=markings)

    msg = email.message.Message()
    msg['Subject'] = "Carga horária cumprida"
    msg['From'] = 'noreply.app.checkin@gmail.com'
    msg['To'] = user.username
    password = 'bczvkwyqpfnyjzxe'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
