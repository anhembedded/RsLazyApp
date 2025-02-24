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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow_autoGen_T(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1291, 770)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1291, 770))
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
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(9, 9, 1250, 702))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_jsonEdit = QFrame(self.widget)
        self.frame_jsonEdit.setObjectName(u"frame_jsonEdit")
        sizePolicy.setHeightForWidth(self.frame_jsonEdit.sizePolicy().hasHeightForWidth())
        self.frame_jsonEdit.setSizePolicy(sizePolicy)
        self.frame_jsonEdit.setMinimumSize(QSize(671, 361))
        self.frame_jsonEdit.setFrameShape(QFrame.StyledPanel)
        self.frame_jsonEdit.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame_jsonEdit, 1, 0, 1, 1)

        self.AppTab = QTabWidget(self.widget)
        self.AppTab.setObjectName(u"AppTab")
        sizePolicy.setHeightForWidth(self.AppTab.sizePolicy().hasHeightForWidth())
        self.AppTab.setSizePolicy(sizePolicy)
        self.AppTab.setMinimumSize(QSize(671, 321))
        self.AppTab.setAutoFillBackground(True)
        self.DHC_Tab = QWidget()
        self.DHC_Tab.setObjectName(u"DHC_Tab")
        self.pushButton = QPushButton(self.DHC_Tab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 240, 111, 31))
        self.layoutWidget = QWidget(self.DHC_Tab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 30, 621, 121))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_intervalUnit = QLabel(self.layoutWidget)
        self.label_intervalUnit.setObjectName(u"label_intervalUnit")

        self.gridLayout.addWidget(self.label_intervalUnit, 0, 0, 1, 1)

        self.comboBox_intervalUnit = QComboBox(self.layoutWidget)
        icon = QIcon(QIcon.fromTheme(u"applications-utilities"))
        self.comboBox_intervalUnit.addItem(icon, "")
        self.comboBox_intervalUnit.addItem("")
        self.comboBox_intervalUnit.setObjectName(u"comboBox_intervalUnit")
        self.comboBox_intervalUnit.setMinimumSize(QSize(91, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.comboBox_intervalUnit.setFont(font)

        self.gridLayout.addWidget(self.comboBox_intervalUnit, 0, 1, 1, 2)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 0, 3, 1, 1)

        self.label_IntervalValue = QLabel(self.layoutWidget)
        self.label_IntervalValue.setObjectName(u"label_IntervalValue")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_IntervalValue.sizePolicy().hasHeightForWidth())
        self.label_IntervalValue.setSizePolicy(sizePolicy1)
        self.label_IntervalValue.setMinimumSize(QSize(97, 29))

        self.gridLayout.addWidget(self.label_IntervalValue, 1, 0, 1, 2)

        self.spinBox_IntervalValue = QSpinBox(self.layoutWidget)
        self.spinBox_IntervalValue.setObjectName(u"spinBox_IntervalValue")
        self.spinBox_IntervalValue.setFont(font)

        self.gridLayout.addWidget(self.spinBox_IntervalValue, 1, 2, 1, 1)

        self.pushButton_3 = QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 1, 3, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout)

        self.groupBox = QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font)
        self.layoutWidget1 = QWidget(self.groupBox)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 30, 143, 60))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.layoutWidget1)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(131, 21))
        self.checkBox.setFont(font)

        self.verticalLayout.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.layoutWidget1)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setMinimumSize(QSize(141, 22))
        self.checkBox_2.setFont(font)

        self.verticalLayout.addWidget(self.checkBox_2)


        self.horizontalLayout_3.addWidget(self.groupBox)

        self.layoutWidget2 = QWidget(self.DHC_Tab)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(30, 180, 621, 30))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_IntervalValue_3 = QLabel(self.layoutWidget2)
        self.label_IntervalValue_3.setObjectName(u"label_IntervalValue_3")

        self.horizontalLayout_4.addWidget(self.label_IntervalValue_3)

        self.lineEdit = QLineEdit(self.layoutWidget2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_4.addWidget(self.lineEdit)

        self.comboBox_intervalUnit_2 = QComboBox(self.layoutWidget2)
        self.comboBox_intervalUnit_2.addItem(icon, "")
        self.comboBox_intervalUnit_2.addItem("")
        self.comboBox_intervalUnit_2.setObjectName(u"comboBox_intervalUnit_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox_intervalUnit_2.sizePolicy().hasHeightForWidth())
        self.comboBox_intervalUnit_2.setSizePolicy(sizePolicy2)
        self.comboBox_intervalUnit_2.setMinimumSize(QSize(91, 0))
        self.comboBox_intervalUnit_2.setFont(font)

        self.horizontalLayout_4.addWidget(self.comboBox_intervalUnit_2)

        self.AppTab.addTab(self.DHC_Tab, "")
        self.VLS_Tab = QWidget()
        self.VLS_Tab.setObjectName(u"VLS_Tab")
        icon1 = QIcon(QIcon.fromTheme(u"address-book-new"))
        self.AppTab.addTab(self.VLS_Tab, icon1, "")
        self.MQTT_Tab = QWidget()
        self.MQTT_Tab.setObjectName(u"MQTT_Tab")
        self.AppTab.addTab(self.MQTT_Tab, "")

        self.gridLayout_2.addWidget(self.AppTab, 0, 0, 1, 1)

        self.groupBox_terminalLike = QGroupBox(self.widget)
        self.groupBox_terminalLike.setObjectName(u"groupBox_terminalLike")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(10)
        sizePolicy3.setHeightForWidth(self.groupBox_terminalLike.sizePolicy().hasHeightForWidth())
        self.groupBox_terminalLike.setSizePolicy(sizePolicy3)
        self.groupBox_terminalLike.setMinimumSize(QSize(571, 700))

        self.gridLayout_2.addWidget(self.groupBox_terminalLike, 0, 1, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1291, 21))
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow_autoGen_T", u"MainWindow", None))
        self.actionChangeVin.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"ChangeVin", None))
        self.actionSetFlag.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"SetFlag", None))
        self.actionTheme.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"Theme", None))
        self.actionAnhTh49.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"AnhTh49", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"TSP pub", None))
        self.label_intervalUnit.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Interval Unit</span></p></body></html>", None))
        self.comboBox_intervalUnit.setItemText(0, QCoreApplication.translate("MainWindow_autoGen_T", u"Days", None))
        self.comboBox_intervalUnit.setItemText(1, QCoreApplication.translate("MainWindow_autoGen_T", u"Minutes", None))

        self.comboBox_intervalUnit.setPlaceholderText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"Set", None))
        self.label_IntervalValue.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Interval Value</span></p></body></html>", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"Set", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow_autoGen_T", u"Consent State", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"AllData", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"LocationData", None))
        self.label_IntervalValue_3.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">MQTT Topic</span></p></body></html>", None))
        self.comboBox_intervalUnit_2.setItemText(0, QCoreApplication.translate("MainWindow_autoGen_T", u"MQTT/DHC", None))
        self.comboBox_intervalUnit_2.setItemText(1, QCoreApplication.translate("MainWindow_autoGen_T", u"MQTT/DHC/result", None))

        self.comboBox_intervalUnit_2.setPlaceholderText("")
        self.AppTab.setTabText(self.AppTab.indexOf(self.DHC_Tab), QCoreApplication.translate("MainWindow_autoGen_T", u"DHC", None))
        self.AppTab.setTabText(self.AppTab.indexOf(self.VLS_Tab), QCoreApplication.translate("MainWindow_autoGen_T", u"VLS", None))
        self.AppTab.setTabText(self.AppTab.indexOf(self.MQTT_Tab), QCoreApplication.translate("MainWindow_autoGen_T", u"MQTT", None))
        self.groupBox_terminalLike.setTitle(QCoreApplication.translate("MainWindow_autoGen_T", u"Your memory saverious", None))
        self.menuLazyApp.setTitle(QCoreApplication.translate("MainWindow_autoGen_T", u"LazyApp", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow_autoGen_T", u"Edit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow_autoGen_T", u"Help", None))
    # retranslateUi

