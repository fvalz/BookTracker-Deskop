import sys
from PyQt5.QtWidgets import QApplication
from login_window import LoginWindow
from main_window import MainWindow
from db import create_users_table, create_books_table, add_user

if __name__ == '__main__':
    create_users_table()
    create_books_table()

    try:
        add_user("admin", "admin123", role="admin")
    except:
        pass

    app = QApplication(sys.argv)
    login = LoginWindow()

    if login.exec_():  # Po udanym logowaniu
        window = MainWindow()
        window.show()  # Główne okno wyświetlane na pełnym ekranie
        sys.exit(app.exec_())
