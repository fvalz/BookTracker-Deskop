import smtplib
import ssl
from email.message import EmailMessage

# Dane nadawcy (zmień na swoje!)
SENDER_EMAIL = "BookTrackerDESKOP@gmail.com"
SENDER_PASSWORD = "wbad dpfv eqlx iqwf"

def send_verification_code(to_email, code):
    try:
        message = EmailMessage()
        message.set_content(f"Twój kod weryfikacyjny to: {code}")
        message["Subject"] = "Kod weryfikacyjny - Twoja aplikacja"
        message["From"] = SENDER_EMAIL
        message["To"] = to_email

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(message)

        return True, None  # Sukces
    except Exception as e:
        return False, str(e)  # Błąd z komunikatem
