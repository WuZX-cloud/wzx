import sys

from myui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication,QMainWindow, QWidget

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.login.clicked.connect(self.login)

    def login(self):
        user_name = self.ui.name_Edit.text()
        passwd = self.ui.passwd_Edit.text()

        if user_name != "" and passwd != "":
            self.ui.info_show.setText(user_name+"正在登录中...，请等待")
        else :
            self.ui.info_show.setText("")
        self.ui.info_show.repaint()

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()
