import os
import smtplib
from email.message import EmailMessage


SMTP_HOST = os.environ["SMTP_HOST"]
SMTP_PORT = int(os.environ.get("SMTP_PORT", "587"))
SMTP_USERNAME = os.environ["SMTP_USERNAME"]
SMTP_PASSWORD = os.environ["SMTP_PASSWORD"]
FROM_EMAIL = os.environ["FROM_EMAIL"]


def send_otc_email(to_email: str, otc: str):
    """Send the one-time login code by email."""

    message = EmailMessage()

    message["Subject"] = "Your login code"
    message["From"] = FROM_EMAIL
    message["To"] = to_email

    message.set_content(
        f"""Your login code is:

{otc}

This code expires in 10 minutes.

If you did not request this code, you can ignore this email.
"""
    )

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(SMTP_USERNAME, SMTP_PASSWORD)
        smtp.send_message(message)
