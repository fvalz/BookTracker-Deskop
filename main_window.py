from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QListView, QVBoxLayout, QLabel
from PyQt5.QtCore import QStringListModel
from add_book_dialog import AddBookDialog
from db import get_books

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Biblioteka - Panel główny")
        self.setGeometry(0, 0, 1920, 1080)  # Ustawiamy okno na pełny ekran (możesz dostosować rozdzielczość)
        self.show()  # Okno jest teraz wyświetlane w pełnym rozmiarze

        # Tworzymy przycisk do dodawania książek
        self.add_book_button = QPushButton("Dodaj książkę", self)
        self.add_book_button.move(350, 50)  # Umieszczamy przycisk na górze

        # Tworzymy przycisk do przełączenia w tryb pełnoekranowy
        self.fullscreen_button = QPushButton("Pełny ekran", self)
        self.fullscreen_button.move(350, 100)  # Umieszczamy przycisk obok

        # Przyciski do obsługi pełnoekranowego trybu
        self.add_book_button.clicked.connect(self.open_add_book)
        self.fullscreen_button.clicked.connect(self.toggle_fullscreen)

        # Dodanie listy książek
        self.books_list = QListView(self)
        self.books_list.setGeometry(50, 150, 700, 350)  # Lista książek
        self.update_books_list()  # Uaktualniamy listę książek

        # Ustawienie głównego layoutu
        layout = QVBoxLayout()
        layout.addWidget(self.add_book_button)
        layout.addWidget(self.fullscreen_button)
        layout.addWidget(self.books_list)

        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_add_book(self):
        dialog = AddBookDialog()
        dialog.exec_()

    def toggle_fullscreen(self):
        # Przełączanie trybu pełnoekranowego
        if self.isFullScreen():
            self.showNormal()  # Przywrócenie normalnego trybu
        else:
            self.showMaximized()  # Pełny ekran

    def update_books_list(self):
        # Pobieranie książek z bazy danych
        books = get_books()
        book_titles = [book[1] for book in books]  # Zakładam, że book[1] to tytuł książki

        # Tworzenie modelu dla QListView
        model = QStringListModel()
        model.setStringList(book_titles)

        # Ustawienie modelu na QListView
        self.books_list.setModel(model)
