from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

from src.config import settings
from src.notification.forms import base_form
from src.api.responses import status_error_400


class Mail:
    link_confirmation: str = f"{settings.server.SERVER_URL}/api/v{settings.server.version}/confirmation"
    
    @staticmethod
    def __send_mail(subject: str, content: str, recipient: str) -> None:
        with smtplib.SMTP_SSL("smtp.mail.ru", 465) as session:
            session.login(settings.mail.mail, settings.mail.password)
    
            msg = MIMEMultipart()
            msg["From"] = settings.mail.mail
            msg["To"] = recipient
            msg["Subject"] = subject
            msg.attach(MIMEText(content, "html"))

            try:
                session.send_message(msg)

            except smtplib.SMTPRecipientsRefused:
                return status_error_400("invalid mail")

            finally:
                session.quit()
    
    def send_register_mail(self, recipient: str, name: str, id: str, special: bool) -> None:
        if not special:
            content_text = f"""
            <p>Для подтверждения перейдите по <a href={self.link_confirmation+f'/access?id={id}'}>этой ссылке</a>.</p>
            <p>Если это были не вы, проигнорируйте это письмо</p>
            """
        else:
            content_text = f"""
            <p>Роль котороую вы выбрали при регистрации необходимо дополнительно подтвердить.</p>
            <p>С вами скоро свяжутся наши администраторы.</p>
            <p>Если это были не вы, для отмены перейдите по <a href="{self.link_confirmation+f'/delete?id={id}'}">этой ссылке</a>.</p>
            """
        content = base_form.format(name=name, text=content_text)
        self.__send_mail("Подтверждение регистрации", content, recipient)
        
        
    def send_switch_password_mail(self, recipient: str, code: str, name: str) -> None:
        content_text = f"""
        <p>С вашего аккаунта поступил запрос на смену пароля, если вы не отправляли его, игнорируйте это письмо.</p>
        <p>Ваш код для смены пароля: <span style="font-weight: 800;font-size: 24px;">{code}</span></p>
        """
        content = base_form.format(name=name, text=content_text)
        self.__send_mail("Смена пароля", content, recipient)
        

mail = Mail()