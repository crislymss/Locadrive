# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaSEDAN.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Carros_C(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-10, 0, 861, 151))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(250, 0, 281, 91))
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("fotos/carro.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(230, 80, 321, 61))
        self.widget_3.setStyleSheet("background-color: rgb(39, 39, 39);")
        self.widget_3.setObjectName("widget_3")
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setGeometry(QtCore.QRect(20, 10, 281, 41))
        self.widget_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_4.setObjectName("widget_4")
        self.label_12 = QtWidgets.QLabel(self.widget_4)
        self.label_12.setGeometry(QtCore.QRect(60, 0, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(15)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 160, 151, 111))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("fotos/fiat-cronos-pd4eanol01jb4u2r7udd6n6yv9i6hnjsxypbcj3pno.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 270, 139, 53))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_27 = QtWidgets.QLabel(self.layoutWidget)
        self.label_27.setObjectName("label_27")
        self.verticalLayout.addWidget(self.label_27)
        self.label_28 = QtWidgets.QLabel(self.layoutWidget)
        self.label_28.setObjectName("label_28")
        self.verticalLayout.addWidget(self.label_28)
        self.label_29 = QtWidgets.QLabel(self.layoutWidget)
        self.label_29.setObjectName("label_29")
        self.verticalLayout.addWidget(self.label_29)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(310, 270, 139, 53))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_30 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_2.addWidget(self.label_30)
        self.label_31 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_2.addWidget(self.label_31)
        self.label_32 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_2.addWidget(self.label_32)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 170, 181, 91))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("fotos/profile-806.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(560, 270, 139, 53))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_33 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_33.setObjectName("label_33")
        self.verticalLayout_3.addWidget(self.label_33)
        self.label_34 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_34.setObjectName("label_34")
        self.verticalLayout_3.addWidget(self.label_34)
        self.label_35 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_3.addWidget(self.label_35)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 360, 151, 71))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("fotos/onix_SEDAN.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.layoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_4.setGeometry(QtCore.QRect(50, 450, 139, 53))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_36 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_36.setObjectName("label_36")
        self.verticalLayout_4.addWidget(self.label_36)
        self.label_37 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_37.setObjectName("label_37")
        self.verticalLayout_4.addWidget(self.label_37)
        self.label_38 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_38.setObjectName("label_38")
        self.verticalLayout_4.addWidget(self.label_38)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(310, 340, 161, 111))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("fotos/Hyundai-HB20s-Vision-1.6.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.layoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_5.setGeometry(QtCore.QRect(300, 450, 139, 53))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_39 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_39.setObjectName("label_39")
        self.verticalLayout_5.addWidget(self.label_39)
        self.label_40 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_40.setObjectName("label_40")
        self.verticalLayout_5.addWidget(self.label_40)
        self.label_41 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_41.setObjectName("label_41")
        self.verticalLayout_5.addWidget(self.label_41)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(550, 340, 151, 91))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("fotos/fiat-grand-siena.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.layoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_6.setGeometry(QtCore.QRect(550, 450, 139, 53))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_42 = QtWidgets.QLabel(self.layoutWidget_6)
        self.label_42.setObjectName("label_42")
        self.verticalLayout_6.addWidget(self.label_42)
        self.label_43 = QtWidgets.QLabel(self.layoutWidget_6)
        self.label_43.setObjectName("label_43")
        self.verticalLayout_6.addWidget(self.label_43)
        self.label_44 = QtWidgets.QLabel(self.layoutWidget_6)
        self.label_44.setObjectName("label_44")
        self.verticalLayout_6.addWidget(self.label_44)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(500, 160, 231, 101))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("fotos/fb119cb4-f6e5-4dae-aa1b-9c2d70044f24.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 530, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.label_12.setText(_translate("MainWindow", "CATEGORIA (C) SEDAN"))
        self.label_27.setText(_translate("MainWindow", "Código: 12"))
        self.label_28.setText(_translate("MainWindow", "Ano: 2020"))
        self.label_29.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><br/></p></body></html>"))
        self.label_29.setText(_translate("MainWindow", "Modelo: Honda City"))
        self.label_30.setText(_translate("MainWindow", "Código: 13"))
        self.label_31.setText(_translate("MainWindow", "Ano: 2020"))
        self.label_32.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><br/></p></body></html>"))
        self.label_32.setText(_translate("MainWindow", "Modelo: Fiat Cronos"))
        self.label_33.setText(_translate("MainWindow", "Código: 14"))
        self.label_34.setText(_translate("MainWindow", "Ano: 2022"))
        self.label_35.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><br/></p></body></html>"))
        self.label_35.setText(_translate("MainWindow", "Modelo: Fiat Yaris"))
        self.label_36.setText(_translate("MainWindow", "Código: 15"))
        self.label_37.setText(_translate("MainWindow", "Ano: 2021"))
        self.label_38.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><br/></p></body></html>"))
        self.label_38.setText(_translate("MainWindow", "Modelo:Onix Plus "))
        self.label_39.setText(_translate("MainWindow", "Código: 16"))
        self.label_40.setText(_translate("MainWindow", "Ano: 2021"))
        self.label_41.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><br/></p></body></html>"))
        self.label_41.setText(_translate("MainWindow", "Modelo: Hyundai HB20s"))
        self.label_42.setText(_translate("MainWindow", "Código: 17"))
        self.label_43.setText(_translate("MainWindow", "Ano: 2021"))
        self.label_44.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><br/></p></body></html>"))
        self.label_44.setText(_translate("MainWindow", "Modelo: Grand Siena"))
        self.pushButton.setText(_translate("MainWindow", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Carros_C()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
