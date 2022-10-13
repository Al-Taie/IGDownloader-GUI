from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog

from ui.dialog.ui_about import Ui_Dialog


class AboutDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.btn_close.clicked.connect(self.close)
