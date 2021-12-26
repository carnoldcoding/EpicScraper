import email, smtplib, ssl
from providers import PROVIDERS
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import os
from os.path import basename


def message_config(number: str, message: str, file_path: str, mime_maintype: str, mime_subtype: str, provider: str, sender_credentials: tuple, subject: str = "sent using py",
                 smtp_server="smtp.gmail.com", smtp_port: int = 465):
    sender_email, email_password = sender_credentials
    receiver_email = f"{number}@{PROVIDERS.get(provider).get('mms')}"


    email_message = MIMEMultipart()
    email_message["Subject"] = subject
    email_message["To"] = receiver_email
    email_message["From"] = sender_email

    email_message.attach(MIMEText(message, "plain"))

    with open(file_path, "rb") as attachment:
        part = MIMEBase(mime_maintype, mime_subtype)
        part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition", f"attachment; filename={basename(file_path)}"
        )

        email_message.attach(part)

        text = email_message.as_string()

    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=ssl.create_default_context()) as email:
        email.login(sender_email, email_password)
        email.sendmail(sender_email, receiver_email, text)


def send_message(message):
    number = os.environ["CELL_NUMBER"]
    message = message
    provider = "Verizon"
    file_path = "output.csv"
    mime_maintype = "text"
    mime_subtype = "csv"
    sender_credentials = (os.environ["BOT_EMAIL"], os.environ["BOT_EMAIL_CODE"])
    message_config(number, message, file_path, mime_maintype, mime_subtype, provider, sender_credentials)
