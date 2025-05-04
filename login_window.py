from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from register_window import RegisterWindow  # Dodajemy import dla okna rejestracji
from db import get_user

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Logowanie")
        self.setFixedSize(300, 150)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Nazwa użytkownika / Email")

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Hasło")

        self.login_button = QPushButton("Zaloguj")
        self.login_button.clicked.connect(self.handle_login)

        
        self.register_button = QPushButton("Zarejestruj się")
        self.register_button.clicked.connect(self.open_register_window)

        
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Użytkownik / Email:"))
        layout.addWidget(self.username_input)
        layout.addWidget(QLabel("Hasło:"))
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)  

        self.setLayout(layout)

    def handle_login(self):
        username_or_email = self.username_input.text()
        password = self.password_input.text()

        
        user = get_user(username_or_email, password)
        if user:
            QMessageBox.information(self, "Sukces", f"Witaj, {user[1]}!")
            self.accept()  
        else:
            QMessageBox.warning(self, "Błąd", "Nieprawidłowy login lub hasło.")
    
    def open_register_window(self):
        
        self.register_window = RegisterWindow()
        self.register_window.exec_()  
