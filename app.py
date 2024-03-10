from PyQt5.QtWidgets import QApplication, QLabel, QWidget

# For accessing command line arguments
import sys

# Establish QApplication instance for app, with ability to pass command line arguments.
app = QApplication(sys.argv)
app.setStyle("Fusion")
label = QLabel("I'm Dumb!")

label.show()

app.exec_()