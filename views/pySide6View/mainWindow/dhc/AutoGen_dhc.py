# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dhc.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_dhcWidget_autoGen_T(object):
    def setupUi(self, dhcWidget):
        if not dhcWidget.objectName():
            dhcWidget.setObjectName(u"dhcWidget")
        dhcWidget.resize(480, 263)
        self.gridLayout = QGridLayout(dhcWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(dhcWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.main = QWidget()
        self.main.setObjectName(u"main")
        self.gridLayout_3 = QGridLayout(self.main)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(self.main)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(327, 92))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox_dhcAllData = QCheckBox(self.groupBox)
        self.checkBox_dhcAllData.setObjectName(u"checkBox_dhcAllData")

        self.verticalLayout_3.addWidget(self.checkBox_dhcAllData)

        self.checkBox_dhclocationData = QCheckBox(self.groupBox)
        self.checkBox_dhclocationData.setObjectName(u"checkBox_dhclocationData")

        self.verticalLayout_3.addWidget(self.checkBox_dhclocationData)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_dhcMqttTopic = QLabel(self.main)
        self.label_dhcMqttTopic.setObjectName(u"label_dhcMqttTopic")

        self.horizontalLayout_5.addWidget(self.label_dhcMqttTopic)

        self.lineEdit_dhcVin = QLineEdit(self.main)
        self.lineEdit_dhcVin.setObjectName(u"lineEdit_dhcVin")

        self.horizontalLayout_5.addWidget(self.lineEdit_dhcVin)

        self.comboBox_dhcMqttTopic = QComboBox(self.main)
        self.comboBox_dhcMqttTopic.addItem("")
        self.comboBox_dhcMqttTopic.addItem("")
        self.comboBox_dhcMqttTopic.setObjectName(u"comboBox_dhcMqttTopic")

        self.horizontalLayout_5.addWidget(self.comboBox_dhcMqttTopic)


        self.gridLayout_3.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.main)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_dhcIntervalUnit = QLabel(self.groupBox_2)
        self.label_dhcIntervalUnit.setObjectName(u"label_dhcIntervalUnit")

        self.gridLayout_2.addWidget(self.label_dhcIntervalUnit, 0, 0, 1, 1)

        self.comboBox_dhcIntervalUnit = QComboBox(self.groupBox_2)
        self.comboBox_dhcIntervalUnit.addItem("")
        self.comboBox_dhcIntervalUnit.addItem("")
        self.comboBox_dhcIntervalUnit.setObjectName(u"comboBox_dhcIntervalUnit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_dhcIntervalUnit.sizePolicy().hasHeightForWidth())
        self.comboBox_dhcIntervalUnit.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.comboBox_dhcIntervalUnit, 0, 1, 1, 1)

        self.pushButton_dhcSetIntervalUnit = QPushButton(self.groupBox_2)
        self.pushButton_dhcSetIntervalUnit.setObjectName(u"pushButton_dhcSetIntervalUnit")

        self.gridLayout_2.addWidget(self.pushButton_dhcSetIntervalUnit, 1, 1, 1, 1)

        self.label_dhcIntervalValue = QLabel(self.groupBox_2)
        self.label_dhcIntervalValue.setObjectName(u"label_dhcIntervalValue")

        self.gridLayout_2.addWidget(self.label_dhcIntervalValue, 2, 0, 1, 1)

        self.spinBox_dhcIntervalValue = QSpinBox(self.groupBox_2)
        self.spinBox_dhcIntervalValue.setObjectName(u"spinBox_dhcIntervalValue")
        sizePolicy.setHeightForWidth(self.spinBox_dhcIntervalValue.sizePolicy().hasHeightForWidth())
        self.spinBox_dhcIntervalValue.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.spinBox_dhcIntervalValue, 2, 1, 1, 1)

        self.pushButton_dhcSetIntervalValue = QPushButton(self.groupBox_2)
        self.pushButton_dhcSetIntervalValue.setObjectName(u"pushButton_dhcSetIntervalValue")

        self.gridLayout_2.addWidget(self.pushButton_dhcSetIntervalValue, 3, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 0, 1, 2, 1)

        self.tabWidget.addTab(self.main, "")
        self.JsonPayload = QWidget()
        self.JsonPayload.setObjectName(u"JsonPayload")
        self.tabWidget.addTab(self.JsonPayload, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(dhcWidget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(dhcWidget)
    # setupUi

    def retranslateUi(self, dhcWidget):
        dhcWidget.setWindowTitle(QCoreApplication.translate("dhcWidget_autoGen_T", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("dhcWidget_autoGen_T", u"Consent State", None))
        self.checkBox_dhcAllData.setText(QCoreApplication.translate("dhcWidget_autoGen_T", u"AllData", None))
        self.checkBox_dhclocationData.setText(QCoreApplication.translate("dhcWidget_autoGen_T", u"LocationData", None))
        self.label_dhcMqttTopic.setText(QCoreApplication.translate("dhcWidget_autoGen_T", u"MQTT topic", None))
        self.comboBox_dhcMqttTopic.setItemText(0, QCoreApplication.translate("dhcWidget_autoGen_T", u"abc/app/DHC", None))
        self.comboBox_dhcMqttTopic.setItemText(1, QCoreApplication.translate("dhcWidget_autoGen_T", u"abc/app/DHC/result", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("dhcWidget_autoGen_T", u"Interval", None))
        self.label_dhcIntervalUnit.setText(QCoreApplication.translate("dhcWidget_autoGen_T", u"Unit", None))
        self.comboBox_dhcIntervalUnit.setItemText(0, QCoreApplication.translate("dhcWidget_autoGen_T", u"Days", None))
        self.comboBox_dhcIntervalUnit.setItemText(1, QCoreApplication.translate("dhcWidget_autoGen_T", u"Minnus", None))

        self.pushButton_dhcSetIntervalUnit.setText(QCoreApplication.translate("dhcWidget_autoGen_T", u"Set", None))
        self.label_dhcIntervalValue.setText(QCoreApplication.translate("dhcWidget_autoGen_T", u"Value", None))
        self.pushButton_dhcSetIntervalValue.setText(QCoreApplication.translate("dhcWidget_autoGen_T", u"Set", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main), QCoreApplication.translate("dhcWidget_autoGen_T", u"Main", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.JsonPayload), QCoreApplication.translate("dhcWidget_autoGen_T", u"jsonPayload", None))
    # retranslateUi

