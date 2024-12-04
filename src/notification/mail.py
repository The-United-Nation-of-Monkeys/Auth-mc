from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

from src.config import settings
from src.notification.forms import register_form, special_register_form, switch_password_form
from src.api.responses import status_error_400

def send_register_mail(recipient: str, name: str, link: str, id: str) -> None:
    with smtplib.SMTP_SSL("smtp.mail.ru", 465) as session:
        session.login(settings.mail.mail, settings.mail.password)
        content = register_form.format(name=name, link=link+f"/access?id={id}", delete_link=link+f"/delete?id={id}")

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

def send_info_special_register_mail(recipient: str, name: str, link: str, id: str) -> None:
    with smtplib.SMTP_SSL("smtp.mail.ru", 465) as session:
        session.login(settings.mail.mail, settings.mail.password)
        content = special_register_form.format(name=name, delete_link=link+f"/delete?id={id}")

        msg = MIMEMultipart()
        msg["From"] = settings.mail.mail
        msg["To"] = recipient
        msg["Subject"] = "Подтверждение регистрации"
        msg.attach(MIMEText(content, "html"))

        try:
            session.send_message(msg)

        except smtplib.SMTPRecipientsRefused:
            return status_error_400("invalid mail")
        
        except smtplib.SMTPDataError:
            return status_error_400("invalid mail")

        finally:
            session.quit()
            
def send_switch_password_mail(recipient: str, code: str) -> None:
    with smtplib.SMTP_SSL("smtp.mail.ru", 465) as session:
        session.login(settings.mail.mail, settings.mail.password)
        content = switch_password_form.format(code=code)

        msg = MIMEMultipart()
        msg["From"] = settings.mail.mail
        msg["To"] = recipient
        msg["Subject"] = "Смена пароля"
        msg.attach(MIMEText(content, "html"))

        try:
            session.send_message(msg)

        except smtplib.SMTPRecipientsRefused:
            return status_error_400("invalid mail")

        finally:
            session.quit()