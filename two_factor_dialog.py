from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class TwoFactorDialog(QDialog):
    def __init__(self, correct_code):
        super().__init__()
        self.setWindowTitle("Weryfikacja dwuetapowa")
        self.setFixedSize(300, 150)
        self.correct_code = correct_code

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Wpisz kod wysłany na e-mail:"))

        self.code_input = QLineEdit()
        layout.addWidget(self.code_input)

        self.verify_button = QPushButton("Zweryfikuj")
        self.verify_button.clicked.connect(self.verify_code)
        layout.addWidget(self.verify_button)

        self.setLayout(layout)

    def verify_code(self):
        if self.code_input.text() == self.correct_code:
            self.accept()
        else:
            QMessageBox.warning(self, "Błąd", "Niepoprawny kod weryfikacyjny.")
