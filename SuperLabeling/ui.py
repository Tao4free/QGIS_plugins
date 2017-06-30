# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SuperLabeling.ui'
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
        Dialog.resize(477, 195)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lbLayer = QtGui.QLabel(Dialog)
        self.lbLayer.setObjectName(_fromUtf8("lbLayer"))
        self.gridLayout.addWidget(self.lbLayer, 0, 0, 1, 1)
        self.txLayer = QtGui.QLineEdit(Dialog)
        self.txLayer.setObjectName(_fromUtf8("txLayer"))
        self.gridLayout.addWidget(self.txLayer, 0, 1, 1, 5)
        self.lbStep1 = QtGui.QLabel(Dialog)
        self.lbStep1.setObjectName(_fromUtf8("lbStep1"))
        self.gridLayout.addWidget(self.lbStep1, 1, 0, 1, 6)
        self.cbField = QtGui.QComboBox(Dialog)
        self.cbField.setObjectName(_fromUtf8("cbField"))
        self.gridLayout.addWidget(self.cbField, 2, 0, 1, 2)
        self.lbStep2 = QtGui.QLabel(Dialog)
        self.lbStep2.setObjectName(_fromUtf8("lbStep2"))
        self.gridLayout.addWidget(self.lbStep2, 4, 0, 2, 3)
        self.txX = QtGui.QLineEdit(Dialog)
        self.txX.setObjectName(_fromUtf8("txX"))
        self.gridLayout.addWidget(self.txX, 4, 5, 1, 1)
        self.lbPoint = QtGui.QLabel(Dialog)
        self.lbPoint.setObjectName(_fromUtf8("lbPoint"))
        self.gridLayout.addWidget(self.lbPoint, 2, 5, 1, 1)
        self.txY = QtGui.QLineEdit(Dialog)
        self.txY.setObjectName(_fromUtf8("txY"))
        self.gridLayout.addWidget(self.txY, 5, 5, 1, 1)
        self.lbX = QtGui.QLabel(Dialog)
        self.lbX.setFrameShape(QtGui.QFrame.NoFrame)
        self.lbX.setObjectName(_fromUtf8("lbX"))
        self.gridLayout.addWidget(self.lbX, 4, 4, 1, 1)
        self.lbY = QtGui.QLabel(Dialog)
        self.lbY.setObjectName(_fromUtf8("lbY"))
        self.gridLayout.addWidget(self.lbY, 5, 4, 1, 1)
        self.pbnEdit = QtGui.QPushButton(Dialog)
        self.pbnEdit.setObjectName(_fromUtf8("pbnEdit"))
        self.gridLayout.addWidget(self.pbnEdit, 2, 2, 1, 1)
        self.lbStep2_2 = QtGui.QLabel(Dialog)
        self.lbStep2_2.setObjectName(_fromUtf8("lbStep2_2"))
        self.gridLayout.addWidget(self.lbStep2_2, 8, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 8, 4, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "SuperLabeling", None))
        self.lbLayer.setText(_translate("Dialog", "<html><head/><body><p>Current layer</p></body></html>", None))
        self.lbStep1.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">1. Choose the field you want to Label, click &quot;Start Edition&quot; </span></p></body></html>", None))
        self.lbStep2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">2. Left Click on canvas where you want to put </span></p><p align=\"center\"><span style=\" font-size:10pt;\">the Label (make click near the feature)</span></p></body></html>", None))
        self.lbPoint.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">The point you click</span></p></body></html>", None))
        self.lbX.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">X</span></p></body></html>", None))
        self.lbY.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Y</p></body></html>", None))
        self.pbnEdit.setText(_translate("Dialog", "Start Edition", None))
        self.lbStep2_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">3. Left double click to hide label</span></p></body></html>", None))

