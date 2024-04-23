import sys

from PyQt6.QtWidgets import (QMainWindow, QTextEdit, QLineEdit, QPushButton,
                             QApplication)


class ChatBotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(700, 500)

        # Add the chat area Widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # Input Field Widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)

        # Add theButton
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 340, 100, 40)

        self.show()


class Chatbot:
    pass


app = QApplication(sys.argv)
main_window = ChatBotWindow()
sys.exit(app.exec())