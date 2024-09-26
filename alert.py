from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import config 

SENDER_EMAIL = config.SENDER_EMAIL
SENDER_PASSWORD = config.SENDER_PASSWORD
RECEIVER_EMAIL = config.RECEIVER_EMAIL
SMTP_SERVER = config.SMTP_SERVER
SMTP_PORT = config.SMTP_PORT

def send_email_alert(product_name, quantity):
    # the email content
    subject = f"Low Stock Alert: {product_name}"
    body = f"Low Stock Alert: {product_name} has only {quantity} items left in stock!"

    # MIMEText object to represent the email
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Connecting to the SMTP server and sending the email
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
            print(f"Email alert sent for {product_name}.")
    except Exception as e:
        print(f"Failed to send email alert for {product_name}: {e}")


if __name__ == "__main__":
    send_email_alert("Sample Product", 5)
