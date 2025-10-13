# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Start.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(200, 200)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleLable = QLabel(self.centralwidget)
        self.titleLable.setObjectName(u"titleLable")
        self.titleLable.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.titleLable)

        self.InputLayout = QHBoxLayout()
        self.InputLayout.setObjectName(u"InputLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.InputLayout.addWidget(self.label)

        self.InputEdit = QLineEdit(self.centralwidget)
        self.InputEdit.setObjectName(u"InputEdit")

        self.InputLayout.addWidget(self.InputEdit)


        self.verticalLayout.addLayout(self.InputLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.okButton = QPushButton(self.centralwidget)
        self.okButton.setObjectName(u"okButton")

        self.horizontalLayout.addWidget(self.okButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 200, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLable.setText(QCoreApplication.translate("MainWindow", u"\u80fd\u56de\u5fc6\u8d77\u4f60\u7684\u540d\u5b57\u5417\uff1f", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Dr.  ", None))
        self.InputEdit.setText("")
        self.InputEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6211\u7684\u540d\u5b57\u662f...", None))
        self.okButton.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4", None))
    # retranslateUi

