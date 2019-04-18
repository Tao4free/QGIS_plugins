# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SuperLabeling.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(477, 195)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.lbLayer = QtWidgets.QLabel(Dialog)
        self.lbLayer.setObjectName("lbLayer")
        self.gridLayout.addWidget(self.lbLayer, 0, 0, 1, 1)
        self.txLayer = QtWidgets.QLineEdit(Dialog)
        self.txLayer.setObjectName("txLayer")
        self.gridLayout.addWidget(self.txLayer, 0, 1, 1, 5)
        self.lbStep1 = QtWidgets.QLabel(Dialog)
        self.lbStep1.setObjectName("lbStep1")
        self.gridLayout.addWidget(self.lbStep1, 1, 0, 1, 6)
        self.cbField = QtWidgets.QComboBox(Dialog)
        self.cbField.setObjectName("cbField")
        self.gridLayout.addWidget(self.cbField, 2, 0, 1, 2)
        self.lbStep2 = QtWidgets.QLabel(Dialog)
        self.lbStep2.setObjectName("lbStep2")
        self.gridLayout.addWidget(self.lbStep2, 4, 0, 2, 3)
        self.txX = QtWidgets.QLineEdit(Dialog)
        self.txX.setObjectName("txX")
        self.gridLayout.addWidget(self.txX, 4, 5, 1, 1)
        self.lbPoint = QtWidgets.QLabel(Dialog)
        self.lbPoint.setObjectName("lbPoint")
        self.gridLayout.addWidget(self.lbPoint, 2, 5, 1, 1)
        self.txY = QtWidgets.QLineEdit(Dialog)
        self.txY.setObjectName("txY")
        self.gridLayout.addWidget(self.txY, 5, 5, 1, 1)
        self.lbX = QtWidgets.QLabel(Dialog)
        self.lbX.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbX.setObjectName("lbX")
        self.gridLayout.addWidget(self.lbX, 4, 4, 1, 1)
        self.lbY = QtWidgets.QLabel(Dialog)
        self.lbY.setObjectName("lbY")
        self.gridLayout.addWidget(self.lbY, 5, 4, 1, 1)
        self.pbnEdit = QtWidgets.QPushButton(Dialog)
        self.pbnEdit.setObjectName("pbnEdit")
        self.gridLayout.addWidget(self.pbnEdit, 2, 2, 1, 1)
        self.lbStep2_2 = QtWidgets.QLabel(Dialog)
        self.lbStep2_2.setObjectName("lbStep2_2")
        self.gridLayout.addWidget(self.lbStep2_2, 8, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 8, 4, 1, 2)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SuperLabeling"))
        self.lbLayer.setText(_translate("Dialog", "<html><head/><body><p>Current layer</p></body></html>"))
        self.lbStep1.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">1. Choose the field you want to Label, click &quot;Start Edition&quot; </span></p></body></html>"))
        self.lbStep2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">2. Left Click on canvas where you want to put </span></p><p align=\"center\"><span style=\" font-size:10pt;\">the Label (make click near the feature)</span></p></body></html>"))
        self.lbPoint.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">The point you click</span></p></body></html>"))
        self.lbX.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">X</span></p></body></html>"))
        self.lbY.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Y</p></body></html>"))
        self.pbnEdit.setText(_translate("Dialog", "Start Edition"))
        self.lbStep2_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">3. Left double click to hide label</span></p></body></html>"))


