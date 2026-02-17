# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLayout, QMainWindow, QMdiArea,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSplitter, QStatusBar, QWidget)

class Ui_MainWindow_autoGen_T(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1622, 770)
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
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.pushButton_config = QPushButton(self.centralwidget)
        self.pushButton_config.setObjectName(u"pushButton_config")
        icon = QIcon(QIcon.fromTheme(u"applications-development"))
        self.pushButton_config.setIcon(icon)

        self.horizontalLayout.addWidget(self.pushButton_config)

        self.pushButton_dhc = QPushButton(self.centralwidget)
        self.pushButton_dhc.setObjectName(u"pushButton_dhc")

        self.horizontalLayout.addWidget(self.pushButton_dhc)

        self.pushButton_vls = QPushButton(self.centralwidget)
        self.pushButton_vls.setObjectName(u"pushButton_vls")
        icon1 = QIcon()
        icon1.addFile(u"../../../resources/protection.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_vls.setIcon(icon1)

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

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.mdiArea_app = QMdiArea(self.splitter)
        self.mdiArea_app.setObjectName(u"mdiArea_app")
        self.mdiArea_app.setMinimumSize(QSize(1224, 480))
        self.mdiArea_app.setFrameShape(QFrame.Shape.Box)
        self.mdiArea_app.setViewMode(QMdiArea.ViewMode.SubWindowView)
        self.splitter.addWidget(self.mdiArea_app)
        self.groupBox_terminalLike = QGroupBox(self.splitter)
        self.groupBox_terminalLike.setObjectName(u"groupBox_terminalLike")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_terminalLike.sizePolicy().hasHeightForWidth())
        self.groupBox_terminalLike.setSizePolicy(sizePolicy1)
        self.splitter.addWidget(self.groupBox_terminalLike)

        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1622, 33))
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

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow_autoGen_T", u"MainWindow", None))
        self.actionChangeVin.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"ChangeVin", None))
        self.actionSetFlag.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"SetFlag", None))
        self.actionTheme.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"Theme", None))
        self.actionAnhTh49.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"AnhTh49", None))
        self.pushButton_config.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"Config", None))
        self.pushButton_dhc.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"DHC", None))
        self.pushButton_vls.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"VLS", None))
        self.pushButton_cust.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"Ecall Apps", None))
        self.pushButton_tile.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"Tile", None))
        self.pushButton_cascade.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"Cascade", None))
        self.pushButton_closeAll.setText(QCoreApplication.translate("MainWindow_autoGen_T", u"CloseAll", None))
        self.groupBox_terminalLike.setTitle(QCoreApplication.translate("MainWindow_autoGen_T", u"Terminal Like", None))
        self.menuLazyApp.setTitle(QCoreApplication.translate("MainWindow_autoGen_T", u"LazyApp", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow_autoGen_T", u"Edit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow_autoGen_T", u"Help", None))
    # retranslateUi

