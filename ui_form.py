# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(691, 331)
        Widget.setMinimumSize(QSize(691, 331))
        Widget.setMaximumSize(QSize(691, 331))
        font = QFont()
        font.setPointSize(14)
        Widget.setFont(font)
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 30, 341, 71))
        self.label.setPixmap(QPixmap(u"Bild/logo_edgewave.jpg"))
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(220, 110, 241, 41))
        self.edit_username = QLineEdit(Widget)
        self.edit_username.setObjectName(u"edit_username")
        self.edit_username.setGeometry(QRect(280, 160, 113, 28))
        font1 = QFont()
        font1.setPointSize(10)
        self.edit_username.setFont(font1)
        self.edit_password = QLineEdit(Widget)
        self.edit_password.setObjectName(u"edit_password")
        self.edit_password.setGeometry(QRect(280, 210, 113, 28))
        self.edit_password.setFont(font1)
        self.loginButton = QPushButton(Widget)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(300, 250, 83, 29))
        self.loginButton.setFont(font1)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"login", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Widget", u"Data Processing Tool", None))
        self.edit_username.setPlaceholderText(QCoreApplication.translate("Widget", u"Username", None))
        self.edit_password.setPlaceholderText(QCoreApplication.translate("Widget", u"Passwort", None))
        self.loginButton.setText(QCoreApplication.translate("Widget", u"login", None))
    # retranslateUi

