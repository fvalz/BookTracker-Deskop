import sys
from PyQt5.QtWidgets import QApplication
from login_window import LoginWindow
from register_window import RegisterWindow
from main_window import MainWindow
from db import create_tables

if __name__ == '__main__':
    app = QApplication(sys.argv)
    create_tables()

    while True:
        login_window = LoginWindow()

        
        def handle_register():
            register_window = RegisterWindow()
            if register_window.exec_() == register_window.Accepted:
                pass  

        login_window.register_button.clicked.connect(handle_register)

        if login_window.exec_() == login_window.Accepted:
            main_window = MainWindow()
            main_window.show()
            sys.exit(app.exec_())  
        else:
            break  
