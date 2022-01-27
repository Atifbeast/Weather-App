from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *

class Ui_SearchedWindow(object):
    def setupUi(self, SearchedWindow):
        SearchedWindow.setObjectName("SearchedWindow")
        SearchedWindow.resize(450, 750)
        self.centralwidget = QtWidgets.QWidget(SearchedWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 450, 750))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../../Users/ATIF SHAIK/Downloads/bigresizethunder.jpg"))
        self.label.setObjectName("label")
        SearchedWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SearchedWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 232, 22))
        self.menubar.setObjectName("menubar")
        SearchedWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SearchedWindow)
        self.statusbar.setObjectName("statusbar")
        SearchedWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SearchedWindow)
        QtCore.QMetaObject.connectSlotsByName(SearchedWindow)

    def retranslateUi(self, SearchedWindow):
        _translate = QtCore.QCoreApplication.translate
        SearchedWindow.setWindowTitle(_translate("SearchedWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SearchedWindow = QtWidgets.QMainWindow()
    ui = Ui_SearchedWindow()
    ui.setupUi(SearchedWindow)
    SearchedWindow.show()
    sys.exit(app.exec_())
