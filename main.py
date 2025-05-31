import sys
from PyQt5.QtWidgets import QApplication
from login_window import LoginWindow
from register_window import RegisterWindow
from main_window import MainWindow
from db import create_tables

def main():
    app = QApplication(sys.argv)
    create_tables()

    while True:
        login_window = LoginWindow()

        def handle_register():
            register_window = RegisterWindow()
            if register_window.exec_() == RegisterWindow.Accepted:
                login_window.username_input.clear()
                login_window.password_input.clear()
                login_window.show()

        if hasattr(login_window, 'register_button'):
            login_window.register_button.clicked.connect(handle_register)

        if login_window.exec_() == LoginWindow.Accepted:
            user = login_window.logged_user  # Pobranie zalogowanego użytkownika
            main_window = MainWindow(current_user=user)
            main_window.show()
            sys.exit(app.exec_())
        else:
            break

if __name__ == '__main__':
    main()
