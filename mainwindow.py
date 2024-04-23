import sys
from PyQt5.QtWidgets import QDialog, QApplication,QVBoxLayout, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox

class LoginWindow(QDialog):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setWindowTitle('Login Form')
        self.setFixedSize(500, 300)

        layout = QVBoxLayout(self)

        welcome_message = QLabel('<font size="6"> Finance Tracker </font>')
        layout.addWidget(welcome_message, 0)

        label_name = QLabel('<font size="4"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please enter your username')
        layout.addWidget(label_name, 1)
        layout.addWidget(self.lineEdit_username, 1)

        label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Please enter your password')
        layout.addWidget(label_password, 2)
        layout.addWidget(self.lineEdit_password, 2)

        button_login = QPushButton('Login')
        button_login.clicked.connect(self.check_password)
        layout.addWidget(button_login, 3)

        self.setLayout(layout)

    def check_password(self):
        msg = QMessageBox()

        if self.lineEdit_username.text() == 'Username' and self.lineEdit_password.text() == '000':
            msg.setText('Success')
            msg.exec_()
            app.quit()
        else:
            msg.setText('Incorrect Password')
            msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = LoginWindow()
    form.show()

    sys.exit(app.exec_())