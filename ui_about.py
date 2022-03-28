# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainjvpXio.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import res_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(360, 480)
        Dialog.setStyleSheet(u"background: transparent;")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 360, 480))
        self.frame.setStyleSheet(u"\n"
"background-color: rgb(40, 44, 52);\n"
"border: 5px;\n"
"border-style: dashed;\n"
"border-radius: 70%;\n"
"border-color: rgb(249, 202, 23);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.frame.setLineWidth(0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 30, 151, 141))
        self.label.setStyleSheet(u"background-color: rgb(212, 213, 217);\n"
"border: 5px;\n"
"border-style: dashed;\n"
"border-radius: 70%;\n"
"border-color: rgb(249, 202, 23);\n"
"")
        self.label.setFrameShadow(QFrame.Sunken)
        self.label.setLineWidth(0)
        self.label.setPixmap(QPixmap(u":/profile.jpg"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(30, 190, 301, 261))
        self.line.setStyleSheet(u"background-color: rgb(216, 217, 222);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 410, 51, 31))
        font = QFont()
        font.setFamily(u"JetBrains Mono")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"border: none;\n"
"background: transparent;\n"
"")
        self.label_2.setOpenExternalLinks(True)
        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(40, 210, 281, 211))
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(u"border: none;\n"
"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)
        self.btn_close = QPushButton(self.frame)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(300, 30, 21, 21))
        self.btn_close.setStyleSheet(u"QPushButton {\n"
"   border:none;\n"
"   border-radius:8px;\n"
"   background-color: rgb(211, 170, 19);\n"
"   color: rgb(59, 59, 59);\n"
"   font: 6pt \"Segoe UI\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(58, 55, 74);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}")
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.btn_close)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<a href=\"https://www.instagram.com/9_tay\" style=\"color:#0665ff\">@9_Tay<a>", None))
        self.textEdit.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'JetBrains Mono'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Open Sans'; font-size:11pt; font-weight:600;\">IG Downloader v2.1</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Open Sans'; font-size:7.8pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Open San"
                        "s'; font-size:10pt; font-weight:600;\">- </span><span style=\" font-family:'Open Sans'; font-size:10pt; font-weight:600; color:#950000;\">Free Application Not For Sale !!</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Open Sans'; font-size:10pt; font-weight:600;\">- For More Tools Follow Me on </span><a href=\"https://www.instagram.com/9_tay\"><span style=\" font-family:'Open Sans'; font-size:10pt; text-decoration: underline; color:#0665ff;\">Instagram</span></a><span style=\" font-family:'Open Sans'; font-size:10pt; font-weight:600;\">.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Open Sans'; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-ind"
                        "ent:0; text-indent:0px;\"><span style=\" font-family:'Open Sans'; font-size:11pt; font-weight:600; color:#950000;\">.\u0628\u0631\u0646\u0627\u0645\u062c \u0645\u062c\u0627\u0646\u064a \u0644\u0627 \u064a\u0633\u0645\u062d \u0628\u0628\u064a\u0639\u0647 -</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Open Sans'; font-size:11pt; font-weight:600;\">.\u062a\u0627\u0628\u0639\u0646\u064a \u0639\u0644\u0649 </span><a href=\"https://www.instagram.com/9_tay\"><span style=\" font-family:'Open Sans'; font-size:11pt; text-decoration: underline; color:#0665ff;\">\u0623\u0646\u0633\u062a\u063a\u0631\u0627\u0645</span></a><span style=\" font-family:'Open Sans'; font-size:11pt; font-weight:600;\"> \u0644\u0644\u0645\u0632\u064a\u062f \u0645\u0646 \u0627\u0644\u0623\u062f\u0648\u0627\u062a -</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px"
                        "; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Open Sans'; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Open Sans'; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Open Sans'; font-size:11pt; font-weight:600;\">\u0633\u0628\u062d\u0627\u0646 \u0627\u0644\u0644\u0647 \u0648\u0628\u062d\u0645\u062f\u0647 \u0633\u0628\u062d\u0627\u0646 \u0627\u0644\u0644\u0647 \u0627\u0644\u0639\u0638\u064a\u0645</span></p></body></html>", None))
        self.btn_close.setText(QCoreApplication.translate("Dialog", u"X", None))
    # retranslateUi

