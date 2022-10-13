import sys

from PySide6.QtWidgets import QApplication

from ui.main.main_app import MainApp
from utils.configurations import version, developer, app_name


def main():
    app = QApplication(sys.argv)
    app.setApplicationName(app_name)
    app.setApplicationVersion(version)
    app.setOrganizationName(developer)
    win = MainApp()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
