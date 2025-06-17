
import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

def send_email_alert(message):
    try:
        msg = MIMEText(message)
        msg['Subject'] = "Trading Alert"
        msg['From'] = os.getenv("EMAIL_ADDRESS")
        msg['To'] = os.getenv("EMAIL_ADDRESS")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(os.getenv("EMAIL_ADDRESS"), os.getenv("EMAIL_PASSWORD"))
            server.send_message(msg)
    except Exception as e:
        print(f"Email failed: {e}")
