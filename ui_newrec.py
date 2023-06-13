# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'megacrud_ui0_newrec.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import res

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(509, 251)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(50, 50, 50, 255), stop:0.427447 rgba(105, 105, 105, 235), stop:1 rgba(128, 128, 128, 255));")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"backgrounf-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_newrec = QLabel(self.frame)
        self.label_newrec.setObjectName(u"label_newrec")
        self.label_newrec.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.label_newrec.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_newrec)

        self.le_fname = QLineEdit(self.frame)
        self.le_fname.setObjectName(u"le_fname")
        self.le_fname.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")

        self.verticalLayout.addWidget(self.le_fname)

        self.le_sname = QLineEdit(self.frame)
        self.le_sname.setObjectName(u"le_sname")
        self.le_sname.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")

        self.verticalLayout.addWidget(self.le_sname)

        self.le_pnumber = QLineEdit(self.frame)
        self.le_pnumber.setObjectName(u"le_pnumber")
        self.le_pnumber.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")

        self.verticalLayout.addWidget(self.le_pnumber)

        self.btn_saverec = QPushButton(self.frame)
        self.btn_saverec.setObjectName(u"btn_saverec")
        self.btn_saverec.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"font: 18pt \"Segoe UI\";\n"
"qproperty-iconSize: 24px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255,255,40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255,255,70);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/icons/post_add_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_saverec.setIcon(icon)

        self.verticalLayout.addWidget(self.btn_saverec)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_newrec.setText(QCoreApplication.translate("Dialog", u"New record", None))
        self.le_fname.setPlaceholderText(QCoreApplication.translate("Dialog", u"First Name", None))
        self.le_sname.setPlaceholderText(QCoreApplication.translate("Dialog", u"Second Name", None))
        self.le_pnumber.setPlaceholderText(QCoreApplication.translate("Dialog", u"Phone number", None))
        self.btn_saverec.setText(QCoreApplication.translate("Dialog", u"Save record", None))
    # retranslateUi

