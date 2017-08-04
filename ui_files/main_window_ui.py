# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(967, 600)
        MainWindow.setStyleSheet("QWidget#frmLogin,QWidget#frmPopup,QWidget#frmHostInfo,QWidget#frmLogout,QWidget#frmConfig,QWidget#frmData,QWidget#frmDefence,QWidget#frmHost,QWidget#frmMain,QWidget#frmPwd,QWidget#frmSelect,QWidget#frmMessageBox{\n"
"    border:1px solid #1B89CA;\n"
"    border-radius:0px;    \n"
"}\n"
"\n"
".QFrame{\n"
"    border:1px solid #5CACEE;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QWidget#widget_title{\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5);\n"
"}\n"
"\n"
"QLabel#lab_Ico,QLabel#lab_Title{\n"
"    border-radius:0px;\n"
"    color: #F0F0F0;\n"
"    background-color:rgba(0,0,0,0);\n"
"    border-style:none;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid #5CACEE;\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"    background: none;\n"
"    selection-background-color: #1B89CA;\n"
"}\n"
"\n"
"QLineEdit[echoMode=\"2\"] { \n"
"    lineedit-password-character: 9679; \n"
"}\n"
"\n"
".QGroupBox{\n"
"    border: 1px solid #5CACEE;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
".QPushButton{\n"
"    border-style: none;\n"
"    border: 0px;\n"
"    color: #F0F0F0;\n"
"    padding: 5px;    \n"
"    min-height: 20px;\n"
"    border-radius:5px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5); \n"
"}\n"
"\n"
".QPushButton[focusPolicy=\"0\"] {\n"
"    border-style: none;\n"
"    border: 0px;\n"
"    color: #F0F0F0;\n"
"    padding: 0px;    \n"
"    min-height: 10px;\n"
"    border-radius:3px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5); \n"
"}\n"
"\n"
".QPushButton:hover{ \n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5CACEE, stop:1 #4F94CD);\n"
"}\n"
"\n"
".QPushButton:pressed{ \n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5);\n"
"}\n"
"\n"
"QPushButton#btnMenu,QPushButton#btnMenu_Min,QPushButton#btnMenu_Max,QPushButton#btnMenu_Close{\n"
"    border-radius:0px;\n"
"    color: #F0F0F0;\n"
"    background-color:rgba(0,0,0,0);\n"
"    border-style:none;\n"
"}\n"
"\n"
"QPushButton#btnMenu:hover,QPushButton#btnMenu_Min:hover,QPushButton#btnMenu_Max:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(25, 134, 199, 0), stop:1 #5CACEE);\n"
"}\n"
"\n"
"QPushButton#btnMenu_Close:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(238, 0, 0, 128), stop:1 rgba(238, 44, 44, 255));\n"
"}\n"
"\n"
"QCheckBox {\n"
"    spacing: 2px; \n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/qss-icons/resources/qss-icons/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/qss-icons/resources/qss-icons/checkbox_checked.png); \n"
"}\n"
"\n"
"QRadioButton {\n"
"    spacing: 2px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 15px; \n"
"    height: 15px; \n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"    image: url(:/qss-icons/resources/qss-icons/radio_normal.png); \n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"    image: url(:/qss-icons/resources/qss-icons/radio_selected.png); \n"
"}\n"
"\n"
"QComboBox,QDateEdit{\n"
"    border-radius: 3px;\n"
"    padding: 1px 10px 1px 5px;\n"
"    border: 1px solid #5CACEE;\n"
"}\n"
"\n"
"QComboBox::drop-down,QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px; \n"
"    border-left-width: 1px;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    border-left-color: #5CACEE;\n"
"}\n"
"\n"
"QComboBox::down-arrow,QDateEdit::down-arrow {\n"
"    background-color:transparent;\n"
"    image: url(:/qss-icons/resources/qss-icons/array_down.png);\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color:#F0F0F0;\n"
"    margin: 2px;\n"
"}\n"
"\n"
"QMenu::item {    \n"
"    padding: 2px 12px 2px 12px;\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    color: #FFFFFF;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5); \n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 1px;\n"
"    background: #5CACEE;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    border: 1px solid #5CACEE;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    width: 5px; \n"
"    margin: 0.5px;\n"
"    background-color: #1B89CA;\n"
"}\n"
"\n"
"QSlider::groove:horizontal,QSlider::add-page:horizontal { \n"
"    background: #808080; \n"
"    height: 8px; \n"
"    border-radius: 3px; \n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    height: 8px; \n"
"    border-radius: 3px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5); \n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 13px; \n"
"    margin-top: -3px; \n"
"    margin-bottom: -3px; \n"
"    border-radius: 6px;\n"
"    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,stop:0.6 #F0F0F0, stop:0.778409 #5CACEE);\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qradialgradient(spread: pad, cx: 0.5, cy: 0.5, radius: 0.5, fx: 0.5, fy: 0.5, stop: 0.6 #F0F0F0,stop:0.778409 #1B89CA);\n"
"}\n"
"\n"
"QSlider::groove:vertical,QSlider::sub-page:vertical {\n"
"    background:#808080; \n"
"    width: 8px; \n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"    width: 8px;\n"
"    border-radius: 3px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5); \n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 14px; \n"
"    margin-left: -3px;\n"
"    margin-right: -3px;\n"
"    border-radius: 6px;\n"
"    background: qradialgradient(spread: pad, cx: 0.5, cy: 0.5, radius: 0.5, fx: 0.5, fy: 0.5, stop: 0.6 #F0F0F0, stop:0.778409 #5CACEE);\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"    background: qradialgradient(spread: pad, cx: 0.5, cy: 0.5, radius: 0.5, fx: 0.5, fy: 0.5, stop: 0.6 #F0F0F0,stop:0.778409 #1B89CA);\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    width:10px; \n"
"    background-color:rgba(0,0,0,0%); \n"
"    padding-top:10px; \n"
"    padding-bottom:10px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    height:10px; \n"
"    background-color:rgba(0,0,0,0%); \n"
"    padding-left:10px; padding-right:10px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    width:10px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5CACEE, stop:1 #4F94CD); \n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    height:10px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5CACEE, stop:1 #4F94CD); \n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    width:10px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5); \n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    height:10px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5); \n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    height:10px;\n"
"    width:10px;\n"
"    subcontrol-position: bottom; \n"
"    subcontrol-origin: margin;\n"
"    border-image: url(:/qss-icons/resources/qss-icons/add-line_vertical.png);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    height:10px;\n"
"    width:10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"    border-image: url(:/qss-icons/resources/qss-icons/add-line_horizontal.png);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    height:10px;\n"
"    width:10px;\n"
"    subcontrol-position: top; \n"
"    subcontrol-origin: margin;\n"
"    border-image: url(:/qss-icons/resources/qss-icons/sub-line_vertical.png);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    height:10px;\n"
"    width:10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"    border-image: url(:/qss-icons/resources/qss-icons/sub-line_horizontal.png);\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical {\n"
"    width:10px;\n"
"    background: #C0C0C0;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal {\n"
"    height:10px;\n"
"    background: #C0C0C0;\n"
"}\n"
"\n"
"QScrollArea {\n"
"    border: 0px ; \n"
"}\n"
"\n"
"QTreeView,QListView,QTableView{\n"
"    border: 1px solid #5CACEE; \n"
"    selection-background-color: #1B89CA;\n"
"    selection-color: #F0F0F0;\n"
"}\n"
"\n"
"QTableView::item:selected, QListView::item:selected, QTreeView::item:selected {\n"
"    color: #F0F0F0;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5); \n"
"}\n"
"\n"
"QTableView::item:hover, QListView::item:hover, QTreeView::item:hover {\n"
"    color: #F0F0F0;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5CACEE, stop:1 #4F94CD); \n"
"}\n"
"\n"
"QTableView::item, QListView::item, QTreeView::item {\n"
"    padding: 5px; \n"
"    margin: 0px; \n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    padding:3px;\n"
"    margin:0px;\n"
"    color:#F0F0F0;\n"
"    border: 1px solid #F0F0F0;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5CACEE, stop:1 #4F94CD);\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border-bottom-left-radius:0px;\n"
"    border-bottom-right-radius:0px;\n"
"    color: #F0F0F0;\n"
"    min-width: 60px;\n"
"    min-height: 20px;\n"
"    padding: 3px 8px 3px 8px;\n"
"    margin:1px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5CACEE, stop:1 #4F94CD); \n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5); \n"
"}\n"
"\n"
"QStatusBar::item {\n"
"     border: 1px solid #5CACEE;\n"
"     border-radius: 3px;\n"
"}\n"
"\n"
"QMainWindow {\n"
"  background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.4 rgb(194, 216, 242),\n"
"                                 stop: 0.4 rgb(194, 216, 242), stop: 1.0 rgb(156, 193, 239));\n"
"  color:rgb(59, 90, 130);\n"
"}\n"
"\n"
"QWidget{\n"
"  background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.4 rgb(194, 216, 242),\n"
"                                 stop: 0.4 rgb(194, 216, 242), stop: 1.0 rgb(156, 193, 239));\n"
"  color:rgb(59, 90, 130);\n"
"}\n"
"\n"
"QDockWidget > QWidget  {\n"
"  border-style:none;\n"
"  background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.4 rgb(194, 216, 242),\n"
"                                 stop: 0.4 rgb(194, 216, 242), stop: 1.0 rgb(156, 193, 239));\n"
"  \n"
"  padding:1px;\n"
"  border-radius: 0px;\n"
"  \n"
"  border-top: 2px solid rgb(136, 163, 205);\n"
"  border-left: 2px solid rgb(136, 163, 205);\n"
"  border-bottom: 1px solid rgb(255, 255, 255);\n"
"  border-right: 1px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QWidget > QDockWidget  {\n"
"   background:white;\n"
"}\n"
"\n"
"QCalendarWidget > QWidget > QToolButton {\n"
"  border-style:none;\n"
"  color:rgb(59, 90, 130);\n"
"  background:transparent;\n"
"  padding:1px;\n"
"  border-radius: 0px;\n"
"}\n"
"\n"
"QCalendarWidget > QWidget#qt_calendar_navigationbar{\n"
"  border-top: 2px solid rgb(136, 163, 205);\n"
"  border-left: 2px solid rgb(136, 163, 205);\n"
"  border-bottom: 1px solid rgb(255, 255, 255);\n"
"  border-right: 1px solid rgb(255, 255, 255);\n"
"  background:transparent;\n"
"  border-top-left-radius: 8px;\n"
"  border-top-right-radius: 8px;    \n"
"}\n"
"\n"
"QCalendarWidget > QWidget#qt_calendar_calendarview  {\n"
"  border-top: 2px solid rgb(136, 163, 205);\n"
"  border-left: 2px solid rgb(136, 163, 205);\n"
"  border-bottom: 1px solid rgb(255, 255, 255);\n"
"  border-right: 1px solid rgb(255, 255, 255);\n"
"  background:white;\n"
"  border-radius: 0px;\n"
"  border-bottom-left-radius: 8px;\n"
"  border-bottom-right-radius: 8px;        \n"
"}\n"
"\n"
"QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex;\n"
"    font-size: 11px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 3px;\n"
"}\n"
"\n"
"QTabWidget::pane {  \n"
"   margin: 1px, 1px, 1px, 1px;\n"
"   border-left: 1px solid rgb(255, 255, 255);\n"
"   border-top: 1px solid rgb(255, 255, 255);\n"
"   border-bottom: 2px solid rgb(136, 163, 205);\n"
"   border-right: 2px solid rgb(136, 163, 205);\n"
"   border-radius: 8px;\n"
"   border-top-left-radius: 0px;\n"
"   padding: 0px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"\n"
"  background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.4 rgb(194, 216, 242),\n"
"                                 stop: 0.4 rgb(194, 216, 242), stop: 1.0 rgb(217, 231, 247));\n"
"  border-left: 1px solid rgb(255, 255, 255);\n"
"  border-top: 1px solid rgb(255, 255, 255);\n"
"  border-bottom: 1px solid rgb(136, 163, 205);\n"
"  border-right: 1px solid rgb(136, 163, 205);\n"
"  border-top-right-radius: 15;\n"
"  border-top-left-radius: 5;    \n"
"  color:rgb(59, 90, 130);\n"
"  padding:5px;\n"
"  min-width: 80px;\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected {\n"
"margin-top: 3px; /* make non-selected tabs look smaller */\n"
"} \n"
"\n"
"QTabBar::tab:first {\n"
"  background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.4 rgb(194, 216, 242),\n"
"                                 stop: 0.4 rgb(194, 216, 242), stop: 1.0 rgb(217, 231, 247));\n"
"\n"
"  border-left: 1px solid rgb(255, 255, 255);\n"
"  border-top: 1px solid rgb(255, 255, 255);\n"
"  border-bottom: 1px solid rgb(136, 163, 205);\n"
"  border-right: 1px solid rgb(136, 163, 205);\n"
"  border-top-right-radius: 15;\n"
"  border-top-left-radius: 5;    \n"
"  color:rgb(59, 90, 130);\n"
"  padding:5px;\n"
"}\n"
"\n"
"QTabBar::tab::selected {\n"
"  background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.8 rgb(194, 216, 242),\n"
"                                 stop: 0.2 rgb(194, 216, 242), stop: 1.0 rgb(217, 231, 247));\n"
"  border-left: 1px solid rgb(255, 255, 255);\n"
"  border-top: 1px solid rgb(255, 255, 255);\n"
"  border-bottom: 1px solid rgb(136, 163, 205);\n"
"  border-right: 2px solid rgb(136, 163, 205);\n"
"  border-top-right-radius: 15;\n"
"  border-top-left-radius: 5;    \n"
"  color:rgb(59, 90, 130);\n"
"  padding:5px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"left: 0px; /* move to the right by 5px */\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0  rgb(217, 231, 247), stop: 0.8 rgb(194, 216, 242),\n"
"stop: 0.2 rgb(194, 216, 242), stop: 1.0 rgb(217, 231, 247));\n"
"}    \n"
"\n"
"QPushButton:hover, QToolButton:hover, QCheckBox:hover, QRadioButton:hover {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0  rgb(217, 231, 247), stop: 0.8 rgb(194, 216, 242),\n"
"stop: 0.2 rgb(194, 216, 242), stop: 1.0 rgb(217, 231, 247));\n"
"}\n"
" \n"
"QComboBox:!editable {\n"
"   min-width: 80px;  \n"
"   min-height: 19px; \n"
"   background-color:transparent;\n"
"   border-left: 1px solid rgb(255, 255, 255);\n"
"   border-top: 1px solid rgb(255, 255, 255);\n"
"   border-bottom: 2px solid rgb(136, 163, 205);\n"
"   border-right: 2px solid rgb(136, 163, 205);\n"
"   background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"   padding:3px;\n"
"   border-radius: 8px;\n"
"}\n"
"\n"
"QComboBox:!editable:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0  rgb(217, 231, 247), stop: 0.8 rgb(194, 216, 242),\n"
"stop: 0.2 rgb(194, 216, 242), stop: 1.0 rgb(217, 231, 247));\n"
"}\n"
"\n"
"QComboBox:!editable:on {\n"
"   min-width: 80px;  \n"
"   min-height: 19px; \n"
"   background:transparent;\n"
"   border-right: 1px solid rgb(255, 255, 255);\n"
"   border-bottom: 1px solid rgb(255, 255, 255);\n"
"   border-top: 2px solid rgb(136, 163, 205);\n"
"   border-left: 2px solid rgb(136, 163, 205);\n"
"   background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"   padding:3px;\n"
"   border-radius: 8px;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"   min-width: 80px;  \n"
"   min-height: 18px; \n"
"   border-right: 1px solid rgb(255, 255, 255);\n"
"   border-bottom: 1px solid rgb(255, 255, 255);\n"
"   border-top: 2px solid rgb(136, 163, 205);\n"
"   border-left: 2px solid rgb(136, 163, 205);\n"
"   background:white;\n"
"   padding:3px;\n"
"   border-radius: 8px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background-color: transparent;\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"}\n"
" \n"
"QComboBox QAbstractItemView {\n"
"   border: 1px solid gray;\n"
"}\n"
"\n"
"QLabel {  \n"
"  background-color:transparent;\n"
"}\n"
"\n"
"QLineEdit, QTextEdit {  \n"
"   background:white;\n"
"   min-width: 80px;  \n"
"   min-height: 16px; \n"
"   border-right: 1px solid rgb(255, 255, 255);\n"
"   border-bottom: 1px solid rgb(255, 255, 255);\n"
"   border-top: 2px solid rgb(136, 163, 205);\n"
"   border-left: 2px solid rgb(136, 163, 205);\n"
"   \n"
"   padding:3px;\n"
"   border-radius: 8px;\n"
"}\n"
"\n"
"QRadioButton {  \n"
"   background:transparent;\n"
"   min-width: 80px;  \n"
"   min-height: 20px; \n"
"   border-left: 1px solid rgb(255, 255, 255);\n"
"   border-top: 1px solid rgb(255, 255, 255);\n"
"   border-bottom: 2px solid rgb(136, 163, 205);\n"
"   border-right: 2px solid rgb(136, 163, 205);\n"
"   background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"  \n"
"   padding:3px;\n"
"   border-radius: 8px;\n"
"}\n"
"\n"
"QCheckBox {  \n"
"   background:transparent;\n"
"   min-width: 80px;  \n"
"   min-height: 20px; \n"
"   border-left: 1px solid rgb(255, 255, 255);\n"
"   border-top: 1px solid rgb(255, 255, 255);\n"
"   border-bottom: 2px solid rgb(136, 163, 205);\n"
"   border-right: 2px solid rgb(136, 163, 205);\n"
"   background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"  \n"
"   padding:3px;\n"
"   border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  border-style:none;\n"
"  min-width: 80px;  \n"
"  min-height: 20px;    \n"
"  border-left: 1px solid rgb(255, 255, 255);\n"
"  border-top: 1px solid rgb(255, 255, 255);\n"
"    \n"
"  border-bottom: 2px solid rgb(136, 163, 205);\n"
"  border-right: 2px solid rgb(136, 163, 205);\n"
"  color:rgb(59, 90, 130);\n"
"  background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"  padding:3px;\n"
"  border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"  border-style:none;   \n"
"  border-top: 2px solid rgb(136, 163, 205);\n"
"  border-left: 2px solid rgb(136, 163, 205);\n"
"    \n"
"  border-bottom: 1px solid rgb(255, 255, 255);\n"
"  border-right: 1px solid rgb(255, 255, 255);\n"
"    \n"
"  color:rgb(59, 90, 130);\n"
"  background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"  padding:3px;\n"
"  border-radius: 8px;\n"
"}\n"
"\n"
"QToolButton {\n"
"  border-style:none;\n"
"  min-width: 80px;  \n"
"  min-height: 16px;     \n"
"  border-left: 1px solid rgb(255, 255, 255);\n"
"  border-top: 1px solid rgb(255, 255, 255);\n"
"    \n"
"  border-bottom: 2px solid rgb(136, 163, 205);\n"
"  border-right: 2px solid rgb(136, 163, 205);\n"
"  color:rgb(59, 90, 130);\n"
"  background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"  padding:3px;\n"
"  border-radius: 8px;\n"
"}\n"
"\n"
"QCheckBox:checked, QRadioButton:checked {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0  rgb(217, 231, 247), stop: 0.8 rgb(194, 216, 242),\n"
"stop: 0.2 rgb(194, 216, 242), stop: 1.0 rgb(217, 231, 247));\n"
"   border-right: 2px solid rgb(255, 255, 255);\n"
"  border-bottom: 2px solid rgb(255, 255, 255);\n"
"  border-top: 2px solid rgb(136, 163, 205);\n"
"  border-left: 2px solid rgb(136, 163, 205);\n"
"}\n"
"\n"
"QCheckBox:indeterminate {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0  rgb(217, 231, 247), stop: 0.8 rgb(194, 216, 242),\n"
"stop: 0.2 rgb(194, 216, 242), stop: 1.0 rgb(217, 231, 247));\n"
"  border-right: 1px solid rgb(255, 255, 255);\n"
"  border-bottom: 1px solid rgb(255, 255, 255);\n"
"    \n"
"  border-top: 1px solid rgb(136, 163, 205);\n"
"  border-left: 1px solid rgb(136, 163, 205);\n"
"}\n"
"\n"
"\n"
"QToolButton:pressed {\n"
"  border-top: 2px solid rgb(136, 163, 205);\n"
"  border-left: 2px solid rgb(136, 163, 205);  \n"
"  border-bottom: 1px solid rgb(255, 255, 255);\n"
"  border-right: 1px solid rgb(255, 255, 255);\n"
"  color:rgb(59, 90, 130);\n"
"  background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"  padding:3px;\n"
"  border-radius: 8px;\n"
"}\n"
"\n"
"QMenu{\n"
"  background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"  color:rgb(59, 90, 130);\n"
"}\n"
"\n"
"QMenuBar\n"
"{\n"
"  background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"  color:rgb(59, 90, 130);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTableView {\n"
"  background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"  border-top: 2px solid rgb(136, 163, 205);\n"
"  border-left: 2px solid rgb(136, 163, 205);\n"
"    \n"
"  border-bottom: 1px solid rgb(255, 255, 255);\n"
"  border-right: 1px solid rgb(255, 255, 255);\n"
"  border-radius: 8px;\n"
"  padding: 0 8px;\n"
"  color:rgb(59, 90, 130);\n"
"}\n"
"\n"
"QHeaderView {\n"
"    background: transparent;\n"
"}\n"
"QHeaderView::section {\n"
"    background: transparent;\n"
"    border: 1px solid gray;\n"
"    padding: 3px;\n"
"}\n"
"\n"
"QTreeView {\n"
"  border-top: 2px solid rgb(136, 163, 205);\n"
"  border-left: 2px solid rgb(136, 163, 205);\n"
"  border-bottom: 1px solid rgb(255, 255, 255);\n"
"  border-right: 1px solid rgb(255, 255, 255);\n"
"  color:rgb(59, 90, 130);\n"
"  background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"  border-radius: 8px;\n"
"  show-decoration-selected: 0;\n"
"}\n"
"\n"
"QGroupBox{\n"
"  border-top: 2px solid rgb(136, 163, 205);\n"
"  border-left: 2px solid rgb(136, 163, 205);\n"
"  border-bottom: 1px solid rgb(255, 255, 255);\n"
"  border-right: 1px solid rgb(255, 255, 255);\n"
"  color:rgb(59, 90, 130);\n"
"  background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"  border-radius: 8px;\n"
"}\n"
"\n"
"QToolBox {\n"
"  border-top: 2px solid rgb(136, 163, 205);\n"
"  border-left: 2px solid rgb(136, 163, 205);\n"
"  border-bottom: 1px solid rgb(255, 255, 255);\n"
"  border-right: 1px solid rgb(255, 255, 255);\n"
"  color:rgb(59, 90, 130);\n"
"  background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"  border-radius: 8px;\n"
"}\n"
"\n"
"QListWidget {\n"
"  border-top: 2px solid rgb(136, 163, 205);\n"
"  border-left: 2px solid rgb(136, 163, 205);\n"
"  border-bottom: 1px solid rgb(255, 255, 255);\n"
"  border-right: 1px solid rgb(255, 255, 255);\n"
"  color:rgb(59, 90, 130);\n"
"  background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"  border-radius: 8px;\n"
"  show-decoration-selected: 1;\n"
"}\n"
"\n"
"QToolBox > QWidget {\n"
"  border-top: 2px solid rgb(136, 163, 205);\n"
"  border-left: 2px solid rgb(136, 163, 205);\n"
"  border-bottom: 1px solid rgb(255, 255, 255);\n"
"  border-right: 1px solid rgb(255, 255, 255);\n"
"  color:rgb(59, 90, 130);\n"
"  background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"  border-radius: 8px;\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"  border-top: 2px solid rgb(136, 163, 205);\n"
"  border-left: 2px solid rgb(136, 163, 205);\n"
"  border-bottom: 1px solid rgb(255, 255, 255);\n"
"  border-right: 1px solid rgb(255, 255, 255);\n"
"  color:rgb(59, 90, 130);\n"
"  background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"  border-radius: 8px;\n"
"}\n"
"\n"
"QSpinBox   {  \n"
"   background:white;\n"
"   border-right: 1px solid rgb(255, 255, 255);\n"
"   border-bottom: 1px solid rgb(255, 255, 255);\n"
"   border-top: 2px solid rgb(136, 163, 205);\n"
"   border-left: 2px solid rgb(136, 163, 205);\n"
"   \n"
"   padding:3px;\n"
"   border-radius: 8px;\n"
"}\n"
"\n"
"QDoubleSpinBox  {  \n"
"   background:white;\n"
"   border-right: 1px solid rgb(255, 255, 255);\n"
"   border-bottom: 1px solid rgb(255, 255, 255);\n"
"   border-top: 2px solid rgb(136, 163, 205);\n"
"   border-left: 2px solid rgb(136, 163, 205);\n"
"   \n"
"   padding:3px;\n"
"   border-radius: 8px;\n"
"}\n"
"\n"
"QDateEdit  {  \n"
"   background:white;\n"
"   border-right: 1px solid rgb(255, 255, 255);\n"
"   border-bottom: 1px solid rgb(255, 255, 255);\n"
"   border-top: 2px solid rgb(136, 163, 205);\n"
"   border-left: 2px solid rgb(136, 163, 205);\n"
"   \n"
"   padding:3px;\n"
"   border-radius: 8px;\n"
"}\n"
"\n"
"QTimeEdit   {  \n"
"   background:white;\n"
"   border-right: 1px solid rgb(255, 255, 255);\n"
"   border-bottom: 1px solid rgb(255, 255, 255);\n"
"   border-top: 2px solid rgb(136, 163, 205);\n"
"   border-left: 2px solid rgb(136, 163, 205);\n"
"   \n"
"   padding:3px;\n"
"   border-radius: 8px;\n"
"}\n"
"\n"
"QDateTimeEdit   {  \n"
"   background:white;\n"
"   border-right: 1px solid rgb(255, 255, 255);\n"
"   border-bottom: 1px solid rgb(255, 255, 255);\n"
"   border-top: 2px solid rgb(136, 163, 205);\n"
"   border-left: 2px solid rgb(136, 163, 205);\n"
"   \n"
"   padding:3px;\n"
"   border-radius: 8px;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: margin; \n"
"    subcontrol-position: top right; \n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"    border-top-right-radius: 8px; \n"
"    border-width: 1px; \n"
"    width: 16px; \n"
"    border-top: 2px solid rgb(136, 163, 205);\n"
" } \n"
" \n"
"QDoubleSpinBox::up-button {\n"
"    subcontrol-origin: margin; \n"
"    subcontrol-position: top right; \n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"    border-top-right-radius: 8px; \n"
"    border-width: 1px; \n"
"    width: 16px; \n"
"    border-top: 2px solid rgb(136, 163, 205);\n"
" } \n"
" \n"
" QDateEdit::up-button  {\n"
"    subcontrol-origin: margin; \n"
"    subcontrol-position: top right; \n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"    border-top-right-radius: 8px; \n"
"    border-width: 1px; \n"
"    width: 16px; \n"
"    border-top: 2px solid rgb(136, 163, 205);\n"
" } \n"
" \n"
" QTimeEdit::up-button  {\n"
"    subcontrol-origin: margin; \n"
"    subcontrol-position: top right; \n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"    border-top-right-radius: 8px; \n"
"    border-width: 1px; \n"
"    width: 16px; \n"
"    border-top: 2px solid rgb(136, 163, 205);\n"
" } \n"
" \n"
"QDateTimeEdit::up-button  {\n"
"    subcontrol-origin: margin; \n"
"    subcontrol-position: top right; \n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"    border-top-right-radius: 8px; \n"
"    border-width: 1px; \n"
"    width: 16px; \n"
"    border-top: 2px solid rgb(136, 163, 205);\n"
" } \n"
"\n"
"QSpinBox::up-arrow{ \n"
"    background-color: transparent;\n"
"    border-left: 3px solid none;\n"
"    border-right: 3px solid none; \n"
"    border-bottom: 3px solid #808080; \n"
"    width: 1px; \n"
"    height: 1px; \n"
"}\n"
"\n"
"QDoubleSpinBox::up-arrow { \n"
"    background-color: transparent;\n"
"    border-left: 3px solid none;\n"
"    border-right: 3px solid none; \n"
"    border-bottom: 3px solid #808080; \n"
"    width: 1px; \n"
"    height: 1px; \n"
"}\n"
"\n"
"QDateEdit::up-arrow { \n"
"    background-color: transparent;\n"
"    border-left: 3px solid none;\n"
"    border-right: 3px solid none; \n"
"    border-bottom: 3px solid #808080; \n"
"    width: 1px; \n"
"    height: 1px; \n"
"}\n"
"\n"
"QTimeEdit::up-arrow { \n"
"    background-color: transparent;\n"
"    border-left: 3px solid none;\n"
"    border-right: 3px solid none; \n"
"    border-bottom: 3px solid #808080; \n"
"    width: 1px; \n"
"    height: 1px; \n"
"}\n"
"\n"
"QSpinBox::up-button:pressed {\n"
"    subcontrol-origin: margin; \n"
"    subcontrol-position: top right; \n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"    border-top-right-radius: 8px; \n"
"    border-width: 1px; \n"
"    width: 15px; \n"
"    border-left: 1px solid #BEBEBE; \n"
"    border-top: 3px solid rgb(136, 163, 205);\n"
" } \n"
" \n"
"QDoubleSpinBox::up-button:pressed {\n"
"    subcontrol-origin: margin; \n"
"    subcontrol-position: top right; \n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"    border-top-right-radius: 8px; \n"
"    border-width: 1px; \n"
"    width: 15px; \n"
"    border-left: 1px solid #BEBEBE; \n"
"    border-top: 3px solid rgb(136, 163, 205);\n"
" } \n"
" \n"
" QDateEdit::up-button:pressed  {\n"
"    subcontrol-origin: margin; \n"
"    subcontrol-position: top right; \n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"    border-top-right-radius: 8px; \n"
"    border-width: 1px; \n"
"    width: 15px; \n"
"    border-left: 1px solid #BEBEBE; \n"
"    border-top: 3px solid rgb(136, 163, 205);\n"
" } \n"
" \n"
" QTimeEdit::up-button:pressed  {\n"
"    subcontrol-origin: margin; \n"
"    subcontrol-position: top right; \n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"    border-top-right-radius: 8px; \n"
"    border-width: 1px; \n"
"    width: 15px; \n"
"    border-left: 1px solid #BEBEBE; \n"
"    border-top: 3px solid rgb(136, 163, 205);\n"
" } \n"
" \n"
"QDateTimeEdit::up-button:pressed  {\n"
"    subcontrol-origin: margin; \n"
"    subcontrol-position: top right; \n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"    border-top-right-radius: 8px; \n"
"    border-width: 1px; \n"
"    width: 15px; \n"
"    border-left: 1px solid #BEBEBE; \n"
"    border-top: 3px solid rgb(136, 163, 205);\n"
" } \n"
" \n"
" QSpinBox::up-arrow:pressed { \n"
"    background-color: transparent;\n"
"    border-left: 3px solid none;\n"
"    border-right: 3px solid none; \n"
"    border-bottom: 3px solid #808080; \n"
"    width: 1px; \n"
"    height: 1px; \n"
"}\n"
"\n"
" QDoubleSpinBox::up-arrow:pressed { \n"
"    background-color: transparent;\n"
"    border-left: 3px solid none;\n"
"    border-right: 3px solid none; \n"
"    border-bottom: 3px solid #808080; \n"
"    width: 1px; \n"
"    height: 1px; \n"
"}\n"
"\n"
" QDateEdit::up-arrow:pressed { \n"
"    background-color: transparent;\n"
"    border-left: 3px solid none;\n"
"    border-right: 3px solid none; \n"
"    border-bottom: 3px solid #808080; \n"
"    width: 1px; \n"
"    height: 1px; \n"
"}\n"
"\n"
" QTimeEdit::up-arrow:pressed { \n"
"    background-color: transparent;\n"
"    border-left: 3px solid none;\n"
"    border-right: 3px solid none; \n"
"    border-bottom: 3px solid #808080; \n"
"    width: 1px; \n"
"    height: 1px; \n"
"}\n"
"\n"
" QSpinBox::down-button {\n"
"    subcontrol-origin: margin; \n"
"    subcontrol-position: bottom right; \n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"    border-bottom-right-radius: 8px; \n"
"    border-width: 1px; \n"
"    width: 16px; \n"
"    border-bottom: 0px;\n"
" } \n"
" \n"
" QDoubleSpinBox::down-button {\n"
"    subcontrol-origin: margin; \n"
"    subcontrol-position: bottom right; \n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"    border-bottom-right-radius: 8px; \n"
"    border-width: 1px; \n"
"    width: 16px; \n"
"    border-bottom: 0px;\n"
" } \n"
" \n"
"  QDateEdit::down-button {\n"
"    subcontrol-origin: margin; \n"
"    subcontrol-position: bottom right; \n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"    border-bottom-right-radius: 8px; \n"
"    border-width: 1px; \n"
"    width: 16px; \n"
"    border-bottom: 0px;\n"
" } \n"
" \n"
"  QTimeEdit::down-button {\n"
"    subcontrol-origin: margin; \n"
"    subcontrol-position: bottom right; \n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"    border-bottom-right-radius: 8px; \n"
"    border-width: 1px; \n"
"    width: 16px; \n"
"    border-bottom: 0px;\n"
" } \n"
"\n"
" QDateTimeEdit::down-button {\n"
"    subcontrol-origin: margin; \n"
"    subcontrol-position: bottom right; \n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"    border-bottom-right-radius: 8px; \n"
"    border-width: 1px; \n"
"    width: 16px; \n"
"    border-bottom: 0px;\n"
" } \n"
"\n"
"QSpinBox::down-arrow  { \n"
"    background-color: transparent;\n"
"    border-left: 3px solid none;\n"
"    border-right: 3px solid none; \n"
"    border-top: 3px solid #808080; \n"
"    width: 1px; \n"
"    height: 1px; \n"
"}\n"
"\n"
"QDoubleSpinBox::down-arrow { \n"
"    background-color: transparent;\n"
"    border-left: 3px solid none;\n"
"    border-right: 3px solid none; \n"
"    border-top: 3px solid #808080; \n"
"    width: 1px; \n"
"    height: 1px; \n"
"}\n"
"\n"
"QDateEdit::down-arrow { \n"
"    background-color: transparent;\n"
"    border-left: 3px solid none;\n"
"    border-right: 3px solid none; \n"
"    border-top: 3px solid #808080; \n"
"    width: 1px; \n"
"    height: 1px; \n"
"}\n"
"\n"
"QTimeEdit::down-arrow { \n"
"    background-color: transparent;\n"
"    border-left: 3px solid none;\n"
"    border-right: 3px solid none; \n"
"    border-top: 3px solid #808080; \n"
"    width: 1px; \n"
"    height: 1px; \n"
"}\n"
"\n"
"QSpinBox::down-button:pressed  {\n"
"    subcontrol-origin: margin; \n"
"    subcontrol-position: bottom right; \n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"    border-bottom-right-radius: 8px; \n"
"    border-width: 1px; \n"
"    width: 14px; \n"
"    border-left: 1px solid #BEBEBE; \n"
"    border-top: 1px solid #BEBEBE; \n"
"    border-right: 1px solid #BEBEBE; \n"
"    border-bottom: 0px;\n"
" } \n"
" \n"
"QDoubleSpinBox::down-button:pressed {\n"
"    subcontrol-origin: margin; \n"
"    subcontrol-position: bottom right; \n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"    border-bottom-right-radius: 8px; \n"
"    border-width: 1px; \n"
"    width: 14px; \n"
"    border-left: 1px solid #BEBEBE; \n"
"    border-top: 1px solid #BEBEBE; \n"
"    border-right: 1px solid #BEBEBE; \n"
"    border-bottom: 0px;\n"
" } \n"
" \n"
" QDateEdit::down-button:pressed  {\n"
"    subcontrol-origin: margin; \n"
"    subcontrol-position: bottom right; \n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"    border-bottom-right-radius: 8px; \n"
"    border-width: 1px; \n"
"    width: 14px; \n"
"    border-left: 1px solid #BEBEBE; \n"
"    border-top: 1px solid #BEBEBE; \n"
"    border-right: 1px solid #BEBEBE; \n"
"    border-bottom: 0px;\n"
" } \n"
" \n"
" QTimeEdit::down-button:pressed  {\n"
"    subcontrol-origin: margin; \n"
"    subcontrol-position: bottom right; \n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"    border-bottom-right-radius: 8px; \n"
"    border-width: 1px; \n"
"    width: 14px; \n"
"    border-left: 1px solid #BEBEBE; \n"
"    border-top: 1px solid #BEBEBE; \n"
"    border-right: 1px solid #BEBEBE; \n"
"    border-bottom: 0px;\n"
" } \n"
" \n"
"QDateTimeEdit::down-button:pressed  {\n"
"    subcontrol-origin: margin; \n"
"    subcontrol-position: bottom right; \n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0  rgb(217, 231, 247), stop: 0.1 rgb(194, 216, 242),\n"
"                                 stop: 0.5 rgb(194, 216, 242), stop: 1.0 rgb(174, 204, 242));\n"
"    border-bottom-right-radius: 8px; \n"
"    border-width: 1px; \n"
"    width: 14px; \n"
"    border-left: 1px solid #BEBEBE; \n"
"    border-top: 1px solid #BEBEBE; \n"
"    border-right: 1px solid #BEBEBE; \n"
"    border-bottom: 0px;\n"
" } \n"
" \n"
"QSpinBox::down-arrow:pressed   { \n"
"    background-color: transparent;\n"
"    border-left: 3px solid none;\n"
"    border-right: 3px solid none; \n"
"    border-top: 3px solid #808080; \n"
"    width: 1px; \n"
"    height: 1px; \n"
"}\n"
"\n"
"QDoubleSpinBox::down-arrow:pressed { \n"
"    background-color: transparent;\n"
"    border-left: 3px solid none;\n"
"    border-right: 3px solid none; \n"
"    border-top: 3px solid #808080; \n"
"    width: 1px; \n"
"    height: 1px; \n"
"}\n"
"\n"
"QDateEdit::down-arrow:pressed { \n"
"    background-color: transparent;\n"
"    border-left: 3px solid none;\n"
"    border-right: 3px solid none; \n"
"    border-top: 3px solid #808080; \n"
"    width: 1px; \n"
"    height: 1px; \n"
"} \n"
" \n"
"QTimeEdit::down-arrow:pressed { \n"
"    background-color: transparent;\n"
"    border-left: 3px solid none;\n"
"    border-right: 3px solid none; \n"
"    border-top: 3px solid #808080; \n"
"    width: 1px; \n"
"    height: 1px; \n"
"} \n"
"\n"
"QHeaderView::section {\n"
"    color: black\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.setComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.setComboBox.setObjectName("setComboBox")
        self.setComboBox.addItem("")
        self.setComboBox.addItem("")
        self.setComboBox.addItem("")
        self.setComboBox.addItem("")
        self.setComboBox.addItem("")
        self.setComboBox.addItem("")
        self.setComboBox.addItem("")
        self.setComboBox.addItem("")
        self.setComboBox.addItem("")
        self.setComboBox.addItem("")
        self.setComboBox.addItem("")
        self.setComboBox.addItem("")
        self.setComboBox.addItem("")
        self.setComboBox.addItem("")
        self.setComboBox.addItem("")
        self.setComboBox.addItem("")
        self.setComboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.setComboBox)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.slotComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.slotComboBox.setObjectName("slotComboBox")
        self.slotComboBox.addItem("")
        self.slotComboBox.addItem("")
        self.slotComboBox.addItem("")
        self.slotComboBox.addItem("")
        self.slotComboBox.addItem("")
        self.slotComboBox.addItem("")
        self.slotComboBox.addItem("")
        self.slotComboBox.addItem("")
        self.slotComboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.slotComboBox)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.starsComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.starsComboBox.setMinimumSize(QtCore.QSize(89, 28))
        self.starsComboBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.starsComboBox.setObjectName("starsComboBox")
        self.starsComboBox.addItem("")
        self.starsComboBox.addItem("")
        self.starsComboBox.addItem("")
        self.starsComboBox.addItem("")
        self.starsComboBox.addItem("")
        self.starsComboBox.addItem("")
        self.starsComboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.starsComboBox)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.minLevelComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.minLevelComboBox.setMinimumSize(QtCore.QSize(89, 28))
        self.minLevelComboBox.setMaximumSize(QtCore.QSize(40, 16777215))
        self.minLevelComboBox.setObjectName("minLevelComboBox")
        self.minLevelComboBox.addItem("")
        self.minLevelComboBox.addItem("")
        self.minLevelComboBox.addItem("")
        self.minLevelComboBox.addItem("")
        self.minLevelComboBox.addItem("")
        self.minLevelComboBox.addItem("")
        self.minLevelComboBox.addItem("")
        self.minLevelComboBox.addItem("")
        self.minLevelComboBox.addItem("")
        self.minLevelComboBox.addItem("")
        self.minLevelComboBox.addItem("")
        self.minLevelComboBox.addItem("")
        self.minLevelComboBox.addItem("")
        self.minLevelComboBox.addItem("")
        self.minLevelComboBox.addItem("")
        self.minLevelComboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.minLevelComboBox)
        self.maxLevelComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.maxLevelComboBox.setMinimumSize(QtCore.QSize(89, 28))
        self.maxLevelComboBox.setMaximumSize(QtCore.QSize(40, 16777215))
        self.maxLevelComboBox.setObjectName("maxLevelComboBox")
        self.maxLevelComboBox.addItem("")
        self.maxLevelComboBox.addItem("")
        self.maxLevelComboBox.addItem("")
        self.maxLevelComboBox.addItem("")
        self.maxLevelComboBox.addItem("")
        self.maxLevelComboBox.addItem("")
        self.maxLevelComboBox.addItem("")
        self.maxLevelComboBox.addItem("")
        self.maxLevelComboBox.addItem("")
        self.maxLevelComboBox.addItem("")
        self.maxLevelComboBox.addItem("")
        self.maxLevelComboBox.addItem("")
        self.maxLevelComboBox.addItem("")
        self.maxLevelComboBox.addItem("")
        self.maxLevelComboBox.addItem("")
        self.maxLevelComboBox.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.maxLevelComboBox)
        self.horizontalLayout_6.addLayout(self.formLayout)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.mainstatComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.mainstatComboBox.setMinimumSize(QtCore.QSize(89, 28))
        self.mainstatComboBox.setMaximumSize(QtCore.QSize(60, 16777215))
        self.mainstatComboBox.setObjectName("mainstatComboBox")
        self.mainstatComboBox.addItem("")
        self.mainstatComboBox.addItem("")
        self.mainstatComboBox.addItem("")
        self.mainstatComboBox.addItem("")
        self.mainstatComboBox.addItem("")
        self.mainstatComboBox.addItem("")
        self.mainstatComboBox.addItem("")
        self.mainstatComboBox.addItem("")
        self.mainstatComboBox.addItem("")
        self.horizontalLayout_7.addWidget(self.mainstatComboBox)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.equippedComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.equippedComboBox.setMinimumSize(QtCore.QSize(89, 28))
        self.equippedComboBox.setMaximumSize(QtCore.QSize(40, 16777215))
        self.equippedComboBox.setObjectName("equippedComboBox")
        self.equippedComboBox.addItem("")
        self.equippedComboBox.addItem("")
        self.equippedComboBox.addItem("")
        self.horizontalLayout_8.addWidget(self.equippedComboBox)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.statusComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.statusComboBox.setMinimumSize(QtCore.QSize(89, 28))
        self.statusComboBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.statusComboBox.setObjectName("statusComboBox")
        self.statusComboBox.addItem("")
        self.statusComboBox.addItem("")
        self.statusComboBox.addItem("")
        self.statusComboBox.addItem("")
        self.statusComboBox.addItem("")
        self.horizontalLayout_9.addWidget(self.statusComboBox)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.classifyButton = QtWidgets.QPushButton(self.centralwidget)
        self.classifyButton.setObjectName("classifyButton")
        self.horizontalLayout_2.addWidget(self.classifyButton)
        self.filtersButton = QtWidgets.QPushButton(self.centralwidget)
        self.filtersButton.setObjectName("filtersButton")
        self.horizontalLayout_2.addWidget(self.filtersButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.runeTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.runeTableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.runeTableWidget.setShowGrid(False)
        self.runeTableWidget.setCornerButtonEnabled(False)
        self.runeTableWidget.setObjectName("runeTableWidget")
        self.runeTableWidget.setColumnCount(12)
        self.runeTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.runeTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.runeTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.runeTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.runeTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.runeTableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.runeTableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.runeTableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.runeTableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.runeTableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.runeTableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.runeTableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.runeTableWidget.setHorizontalHeaderItem(11, item)
        self.runeTableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.runeTableWidget)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 967, 21))
        self.menubar.setObjectName("menubar")
        self.menuNew = QtWidgets.QMenu(self.menubar)
        self.menuNew.setObjectName("menuNew")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/resources/icons/document-open-8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setIconVisibleInMenu(False)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setIconVisibleInMenu(False)
        self.actionExit.setObjectName("actionExit")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/resources/icons/system-run-6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreferences.setIcon(icon1)
        self.actionPreferences.setIconVisibleInMenu(False)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/resources/icons/help-about-3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon2)
        self.actionAbout.setIconVisibleInMenu(True)
        self.actionAbout.setObjectName("actionAbout")
        self.menuNew.addAction(self.actionOpen)
        self.menuNew.addSeparator()
        self.menuNew.addSeparator()
        self.menuNew.addAction(self.actionExit)
        self.menuSettings.addAction(self.actionPreferences)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuNew.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionPreferences)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Set"))
        self.setComboBox.setCurrentText(_translate("MainWindow", "All"))
        self.setComboBox.setItemText(0, _translate("MainWindow", "All"))
        self.setComboBox.setItemText(1, _translate("MainWindow", "Swift"))
        self.setComboBox.setItemText(2, _translate("MainWindow", "Fatal"))
        self.setComboBox.setItemText(3, _translate("MainWindow", "Despair"))
        self.setComboBox.setItemText(4, _translate("MainWindow", "Violent"))
        self.setComboBox.setItemText(5, _translate("MainWindow", "Rage"))
        self.setComboBox.setItemText(6, _translate("MainWindow", "Vampire"))
        self.setComboBox.setItemText(7, _translate("MainWindow", "Energy"))
        self.setComboBox.setItemText(8, _translate("MainWindow", "Blade"))
        self.setComboBox.setItemText(9, _translate("MainWindow", "Focus"))
        self.setComboBox.setItemText(10, _translate("MainWindow", "Guard"))
        self.setComboBox.setItemText(11, _translate("MainWindow", "Shield"))
        self.setComboBox.setItemText(12, _translate("MainWindow", "Revenge"))
        self.setComboBox.setItemText(13, _translate("MainWindow", "Endure"))
        self.setComboBox.setItemText(14, _translate("MainWindow", "Will"))
        self.setComboBox.setItemText(15, _translate("MainWindow", "Nemesis"))
        self.setComboBox.setItemText(16, _translate("MainWindow", "Destroy"))
        self.label_2.setText(_translate("MainWindow", "Slot"))
        self.slotComboBox.setItemText(0, _translate("MainWindow", "All"))
        self.slotComboBox.setItemText(1, _translate("MainWindow", "Odd"))
        self.slotComboBox.setItemText(2, _translate("MainWindow", "Even"))
        self.slotComboBox.setItemText(3, _translate("MainWindow", "1"))
        self.slotComboBox.setItemText(4, _translate("MainWindow", "2"))
        self.slotComboBox.setItemText(5, _translate("MainWindow", "3"))
        self.slotComboBox.setItemText(6, _translate("MainWindow", "4"))
        self.slotComboBox.setItemText(7, _translate("MainWindow", "5"))
        self.slotComboBox.setItemText(8, _translate("MainWindow", "6"))
        self.label_3.setText(_translate("MainWindow", "Stars"))
        self.starsComboBox.setItemText(0, _translate("MainWindow", "All"))
        self.starsComboBox.setItemText(1, _translate("MainWindow", "1"))
        self.starsComboBox.setItemText(2, _translate("MainWindow", "2"))
        self.starsComboBox.setItemText(3, _translate("MainWindow", "3"))
        self.starsComboBox.setItemText(4, _translate("MainWindow", "4"))
        self.starsComboBox.setItemText(5, _translate("MainWindow", "5"))
        self.starsComboBox.setItemText(6, _translate("MainWindow", "6"))
        self.label_4.setText(_translate("MainWindow", "Level"))
        self.label_7.setText(_translate("MainWindow", "Min"))
        self.label_8.setText(_translate("MainWindow", "Max"))
        self.minLevelComboBox.setItemText(0, _translate("MainWindow", "0"))
        self.minLevelComboBox.setItemText(1, _translate("MainWindow", "1"))
        self.minLevelComboBox.setItemText(2, _translate("MainWindow", "2"))
        self.minLevelComboBox.setItemText(3, _translate("MainWindow", "3"))
        self.minLevelComboBox.setItemText(4, _translate("MainWindow", "4"))
        self.minLevelComboBox.setItemText(5, _translate("MainWindow", "5"))
        self.minLevelComboBox.setItemText(6, _translate("MainWindow", "6"))
        self.minLevelComboBox.setItemText(7, _translate("MainWindow", "7"))
        self.minLevelComboBox.setItemText(8, _translate("MainWindow", "8"))
        self.minLevelComboBox.setItemText(9, _translate("MainWindow", "9"))
        self.minLevelComboBox.setItemText(10, _translate("MainWindow", "10"))
        self.minLevelComboBox.setItemText(11, _translate("MainWindow", "11"))
        self.minLevelComboBox.setItemText(12, _translate("MainWindow", "12"))
        self.minLevelComboBox.setItemText(13, _translate("MainWindow", "13"))
        self.minLevelComboBox.setItemText(14, _translate("MainWindow", "14"))
        self.minLevelComboBox.setItemText(15, _translate("MainWindow", "15"))
        self.maxLevelComboBox.setCurrentText(_translate("MainWindow", "0"))
        self.maxLevelComboBox.setItemText(0, _translate("MainWindow", "0"))
        self.maxLevelComboBox.setItemText(1, _translate("MainWindow", "1"))
        self.maxLevelComboBox.setItemText(2, _translate("MainWindow", "2"))
        self.maxLevelComboBox.setItemText(3, _translate("MainWindow", "3"))
        self.maxLevelComboBox.setItemText(4, _translate("MainWindow", "4"))
        self.maxLevelComboBox.setItemText(5, _translate("MainWindow", "5"))
        self.maxLevelComboBox.setItemText(6, _translate("MainWindow", "6"))
        self.maxLevelComboBox.setItemText(7, _translate("MainWindow", "7"))
        self.maxLevelComboBox.setItemText(8, _translate("MainWindow", "8"))
        self.maxLevelComboBox.setItemText(9, _translate("MainWindow", "9"))
        self.maxLevelComboBox.setItemText(10, _translate("MainWindow", "10"))
        self.maxLevelComboBox.setItemText(11, _translate("MainWindow", "11"))
        self.maxLevelComboBox.setItemText(12, _translate("MainWindow", "12"))
        self.maxLevelComboBox.setItemText(13, _translate("MainWindow", "13"))
        self.maxLevelComboBox.setItemText(14, _translate("MainWindow", "14"))
        self.maxLevelComboBox.setItemText(15, _translate("MainWindow", "15"))
        self.label_5.setText(_translate("MainWindow", "Main Stat"))
        self.mainstatComboBox.setItemText(0, _translate("MainWindow", "All"))
        self.mainstatComboBox.setItemText(1, _translate("MainWindow", "SPD"))
        self.mainstatComboBox.setItemText(2, _translate("MainWindow", "HP"))
        self.mainstatComboBox.setItemText(3, _translate("MainWindow", "DEF"))
        self.mainstatComboBox.setItemText(4, _translate("MainWindow", "ATK"))
        self.mainstatComboBox.setItemText(5, _translate("MainWindow", "CRI Dmg"))
        self.mainstatComboBox.setItemText(6, _translate("MainWindow", "CRI Rate"))
        self.mainstatComboBox.setItemText(7, _translate("MainWindow", "Accuracy"))
        self.mainstatComboBox.setItemText(8, _translate("MainWindow", "Resistance"))
        self.label_6.setText(_translate("MainWindow", "Equipped"))
        self.equippedComboBox.setItemText(0, _translate("MainWindow", "All"))
        self.equippedComboBox.setItemText(1, _translate("MainWindow", "Yes"))
        self.equippedComboBox.setItemText(2, _translate("MainWindow", "No"))
        self.label_9.setText(_translate("MainWindow", "Status"))
        self.statusComboBox.setItemText(0, _translate("MainWindow", "All"))
        self.statusComboBox.setItemText(1, _translate("MainWindow", "Check"))
        self.statusComboBox.setItemText(2, _translate("MainWindow", "Sell"))
        self.statusComboBox.setItemText(3, _translate("MainWindow", "Keep"))
        self.statusComboBox.setItemText(4, _translate("MainWindow", "Reappraise"))
        self.classifyButton.setText(_translate("MainWindow", "Classify"))
        self.filtersButton.setText(_translate("MainWindow", "Apply Filters"))
        self.runeTableWidget.setSortingEnabled(True)
        item = self.runeTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Equipped"))
        item = self.runeTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Original Quality"))
        item = self.runeTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Slot"))
        item = self.runeTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Rune Set"))
        item = self.runeTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Level"))
        item = self.runeTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Stars"))
        item = self.runeTableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Main Stat"))
        item = self.runeTableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Fixed Stat"))
        item = self.runeTableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Substats"))
        item = self.runeTableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Type"))
        item = self.runeTableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "VPM Efficiency"))
        item = self.runeTableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Barion Efficiency"))
        self.menuNew.setTitle(_translate("MainWindow", "New"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

import ui_files.resources_rc