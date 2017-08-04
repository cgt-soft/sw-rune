import os
import sys
import PyQt5
__author__ = 'CGT'

file_name = 'main'
cwd_path = os.getcwd()                              # C:\Users\Christian\Desktop\cgt-soft\sw-rune
scripts_path = os.path.dirname(sys.executable)      # C:\Users\Christian\Desktop\cgt-soft\VENVs\sw-rune-py35\Scripts
pyqt_path = os.path.dirname(PyQt5.__file__)
# print('{}\pyinstaller.exe --path {}\Qt\\bin --onefile -w --icon={}\\favicon.icon --clean {}'.format(scripts_path, pyqt_path, cwd_path, file_to_build))
# comand = '{}\pyinstaller.exe --path {}\Qt\\bin --onefile -w --clean {}'.format(scripts_path, pyqt_path, file_to_build)
comand = '{}\pyinstaller.exe {}.spec'.format(scripts_path, file_name)
os.system(comand)
