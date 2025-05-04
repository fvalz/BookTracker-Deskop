from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from db import add_user, get_user_by_email, get_user_by_username

class RegisterWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rejestracja")
        self.setFixedSize(300, 250)

        layout = QVBoxLayout()

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Nazwa użytkownika")
        layout.addWidget(QLabel("Nazwa użytkownika:"))
        layout.addWidget(self.username_input)

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        layout.addWidget(QLabel("Email:"))
        layout.addWidget(self.email_input)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Hasło")
        layout.addWidget(QLabel("Hasło:"))
        layout.addWidget(self.password_input)

        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setEchoMode(QLineEdit.Password)
        self.confirm_password_input.setPlaceholderText("Potwierdź hasło")
        layout.addWidget(QLabel("Potwierdź hasło:"))
        layout.addWidget(self.confirm_password_input)

        self.register_button = QPushButton("Zarejestruj")
        self.register_button.clicked.connect(self.handle_register)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

    def handle_register(self):
        username = self.username_input.text().strip()
        email = self.email_input.text().strip()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()

        if not username or not email or not password or not confirm_password:
            QMessageBox.warning(self, "Błąd", "Wszystkie pola są wymagane.")
            return

        if password != confirm_password:
            QMessageBox.warning(self, "Błąd", "Hasła nie są takie same.")
            return

        if get_user_by_username(username):
            QMessageBox.warning(self, "Błąd", "Użytkownik o tej nazwie już istnieje.")
            return

        if get_user_by_email(email):
            QMessageBox.warning(self, "Błąd", "Użytkownik z tym adresem e-mail już istnieje.")
            return

        add_user(username, password, email)
        QMessageBox.information(self, "Sukces", "Rejestracja zakończona sukcesem!")
        self.accept()  # <-- Zamyka okno rejestracji
