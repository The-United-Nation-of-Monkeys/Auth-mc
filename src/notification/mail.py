from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

from src.config import settings
from src.notification.forms import register_form
from src.api.responses import status_error_400

def send_register_mail(recipient: str, name: str, link: str) -> None:
    with smtplib.SMTP_SSL("smtp.mail.ru", 465) as session:
        session.login(settings.mail.mail, settings.mail.password)
        content = register_form.format(name=name, link=link)

        msg = MIMEMultipart()
        msg["From"] = settings.mail.mail
        msg["To"] = recipient
        msg["Subject"] = "Подтверждение регистрации"
        msg.attach(MIMEText(content, "html"))

        try:
            session.send_message(msg)

        except smtplib.SMTPRecipientsRefused:
            return status_error_400("invalid mail")

        finally:
            session.quit()