# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vls.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_vls_autoGen_T(object):
    def setupUi(self, vls):
        if not vls.objectName():
            vls.setObjectName(u"vls")
        vls.resize(685, 218)
        icon = QIcon(QIcon.fromTheme(u"audio-input-microphone"))
        vls.setWindowIcon(icon)
        self.gridLayout = QGridLayout(vls)
        self.gridLayout.setObjectName(u"gridLayout")
        self.vlsWidget = QTabWidget(vls)
        self.vlsWidget.setObjectName(u"vlsWidget")
        self.main_vls = QWidget()
        self.main_vls.setObjectName(u"main_vls")
        self.gridLayout_4 = QGridLayout(self.main_vls)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox_3 = QGroupBox(self.main_vls)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(327, 92))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.comboBox_vlsPriority = QComboBox(self.groupBox_3)
        self.comboBox_vlsPriority.addItem("")
        self.comboBox_vlsPriority.addItem("")
        self.comboBox_vlsPriority.setObjectName(u"comboBox_vlsPriority")

        self.verticalLayout_4.addWidget(self.comboBox_vlsPriority)


        self.gridLayout_4.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_vlsVinMqttTopic = QLabel(self.main_vls)
        self.label_vlsVinMqttTopic.setObjectName(u"label_vlsVinMqttTopic")

        self.horizontalLayout_6.addWidget(self.label_vlsVinMqttTopic)

        self.lineEdit_vlsVin = QLineEdit(self.main_vls)
        self.lineEdit_vlsVin.setObjectName(u"lineEdit_vlsVin")

        self.horizontalLayout_6.addWidget(self.lineEdit_vlsVin)

        self.comboBox_vlsMqttToppic = QComboBox(self.main_vls)
        self.comboBox_vlsMqttToppic.addItem("")
        self.comboBox_vlsMqttToppic.addItem("")
        self.comboBox_vlsMqttToppic.addItem("")
        self.comboBox_vlsMqttToppic.addItem("")
        self.comboBox_vlsMqttToppic.setObjectName(u"comboBox_vlsMqttToppic")

        self.horizontalLayout_6.addWidget(self.comboBox_vlsMqttToppic)


        self.gridLayout_4.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.main_vls)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.formLayout_3 = QFormLayout(self.groupBox_4)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_vlsIntervalUnit = QLabel(self.groupBox_4)
        self.label_vlsIntervalUnit.setObjectName(u"label_vlsIntervalUnit")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_vlsIntervalUnit)

        self.comboBox_vlsIntervalUnit = QComboBox(self.groupBox_4)
        self.comboBox_vlsIntervalUnit.addItem("")
        self.comboBox_vlsIntervalUnit.addItem("")
        self.comboBox_vlsIntervalUnit.setObjectName(u"comboBox_vlsIntervalUnit")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.comboBox_vlsIntervalUnit)

        self.pushButton_vlsSetIntervalUnit = QPushButton(self.groupBox_4)
        self.pushButton_vlsSetIntervalUnit.setObjectName(u"pushButton_vlsSetIntervalUnit")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.pushButton_vlsSetIntervalUnit)

        self.label_vlsIntervalValue = QLabel(self.groupBox_4)
        self.label_vlsIntervalValue.setObjectName(u"label_vlsIntervalValue")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_vlsIntervalValue)

        self.spinBox_vlsValue = QSpinBox(self.groupBox_4)
        self.spinBox_vlsValue.setObjectName(u"spinBox_vlsValue")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_vlsValue.sizePolicy().hasHeightForWidth())
        self.spinBox_vlsValue.setSizePolicy(sizePolicy)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.spinBox_vlsValue)

        self.pushButton_vlsSetIntervalValue = QPushButton(self.groupBox_4)
        self.pushButton_vlsSetIntervalValue.setObjectName(u"pushButton_vlsSetIntervalValue")

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.pushButton_vlsSetIntervalValue)


        self.gridLayout_4.addWidget(self.groupBox_4, 0, 1, 2, 1)

        self.vlsWidget.addTab(self.main_vls, "")
        self.JsonPayload_vls = QWidget()
        self.JsonPayload_vls.setObjectName(u"JsonPayload_vls")
        self.vlsWidget.addTab(self.JsonPayload_vls, "")

        self.gridLayout.addWidget(self.vlsWidget, 0, 0, 1, 1)


        self.retranslateUi(vls)

        self.vlsWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(vls)
    # setupUi

    def retranslateUi(self, vls):
        vls.setWindowTitle(QCoreApplication.translate("vls_autoGen_T", u"Form", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("vls_autoGen_T", u"Priority", None))
        self.comboBox_vlsPriority.setItemText(0, QCoreApplication.translate("vls_autoGen_T", u"EMERGENCY", None))
        self.comboBox_vlsPriority.setItemText(1, QCoreApplication.translate("vls_autoGen_T", u"NON_EMERGENCY", None))

        self.label_vlsVinMqttTopic.setText(QCoreApplication.translate("vls_autoGen_T", u"MQTT topic", None))
        self.comboBox_vlsMqttToppic.setItemText(0, QCoreApplication.translate("vls_autoGen_T", u"abc/app/Vls", None))
        self.comboBox_vlsMqttToppic.setItemText(1, QCoreApplication.translate("vls_autoGen_T", u"app/vls/voice", None))
        self.comboBox_vlsMqttToppic.setItemText(2, QCoreApplication.translate("vls_autoGen_T", u"app/vls/stop", None))
        self.comboBox_vlsMqttToppic.setItemText(3, QCoreApplication.translate("vls_autoGen_T", u"abc/app/DHC/result", None))

        self.groupBox_4.setTitle(QCoreApplication.translate("vls_autoGen_T", u"Interval", None))
        self.label_vlsIntervalUnit.setText(QCoreApplication.translate("vls_autoGen_T", u"Unit", None))
        self.comboBox_vlsIntervalUnit.setItemText(0, QCoreApplication.translate("vls_autoGen_T", u"Days", None))
        self.comboBox_vlsIntervalUnit.setItemText(1, QCoreApplication.translate("vls_autoGen_T", u"Minnus", None))

        self.pushButton_vlsSetIntervalUnit.setText(QCoreApplication.translate("vls_autoGen_T", u"Set", None))
        self.label_vlsIntervalValue.setText(QCoreApplication.translate("vls_autoGen_T", u"Value", None))
        self.pushButton_vlsSetIntervalValue.setText(QCoreApplication.translate("vls_autoGen_T", u"Set", None))
        self.vlsWidget.setTabText(self.vlsWidget.indexOf(self.main_vls), QCoreApplication.translate("vls_autoGen_T", u"Main", None))
        self.vlsWidget.setTabText(self.vlsWidget.indexOf(self.JsonPayload_vls), QCoreApplication.translate("vls_autoGen_T", u"jsonPayload", None))
    # retranslateUi

