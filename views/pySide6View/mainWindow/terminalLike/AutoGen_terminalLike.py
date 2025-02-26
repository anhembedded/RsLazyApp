# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'terminalLike.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLineEdit,
    QPlainTextEdit, QSizePolicy, QVBoxLayout, QWidget)

class Ui_terminalLike_autoGen_T(object):
    def setupUi(self, terminalLike):
        if not terminalLike.objectName():
            terminalLike.setObjectName(u"terminalLike")
        terminalLike.resize(616, 501)
        self.gridLayout = QGridLayout(terminalLike)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plainTextEdit_output = QPlainTextEdit(terminalLike)
        self.plainTextEdit_output.setObjectName(u"plainTextEdit_output")
        self.plainTextEdit_output.setFrameShape(QFrame.Shape.StyledPanel)
        self.plainTextEdit_output.setFrameShadow(QFrame.Shadow.Sunken)
        self.plainTextEdit_output.setReadOnly(True)

        self.verticalLayout.addWidget(self.plainTextEdit_output)

        self.lineEdit_input = QLineEdit(terminalLike)
        self.lineEdit_input.setObjectName(u"lineEdit_input")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        self.lineEdit_input.setFont(font)

        self.verticalLayout.addWidget(self.lineEdit_input)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(terminalLike)

        QMetaObject.connectSlotsByName(terminalLike)
    # setupUi

    def retranslateUi(self, terminalLike):
        terminalLike.setWindowTitle(QCoreApplication.translate("terminalLike_autoGen_T", u"terminalLike", None))
    # retranslateUi

