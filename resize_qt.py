# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resize.ui'
#
# Created: Tue Jul  1 14:55:40 2014
#      by: PyQt4 UI code generator 4.10.4
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
        Dialog.resize(512, 391)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.inputFolders = QtGui.QListWidget(Dialog)
        self.inputFolders.setGeometry(QtCore.QRect(10, 31, 491, 141))
        self.inputFolders.setObjectName(_fromUtf8("inputFolders"))
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 360, 491, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 181, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.resizeButton = QtGui.QPushButton(Dialog)
        self.resizeButton.setGeometry(QtCore.QRect(305, 330, 98, 27))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.resizeButton.setFont(font)
        self.resizeButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.resizeButton.setDefault(True)
        self.resizeButton.setObjectName(_fromUtf8("resizeButton"))
        self.removeInputFolderButton = QtGui.QPushButton(Dialog)
        self.removeInputFolderButton.setGeometry(QtCore.QRect(350, 180, 151, 27))
        self.removeInputFolderButton.setObjectName(_fromUtf8("removeInputFolderButton"))
        self.addInputFolderButton = QtGui.QPushButton(Dialog)
        self.addInputFolderButton.setGeometry(QtCore.QRect(250, 180, 98, 27))
        self.addInputFolderButton.setObjectName(_fromUtf8("addInputFolderButton"))
        self.outputFolder = QtGui.QLineEdit(Dialog)
        self.outputFolder.setGeometry(QtCore.QRect(10, 240, 471, 27))
        self.outputFolder.setObjectName(_fromUtf8("outputFolder"))
        self.chooseOutputFolderButton = QtGui.QToolButton(Dialog)
        self.chooseOutputFolderButton.setGeometry(QtCore.QRect(480, 240, 23, 25))
        self.chooseOutputFolderButton.setObjectName(_fromUtf8("chooseOutputFolderButton"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 220, 231, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 293, 201, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.maxWidth = QtGui.QSpinBox(Dialog)
        self.maxWidth.setGeometry(QtCore.QRect(210, 290, 60, 27))
        self.maxWidth.setMinimum(50)
        self.maxWidth.setMaximum(500)
        self.maxWidth.setProperty("value", 100)
        self.maxWidth.setObjectName(_fromUtf8("maxWidth"))
        self.maxHeight = QtGui.QSpinBox(Dialog)
        self.maxHeight.setGeometry(QtCore.QRect(285, 290, 60, 27))
        self.maxHeight.setMinimum(50)
        self.maxHeight.setMaximum(500)
        self.maxHeight.setProperty("value", 100)
        self.maxHeight.setObjectName(_fromUtf8("maxHeight"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(274, 295, 9, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.cancelButton = QtGui.QPushButton(Dialog)
        self.cancelButton.setEnabled(False)
        self.cancelButton.setGeometry(QtCore.QRect(405, 330, 98, 27))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Resize Images", None))
        self.label.setText(_translate("Dialog", "Folders containing images:", None))
        self.resizeButton.setText(_translate("Dialog", "Resize!", None))
        self.removeInputFolderButton.setText(_translate("Dialog", "Remove selected", None))
        self.addInputFolderButton.setText(_translate("Dialog", "Add...", None))
        self.chooseOutputFolderButton.setText(_translate("Dialog", "...", None))
        self.label_2.setText(_translate("Dialog", "Folder to save resized images into:", None))
        self.label_3.setText(_translate("Dialog", "Max size of resulting images:", None))
        self.label_4.setText(_translate("Dialog", "x", None))
        self.cancelButton.setText(_translate("Dialog", "Cancel", None))

