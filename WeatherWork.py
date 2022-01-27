from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
import sys
from SearchedScreen import Ui_SearchedWindow
import requests
import json

class Ui_SecondWindow(object):
    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(450, 750)    #229 381
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 450, 750))
        #self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../../Users/ATIF SHAIK/Downloads/weatherappbg.png"))
        self.label.setObjectName("label")

        self.searchbut = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.clig())
        self.searchbut.setGeometry(QtCore.QRect(10, 150, 104, 31))
        font = QtGui.QFont()
        self.searchbut.setFont(font)
        self.searchbut.setFlat(False)
        self.searchbut.setObjectName("searchbut")


        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 100, 450, 30))
        self.lineEdit.setFont(QFont('comicsansms',10))
        self.lineEdit.setPlaceholderText('Search Cities')
        self.lineEdit.setObjectName("lineEdit")


        SecondWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SecondWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 229, 22))
        self.menubar.setObjectName("menubar")
        SecondWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SecondWindow)
        self.statusbar.setObjectName("statusbar")
        SecondWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)


    def clig(self):
        searchedcity = self.lineEdit.text()
        searchedcity = searchedcity.lower()
        try :
            if searchedcity == 'israel' or searchedcity == 'tel aviv' or searchedcity == 'yafo' or searchedcity == 'jerusalem' or searchedcity == 'haifa' or searchedcity == 'lod' or searchedcity == 'netanya' or searchedcity == 'ramla' or searchedcity == 'tel aviv yafo' or searchedcity == 'tiberias':
                city = {'q': 'Ramallah'}
                req = requests.get(
                    'http://api.weatherapi.com/v1/current.json?key=497b05cd09394f9bb0580524222501&aqi=yes&alerts=yes',
                    params=city).json()
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_SearchedWindow()
                self.ui.setupUi(self.window)
                city = req['location']['name']  # D
                country = req['location']['country']
                tempC = req['current']['temp_c']
                tempC = str(f'{tempC} °C')
                comments = req['current']['condition']['text']  # D
                windkph = req['current']['wind_kph']  # D
                windkph = str(f'{windkph}km/h')  # D
                winddir = req['current']['wind_dir']
                humidity = req['current']['humidity']  # D
                humidity = str(f'{humidity}%')  # D
                UVindex = req['current']['uv']  # D
                UVindex = str(UVindex)  # D
                Airquality = req['current']['air_quality']
                feelslike = req['current']['feelslike_c']  # D
                feelslike = str(f'{feelslike} °C')  # D
                pressure_mmhg = req['current']['pressure_in']  # D
                pressure_mmhg = str(f'{pressure_mmhg} mmhg')  # D
                visibility_kms = req['current']['vis_km']
                visibility_kms = int(visibility_kms)
                visibility_kms = str(f'{visibility_kms} Kms')

                self.ui.labelP = QtWidgets.QLabel('Did You Mean Palestine ??',self.ui.label)
                self.ui.labelP.move(5, 0)
                self.ui.labelP.setStyleSheet('QLabel {color: white;}')
                self.ui.labelP.setFont(QFont('Arial', 20))

                self.ui.labelC = QtWidgets.QLabel(country, self.ui.label)
                self.ui.labelC.move(164, 90)
                self.ui.labelC.setFont(QFont('Arial', 10))
                self.ui.labelC.setStyleSheet('QLabel {color: white;}')

                self.ui.labeltemp = QtWidgets.QLabel(tempC, self.ui.label)
                self.ui.labeltemp.setFont(QFont('Arial', 30))
                self.ui.labeltemp.setStyleSheet('QLabel {color: white;}')
                self.ui.labeltemp.move(133, 150)

                self.ui.labeltext = QtWidgets.QLabel(comments, self.ui.label)
                self.ui.labeltext.setFont(QFont('Arial', 10))
                self.ui.labeltext.setStyleSheet('QLabel {color: white;}')
                self.ui.labeltext.move(180, 220)

                self.ui.realfeels = QtWidgets.QLabel('Real Feel', self.ui.label)
                self.ui.realfeels.setFont(QFont('Arial', 12))
                self.ui.realfeels.setStyleSheet('QLabel {color: white;}')
                self.ui.realfeels.move(20, 320)

                self.ui.labelfeels = QtWidgets.QLabel(feelslike, self.ui.label)
                self.ui.labelfeels.setFont(QFont('Arial', 10))
                self.ui.labelfeels.setStyleSheet('QLabel {color: white;}')
                self.ui.labelfeels.move(30, 350)

                self.ui.texthumidity = QtWidgets.QLabel('Humidity', self.ui.label)
                self.ui.texthumidity.setFont(QFont('Arial', 12))
                self.ui.texthumidity.setStyleSheet('QLabel {color: white;}')
                self.ui.texthumidity.move(300, 320)

                self.ui.labelhumidity = QtWidgets.QLabel(humidity, self.ui.label)
                self.ui.labelhumidity.setFont(QFont('Arial', 10))
                self.ui.labelhumidity.setStyleSheet('QLabel {color: white;}')
                self.ui.labelhumidity.move(320, 350)

                self.ui.textpressure = QtWidgets.QLabel('Pressure(mm-hg)', self.ui.label)
                self.ui.textpressure.setFont(QFont('Arial', 11))
                self.ui.textpressure.setStyleSheet('QLabel {color: white;}')
                self.ui.textpressure.move(20, 410)

                self.ui.textpressure = QtWidgets.QLabel(pressure_mmhg, self.ui.label)
                self.ui.textpressure.setFont(QFont('Arial', 10))
                self.ui.textpressure.setStyleSheet('QLabel {color: white;}')
                self.ui.textpressure.move(30, 440)

                self.ui.textuv = QtWidgets.QLabel('UV Index', self.ui.label)
                self.ui.textuv.setFont(QFont('Arial', 11))
                self.ui.textuv.setStyleSheet('QLabel {color: white;}')
                self.ui.textuv.move(300, 410)

                self.ui.labeluv = QtWidgets.QLabel(UVindex, self.ui.label)
                self.ui.labeluv.setFont(QFont('Arial', 10))
                self.ui.labeluv.setStyleSheet('QLabel {color: white;}')
                self.ui.labeluv.move(325, 440)

                self.ui.windspeedtext = QtWidgets.QLabel('Wind Speed', self.ui.label)
                self.ui.windspeedtext.setFont(QFont('Arial', 12))
                self.ui.windspeedtext.setStyleSheet('QLabel {color: white;}')
                self.ui.windspeedtext.move(20, 500)

                self.ui.windspeedlabel = QtWidgets.QLabel(windkph, self.ui.label)
                self.ui.windspeedlabel.setFont(QFont('Arial', 10))
                self.ui.windspeedlabel.setStyleSheet('QLabel {color: white;}')
                self.ui.windspeedlabel.move(30, 530)

                self.ui.winddirtext = QtWidgets.QLabel('Wind Direction', self.ui.label)
                self.ui.winddirtext.setFont(QFont('Arial', 12))
                self.ui.winddirtext.setStyleSheet('QLabel {color: white;}')
                self.ui.winddirtext.move(280, 510)

                self.ui.winddirlabel = QtWidgets.QLabel(winddir, self.ui.label)
                self.ui.winddirlabel.setFont(QFont('Arial', 10))
                self.ui.winddirlabel.setStyleSheet('QLabel {color: white;}')
                self.ui.winddirlabel.move(322, 540)

                self.ui.visibilitytext = QtWidgets.QLabel('Visibility', self.ui.label)
                self.ui.visibilitytext.setFont(QFont('Arial', 12))
                self.ui.visibilitytext.setStyleSheet('QLabel {color: white;}')
                self.ui.visibilitytext.move(177, 570)

                self.ui.visibilitylabel = QtWidgets.QLabel(visibility_kms, self.ui.label)
                self.ui.visibilitylabel.setFont(QFont('Arial', 12))
                self.ui.visibilitylabel.setStyleSheet('QLabel {color: white;}')
                self.ui.visibilitylabel.move(175, 610)

                self.ui.label = QtWidgets.QLabel(city, self.ui.label)
                self.ui.label.move(140, 50)
                self.ui.label.setFont(QFont('Arial', 15))
                self.ui.label.setStyleSheet('QLabel {color: white;}')

                self.window.show()


            else:
                city = {'q': ''}
                city['q'] = searchedcity
                req = requests.get(
                    'http://api.weatherapi.com/v1/current.json?key=497b05cd09394f9bb0580524222501&aqi=yes&alerts=yes',
                    params=city).json()
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_SearchedWindow()
                self.ui.setupUi(self.window)

                city = req['location']['name']  # D
                country = req['location']['country']
                tempC = req['current']['temp_c']
                tempC = str(f'{tempC} °C')
                comments = req['current']['condition']['text']  # D
                windkph = req['current']['wind_kph']  # D
                windkph = str(f'{windkph}km/h')  # D
                winddir = req['current']['wind_dir']
                humidity = req['current']['humidity']  # D
                humidity = str(f'{humidity}%')  # D
                UVindex = req['current']['uv']  # D
                UVindex = str(UVindex)  # D
                Airquality = req['current']['air_quality']
                feelslike = req['current']['feelslike_c']  # D
                feelslike = str(f'{feelslike} °C')  # D
                pressure_mmhg = req['current']['pressure_in']  # D
                pressure_mmhg = str(f'{pressure_mmhg} mmhg')  # D
                visibility_kms = req['current']['vis_km']
                visibility_kms = int(visibility_kms)
                visibility_kms = str(f'{visibility_kms} Kms')

                # self.ui.labelP = QtWidgets.QLabel('Did You Mean Palestine ??', self.ui.label)
                # self.ui.labelP.move(5, 0)
                # self.ui.labelP.setStyleSheet('QLabel {color: white;}')
                # self.ui.labelP.setFont(QFont('Arial', 20))

                self.ui.labelC = QtWidgets.QLabel(country, self.ui.label)
                self.ui.labelC.move(175, 90)
                self.ui.labelC.setFont(QFont('Arial', 10))
                self.ui.labelC.setStyleSheet('QLabel {color: white;}')

                self.ui.labeltemp = QtWidgets.QLabel(tempC, self.ui.label)
                self.ui.labeltemp.setFont(QFont('Arial', 30))
                self.ui.labeltemp.setStyleSheet('QLabel {color: white;}')
                self.ui.labeltemp.move(133, 150)

                self.ui.labeltext = QtWidgets.QLabel(comments, self.ui.label)
                self.ui.labeltext.setFont(QFont('Arial', 10))
                self.ui.labeltext.setStyleSheet('QLabel {color: white;}')
                self.ui.labeltext.move(180, 220)

                self.ui.realfeels = QtWidgets.QLabel('Real Feel', self.ui.label)
                self.ui.realfeels.setFont(QFont('Arial', 12))
                self.ui.realfeels.setStyleSheet('QLabel {color: white;}')
                self.ui.realfeels.move(20, 320)

                self.ui.labelfeels = QtWidgets.QLabel(feelslike, self.ui.label)
                self.ui.labelfeels.setFont(QFont('Arial', 10))
                self.ui.labelfeels.setStyleSheet('QLabel {color: white;}')
                self.ui.labelfeels.move(30, 350)

                self.ui.texthumidity = QtWidgets.QLabel('Humidity', self.ui.label)
                self.ui.texthumidity.setFont(QFont('Arial', 12))
                self.ui.texthumidity.setStyleSheet('QLabel {color: white;}')
                self.ui.texthumidity.move(300, 320)

                self.ui.labelhumidity = QtWidgets.QLabel(humidity, self.ui.label)
                self.ui.labelhumidity.setFont(QFont('Arial', 10))
                self.ui.labelhumidity.setStyleSheet('QLabel {color: white;}')
                self.ui.labelhumidity.move(320, 350)

                self.ui.textpressure = QtWidgets.QLabel('Pressure(mm-hg)', self.ui.label)
                self.ui.textpressure.setFont(QFont('Arial', 11))
                self.ui.textpressure.setStyleSheet('QLabel {color: white;}')
                self.ui.textpressure.move(20, 410)

                self.ui.textpressure = QtWidgets.QLabel(pressure_mmhg, self.ui.label)
                self.ui.textpressure.setFont(QFont('Arial', 10))
                self.ui.textpressure.setStyleSheet('QLabel {color: white;}')
                self.ui.textpressure.move(30, 440)

                self.ui.textuv = QtWidgets.QLabel('UV Index', self.ui.label)
                self.ui.textuv.setFont(QFont('Arial', 11))
                self.ui.textuv.setStyleSheet('QLabel {color: white;}')
                self.ui.textuv.move(300, 410)

                self.ui.labeluv = QtWidgets.QLabel(UVindex, self.ui.label)
                self.ui.labeluv.setFont(QFont('Arial', 10))
                self.ui.labeluv.setStyleSheet('QLabel {color: white;}')
                self.ui.labeluv.move(325, 440)

                self.ui.windspeedtext = QtWidgets.QLabel('Wind Speed', self.ui.label)
                self.ui.windspeedtext.setFont(QFont('Arial', 12))
                self.ui.windspeedtext.setStyleSheet('QLabel {color: white;}')
                self.ui.windspeedtext.move(20, 500)

                self.ui.windspeedlabel = QtWidgets.QLabel(windkph, self.ui.label)
                self.ui.windspeedlabel.setFont(QFont('Arial', 10))
                self.ui.windspeedlabel.setStyleSheet('QLabel {color: white;}')
                self.ui.windspeedlabel.move(30, 530)

                self.ui.winddirtext = QtWidgets.QLabel('Wind Direction', self.ui.label)
                self.ui.winddirtext.setFont(QFont('Arial', 12))
                self.ui.winddirtext.setStyleSheet('QLabel {color: white;}')
                self.ui.winddirtext.move(280, 510)

                self.ui.winddirlabel = QtWidgets.QLabel(winddir, self.ui.label)
                self.ui.winddirlabel.setFont(QFont('Arial', 10))
                self.ui.winddirlabel.setStyleSheet('QLabel {color: white;}')
                self.ui.winddirlabel.move(322, 540)

                self.ui.visibilitytext = QtWidgets.QLabel('Visibility', self.ui.label)
                self.ui.visibilitytext.setFont(QFont('Arial', 12))
                self.ui.visibilitytext.setStyleSheet('QLabel {color: white;}')
                self.ui.visibilitytext.move(177, 570)

                self.ui.visibilitylabel = QtWidgets.QLabel(visibility_kms, self.ui.label)
                self.ui.visibilitylabel.setFont(QFont('Arial', 12))
                self.ui.visibilitylabel.setStyleSheet('QLabel {color: white;}')
                self.ui.visibilitylabel.move(175, 610)

                self.ui.label = QtWidgets.QLabel(city, self.ui.label)
                self.ui.label.move(165, 50)
                self.ui.label.setFont(QFont('Arial', 15))
                self.ui.label.setStyleSheet('QLabel {color: white;}')

                self.window.show()

        except Exception as e:
            pass





    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "MainWindow"))
        self.searchbut.setText(_translate("SecondWindow", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(SecondWindow)
    SecondWindow.show()
    sys.exit(app.exec_())
