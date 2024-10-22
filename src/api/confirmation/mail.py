
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import smtplib

class Mail:
    def sendConfirmationMessage():
        with smtplib.SMTP_PORT("smtp.mail.ru", 465) as session:    
            
            session.login("vbiusaubwq@mail.ru", "BEC5icSYQMArJmrmdjbE")
            
            msg = MIMEMultipart()
            msg["From"] = "vbiusaubwq@mail.ru"
            msg["To"] = "skliar-il@mail.ru"
            msg["Subject"] = "win"
            msg.attach(MIMEText("asdasdasd", "plain"))
            
            session.send_message()
            
            session.send_message(msg)
            session.quit()
        
        
