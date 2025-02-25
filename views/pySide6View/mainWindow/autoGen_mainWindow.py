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
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(9, 9, 1250, 702))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_jsonEdit = QFrame(self.layoutWidget)
        self.frame_jsonEdit.setObjectName(u"frame_jsonEdit")
        sizePolicy.setHeightForWidth(self.frame_jsonEdit.sizePolicy().hasHeightForWidth())
        self.frame_jsonEdit.setSizePolicy(sizePolicy)
        self.frame_jsonEdit.setMinimumSize(QSize(671, 361))
        self.frame_jsonEdit.setFrameShape(QFrame.StyledPanel)
        self.frame_jsonEdit.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame_jsonEdit, 1, 0, 1, 1)

        self.groupBox_terminalLike = QGroupBox(self.layoutWidget)
        self.groupBox_terminalLike.setObjectName(u"groupBox_terminalLike")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(10)
        sizePolicy1.setHeightForWidth(self.groupBox_terminalLike.sizePolicy().hasHeightForWidth())
        self.groupBox_terminalLike.setSizePolicy(sizePolicy1)
        self.groupBox_terminalLike.setMinimumSize(QSize(571, 700))

        self.gridLayout_2.addWidget(self.groupBox_terminalLike, 0, 1, 2, 1)

        self.AppTab = QTabWidget(self.layoutWidget)
        self.AppTab.setObjectName(u"AppTab")
        sizePolicy.setHeightForWidth(self.AppTab.sizePolicy().hasHeightForWidth())
        self.AppTab.setSizePolicy(sizePolicy)
        self.AppTab.setMinimumSize(QSize(671, 321))
        self.AppTab.setAutoFillBackground(True)
        self.DHC_Tab = QWidget()
        self.DHC_Tab.setObjectName(u"DHC_Tab")
        self.pushButton_pubMqttDhc = QPushButton(self.DHC_Tab)
        self.pushButton_pubMqttDhc.setObjectName(u"pushButton_pubMqttDhc")
        self.pushButton_pubMqttDhc.setGeometry(QRect(30, 240, 111, 31))
        self.layoutWidget1 = QWidget(self.DHC_Tab)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(30, 30, 621, 121))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_intervalUnit = QLabel(self.layoutWidget1)
        self.label_intervalUnit.setObjectName(u"label_intervalUnit")

        self.gridLayout.addWidget(self.label_intervalUnit, 0, 0, 1, 1)

        self.comboBox_intervalUnit = QComboBox(self.layoutWidget1)
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

        self.pushButton_setIntervalUnit = QPushButton(self.layoutWidget1)
        self.pushButton_setIntervalUnit.setObjectName(u"pushButton_setIntervalUnit")

        self.gridLayout.addWidget(self.pushButton_setIntervalUnit, 0, 3, 1, 1)

        self.label_IntervalValue = QLabel(self.layoutWidget1)
        self.label_IntervalValue.setObjectName(u"label_IntervalValue")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_IntervalValue.sizePolicy().hasHeightForWidth())
        self.label_IntervalValue.setSizePolicy(sizePolicy2)
        self.label_IntervalValue.setMinimumSize(QSize(97, 29))

        self.gridLayout.addWidget(self.label_IntervalValue, 1, 0, 1, 2)

        self.spinBox_IntervalValue = QSpinBox(self.layoutWidget1)
        self.spinBox_IntervalValue.setObjectName(u"spinBox_IntervalValue")
        self.spinBox_IntervalValue.setFont(font)

        self.gridLayout.addWidget(self.spinBox_IntervalValue, 1, 2, 1, 1)

        self.pushButton_setIntervalValue = QPushButton(self.layoutWidget1)
        self.pushButton_setIntervalValue.setObjectName(u"pushButton_setIntervalValue")

        self.gridLayout.addWidget(self.pushButton_setIntervalValue, 1, 3, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout)

        self.groupBox_consentState = QGroupBox(self.layoutWidget1)
        self.groupBox_consentState.setObjectName(u"groupBox_consentState")
        self.groupBox_consentState.setFont(font)
        self.layoutWidget2 = QWidget(self.groupBox_consentState)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 30, 143, 60))
        self.verticalLayout = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBox_allData = QCheckBox(self.layoutWidget2)
        self.checkBox_allData.setObjectName(u"checkBox_allData")
        self.checkBox_allData.setMinimumSize(QSize(131, 21))
        self.checkBox_allData.setFont(font)

        self.verticalLayout.addWidget(self.checkBox_allData)

        self.checkBox_locationData = QCheckBox(self.layoutWidget2)
        self.checkBox_locationData.setObjectName(u"checkBox_locationData")
        self.checkBox_locationData.setMinimumSize(QSize(141, 22))
        self.checkBox_locationData.setFont(font)

        self.verticalLayout.addWidget(self.checkBox_locationData)


        self.horizontalLayout_3.addWidget(self.groupBox_consentState)

        self.layoutWidget3 = QWidget(self.DHC_Tab)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(30, 180, 621, 30))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_dhcMqttTopic = QLabel(self.layoutWidget3)
        self.label_dhcMqttTopic.setObjectName(u"label_dhcMqttTopic")

        self.horizontalLayout_4.addWidget(self.label_dhcMqttTopic)

        self.lineEdit_vinToppicDhc = QLineEdit(self.layoutWidget3)
        self.lineEdit_vinToppicDhc.setObjectName(u"lineEdit_vinToppicDhc")

        self.horizontalLayout_4.addWidget(self.lineEdit_vinToppicDhc)

        self.comboBox_mqttTopicDhc = QComboBox(self.layoutWidget3)
        self.comboBox_mqttTopicDhc.addItem(icon, "")
        self.comboBox_mqttTopicDhc.addItem("")
        self.comboBox_mqttTopicDhc.setObjectName(u"comboBox_mqttTopicDhc")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.comboBox_mqttTopicDhc.sizePolicy().hasHeightForWidth())
        self.comboBox_mqttTopicDhc.setSizePolicy(sizePolicy3)
        self.comboBox_mqttTopicDhc.setMinimumSize(QSize(91, 0))
        self.comboBox_mqttTopicDhc.setFont(font)

        self.horizontalLayout_4.addWidget(self.comboBox_mqttTopicDhc)

        self.AppTab.addTab(self.DHC_Tab, "")
        self.VLS_Tab = QWidget()
        self.VLS_Tab.setObjectName(u"VLS_Tab")
        icon1 = QIcon(QIcon.fromTheme(u"address-book-new"))
        self.AppTab.addTab(self.VLS_Tab, icon1, "")
        self.MQTT_Tab = QWidget()
        self.MQTT_Tab.setObjectName(u"MQTT_Tab")
        self.AppTab.addTab(self.MQTT_Tab, "")
        self.Config_Tab = QWidget()
        self.Config_Tab.setObjectName(u"Config_Tab")
        self.checkBox_dhc = QCheckBox(self.Config_Tab)
        self.checkBox_dhc.setObjectName(u"checkBox_dhc")
        self.checkBox_dhc.setGeometry(QRect(40, 40, 77, 22))
        self.checkBox_vls = QCheckBox(self.Config_Tab)
        self.checkBox_vls.setObjectName(u"checkBox_vls")
        self.checkBox_vls.setGeometry(QRect(40, 80, 77, 22))
        self.checkBox_rsn = QCheckBox(self.Config_Tab)
        self.checkBox_rsn.setObjectName(u"checkBox_rsn")
        self.checkBox_rsn.setGeometry(QRect(40, 120, 77, 22))
        self.checkBox_sos = QCheckBox(self.Config_Tab)
        self.checkBox_sos.setObjectName(u"checkBox_sos")
        self.checkBox_sos.setGeometry(QRect(40, 160, 77, 22))
        self.checkBox_acn = QCheckBox(self.Config_Tab)
        self.checkBox_acn.setObjectName(u"checkBox_acn")
        self.checkBox_acn.setGeometry(QRect(40, 190, 77, 22))
        self.lineEdit_didFlag = QLineEdit(self.Config_Tab)
        self.lineEdit_didFlag.setObjectName(u"lineEdit_didFlag")
        self.lineEdit_didFlag.setGeometry(QRect(90, 230, 113, 24))
        self.label_did = QLabel(self.Config_Tab)
        self.label_did.setObjectName(u"label_did")
        self.label_did.setGeometry(QRect(30, 230, 49, 16))
        self.pushButton_setVin = QPushButton(self.Config_Tab)
        self.pushButton_setVin.setObjectName(u"pushButton_setVin")
        self.pushButton_setVin.setGeometry(QRect(290, 60, 80, 31))
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_setVin.sizePolicy().hasHeightForWidth())
        self.pushButton_setVin.setSizePolicy(sizePolicy4)
        self.pushButton_getVin = QPushButton(self.Config_Tab)
        self.pushButton_getVin.setObjectName(u"pushButton_getVin")
        self.pushButton_getVin.setGeometry(QRect(290, 110, 80, 31))
        sizePolicy4.setHeightForWidth(self.pushButton_getVin.sizePolicy().hasHeightForWidth())
        self.pushButton_getVin.setSizePolicy(sizePolicy4)
        self.frame = QFrame(self.Config_Tab)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(400, 110, 181, 31))
        sizePolicy4.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy4)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_getVin = QLabel(self.frame)
        self.label_getVin.setObjectName(u"label_getVin")
        self.label_getVin.setGeometry(QRect(0, 0, 181, 31))
        self.label_getVin.setMidLineWidth(1)
        self.label_getVin.setMargin(1)
        self.lineEdit_setVin = QLineEdit(self.Config_Tab)
        self.lineEdit_setVin.setObjectName(u"lineEdit_setVin")
        self.lineEdit_setVin.setGeometry(QRect(390, 60, 181, 31))
        sizePolicy4.setHeightForWidth(self.lineEdit_setVin.sizePolicy().hasHeightForWidth())
        self.lineEdit_setVin.setSizePolicy(sizePolicy4)
        self.AppTab.addTab(self.Config_Tab, "")

        self.gridLayout_2.addWidget(self.AppTab, 0, 0, 1, 1)

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

        self.AppTab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow_autoGen_T", u"MainWindow", None))
        self.actionChangeVin.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"ChangeVin", None))
        self.actionSetFlag.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"SetFlag", None))
        self.actionTheme.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"Theme", None))
        self.actionAnhTh49.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"AnhTh49", None))
        self.groupBox_terminalLike.setTitle(QCoreApplication.translate("MainWindow_autoGen_T", u"Your memory saverious", None))
        self.pushButton_pubMqttDhc.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"TSP pub", None))
        self.label_intervalUnit.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Interval Unit</span></p></body></html>", None))
        self.comboBox_intervalUnit.setItemText(0, QCoreApplication.translate("MainWindow_autoGen_T", u"Days", None))
        self.comboBox_intervalUnit.setItemText(1, QCoreApplication.translate("MainWindow_autoGen_T", u"Minutes", None))

        self.comboBox_intervalUnit.setPlaceholderText("")
        self.pushButton_setIntervalUnit.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"Set", None))
        self.label_IntervalValue.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Interval Value</span></p></body></html>", None))
        self.pushButton_setIntervalValue.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"Set", None))
        self.groupBox_consentState.setTitle(QCoreApplication.translate("MainWindow_autoGen_T", u"Consent State", None))
        self.checkBox_allData.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"AllData", None))
        self.checkBox_locationData.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"LocationData", None))
        self.label_dhcMqttTopic.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">MQTT Topic</span></p></body></html>", None))
        self.comboBox_mqttTopicDhc.setItemText(0, QCoreApplication.translate("MainWindow_autoGen_T", u"MQTT/DHC", None))
        self.comboBox_mqttTopicDhc.setItemText(1, QCoreApplication.translate("MainWindow_autoGen_T", u"MQTT/DHC/result", None))

        self.comboBox_mqttTopicDhc.setPlaceholderText("")
        self.AppTab.setTabText(self.AppTab.indexOf(self.DHC_Tab), QCoreApplication.translate("MainWindow_autoGen_T", u"DHC", None))
        self.AppTab.setTabText(self.AppTab.indexOf(self.VLS_Tab), QCoreApplication.translate("MainWindow_autoGen_T", u"VLS", None))
        self.AppTab.setTabText(self.AppTab.indexOf(self.MQTT_Tab), QCoreApplication.translate("MainWindow_autoGen_T", u"MQTT", None))
        self.checkBox_dhc.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"DHC", None))
        self.checkBox_vls.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"VLS", None))
        self.checkBox_rsn.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"RSN", None))
        self.checkBox_sos.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"SOS", None))
        self.checkBox_acn.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"ACN", None))
        self.label_did.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"DID FLag", None))
        self.pushButton_setVin.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"Set Vin", None))
        self.pushButton_getVin.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"Get Vin", None))
        self.label_getVin.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"DID FLag", None))
        self.AppTab.setTabText(self.AppTab.indexOf(self.Config_Tab), QCoreApplication.translate("MainWindow_autoGen_T", u"Config", None))
        self.menuLazyApp.setTitle(QCoreApplication.translate("MainWindow_autoGen_T", u"LazyApp", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow_autoGen_T", u"Edit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow_autoGen_T", u"Help", None))
    # retranslateUi

