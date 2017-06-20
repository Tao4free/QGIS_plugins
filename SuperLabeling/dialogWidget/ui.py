# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './EasyMinimumLabeling_ver2.0_seperate.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(456, 190)
        self.lbY = QtGui.QLabel(Dialog)
        self.lbY.setGeometry(QtCore.QRect(310, 130, 16, 16))
        self.lbY.setObjectName(_fromUtf8("lbY"))
        self.lbStep2 = QtGui.QLabel(Dialog)
        self.lbStep2.setGeometry(QtCore.QRect(10, 90, 261, 38))
        self.lbStep2.setObjectName(_fromUtf8("lbStep2"))
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(290, 160, 161, 23))
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.lbPoint = QtGui.QLabel(Dialog)
        self.lbPoint.setGeometry(QtCore.QRect(340, 80, 108, 16))
        self.lbPoint.setObjectName(_fromUtf8("lbPoint"))
        self.lbStep1 = QtGui.QLabel(Dialog)
        self.lbStep1.setGeometry(QtCore.QRect(10, 40, 401, 16))
        self.lbStep1.setObjectName(_fromUtf8("lbStep1"))
        self.lbX = QtGui.QLabel(Dialog)
        self.lbX.setGeometry(QtCore.QRect(310, 100, 16, 16))
        self.lbX.setFrameShape(QtGui.QFrame.NoFrame)
        self.lbX.setObjectName(_fromUtf8("lbX"))
        self.cbField = QtGui.QComboBox(Dialog)
        self.cbField.setGeometry(QtCore.QRect(20, 60, 121, 20))
        self.cbField.setObjectName(_fromUtf8("cbField"))
        self.txX = QtGui.QLineEdit(Dialog)
        self.txX.setGeometry(QtCore.QRect(330, 100, 121, 21))
        self.txX.setObjectName(_fromUtf8("txX"))
        self.txY = QtGui.QLineEdit(Dialog)
        self.txY.setGeometry(QtCore.QRect(330, 130, 121, 21))
        self.txY.setObjectName(_fromUtf8("txY"))
        self.lbLayer = QtGui.QLabel(Dialog)
        self.lbLayer.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.lbLayer.setObjectName(_fromUtf8("lbLayer"))
        self.txLayer = QtGui.QLineEdit(Dialog)
        self.txLayer.setGeometry(QtCore.QRect(90, 10, 341, 21))
        self.txLayer.setObjectName(_fromUtf8("txLayer"))
        self.pbnEdit = QtGui.QPushButton(Dialog)
        self.pbnEdit.setGeometry(QtCore.QRect(240, 60, 75, 23))
        self.pbnEdit.setObjectName(_fromUtf8("pbnEdit"))
        self.lbStep2_2 = QtGui.QLabel(Dialog)
        self.lbStep2_2.setGeometry(QtCore.QRect(10, 130, 271, 38))
        self.lbStep2_2.setObjectName(_fromUtf8("lbStep2_2"))
        self.pbnGenerate = QtGui.QPushButton(Dialog)
        self.pbnGenerate.setGeometry(QtCore.QRect(160, 60, 61, 23))
        self.pbnGenerate.setObjectName(_fromUtf8("pbnGenerate"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "SuperLabeling", None))
        self.lbY.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Y</p></body></html>", None))
        self.lbStep2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">2. Left Click on canvas where you want to put </span></p><p align=\"center\"><span style=\" font-size:10pt;\">the Label (make click near the feature)</span></p></body></html>", None))
        self.lbPoint.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">The point you click</span></p></body></html>", None))
        self.lbStep1.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">1. Choose the field you want to Label, click &quot;Start Edition&quot; </span></p></body></html>", None))
        self.lbX.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">X</span></p></body></html>", None))
        self.lbLayer.setText(_translate("Dialog", "<html><head/><body><p>Current layer</p></body></html>", None))
        self.pbnEdit.setText(_translate("Dialog", "Start Edition", None))
        self.lbStep2_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">3. Right click or click &quot;Aplpy&quot; to complete labeling</span></p></body></html>", None))
        self.pbnGenerate.setText(_translate("Dialog", "Generate", None))

