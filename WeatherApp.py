from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
import json
import requests
from WeatherWork import Ui_SecondWindow

url = 'http://api.weatherapi.com/v1/current.json?key=497b05cd09394f9bb0580524222501&q=Bangalore&aqi=yes&alerts=yes'

req = requests.get(url).json()

city = req['location']['name'] #D
country = req['location']['country'] #D
tempC = req['current']['temp_c'] #D
tempC = str(f'{tempC} °C') #D
comments = req['current']['condition']['text'] #D
windkph = req['current']['wind_kph'] #D
windkph = str(f'{windkph}km/h') #D
winddir = req['current']['wind_dir']
humidity = req['current']['humidity'] #D
humidity = str(f'{humidity}%') #D
UVindex = req['current']['uv'] #D
UVindex = str(UVindex) #D
Airquality = req['current']['air_quality']
feelslike = req['current']['feelslike_c'] #D
feelslike = str(f'{feelslike} °C') #D
pressure_mmhg = req['current']['pressure_in'] #D
pressure_mmhg = str(f'{pressure_mmhg} mmhg') #D
visibility_kms = req['current']['vis_km']
visibility_kms = int(visibility_kms)
visibility_kms = str(f'{visibility_kms} Kms')

class Ui_MainWindow(object):
    def Search(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self.window)
        self.window.show()



    def setupUi(self, MainWindow):                              #.set = setText()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)

        self.labelcity = QtWidgets.QLabel(city,self.label)
        self.labelcity.setFont(QFont('Arial', 20))
        self.labelcity.setStyleSheet('QLabel {color: white;}')
        self.labelcity.move(145,10)

        self.labelcountry = QtWidgets.QLabel(country,self.label)
        self.labelcountry.setFont(QFont('Arial', 10))
        self.labelcountry.setStyleSheet('QLabel {color: white;}')
        self.labelcountry.move(200, 60)

        self.labeltemp = QtWidgets.QLabel(tempC, self.label)
        self.labeltemp.setFont(QFont('Arial', 30))
        self.labeltemp.setStyleSheet('QLabel {color: white;}')
        self.labeltemp.move(137, 130)

        self.labeltext = QtWidgets.QLabel(comments, self.label)
        self.labeltext.setFont(QFont('Arial', 10))
        self.labeltext.setStyleSheet('QLabel {color: white;}')
        self.labeltext.move(175, 200)

        self.realfeels = QtWidgets.QLabel('Real Feel', self.label)
        self.realfeels.setFont(QFont('Arial', 12))
        self.realfeels.setStyleSheet('QLabel {color: white;}')
        self.realfeels.move(20, 310)

        self.labelfeels = QtWidgets.QLabel(feelslike, self.label)
        self.labelfeels.setFont(QFont('Arial', 10))
        self.labelfeels.setStyleSheet('QLabel {color: white;}')
        self.labelfeels.move(30, 340)

        self.texthumidity = QtWidgets.QLabel('Humidity', self.label)
        self.texthumidity.setFont(QFont('Arial', 12))
        self.texthumidity.setStyleSheet('QLabel {color: white;}')
        self.texthumidity.move(300, 310)

        self.labelhumidity = QtWidgets.QLabel(humidity, self.label)
        self.labelhumidity.setFont(QFont('Arial', 10))
        self.labelhumidity.setStyleSheet('QLabel {color: white;}')
        self.labelhumidity.move(320, 340)

        self.textpressure = QtWidgets.QLabel('Pressure(mm-hg)', self.label)
        self.textpressure.setFont(QFont('Arial', 11))
        self.textpressure.setStyleSheet('QLabel {color: white;}')
        self.textpressure.move(20, 400)

        self.textpressure = QtWidgets.QLabel(pressure_mmhg, self.label)
        self.textpressure.setFont(QFont('Arial', 10))
        self.textpressure.setStyleSheet('QLabel {color: white;}')
        self.textpressure.move(30, 430)

        self.textuv = QtWidgets.QLabel('UV Index', self.label)
        self.textuv.setFont(QFont('Arial', 11))
        self.textuv.setStyleSheet('QLabel {color: white;}')
        self.textuv.move(300, 400)

        self.labeluv = QtWidgets.QLabel(UVindex, self.label)
        self.labeluv.setFont(QFont('Arial', 10))
        self.labeluv.setStyleSheet('QLabel {color: white;}')
        self.labeluv.move(325, 430)

        self.windspeedtext = QtWidgets.QLabel('Wind Speed', self.label)
        self.windspeedtext.setFont(QFont('Arial', 12))
        self.windspeedtext.setStyleSheet('QLabel {color: white;}')
        self.windspeedtext.move(20, 490)

        self.windspeedlabel = QtWidgets.QLabel(windkph, self.label)
        self.windspeedlabel.setFont(QFont('Arial', 10))
        self.windspeedlabel.setStyleSheet('QLabel {color: white;}')
        self.windspeedlabel.move(30, 520)

        self.winddirtext = QtWidgets.QLabel('Wind Direction', self.label)
        self.winddirtext.setFont(QFont('Arial', 12))
        self.winddirtext.setStyleSheet('QLabel {color: white;}')
        self.winddirtext.move(280, 490)

        self.winddirlabel = QtWidgets.QLabel(winddir, self.label)
        self.winddirlabel.setFont(QFont('Arial', 10))
        self.winddirlabel.setStyleSheet('QLabel {color: white;}')
        self.winddirlabel.move(322, 520)

        self.visibilitytext = QtWidgets.QLabel('Visibility', self.label)
        self.visibilitytext.setFont(QFont('Arial', 12))
        self.visibilitytext.setStyleSheet('QLabel {color: white;}')
        self.visibilitytext.move(177, 570)

        self.visibilitylabel = QtWidgets.QLabel(visibility_kms, self.label)
        self.visibilitylabel.setFont(QFont('Arial', 12))
        self.visibilitylabel.setStyleSheet('QLabel {color: white;}')
        self.visibilitylabel.move(186, 610)

        self.qpushbutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.Search())
        self.qpushbutton.setGeometry(QtCore.QRect(10, 10, 31, 31))       #50 16 50 40
        self.label.setGeometry(QtCore.QRect(0, 0, 450, 750))
        self.label.setLineWidth(1)
        self.label.setPixmap(QtGui.QPixmap("../../../../Users/ATIF SHAIK/Downloads/bigresizethunder.jpg"))
        self.label.setObjectName("label")
        self.aqibut = QtWidgets.QPushButton(self.centralwidget)
        self.aqibut.setGeometry(QtCore.QRect(190, 230, 80, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.qpushbutton.setFont(font)
        self.qpushbutton.setObjectName("qpushbutton")
        self.aqibut.setFont(font)
        self.aqibut.setObjectName("AQIbut")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 232, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.qpushbutton.setText(_translate("MainWindow", "+"))
        self.aqibut.setText(_translate("MainWindow", "AQI"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
