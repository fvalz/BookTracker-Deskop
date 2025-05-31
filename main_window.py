from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QListView
import os

class MainWindow(QMainWindow):
    def __init__(self, current_user):
        super().__init__()
        self.setWindowTitle("Biblioteka - Panel główny")
        self.setGeometry(0, 0, 1920, 1080)
        self.show()

        self.current_user = current_user

        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QPushButton {
                background-color: #007BFF;
                color: white;
                border-radius: 10px;
                font-size: 14px;
                padding: 10px;
                margin-bottom: 10px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QPushButton:pressed {
                background-color: #004085;
            }
            QListView {
                border: 1px solid #ddd;
                border-radius: 10px;
                padding: 10px;
                background-color: white;
            }
        """)

        # Lista książek (pusta, bez funkcjonalności)
        self.books_list = QListView()

        # Przyciski (bez funkcjonalności)
        self.add_book_button = QPushButton("Dodaj książkę")
        self.edit_book_button = QPushButton("Edytuj książkę")
        self.delete_book_button = QPushButton("Usuń książkę")

        self.logout_button = QPushButton("Wyloguj")
        self.logout_button.clicked.connect(self.logout_user)

        layout = QVBoxLayout()
        layout.addWidget(self.add_book_button)
        layout.addWidget(self.edit_book_button)
        layout.addWidget(self.delete_book_button)
        layout.addWidget(self.logout_button)
        layout.addWidget(self.books_list)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def logout_user(self):
        try:
            os.remove("remember_me.txt")
        except FileNotFoundError:
            pass

        self.close()

        from login_window import LoginWindow
        login = LoginWindow()
        if login.exec_():
            self.__init__(login.logged_user)
            self.show()
