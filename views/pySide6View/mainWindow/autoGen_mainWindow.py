# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QTabWidget,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionChangeVin = QAction(MainWindow)
        self.actionChangeVin.setObjectName(u"actionChangeVin")
        self.actionSetFlag = QAction(MainWindow)
        self.actionSetFlag.setObjectName(u"actionSetFlag")
        self.actionTheme = QAction(MainWindow)
        self.actionTheme.setObjectName(u"actionTheme")
        self.actionAnhTh49 = QAction(MainWindow)
        self.actionAnhTh49.setObjectName(u"actionAnhTh49")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.AppTab = QTabWidget(self.centralwidget)
        self.AppTab.setObjectName(u"AppTab")
        self.AppTab.setAutoFillBackground(True)
        self.DHC_Tab = QWidget()
        self.DHC_Tab.setObjectName(u"DHC_Tab")
        self.AppTab.addTab(self.DHC_Tab, "")
        self.VLS_Tab = QWidget()
        self.VLS_Tab.setObjectName(u"VLS_Tab")
        icon = QIcon(QIcon.fromTheme(u"address-book-new"))
        self.AppTab.addTab(self.VLS_Tab, icon, "")
        self.MQTT_Tab = QWidget()
        self.MQTT_Tab.setObjectName(u"MQTT_Tab")
        self.AppTab.addTab(self.MQTT_Tab, "")

        self.horizontalLayout.addWidget(self.AppTab)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuLazyApp = QMenu(self.menubar)
        self.menuLazyApp.setObjectName(u"menuLazyApp")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuLazyApp.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuLazyApp.addAction(self.actionChangeVin)
        self.menuLazyApp.addAction(self.actionSetFlag)
        self.menuEdit.addAction(self.actionTheme)
        self.menuHelp.addAction(self.actionAnhTh49)

        self.retranslateUi(MainWindow)

        self.AppTab.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionChangeVin.setText(QCoreApplication.translate("MainWindow", u"ChangeVin", None))
        self.actionSetFlag.setText(QCoreApplication.translate("MainWindow", u"SetFlag", None))
        self.actionTheme.setText(QCoreApplication.translate("MainWindow", u"Theme", None))
        self.actionAnhTh49.setText(QCoreApplication.translate("MainWindow", u"AnhTh49", None))
        self.AppTab.setTabText(self.AppTab.indexOf(self.DHC_Tab), QCoreApplication.translate("MainWindow", u"DHC", None))
        self.AppTab.setTabText(self.AppTab.indexOf(self.VLS_Tab), QCoreApplication.translate("MainWindow", u"VLS", None))
        self.AppTab.setTabText(self.AppTab.indexOf(self.MQTT_Tab), QCoreApplication.translate("MainWindow", u"MQTT", None))
        self.menuLazyApp.setTitle(QCoreApplication.translate("MainWindow", u"LazyApp", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

