from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QInputDialog, QHBoxLayout
)
from db import get_user
from email_utils import send_verification_code
import random

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Logowanie")
        self.setFixedSize(300, 240)

        layout = QVBoxLayout()

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Nazwa użytkownika lub email")
        layout.addWidget(QLabel("Nazwa użytkownika lub email:"))
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Hasło")
        layout.addWidget(QLabel("Hasło:"))
        layout.addWidget(self.password_input)

        self.login_button = QPushButton("Zaloguj")
        self.login_button.clicked.connect(self.handle_login)
        layout.addWidget(self.login_button)

        # Przycisk do rejestracji
        register_layout = QHBoxLayout()
        register_label = QLabel("Nie masz konta?")
        register_button = QPushButton("Zarejestruj się")
        register_button.setFlat(True)
        register_button.clicked.connect(self.open_register)
        register_layout.addWidget(register_label)
        register_layout.addWidget(register_button)
        layout.addLayout(register_layout)

        self.setLayout(layout)
        self.logged_user = None

    def handle_login(self):
        username_or_email = self.username_input.text().strip()
        password = self.password_input.text()

        user = get_user(username_or_email, password)
        if not user:
            QMessageBox.warning(self, "Błąd", "Niepoprawna nazwa użytkownika/email lub hasło.")
            return

        print("debug - user tuple:", user)

        email = user[3]  # Upewniamy się, że to jest adres e-mail, a nie hash hasła
        print("debug - email used for verification:", email)

        # Generowanie 6-cyfrowego kodu
        code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        print("debug - generated code:", code)

        # Wysyłka kodu
        success, error_msg = send_verification_code(email, code)
        if not success:
            QMessageBox.warning(self, "Błąd", f"Nie udało się wysłać kodu weryfikacyjnego:\n{error_msg}")
            return

        # Wprowadzanie kodu
        code_input, ok = QInputDialog.getText(
            self,
            "Weryfikacja dwuetapowa",
            f"Wysłano kod na {email}. Podaj kod:"
        )

        if not ok:
            QMessageBox.information(self, "Anulowano", "Logowanie anulowane.")
            return

        if code_input != code:
            QMessageBox.warning(self, "Błąd", "Niepoprawny kod weryfikacyjny.")
            return

        # Sukces
        self.logged_user = user
        QMessageBox.information(self, "Sukces", "Zalogowano pomyślnie!")
        self.accept()

    def open_register(self):
        from register_window import RegisterWindow
        register_dialog = RegisterWindow()
        if register_dialog.exec_():
            QMessageBox.information(self, "Rejestracja", "Rejestracja zakończona sukcesem! Możesz się teraz zalogować.")
