from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QPushButton, QListWidget, QMessageBox
)
from db import get_all_users, ban_user  # zamienione z delete_user_by_id na ban_user

class AdminPanel(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Panel administratora")
        self.setMinimumSize(400, 400)

        self.user_list = QListWidget()
        self.load_users()

        self.delete_button = QPushButton("Zbanuj zaznaczonego użytkownika")
        self.delete_button.clicked.connect(self.ban_user)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Lista użytkowników:"))
        layout.addWidget(self.user_list)
        layout.addWidget(self.delete_button)

        self.setLayout(layout)

    def load_users(self):
        self.user_list.clear()
        users = get_all_users()
        for user in users:
            self.user_list.addItem(f"{user[0]} | {user[1]} | {user[2]} | {user[3]}")  # id | username | email | role

    def ban_user(self):
        selected = self.user_list.currentItem()
        if not selected:
            QMessageBox.warning(self, "Błąd", "Wybierz użytkownika.")
            return

        user_info = selected.text()
        user_id = int(user_info.split(" | ")[0])

        confirm = QMessageBox.question(self, "Potwierdzenie", f"Czy na pewno chcesz usunąć użytkownika ID {user_id}?",
                                       QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            ban_user(user_id)
            QMessageBox.information(self, "Sukces", "Użytkownik został zbanowany.")
            self.load_users()
