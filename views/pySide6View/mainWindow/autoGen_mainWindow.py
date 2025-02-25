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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMdiArea, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpinBox, QSplitter, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow_autoGen_T(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1418, 777)
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
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.mdiArea_app = QMdiArea(self.splitter)
        self.mdiArea_app.setObjectName(u"mdiArea_app")
        self.mdiArea_app.setMinimumSize(QSize(1224, 480))
        self.mdiArea_app.setFrameShape(QFrame.Shape.Box)
        self.mdiArea_app.setViewMode(QMdiArea.ViewMode.SubWindowView)
        self.subwindow_dhc = QWidget()
        self.subwindow_dhc.setObjectName(u"subwindow_dhc")
        self.gridLayout_2 = QGridLayout(self.subwindow_dhc)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.subwindow_dhc)
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
        self.checkBox_allData = QCheckBox(self.groupBox)
        self.checkBox_allData.setObjectName(u"checkBox_allData")

        self.verticalLayout_3.addWidget(self.checkBox_allData)

        self.checkBox_locationData = QCheckBox(self.groupBox)
        self.checkBox_locationData.setObjectName(u"checkBox_locationData")

        self.verticalLayout_3.addWidget(self.checkBox_locationData)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.main)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout_2 = QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_dhcIntervalUnit = QLabel(self.groupBox_2)
        self.label_dhcIntervalUnit.setObjectName(u"label_dhcIntervalUnit")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_dhcIntervalUnit)

        self.comboBox_dhcIntervalUnit = QComboBox(self.groupBox_2)
        self.comboBox_dhcIntervalUnit.addItem("")
        self.comboBox_dhcIntervalUnit.addItem("")
        self.comboBox_dhcIntervalUnit.setObjectName(u"comboBox_dhcIntervalUnit")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.comboBox_dhcIntervalUnit)

        self.pushButton_dhcSetIntervalUnit = QPushButton(self.groupBox_2)
        self.pushButton_dhcSetIntervalUnit.setObjectName(u"pushButton_dhcSetIntervalUnit")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.pushButton_dhcSetIntervalUnit)

        self.label_dhcIntervalValue = QLabel(self.groupBox_2)
        self.label_dhcIntervalValue.setObjectName(u"label_dhcIntervalValue")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_dhcIntervalValue)

        self.spinBox_dhcIntervalValue = QSpinBox(self.groupBox_2)
        self.spinBox_dhcIntervalValue.setObjectName(u"spinBox_dhcIntervalValue")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.spinBox_dhcIntervalValue.sizePolicy().hasHeightForWidth())
        self.spinBox_dhcIntervalValue.setSizePolicy(sizePolicy1)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.spinBox_dhcIntervalValue)

        self.pushButton_dhcSetIntervalValue = QPushButton(self.groupBox_2)
        self.pushButton_dhcSetIntervalValue.setObjectName(u"pushButton_dhcSetIntervalValue")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.pushButton_dhcSetIntervalValue)


        self.gridLayout_3.addWidget(self.groupBox_2, 0, 1, 2, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_dhcMqttTopic = QLabel(self.main)
        self.label_dhcMqttTopic.setObjectName(u"label_dhcMqttTopic")

        self.horizontalLayout_5.addWidget(self.label_dhcMqttTopic)

        self.lineEdit_dhcVin = QLineEdit(self.main)
        self.lineEdit_dhcVin.setObjectName(u"lineEdit_dhcVin")

        self.horizontalLayout_5.addWidget(self.lineEdit_dhcVin)

        self.comboBox = QComboBox(self.main)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_5.addWidget(self.comboBox)


        self.gridLayout_3.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        self.tabWidget.addTab(self.main, "")
        self.JsonPayload = QWidget()
        self.JsonPayload.setObjectName(u"JsonPayload")
        self.tabWidget.addTab(self.JsonPayload, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.mdiArea_app.addSubWindow(self.subwindow_dhc)
        self.subwindow_vls = QWidget()
        self.subwindow_vls.setObjectName(u"subwindow_vls")
        self.mdiArea_app.addSubWindow(self.subwindow_vls)
        self.subwindow_config = QWidget()
        self.subwindow_config.setObjectName(u"subwindow_config")
        self.horizontalLayout_4 = QHBoxLayout(self.subwindow_config)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox_flagDhc = QCheckBox(self.subwindow_config)
        self.checkBox_flagDhc.setObjectName(u"checkBox_flagDhc")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.checkBox_flagDhc.setFont(font)

        self.verticalLayout.addWidget(self.checkBox_flagDhc)

        self.checkBox_flagAcn = QCheckBox(self.subwindow_config)
        self.checkBox_flagAcn.setObjectName(u"checkBox_flagAcn")
        self.checkBox_flagAcn.setFont(font)

        self.verticalLayout.addWidget(self.checkBox_flagAcn)

        self.checkBox_flagRsn = QCheckBox(self.subwindow_config)
        self.checkBox_flagRsn.setObjectName(u"checkBox_flagRsn")
        self.checkBox_flagRsn.setFont(font)

        self.verticalLayout.addWidget(self.checkBox_flagRsn)

        self.checkBox_flagVls = QCheckBox(self.subwindow_config)
        self.checkBox_flagVls.setObjectName(u"checkBox_flagVls")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.checkBox_flagVls.sizePolicy().hasHeightForWidth())
        self.checkBox_flagVls.setSizePolicy(sizePolicy2)
        self.checkBox_flagVls.setFont(font)

        self.verticalLayout.addWidget(self.checkBox_flagVls)

        self.checkBox_flagSos = QCheckBox(self.subwindow_config)
        self.checkBox_flagSos.setObjectName(u"checkBox_flagSos")
        self.checkBox_flagSos.setFont(font)
        icon = QIcon(QIcon.fromTheme(u"dialog-warning"))
        self.checkBox_flagSos.setIcon(icon)

        self.verticalLayout.addWidget(self.checkBox_flagSos)

        self.checkBox_flagTelematic = QCheckBox(self.subwindow_config)
        self.checkBox_flagTelematic.setObjectName(u"checkBox_flagTelematic")
        self.checkBox_flagTelematic.setFont(font)
        icon1 = QIcon(QIcon.fromTheme(u"applications-internet"))
        self.checkBox_flagTelematic.setIcon(icon1)

        self.verticalLayout.addWidget(self.checkBox_flagTelematic)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_didValue = QLabel(self.subwindow_config)
        self.label_didValue.setObjectName(u"label_didValue")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_didValue.sizePolicy().hasHeightForWidth())
        self.label_didValue.setSizePolicy(sizePolicy3)
        self.label_didValue.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_didValue)

        self.lineEdit_didValue = QLineEdit(self.subwindow_config)
        self.lineEdit_didValue.setObjectName(u"lineEdit_didValue")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineEdit_didValue.sizePolicy().hasHeightForWidth())
        self.lineEdit_didValue.setSizePolicy(sizePolicy4)
        self.lineEdit_didValue.setMaximumSize(QSize(85, 16777215))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.lineEdit_didValue.setFont(font1)
        self.lineEdit_didValue.setCursor(QCursor(Qt.CursorShape.IBeamCursor))

        self.horizontalLayout_2.addWidget(self.lineEdit_didValue)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.pushButton_getVinId = QPushButton(self.subwindow_config)
        self.pushButton_getVinId.setObjectName(u"pushButton_getVinId")
        self.pushButton_getVinId.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.pushButton_getVinId)

        self.pushButton_setVinId = QPushButton(self.subwindow_config)
        self.pushButton_setVinId.setObjectName(u"pushButton_setVinId")
        self.pushButton_setVinId.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.pushButton_setVinId)

        self.lineEdit_setVinId = QLineEdit(self.subwindow_config)
        self.lineEdit_setVinId.setObjectName(u"lineEdit_setVinId")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lineEdit_setVinId.sizePolicy().hasHeightForWidth())
        self.lineEdit_setVinId.setSizePolicy(sizePolicy5)
        self.lineEdit_setVinId.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_setVinId)

        self.lineEdit_getVinId = QLineEdit(self.subwindow_config)
        self.lineEdit_getVinId.setObjectName(u"lineEdit_getVinId")
        sizePolicy5.setHeightForWidth(self.lineEdit_getVinId.sizePolicy().hasHeightForWidth())
        self.lineEdit_getVinId.setSizePolicy(sizePolicy5)
        self.lineEdit_getVinId.setFont(font)
        self.lineEdit_getVinId.setMaxLength(32767)
        self.lineEdit_getVinId.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_getVinId)


        self.horizontalLayout_3.addLayout(self.formLayout)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.mdiArea_app.addSubWindow(self.subwindow_config)
        self.splitter.addWidget(self.mdiArea_app)
        self.groupBox_terminalLike = QGroupBox(self.splitter)
        self.groupBox_terminalLike.setObjectName(u"groupBox_terminalLike")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.groupBox_terminalLike.sizePolicy().hasHeightForWidth())
        self.groupBox_terminalLike.setSizePolicy(sizePolicy6)
        self.splitter.addWidget(self.groupBox_terminalLike)

        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.pushButton_config = QPushButton(self.centralwidget)
        self.pushButton_config.setObjectName(u"pushButton_config")
        icon2 = QIcon(QIcon.fromTheme(u"applications-development"))
        self.pushButton_config.setIcon(icon2)

        self.horizontalLayout.addWidget(self.pushButton_config)

        self.pushButton_dhc = QPushButton(self.centralwidget)
        self.pushButton_dhc.setObjectName(u"pushButton_dhc")

        self.horizontalLayout.addWidget(self.pushButton_dhc)

        self.pushButton_vls = QPushButton(self.centralwidget)
        self.pushButton_vls.setObjectName(u"pushButton_vls")
        icon3 = QIcon()
        icon3.addFile(u"../../../resources/protection.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_vls.setIcon(icon3)

        self.horizontalLayout.addWidget(self.pushButton_vls)

        self.pushButton_cust = QPushButton(self.centralwidget)
        self.pushButton_cust.setObjectName(u"pushButton_cust")

        self.horizontalLayout.addWidget(self.pushButton_cust)

        self.pushButton_tile = QPushButton(self.centralwidget)
        self.pushButton_tile.setObjectName(u"pushButton_tile")

        self.horizontalLayout.addWidget(self.pushButton_tile)

        self.pushButton_cascade = QPushButton(self.centralwidget)
        self.pushButton_cascade.setObjectName(u"pushButton_cascade")

        self.horizontalLayout.addWidget(self.pushButton_cascade)

        self.pushButton_closeAll = QPushButton(self.centralwidget)
        self.pushButton_closeAll.setObjectName(u"pushButton_closeAll")

        self.horizontalLayout.addWidget(self.pushButton_closeAll)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1418, 33))
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
        self.pushButton_tile.clicked.connect(self.mdiArea_app.tileSubWindows)
        self.pushButton_closeAll.clicked.connect(self.mdiArea_app.closeAllSubWindows)
        self.pushButton_cascade.clicked.connect(self.mdiArea_app.cascadeSubWindows)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow_autoGen_T", u"MainWindow", None))
        self.actionChangeVin.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"ChangeVin", None))
        self.actionSetFlag.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"SetFlag", None))
        self.actionTheme.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"Theme", None))
        self.actionAnhTh49.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"AnhTh49", None))
        self.subwindow_dhc.setWindowTitle(QCoreApplication.translate("MainWindow_autoGen_T", u"DHC", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow_autoGen_T", u"Consent State", None))
        self.checkBox_allData.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"AllData", None))
        self.checkBox_locationData.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"LocationData", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow_autoGen_T", u"Interval", None))
        self.label_dhcIntervalUnit.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"Unit", None))
        self.comboBox_dhcIntervalUnit.setItemText(0, QCoreApplication.translate("MainWindow_autoGen_T", u"Days", None))
        self.comboBox_dhcIntervalUnit.setItemText(1, QCoreApplication.translate("MainWindow_autoGen_T", u"Minnus", None))

        self.pushButton_dhcSetIntervalUnit.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"Set", None))
        self.label_dhcIntervalValue.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"Value", None))
        self.pushButton_dhcSetIntervalValue.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"Set", None))
        self.label_dhcMqttTopic.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"MQTT topic", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow_autoGen_T", u"abc/app/DHC", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow_autoGen_T", u"abc/app/DHC/result", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main), QCoreApplication.translate("MainWindow_autoGen_T", u"Main", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.JsonPayload), QCoreApplication.translate("MainWindow_autoGen_T", u"jsonPayload", None))
        self.subwindow_vls.setWindowTitle(QCoreApplication.translate("MainWindow_autoGen_T", u"VLS", None))
        self.subwindow_config.setWindowTitle(QCoreApplication.translate("MainWindow_autoGen_T", u"Config", None))
        self.checkBox_flagDhc.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"DHC", None))
        self.checkBox_flagAcn.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"ACN", None))
        self.checkBox_flagRsn.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"RSN", None))
        self.checkBox_flagVls.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"VLS", None))
#if QT_CONFIG(shortcut)
        self.checkBox_flagVls.setShortcut(QCoreApplication.translate("MainWindow_autoGen_T", u"Ctrl+1", None))
#endif // QT_CONFIG(shortcut)
        self.checkBox_flagSos.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"SOS", None))
        self.checkBox_flagTelematic.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"Telematic", None))
        self.label_didValue.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"DID value", None))
        self.lineEdit_didValue.setText("")
        self.lineEdit_didValue.setPlaceholderText(QCoreApplication.translate("MainWindow_autoGen_T", u"0x00", None))
        self.pushButton_getVinId.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"Get VinID", None))
        self.pushButton_setVinId.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"Set VinID", None))
        self.lineEdit_getVinId.setInputMask("")
        self.lineEdit_getVinId.setPlaceholderText(QCoreApplication.translate("MainWindow_autoGen_T", u"vinId get from board", None))
        self.groupBox_terminalLike.setTitle(QCoreApplication.translate("MainWindow_autoGen_T", u"Terminal Like", None))
        self.pushButton_config.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"Config", None))
        self.pushButton_dhc.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"DHC", None))
        self.pushButton_vls.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"VLS", None))
        self.pushButton_cust.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"Ecall Apps", None))
        self.pushButton_tile.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"Tile", None))
        self.pushButton_cascade.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"Cascade", None))
        self.pushButton_closeAll.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"CloseAll", None))
        self.menuLazyApp.setTitle(QCoreApplication.translate("MainWindow_autoGen_T", u"LazyApp", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow_autoGen_T", u"Edit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow_autoGen_T", u"Help", None))
    # retranslateUi

