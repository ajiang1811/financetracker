from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QFormLayout,
    QGroupBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QMainWindow,
    QLabel,
    QLineEdit,
    QTextEdit
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createUI()

    def createUI(self):
        # Creating main window
        self.setWindowTitle("Finance Tracker")
        self.resize(800, 500)
        self.setMinimumSize(500, 450)

        # Create Central widget and layout
        self.centralWidget = QWidget()
        self.verticalLayout = QVBoxLayout()
        self.centralWidget.setLayout(self.verticalLayout)
        # setting central widget
        self.setCentralWidget(self.centralWidget)



if (__name__ == "__main__"):
    # Establish QApplication instance for app, with ability to pass command line arguments.
    app = QApplication([])

    # Create QtWidget main window
    window = MainWindow()
    window.show()

    # Start event loop
    app.exec()
