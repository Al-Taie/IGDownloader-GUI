import re
import traceback
from os import startfile
import browser_cookie3
from PySide6.QtCore import Qt, QThreadPool, QPoint, QSize
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QMenu, QSystemTrayIcon, QApplication, QMainWindow, QMessageBox, QInputDialog

from data.api_service import ApiService
from data.db import is_new_update
from data.downloader import Downloader
from ui.dialog.about_dialog import AboutDialog
from ui.main.ui_main import Ui_Form
from utils.configurations import app_name, PATH_IG_DOWNLOAD, HEADERS, PATH_DOWNLOADS, version
from utils.worker import Worker


class MainApp(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.offset = QPoint()
        self.about = AboutDialog()
        self.clipboard = QApplication.clipboard()
        self.last_clipboard = list()

        self.threadpool = QThreadPool()

        self.__downloader = Downloader()

        # CHECK FOR UPDATE
        self.on_start()

        self.setupUi(self)
        # REMOVE TITLE BAR
        self.setWindowFlags(Qt.FramelessWindowHint
                            | Qt.WindowStaysOnTopHint)

        # REMOVE BACKGROUND
        self.setAttribute(Qt.WA_TranslucentBackground)

        # SysTray Icon
        self.tray = QSystemTrayIcon(self)
        self.setWindowIcon(QIcon(':/icon.png'))

        # Check if System supports STray icons
        if self.tray.isSystemTrayAvailable():
            self.tray.setIcon(self.windowIcon())
            self.tray.setToolTip(app_name)
            self.tray.activated.connect(self.on_tray_activated)

            # Context Menu
            context_menu = QMenu()
            action_show = context_menu.addAction('Show/Hide')
            action_show.triggered.connect(lambda: self.hide() if self.isVisible() else self.show())
            action_about = context_menu.addAction('About')
            action_about.triggered.connect(self.about.show)
            action_quit = context_menu.addAction('Quit')
            action_quit.triggered.connect(self.close)

            self.tray.setContextMenu(context_menu)
            self.tray.show()
        else:
            # Destroy unused var
            self.tray = None

        # SHOW WINDOW
        self.show()

        # HANDLE BUTTONS
        self.handle_buttons()
        self.lbl_update.setVisible(False)
        self.cookies = ''
        self.api_service = ApiService(cookie=self.cookies)

    # SYSTEM TRAY CLICK EVENT
    def on_tray_activated(self, reason):
        if (reason == QSystemTrayIcon.DoubleClick
                or reason == QSystemTrayIcon.Trigger):
            self.hide() if self.isVisible() else self.show()
        elif reason == QSystemTrayIcon.MiddleClick:
            self.close()

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.offset = event.globalPosition().toPoint() - self.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPosition().toPoint() - self.offset)
            event.accept()

    def cookie_dialog(self):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)

        is_logged = bool(self.cookies)
        title = 'Logout' if is_logged else 'Login'
        self.btn_cookie.setToolTip('Login' if is_logged else 'Logout')

        icon = QPixmap()

        if is_logged:
            icon.load(u":/logout.png")
        else:
            icon.load(u":/login.png")

        msg.setIconPixmap(icon.scaled(48, 48, Qt.KeepAspectRatio))

        msg.setText(f"Instagram {title}")
        msg.setInformativeText(f"Do you want to {title}?")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        if not is_logged:
            msg.setDetailedText('Please open your browser then login into Instagram, '
                                'after that clik Ok, '
                                'if you already logged just click Ok.')

        status = msg.exec() == QMessageBox.Ok
        icon = QIcon()

        if status and not is_logged:
            icon.addFile(u":/logout.png", QSize(), QIcon.Normal, QIcon.Off)
            self.btn_cookie.setIcon(icon)
            self.cookies = browser_cookie3.load(domain_name='instagram.com')
            self.api_service.cookie = self.cookies
        elif status and is_logged:
            icon.addFile(u":/login.png", QSize(), QIcon.Normal, QIcon.Off)
            self.btn_cookie.setIcon(icon)
            self.cookies = {}
            self.api_service.cookie = self.cookies

    def handle_buttons(self):
        self.btn_run.clicked.connect(self.run_btn)
        self.btn_min.clicked.connect(self.hide)
        self.btn_exit.clicked.connect(self.close)
        self.btn_folder.clicked.connect(self.open_folder)
        self.btn_cookie.clicked.connect(self.cookie_dialog)
        self.btn_info.clicked.connect(self.show_about)
        self.clipboard.dataChanged.connect(self.detect_url)

    def show_about(self):
        if self.about.isVisible():
            self.about.hide()
        else:
            self.about.show()

    @staticmethod
    def open_folder():
        try:
            startfile(PATH_IG_DOWNLOAD)
        except FileNotFoundError:
            pass

    def run_btn(self):
        if self.btn_run.isChecked():
            self.btn_run.setText('STOP')
        else:
            self.btn_run.setText('START')

    def handle_progress(self, total, current):
        progress = int(current * 100 / total)
        self.progressBar.setValue(progress)

    def detect_url(self):
        pattern = r'((?:http|https).*\.instagram\.com/(?:p|reel)/[a-zA-Z0-9_\-]+)'
        text = self.clipboard.text()
        if text in self.last_clipboard:
            return
        elif len(self.last_clipboard) == 50:
            self.last_clipboard = []

        if (url := re.search(pattern, text)) and self.btn_run.isChecked():
            url = url.group(1) + '/?__a=1&__d=dis'
            self.clipboard.clear()
            self.last_clipboard.append(text)
            worker = Worker(self.work, url=url)
            self.threadpool.start(worker)

    def work(self, url):

        def on_progress(total_size=1, current_size=0):
            self.handle_progress(total_size, current_size)

        try:
            post = self.api_service.get_post(url=url, headers=HEADERS)

            if post.is_slide:
                for index, media_item in enumerate(post.items, start=1):
                    self.lbl_count.setText(f'{post.count}/{index}')
                    self.__downloader.download_prepare(media_item=media_item,
                                                       index=index,
                                                       on_progress=on_progress,
                                                       post=post)
            else:
                self.__downloader.download_prepare(media_item=post.item,
                                                   on_progress=on_progress,
                                                   post=post)
        except Exception as e:
            traceback.print_exception(e.__traceback__)
            self.lbl_status.setText('Error')
        else:
            self.lbl_status.setText('OK')

    def msgbox(self, details=''):
        details = details.replace('\\n ', '\n')
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText("There is a new update")
        msg.setInformativeText("Do you want to update?")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setDetailedText(details)
        return msg.exec() == QMessageBox.Ok

    def install_update(self):
        filename = PATH_DOWNLOADS + 'IG Downloader.msi'
        startfile(filename)
        self.close()

    def on_start(self):
        worker = Worker(is_new_update, float(version))
        worker.signals.finished.connect(lambda: print(f'Check Update Finished'))
        worker.signals.result.connect(self.check_update)
        self.threadpool.start(worker)

    def check_update(self, *args, **kwargs):
        if not (update := args[0]):
            return

        if update.url and self.msgbox(update.description):
            filename = PATH_DOWNLOADS + 'IG Downloader.msi'
            headers = {'Range': 'bytes=0-'}
            worker = Worker(self.__downloader.download, update.url, filename, headers)
            worker.signals.finished.connect(self.install_update)
            self.threadpool.start(worker)
            self.lbl_update.setVisible(True)
            self.lbl_status.setText('Updating')
