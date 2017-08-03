__author__ = 'CGT'
import os

# ui_files = ['about.ui', 'mainwindow.ui', 'mainwindow_toolbar.ui', 'preferences.ui']
os.system('C:\Python35\Scripts\pyuic5.exe ui_files/main_window.ui -o ui_files/main_window_ui.py')
os.system('C:\Python35\Scripts\pyuic5.exe ui_files/about.ui -o ui_files/about_ui.py')
os.system('C:\Python35\Scripts\pyuic5.exe ui_files/preferences.ui -o ui_files/preferences_ui.py')

os.system('C:\Python361\Scripts\pyrcc5.exe ui_files/resources.qrc -o ui_files/resources_rc.py')

with open('ui_files/main_window_ui.py','r') as f:
    lines = f.readlines()

lines[-1] = 'import ui_files.resources_rc'

with open('ui_files/main_window_ui.py','w') as f:
    f.writelines(lines)

with open('ui_files/preferences_ui.py','r') as f:
    lines = f.readlines()

lines[-1] = 'import ui_files.resources_rc'

with open('ui_files/preferences_ui.py','w') as f:
    f.writelines(lines)