from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from db import get_user

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Logowanie")
        self.setGeometry(0, 0, 1920, 1080)  # Ustawiamy okno na pełny ekran
        self.show()  # Okno jest teraz wyświetlane w pełnym rozmiarze

        # Ustawiamy wygląd okna logowania
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Nazwa użytkownika")

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Hasło")

        self.login_button = QPushButton("Zaloguj")
        self.login_button.clicked.connect(self.handle_login)

        # Layout dla elementów
        form_layout = QVBoxLayout()
        form_layout.addWidget(QLabel("Użytkownik:"))
        form_layout.addWidget(self.username_input)
        form_layout.addWidget(QLabel("Hasło:"))
        form_layout.addWidget(self.password_input)
        form_layout.addWidget(self.login_button)

        # Główne ustawienie layoutu
        main_layout = QVBoxLayout()
        main_layout.addStretch(1)  # Dodaje przestrzeń do góry
        main_layout.addLayout(form_layout)  # Dodajemy formularz
        main_layout.addStretch(1)  # Dodaje przestrzeń do dołu

        self.setLayout(main_layout)

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        user = get_user(username, password)
        if user:
            QMessageBox.information(self, "Sukces", f"Witaj, {username}!")
            self.accept()  # zamyka okno logowania
        else:
            QMessageBox.warning(self, "Błąd", "Nieprawidłowy login lub hasło.")
