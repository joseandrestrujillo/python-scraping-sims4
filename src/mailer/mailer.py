from decouple import config
import json
from email.message import EmailMessage
import ssl
import smtplib

class mailer:
    def __init__(self) -> None:
        self.mailer = config('MAILER_EMAIL')
        self.password = config('MAILER_PASSWORD')
        self.receptors = config('RECEPTOR_EMAILS').strip('][').split(', ')

    def sendMail(self, subject, content):
        for receptor in self.receptors:
            em = EmailMessage()
            em['From'] = self.mailer
            em['To'] = receptor
            em['Subject'] = subject
            em.set_content(content, subtype="html")
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smpt:
                smpt.login(self.mailer, self.password)
                smpt.sendmail(self.mailer, receptor, em.as_string())
            print(f"mail enviado a {receptor}")

