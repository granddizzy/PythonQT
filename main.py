from PyQt6 import QtWidgets
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowTitle("Моя программа")
        self.resize(300, 70)

        label = QtWidgets.QLabel("<center>Дратути</center>")
        btnQuit = QtWidgets.QPushButton("Закрыть")

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(label)
        vbox.addWidget(btnQuit)

        self.setLayout(vbox)

        btnQuit.clicked.connect(app.quit)

app = QtWidgets.QApplication(sys.argv)

w = MyWidget()
w.show()

sys.exit(app.exec())