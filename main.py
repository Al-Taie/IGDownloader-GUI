import re
import sys
from os import mkdir, path, getlogin, startfile

import requests
from PySide6.QtCore import QThreadPool, Qt, Signal, Slot, QObject, QRunnable
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QMenu, QSystemTrayIcon, QMessageBox
import traceback

from db import is_new_update
from ui_about import Ui_Dialog
from ui_main import Ui_Form

headers = {'authority': 'www.instagram.com',
           'method': 'GET',
           'scheme': 'https',
           'accept': ('text/html,application/xhtml+xml,application/xml;q=0.9,'
                      'image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'),
           'accept-encoding': 'gzip, deflate, br',
           'accept-language': 'ar,en;q=0.9',
           'cache-control': 'max-age=0',
           'sec-fetch-dest': 'document',
           'sec-fetch-mode': 'navigate',
           'sec-fetch-site': 'none',
           'sec-fetch-user': '?1',
           'upgrade-insecure-requests': '1',
           'user-agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63')}
app_name = 'IG Downloader'
developer = 'Ahmed Al-Taie'
version = '2.1'
__version__ = float(version)

PC_USER = getlogin()
PATH_DOWNLOADS = f'C:/Users/{PC_USER}/Downloads/'
PATH_IGDOWNLOAD = PATH_DOWNLOADS + app_name

class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    progress
        int indicating % progress

    '''
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, func, url='', *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.url = url
        self.func = func
        self.args = args
        self.kwargs = kwargs      
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.func(self.url, *self.args)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            try:
                self.signals.finished.emit()  # Done
            except RuntimeError:
                return

    def stop(self):
        self.terminate()


class About(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.btn_close.clicked.connect(self.close)


class MainApp(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.about = About()
        self.clipboard = QApplication.clipboard()
        self.last_clipboard = list()
        
        self.threadpool = QThreadPool()
        
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

    # SYSTEM TRAY CLICK EVENT
    def on_tray_activated(self, reason):
        if (reason == QSystemTrayIcon.DoubleClick
                or reason == QSystemTrayIcon.Trigger):
            self.hide() if self.isVisible() else self.show()
        elif reason == QSystemTrayIcon.MiddleClick:
            self.close()

    # MOVE WINDOW
    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.c_pos = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.c_pos)
            event.accept()

    # END MOVE WINDOW
    # END EVENTS

    def handle_buttons(self):
        self.btn_run.clicked.connect(self.run_btn)
        self.btn_min.clicked.connect(self.hide)
        self.btn_exit.clicked.connect(self.close)
        self.btn_folder.clicked.connect(self.open_folder)
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
            startfile(PATH_IGDOWNLOAD)
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
        pattern = r'((?:http|https).*\.instagram\.com/p/[a-zA-Z0-9_\-]+)'
        text = self.clipboard.text()
        if text in self.last_clipboard:
            return
        elif len(self.last_clipboard) == 50:
            self.last_clipboard = []
        
        if (url := re.search(pattern, text)) and self.btn_run.isChecked():
            url = url.group(1) + '/?__a=1'
            self.clipboard.clear()
            self.last_clipboard.append(text) 
            worker = Worker(self.work, url=url)
            # worker.signals.finished.connect(lambda: print(f'Finish'))
            # worker.signals.result.connect()
            # worker.signals.progress.connect(self.progress_fn)
            # Execute
            self.threadpool.start(worker)

    def work(self, url):
        try:
            with requests.get(url, headers=headers) as res:
                res_json = res.json()
                items = res_json.get('graphql').get('shortcode_media')
                is_video = items.get('is_video')
                is_slide = items.get('edge_sidecar_to_children') is not None
                short_code = items["shortcode"]
                username = items['owner']['username']

            if is_slide:
                post_list: list = items.get('edge_sidecar_to_children').get('edges')
                post_count = len(post_list)

                for i, post in enumerate(post_list, start=1):
                    items = post['node']
                    is_video = items.get('is_video')
                    short_code = short_code.replace(f'_{i - 1}', '')
                    short_code += f'_{i}'
                    self.download_prepear(items=items,
                                          username=username,
                                          short_code=short_code,
                                          is_video=is_video,
                                          post_count=post_count,
                                          current_post=i)
            else:
                self.download_prepear(items=items,
                                      username=username,
                                      short_code=short_code,
                                      is_video=is_video,
                                      post_count=1, current_post=1)
        except Exception as e:
            self.lbl_status.setText('Error')
        else:
            self.lbl_status.setText('OK')

    @staticmethod
    def folder(name, user):
        root = PATH_IGDOWNLOAD
        sub = f'{root}/{name}'
        paths = [root, sub, f'{sub}/{user}']
        [None if path.isdir(p) else mkdir(p) for p in paths]
        return paths[-1]

    def msgbox(self, detailes=''):
        detailes = detailes.replace('\\n ', '\n')
        msg = QMessageBox(self)
        msg.setIcon(msg.Information)
        msg.setText("There is a new update")
        msg.setInformativeText("Do you want to update?")
        msg.setStandardButtons(msg.Ok | msg.Cancel)
        msg.setDetailedText(detailes)
        return (msg.exec() == msg.Ok)

    def install_update(self):
        filename = PATH_DOWNLOADS + 'IG Downloader.msi'
        startfile(filename)
        self.close()

    def on_start(self):
        worker = Worker(is_new_update, __version__)
        worker.signals.finished.connect(lambda: print(f'Check Update Finished'))
        worker.signals.result.connect(self.check_update)
        # Execute
        self.threadpool.start(worker)

    def check_update(self, *args, **kwargs):
        try:
            url, description = args[0]
        except (TypeError, ValueError):
            return
        
        if url and self.msgbox(description):
            filename = PATH_DOWNLOADS + 'IG Downloader.msi'
            headers = {'Range': 'bytes=0-'} 
            worker = Worker(self.download, url, filename, headers)
            worker.signals.finished.connect(self.install_update)
            # worker.signals.result.connect()
            # Execute
            self.threadpool.start(worker)
            self.lbl_update.setVisible(True)
            self.lbl_status.setText('Updating')

    def download_prepear(self, *args, **kwargs):
        (items, username,
         short_code, is_video,
         post_count, current_post) = kwargs.values()
        self.lbl_count.setText(f'{post_count}/{current_post}')

        if is_video:
            url = items.get('video_url')
            save_path = self.folder('videos', username)
            filename = f'{save_path}/{short_code}.mp4'
        else:
            url = items.get('display_url')
            save_path = self.folder('Images', username)
            filename = f'{save_path}/{short_code}.jpg'
        self.download(url, filename)

    def download(self, url, filename, headers={}, *args, **kwargs):
        with requests.get(url, headers=headers, stream=True) as resp:
            try:
                total_size = int(resp.headers.get('content-length'))
            except TypeError:
                content_length = resp.headers.get('Content-Range')
                if content_length:
                    content_length = content_length.split('/')[-1]
                    total_size = int(content_length)
                else:
                    return
                
            current_size = 0  
            
            with open(filename, 'wb') as f:
                for chunk in resp.iter_content(chunk_size=total_size // 100):
                    current_size += len(chunk)
                    try:
                        self.handle_progress(total_size, current_size)
                    except RuntimeError:
                        return
                    f.write(chunk) if chunk else None


def main():
    app = QApplication(sys.argv)
    app.setApplicationName(app_name)
    app.setApplicationVersion(version)
    app.setOrganizationName(developer)
    win = MainApp()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
