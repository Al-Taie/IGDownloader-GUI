# cx_run.py
import sys

from cx_Freeze import setup, Executable

# Replaces commandline arg 'build'
sys.argv.append("bdist_msi")

# If need to include/exclude module/packages
includes = ['multiprocessing', 'uuid']
excludes = ['tkinter', 'asyncio', 'unittest',
            'xmlrpc', 'xml', 'test', 'PySide6', 'shiboken6', 'pymongo', 'dns', 'bson']
packages = None

author = 'Ahmed Al-Taie'
target_name = 'IG Downloader'
target_dir = None
upgrade_code = '{46B28C0C-42F9-46F7-8232-B434AA6DE5F9}'

icon = 'resources/icon.ico'
files = ['lib/']

# "StartupShortcut",        # Shortcut
# "StartupFolder",          # Directory_

# Console or Win32GUI
base = None
if sys.platform == "win32":
    # base = 'Console'
    base = 'Win32GUI'

# Name of file to make ".exe" of
filename = 'main.py'
setup(
    author=author,
    name=target_name,
    version='2.1',
    description='IG Downloader By Ahmed Al-Taie | @9_tay',
    options={'build_exe': {'include_files': files,
                           'excludes': excludes,
                           'packages': packages,
                           'includes': includes,
                           'optimize': 2},

             'bdist_msi': {'target_name': target_name,
                           'initial_target_dir': target_dir,
                           'upgrade_code': upgrade_code,
                           'install_icon': icon}},
    executables=[Executable(filename, base=base, icon=icon,
                            shortcut_name=target_name,
                            shortcut_dir='DesktopFolder')])

# --|  From command line
# py setup.py bdist_msi
