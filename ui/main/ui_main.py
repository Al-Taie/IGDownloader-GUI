# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QProgressBar,
    QSizePolicy, QToolButton, QWidget)
import res_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(320, 220)
        Form.setMinimumSize(QSize(320, 220))
        Form.setMaximumSize(QSize(320, 220))
        font = QFont()
        Form.setFont(font)
        Form.setStyleSheet(u"QToolTip {\n"
"  background-color: #148CD2;\n"
"  border: 1px solid #19232D;\n"
"  color: #C6C8D1;\n"
"  padding: 0px;\n"
"}")
        self.bg = QFrame(Form)
        self.bg.setObjectName(u"bg")
        self.bg.setGeometry(QRect(0, 0, 320, 220))
        self.bg.setMaximumSize(QSize(320, 220))
        self.bg.setStyleSheet(u"background-color: rgb(28, 29, 32);")
        self.bg.setFrameShape(QFrame.NoFrame)
        self.bg.setFrameShadow(QFrame.Raised)
        self.btn_run = QToolButton(self.bg)
        self.btn_run.setObjectName(u"btn_run")
        self.btn_run.setGeometry(QRect(110, 50, 100, 100))
        font1 = QFont()
        font1.setBold(True)
        self.btn_run.setFont(font1)
        self.btn_run.setStyleSheet(u"QToolButton {\n"
"border-radius: 50;\n"
"color: rgb(208, 208, 208);\n"
"background-color: rgb(40, 44, 52);\n"
" }\n"
"\n"
"QToolButton::hover\n"
"{\n"
"    background-color: rgb(64, 70, 83);\n"
"}\n"
"\n"
"QToolButton::checked\n"
"{\n"
"    background-color: rgb(85, 170, 127);\n"
"	color: rgb(149, 0, 0);\n"
"}\n"
"QToolButton::checked::hover\n"
"{\n"
"    background-color: rgb(0, 211, 102);\n"
"	color: rgb(170, 0, 0);\n"
"}")
        self.btn_run.setCheckable(True)
        self.lbl_dev = QLabel(self.bg)
        self.lbl_dev.setObjectName(u"lbl_dev")
        self.lbl_dev.setGeometry(QRect(-20, 190, 361, 20))
        font2 = QFont()
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(True)
        self.lbl_dev.setFont(font2)
        self.lbl_dev.setStyleSheet(u"QLabel {\n"
"color: rgb(78, 86, 102);\n"
"}")
        self.lbl_dev.setTextFormat(Qt.AutoText)
        self.lbl_dev.setScaledContents(True)
        self.lbl_dev.setAlignment(Qt.AlignCenter)
        self.lbl_dev.setOpenExternalLinks(True)
        self.btn_exit = QToolButton(self.bg)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setGeometry(QRect(296, 10, 16, 16))
        font3 = QFont()
        font3.setBold(False)
        self.btn_exit.setFont(font3)
        self.btn_exit.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QToolButton {\n"
"border-radius: 8;\n"
"background-color: rgb(170, 0, 0);\n"
" }\n"
"\n"
"QToolButton::hover\n"
"{\n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.btn_min = QToolButton(self.bg)
        self.btn_min.setObjectName(u"btn_min")
        self.btn_min.setGeometry(QRect(276, 10, 16, 16))
        self.btn_min.setFont(font1)
        self.btn_min.setStyleSheet(u"QToolButton {\n"
"border-radius: 8;\n"
"background-color: rgb(170, 85, 0);\n"
" }\n"
"\n"
"QToolButton::hover\n"
"{\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.progressBar = QProgressBar(self.bg)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(90, 160, 141, 23))
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet(u"QProgressBar\n"
"{	color: rgb(40, 44, 52);\n"
"}\n"
"\n"
"QProgressBar:horizontal\n"
"{\n"
"    background-color: #626568;\n"
"    border: 0.1ex solid #31363b;\n"
"    border-radius: 0.3ex;\n"
"    height: 0.5ex;\n"
"    text-align: center;\n"
"    margin-top: 0.5ex;\n"
"    margin-bottom: 0.5ex;\n"
"    margin-right: 0ex;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QProgressBar::chunk:horizontal\n"
"{\n"
"    background-color: #3daee9;\n"
"    border: 0.1ex transparent;\n"
"    border-radius: 0.3ex;\n"
"}")
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)
        self.lbl_count = QLabel(self.bg)
        self.lbl_count.setObjectName(u"lbl_count")
        self.lbl_count.setGeometry(QRect(249, 195, 61, 21))
        self.lbl_count.setFont(font)
        self.lbl_count.setStyleSheet(u"QLabel {\n"
"color: rgb(90, 99, 117);\n"
"}")
        self.lbl_count.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_status = QLabel(self.bg)
        self.lbl_status.setObjectName(u"lbl_status")
        self.lbl_status.setGeometry(QRect(9, 195, 61, 20))
        self.lbl_status.setFont(font)
        self.lbl_status.setStyleSheet(u"QLabel {\n"
"color: rgb(90, 99, 117);\n"
"}\n"
"")
        self.lbl_status.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl_name = QLabel(self.bg)
        self.lbl_name.setObjectName(u"lbl_name")
        self.lbl_name.setGeometry(QRect(-1, 5, 131, 20))
        font4 = QFont()
        font4.setPointSize(8)
        font4.setBold(True)
        font4.setItalic(False)
        font4.setUnderline(True)
        self.lbl_name.setFont(font4)
        self.lbl_name.setStyleSheet(u"color: rgb(78, 86, 102);")
        self.lbl_name.setTextFormat(Qt.AutoText)
        self.lbl_name.setScaledContents(True)
        self.lbl_name.setAlignment(Qt.AlignCenter)
        self.lbl_name.setOpenExternalLinks(True)
        self.btn_info = QToolButton(self.bg)
        self.btn_info.setObjectName(u"btn_info")
        self.btn_info.setGeometry(QRect(256, 10, 16, 16))
        self.btn_info.setFont(font1)
        self.btn_info.setStyleSheet(u"QToolButton {\n"
"border-radius: 8;\n"
"background-color: rgb(0, 85, 127);\n"
" }\n"
"\n"
"QToolButton::hover\n"
"{\n"
"    background-color: rgb(0, 170, 255);\n"
"}")
        self.btn_folder = QToolButton(self.bg)
        self.btn_folder.setObjectName(u"btn_folder")
        self.btn_folder.setGeometry(QRect(237, 10, 14, 14))
        self.btn_folder.setFont(font1)
        self.btn_folder.setStyleSheet(u"QToolButton {\n"
"border-radius: 8;\n"
"background-color: transparent;\n"
" }\n"
"\n"
"QToolButton::hover\n"
"{\n"
"    background-color: rgb(249, 190, 44);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_folder.setIcon(icon)
        self.btn_folder.setCheckable(False)
        self.btn_folder.setChecked(False)
        self.btn_folder.setPopupMode(QToolButton.DelayedPopup)
        self.btn_folder.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        self.lbl_update = QLabel(self.bg)
        self.lbl_update.setObjectName(u"lbl_update")
        self.lbl_update.setGeometry(QRect(10, 30, 301, 16))
        font5 = QFont()
        font5.setPointSize(8)
        font5.setBold(True)
        self.lbl_update.setFont(font5)
        self.lbl_update.setStyleSheet(u"QLabel {\n"
"    color: rgb(175, 5, 0);\n"
"    border-radius: 8;\n"
"	background-color: rgb(190, 200, 0);\n"
"}\n"
"\n"
"QLabel::hover\n"
"{\n"
"    color: rgb(205, 0, 0);\n"
"	 background-color: rgb(200, 200, 0);\n"
"}")
        self.lbl_update.setAlignment(Qt.AlignCenter)
        self.btn_cookie = QToolButton(self.bg)
        self.btn_cookie.setObjectName(u"btn_cookie")
        self.btn_cookie.setGeometry(QRect(212, 7, 20, 20))
        self.btn_cookie.setFont(font1)
        self.btn_cookie.setStyleSheet(u"QToolButton {\n"
"border-radius: 8;\n"
"background-color: transparent;\n"
" }\n"
"\n"
"QToolButton::hover\n"
"{\n"
"	\n"
"\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/login.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cookie.setIcon(icon1)
        self.btn_cookie.setIconSize(QSize(17, 17))
        self.btn_cookie.setCheckable(False)
        self.btn_cookie.setChecked(False)
        self.btn_cookie.setPopupMode(QToolButton.DelayedPopup)
        self.btn_cookie.setToolButtonStyle(Qt.ToolButtonFollowStyle)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle("")
        self.btn_run.setText(QCoreApplication.translate("Form", u"START", None))
#if QT_CONFIG(tooltip)
        self.lbl_dev.setToolTip(QCoreApplication.translate("Form", u"Follow Me!", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_dev.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Devloped by: <a href=\"https://www.instagram.com/9_tay\"><span style=\" text-decoration: underline; color:#737f96;\">@9_tay</span></a></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btn_exit.setToolTip(QCoreApplication.translate("Form", u"Exit", None))
#endif // QT_CONFIG(tooltip)
        self.btn_exit.setText(QCoreApplication.translate("Form", u"X", None))
#if QT_CONFIG(tooltip)
        self.btn_min.setToolTip(QCoreApplication.translate("Form", u"System tray", None))
#endif // QT_CONFIG(tooltip)
        self.btn_min.setText(QCoreApplication.translate("Form", u"-", None))
#if QT_CONFIG(tooltip)
        self.lbl_count.setToolTip(QCoreApplication.translate("Form", u"Counter", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_count.setText(QCoreApplication.translate("Form", u"0/0", None))
#if QT_CONFIG(tooltip)
        self.lbl_status.setToolTip(QCoreApplication.translate("Form", u"Status", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_status.setText(QCoreApplication.translate("Form", u"-----", None))
        self.lbl_name.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><a href=\"https://www.instagram.com/9_tay\"><span style=\" text-decoration: underline; color:#4a5261;\">IG Downloader v2.1</span></a></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btn_info.setToolTip(QCoreApplication.translate("Form", u"Info", None))
#endif // QT_CONFIG(tooltip)
        self.btn_info.setText(QCoreApplication.translate("Form", u"!", None))
#if QT_CONFIG(tooltip)
        self.btn_folder.setToolTip(QCoreApplication.translate("Form", u"Download Folder", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.btn_folder.setShortcut(QCoreApplication.translate("Form", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.lbl_update.setToolTip(QCoreApplication.translate("Form", u"Status", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_update.setText(QCoreApplication.translate("Form", u"Please don't exit until update completed", None))
#if QT_CONFIG(tooltip)
        self.btn_cookie.setToolTip(QCoreApplication.translate("Form", u"Login", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.btn_cookie.setShortcut(QCoreApplication.translate("Form", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

