from PyQt6 import QtWidgets
import sys
import my_window


class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        #         self.setWindowTitle("Моя программа")
        #         self.resize(300, 70)
        #
        #         label = QtWidgets.QLabel("Поиск по классификатору МКБ:")
        #         btnQuit = QtWidgets.QPushButton("Закрыть")
        #         btnSearch = QtWidgets.QPushButton("Найти")
        #
        #         line = QLineEdit()
        #
        #         vbox = QtWidgets.QVBoxLayout()
        #         vbox.addWidget(label)
        #         vbox.addWidget(btnSearch)
        #         vbox.addWidget(line)
        #         vbox.addWidget(btnQuit)
        #         vbox.addWidget(line)
        #
        #         self.setLayout(vbox)
        #
        #         btnQuit.clicked.connect(app.quit)
        #         @btnSearch.clicked.connect
        #         def click():
        #             self.search()
        #
        #     def search(self):
        #         print("Надо что-то найти...")

        self.ui = my_window.Ui_Form()
        self.ui.setupUi(self)

        # connect signals
        self.ui.pushButton_2.clicked.connect(self.close)
        self.ui.pushButton.clicked.connect(self.search)
        # def click():
        #     self.search()

    def search(self):
        query = self.ui.lineEdit.text()
        if (query):
            print("Надо найти: " + self.ui.lineEdit.text())


app = QtWidgets.QApplication(sys.argv)

w = MyWidget()
w.show()

sys.exit(app.exec())
