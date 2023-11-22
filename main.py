from PyQt6 import QtWidgets
import sys
import my_window


def parse_mkb_code(key: str) -> (str, str, str):
    key = key.replace(".", "")
    liter = key[0]
    group = key[1:3]

    if len(key) > 3:
        num = key[3:len(key)]
    else:
        num = ""

    return liter, group, num


def get_mkb_code(item: QtWidgets.QTreeWidgetItem) -> str:
    parent = item.parent()
    code = item.text(0)
    while parent:
        code = parent.text(0) + code
        parent = parent.parent()

    if len(code) > 3:
        code = code[0:3] + "." + code[3:len(code)]

    return code


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

        # self.tree = QtWidgets.QTreeWidget()

        # connect signals
        self.ui.pushButton_2.clicked.connect(self.close)
        self.ui.pushButton.clicked.connect(self.search)

        self.ui.treeWidget.currentItemChanged.connect(self.show_decription)
        # def click():
        #     self.search()

    def search(self):
        query = self.ui.lineEdit.text()
        if query:
            # rint("Надо найти: " + self.ui.lineEdit.text())
            self.ui.textBrowser.setText("Надо найти: " + self.ui.lineEdit.text())

    def show_decription(self, item):
        self.ui.textBrowser.setText(get_mkb_code(item) + " " + item.text(1))

    def fill_tree(self):
        with open('spr_mkb10.csv', "r", encoding="UTF-8") as file:
            data = file.readlines()

            parents = []
            for line in data:
                arr_line = line.replace("\n", "").replace("\ufeff", "").split(";")

                item = QtWidgets.QTreeWidgetItem()
                item.setText(1, arr_line[1])

                liter, group, num = parse_mkb_code(arr_line[0])

                if len(parents) > 0:
                    previous_liter, previous_group, _ = parse_mkb_code(get_mkb_code(parents[len(parents) - 1]))
                else:
                    previous_liter, previous_group, = None, None

                if previous_liter != liter:
                    itemTop = QtWidgets.QTreeWidgetItem()
                    itemTop.setText(0, liter)
                    self.ui.treeWidget.addTopLevelItem(itemTop)
                    parents = [itemTop]

                    parents[len(parents) - 1].addChild(item)
                    item.setText(0, group)
                    parents.append(item)
                else:
                    if group != previous_group:
                        parents.pop()
                        parents[len(parents) - 1].addChild(item)
                        item.setText(0, group)
                        parents.append(item)
                    else:
                        item.setText(0, num)
                        parents[len(parents) - 1].addChild(item)


app = QtWidgets.QApplication(sys.argv)

w = MyWidget()
w.fill_tree()
w.show()

sys.exit(app.exec())
