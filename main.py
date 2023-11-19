from PyQt6 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

w = QtWidgets.QWidget()
w.setWindowTitle("Моя программа")
w.resize(300, 70)

label = QtWidgets.QLabel("<center>Дратути</center>")
btnQuit = QtWidgets.QPushButton("Закрыть")

vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(btnQuit)

w.setLayout(vbox)

btnQuit.clicked.connect(app.quit)

w.show()
sys.exit(app.exec())