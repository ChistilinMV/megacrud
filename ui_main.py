# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'megacrud_ui0.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QMainWindow,
    QPushButton, QSizePolicy, QTableView, QVBoxLayout,
    QWidget)
import res

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(699, 562)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(50, 50, 50, 255), stop:0.427447 rgba(105, 105, 105, 235), stop:1 rgba(128, 128, 128, 255));\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(11, 2, 679, 551))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_newrec = QPushButton(self.widget)
        self.btn_newrec.setObjectName(u"btn_newrec")
        self.btn_newrec.setMinimumSize(QSize(221, 81))
        self.btn_newrec.setStyleSheet(u"QPushButton {\n"
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
        self.btn_newrec.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_newrec)

        self.btn_editrec = QPushButton(self.widget)
        self.btn_editrec.setObjectName(u"btn_editrec")
        self.btn_editrec.setMinimumSize(QSize(221, 81))
        self.btn_editrec.setStyleSheet(u"QPushButton {\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/edit_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_editrec.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btn_editrec)

        self.btn_delrec = QPushButton(self.widget)
        self.btn_delrec.setObjectName(u"btn_delrec")
        self.btn_delrec.setMinimumSize(QSize(221, 81))
        self.btn_delrec.setStyleSheet(u"QPushButton {\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/delete_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delrec.setIcon(icon2)

        self.horizontalLayout.addWidget(self.btn_delrec)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableView = QTableView(self.widget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setMinimumSize(QSize(677, 460))
        self.tableView.setStyleSheet(u"QTableView {\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"}\n"
"QtableView::section {\n"
"background-color: rgba(53, 53, 53);\n"
"color: white;\n"
"border:none;\n"
"heigh: 50px;\n"
"font-size: 14pt;\n"
"}\n"
"QTableView::item {\n"
"border-style: none;\n"
"border-bottom: rgba(255, 255, 255, 50);\n"
"}\n"
"QTableView::item:select {\n"
"border: none;\n"
"color: rgba(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 50);\n"
"}")
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setShowGrid(False)
        self.tableView.horizontalHeader().setDefaultSectionSize(135)

        self.verticalLayout.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MegaCRUD", None))
        self.btn_newrec.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.btn_editrec.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.btn_delrec.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
    # retranslateUi

