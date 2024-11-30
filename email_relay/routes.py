import os
from flask import  request
from email_relay import app, mail
from flask_mail import Message


@app.route('/send_mail', methods=['POST'])
def send_mail():
    data = request.form
    secret = os.environ.get("SECRET")
    sender = os.environ.get("MAIL_USERNAME")
    if 'subject' in data \
    and 'body' in data \
    and 'sender' in data \
    and 'recipient' in data \
    and secret == data['secret'] \
    and sender == data['sender']:
        msg = Message(
            subject = data['subject'],
            recipients = [data['recipient']],
            body = data['body'],
            sender = sender,
        )
        mail.send(msg)
        return {'email': 'sent'}
    return {'email': 'not sent'}