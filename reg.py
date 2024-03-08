# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newwallet.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QTextEdit,
    QWidget)
import res_rc

class Ui_Reg(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(452, 300)
        Dialog.setModal(True)
        Dialog.setStyleSheet(u"\n"
"background-color:#16191d;\n"
"QPushButton{background-color: rgba(0, 0, 0, 0);\n"
"font-size:28px;\n"
"color:white;\n"
"hover:{color:white;}\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"border: 2px solid rgba(255,255,255,40);\n"
"border-radius:10px;\n"
"background-color: rgba(255,255,255,60);\n"
"}\n"
"border: 5px solid rgba(255,255,255,40);\n"
"")
        self.frame = QFrame(Dialog)
        icon = QIcon()
        icon.addFile(u":/icon/icons/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 451, 301))
        self.frame.setMinimumSize(QSize(451, 301))
        self.frame.setMaximumSize(QSize(451, 301))
        self.frame.setStyleSheet(u"#frame{border: 5px solid rgba(255,255,255,40);}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.headerContainer = QWidget(self.frame)
        self.headerContainer.setObjectName(u"headerContainer")
        self.headerContainer.setGeometry(QRect(120, 10, 321, 41))
        self.headerContainer.setStyleSheet(u"background-color:#ffff;")
        self.horizontalLayout_5 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_5.addWidget(self.frame_7, 0, Qt.AlignHCenter)

        self.frame_6 = QFrame(self.headerContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.headerContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.hide_btn = QPushButton(self.frame_8)
        self.hide_btn.setObjectName(u"hide_btn")
        self.hide_btn.setStyleSheet(u"border:none;")
        icon = QIcon()
        icon.addFile(u":/icon/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.hide_btn.setIcon(icon)
        self.hide_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.hide_btn)

        self.close_btn = QPushButton(self.frame_8)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setStyleSheet(u"border:none;")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon1)
        self.close_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.close_btn)


        self.horizontalLayout_5.addWidget(self.frame_8, 0, Qt.AlignRight)

        self.ok_btn = QPushButton(self.frame)
        self.ok_btn.setObjectName(u"ok_btn")
        self.ok_btn.setGeometry(QRect(190, 230, 75, 41))
        font = QFont()
        font.setFamilies([u"MS Sans Serif"])
        self.ok_btn.setFont(font)
        self.ok_btn.setStyleSheet(u"QPushButton{background-color: rgba(0, 0, 0, 0);\n"
"font-size:28px;\n"
"color:white;\n"
"hover:{color:white;}\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"border: 2px solid rgba(255,255,255,40);\n"
"border-radius:10px;\n"
"background-color: rgba(255,255,255,60);\n"
"}")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 80, 91, 31))
        font1 = QFont()
        font1.setFamilies([u"MS Sans Serif"])
        font1.setPointSize(16)
        font1.setHintingPreference(QFont.PreferDefaultHinting)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color:white;")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 160, 91, 41))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color:white;")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.label_4.setWordWrap(True)
        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(140, 80, 191, 31))
        font2 = QFont()
        font2.setFamilies([u"MS Sans Serif"])
        font2.setPointSize(13)
        self.textEdit.setFont(font2)
        self.textEdit.setStyleSheet(u"color:white;")
        self.textEdit_2 = QTextEdit(self.frame)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(140, 160, 191, 31))
        self.textEdit_2.setFont(font2)
        self.textEdit_2.setStyleSheet(u"color:white;")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.hide_btn.setText("")
        self.close_btn.setText("")
        self.ok_btn.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Password:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Confirm:", None))
    # retranslateUi

