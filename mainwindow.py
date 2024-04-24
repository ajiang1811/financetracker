import sys
from PyQt5.QtWidgets import (
    QDialog,
    QMainWindow,
    QApplication,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QLabel,
    QLineEdit,
    QMessageBox,
    QGridLayout
)
class LoginWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Login Form')
        self.setFixedSize(500, 300)

        self.layout = QVBoxLayout(self)

        welcome_message = QLabel('<font size="6"> Finance Tracker </font>')
        self.layout.addWidget(welcome_message, 0)

        label_name = QLabel('<font size="4"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please enter your username')
        self.layout.addWidget(label_name, 1)
        self.layout.addWidget(self.lineEdit_username, 1)

        label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Please enter your password')
        self.layout.addWidget(label_password, 2)
        self.layout.addWidget(self.lineEdit_password, 2)

        button_login = QPushButton('Login')
        button_login.clicked.connect(self.check_password)
        self.layout.addWidget(button_login, 3)

        self.setLayout(self.layout)

    def check_password(self):
        msg = QMessageBox()

        if self.lineEdit_username.text() == 'Username' and self.lineEdit_password.text() == '000':
            msg.setText('Success')
            msg.exec_()
            app.quit()
        else:
            msg.setText('Incorrect Password')
            msg.exec_()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.widget = QWidget()
        self.layout = QGridLayout()
        self.setCentralWidget(widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())