import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

""" 
Local Test Only
from dotenv import load_dotenv
load_dotenv()
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD') 
"""

email = os.environ['EMAIL']
password = os.environ['PASSWORD']

def mail(idVacancie, title, positionDescription, location, workplacePolicy, tags, url):
  mail_body = f'ID: {idVacancie}\nTítulo: {title}\n\nDescrição: {positionDescription}\n\nLocalização: {location}\nPolítica: {workplacePolicy}\nTags: {tags}\n\nUrl: {url}'
  message = MIMEMultipart()
  message['From'] = email
  message['To'] = email
  message['Subject'] = f'Nova vaga YellowIpe: {title}'
  message.attach(MIMEText(mail_body,'plain'))
  session = smtplib.SMTP('smtp.gmail.com', 587)
  session.starttls()
  session.login(email, password)
  text = message.as_string()
  session.sendmail(email, email, text)
  session.quit()