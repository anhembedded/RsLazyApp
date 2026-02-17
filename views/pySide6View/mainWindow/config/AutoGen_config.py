# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_configWidget_autoGen_T(object):
    def setupUi(self, configWidget):
        if not configWidget.objectName():
            configWidget.setObjectName(u"configWidget")
        configWidget.resize(829, 277)
        self.horizontalLayout = QHBoxLayout(configWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_5 = QGroupBox(configWidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout = QVBoxLayout(self.groupBox_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox_flagDhc = QCheckBox(self.groupBox_5)
        self.checkBox_flagDhc.setObjectName(u"checkBox_flagDhc")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.checkBox_flagDhc.setFont(font)

        self.verticalLayout.addWidget(self.checkBox_flagDhc)

        self.checkBox_flagAcn = QCheckBox(self.groupBox_5)
        self.checkBox_flagAcn.setObjectName(u"checkBox_flagAcn")
        self.checkBox_flagAcn.setFont(font)

        self.verticalLayout.addWidget(self.checkBox_flagAcn)

        self.checkBox_flagRsn = QCheckBox(self.groupBox_5)
        self.checkBox_flagRsn.setObjectName(u"checkBox_flagRsn")
        self.checkBox_flagRsn.setFont(font)

        self.verticalLayout.addWidget(self.checkBox_flagRsn)

        self.checkBox_flagVls = QCheckBox(self.groupBox_5)
        self.checkBox_flagVls.setObjectName(u"checkBox_flagVls")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_flagVls.sizePolicy().hasHeightForWidth())
        self.checkBox_flagVls.setSizePolicy(sizePolicy)
        self.checkBox_flagVls.setFont(font)

        self.verticalLayout.addWidget(self.checkBox_flagVls)

        self.checkBox_flagSos = QCheckBox(self.groupBox_5)
        self.checkBox_flagSos.setObjectName(u"checkBox_flagSos")
        self.checkBox_flagSos.setFont(font)
        icon = QIcon(QIcon.fromTheme(u"dialog-warning"))
        self.checkBox_flagSos.setIcon(icon)

        self.verticalLayout.addWidget(self.checkBox_flagSos)

        self.checkBox = QCheckBox(self.groupBox_5)
        self.checkBox.setObjectName(u"checkBox")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.checkBox.setFont(font1)

        self.verticalLayout.addWidget(self.checkBox)

        self.checkBox_flagTelematic = QCheckBox(self.groupBox_5)
        self.checkBox_flagTelematic.setObjectName(u"checkBox_flagTelematic")
        self.checkBox_flagTelematic.setFont(font)
        icon1 = QIcon(QIcon.fromTheme(u"applications-internet"))
        self.checkBox_flagTelematic.setIcon(icon1)

        self.verticalLayout.addWidget(self.checkBox_flagTelematic)


        self.verticalLayout_2.addWidget(self.groupBox_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_didValue = QLabel(configWidget)
        self.label_didValue.setObjectName(u"label_didValue")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_didValue.sizePolicy().hasHeightForWidth())
        self.label_didValue.setSizePolicy(sizePolicy1)
        self.label_didValue.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_didValue)

        self.lineEdit_didValue = QLineEdit(configWidget)
        self.lineEdit_didValue.setObjectName(u"lineEdit_didValue")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_didValue.sizePolicy().hasHeightForWidth())
        self.lineEdit_didValue.setSizePolicy(sizePolicy2)
        self.lineEdit_didValue.setMaximumSize(QSize(85, 16777215))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.lineEdit_didValue.setFont(font2)
        self.lineEdit_didValue.setCursor(QCursor(Qt.CursorShape.IBeamCursor))

        self.horizontalLayout_2.addWidget(self.lineEdit_didValue)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.groupBox_6 = QGroupBox(configWidget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.formLayout = QFormLayout(self.groupBox_6)
        self.formLayout.setObjectName(u"formLayout")
        self.pushButton_getVinId = QPushButton(self.groupBox_6)
        self.pushButton_getVinId.setObjectName(u"pushButton_getVinId")
        self.pushButton_getVinId.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.pushButton_getVinId)

        self.pushButton_setVinId = QPushButton(self.groupBox_6)
        self.pushButton_setVinId.setObjectName(u"pushButton_setVinId")
        self.pushButton_setVinId.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.pushButton_setVinId)

        self.lineEdit_setVinId = QLineEdit(self.groupBox_6)
        self.lineEdit_setVinId.setObjectName(u"lineEdit_setVinId")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEdit_setVinId.sizePolicy().hasHeightForWidth())
        self.lineEdit_setVinId.setSizePolicy(sizePolicy3)
        self.lineEdit_setVinId.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEdit_setVinId)

        self.lineEdit_getVinId = QLineEdit(self.groupBox_6)
        self.lineEdit_getVinId.setObjectName(u"lineEdit_getVinId")
        sizePolicy3.setHeightForWidth(self.lineEdit_getVinId.sizePolicy().hasHeightForWidth())
        self.lineEdit_getVinId.setSizePolicy(sizePolicy3)
        self.lineEdit_getVinId.setFont(font)
        self.lineEdit_getVinId.setMaxLength(32767)
        self.lineEdit_getVinId.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit_getVinId)


        self.horizontalLayout.addWidget(self.groupBox_6)


        self.retranslateUi(configWidget)

        QMetaObject.connectSlotsByName(configWidget)
    # setupUi

    def retranslateUi(self, configWidget):
        configWidget.setWindowTitle(QCoreApplication.translate("configWidget_autoGen_T", u"Form", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("configWidget_autoGen_T", u"Set Flags", None))
        self.checkBox_flagDhc.setText(QCoreApplication.translate("configWidget_autoGen_T", u"DHC", None))
        self.checkBox_flagAcn.setText(QCoreApplication.translate("configWidget_autoGen_T", u"ACN", None))
        self.checkBox_flagRsn.setText(QCoreApplication.translate("configWidget_autoGen_T", u"RSN", None))
        self.checkBox_flagVls.setText(QCoreApplication.translate("configWidget_autoGen_T", u"VLS", None))
#if QT_CONFIG(shortcut)
        self.checkBox_flagVls.setShortcut(QCoreApplication.translate("configWidget_autoGen_T", u"Ctrl+1", None))
#endif // QT_CONFIG(shortcut)
        self.checkBox_flagSos.setText(QCoreApplication.translate("configWidget_autoGen_T", u"SOS", None))
        self.checkBox.setText(QCoreApplication.translate("configWidget_autoGen_T", u"Cust active", None))
        self.checkBox_flagTelematic.setText(QCoreApplication.translate("configWidget_autoGen_T", u"Telematic", None))
        self.label_didValue.setText(QCoreApplication.translate("configWidget_autoGen_T", u"DID value", None))
        self.lineEdit_didValue.setText("")
        self.lineEdit_didValue.setPlaceholderText(QCoreApplication.translate("configWidget_autoGen_T", u"0x00", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("configWidget_autoGen_T", u"Vin ID", None))
        self.pushButton_getVinId.setText(QCoreApplication.translate("configWidget_autoGen_T", u"Get VinID", None))
        self.pushButton_setVinId.setText(QCoreApplication.translate("configWidget_autoGen_T", u"Set VinID", None))
        self.lineEdit_getVinId.setInputMask("")
        self.lineEdit_getVinId.setPlaceholderText(QCoreApplication.translate("configWidget_autoGen_T", u"vinId get from board", None))
    # retranslateUi

