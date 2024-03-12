import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Finance Tracker")

        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, e):
        self.label.setText("Mouse moved")

    def mousePressEvent(self, e):
        self.label.setText("Mouse Pressed")

    def mouseReleaseEvent(self, e):
        self.label.setText("Mouse Released")

    def mouseDoubleClickEvent(self, e):
        self.label.setText("Mouse double clicked")





# Establish QApplication instance for app, with ability to pass command line arguments.
app = QApplication(sys.argv)

# Create QtWidget main window
window = MainWindow()
window.show()

# Start event loop
app.exec()
