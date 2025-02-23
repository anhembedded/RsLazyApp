# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lazyapp.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_LazyAppMainWindow(object):
    def setupUi(self, LazyAppMainWindow):
        if not LazyAppMainWindow.objectName():
            LazyAppMainWindow.setObjectName(u"LazyAppMainWindow")
        LazyAppMainWindow.resize(477, 286)
        self.verticalLayout = QVBoxLayout(LazyAppMainWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelName = QLabel(LazyAppMainWindow)
        self.labelName.setObjectName(u"labelName")

        self.horizontalLayout.addWidget(self.labelName)   

        self.lineEditName = QLineEdit(LazyAppMainWindow)
        self.lineEditName.setObjectName(u"lineEditName")

        self.horizontalLayout.addWidget(self.lineEditName)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelWhat = QLabel(LazyAppMainWindow)
        self.labelWhat.setObjectName(u"labelWhat")

        self.horizontalLayout_2.addWidget(self.labelWhat)

        self.lineEditWhat = QLineEdit(LazyAppMainWindow)
        self.lineEditWhat.setObjectName(u"lineEditWhat")

        self.horizontalLayout_2.addWidget(self.lineEditWhat)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.pushButton = QPushButton(LazyAppMainWindow)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon(QIcon.fromTheme(u"call-stop"))
        self.pushButton.setIcon(icon)

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(LazyAppMainWindow)

        QMetaObject.connectSlotsByName(LazyAppMainWindow)
    # setupUi

    def retranslateUi(self, LazyAppMainWindow):
        LazyAppMainWindow.setWindowTitle(QCoreApplication.translate("LazyAppMainWindow", u"Form", None))
        self.labelName.setText(QCoreApplication.translate("LazyAppMainWindow", u"Name ???:", None))
        self.labelWhat.setText(QCoreApplication.translate("LazyAppMainWindow", u"What ???:", None))
        self.pushButton.setText(QCoreApplication.translate("LazyAppMainWindow", u"Submit", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    LazyAppMainWindow = QWidget()
    ui = Ui_LazyAppMainWindow()
    ui.setupUi(LazyAppMainWindow)
    LazyAppMainWindow.show()
    sys.exit(app.exec())