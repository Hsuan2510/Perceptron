# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import sys


class Show_Pic_Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent) 
        # 將matplotlib 帶進 Qt 接口
        self.canvas = FigureCanvas(Figure(figsize=(6, 4)))  # 調整這裡的大小

        self.toolbar = NavigationToolbar(self.canvas, self)  # 加入matplotlib 的 toolbar
        layout = QtWidgets.QVBoxLayout()  # 在視窗上增加放toolbar和畫布的地方
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.canvas.train = self.canvas.figure.add_subplot(121)
        self.canvas.train.set_xlabel("X")
        self.canvas.train.set_ylabel("Y")
        self.canvas.train.set_title("Training Data")
        self.canvas.test = self.canvas.figure.add_subplot(122)
        self.canvas.test.set_xlabel("X")
        self.canvas.test.set_ylabel("Y")
        self.canvas.test.set_title("Test Data")
        self.canvas.figure.subplots_adjust(wspace=0.75) # 
        self.setLayout(layout)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(954, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dataset_button = QtWidgets.QPushButton(self.centralwidget)
        self.dataset_button.setGeometry(QtCore.QRect(50, 420, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.dataset_button.setFont(font)
        self.dataset_button.setObjectName("dataset_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 490, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.epoch_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.epoch_spinBox.setGeometry(QtCore.QRect(170, 490, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.epoch_spinBox.setFont(font)
        self.epoch_spinBox.setObjectName("epoch_spinBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 560, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.learing_rate_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.learing_rate_spinBox.setGeometry(QtCore.QRect(260, 560, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.learing_rate_spinBox.setFont(font)
        self.learing_rate_spinBox.setObjectName("learing_rate_spinBox")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(470, 490, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(470, 540, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(470, 590, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.training_button = QtWidgets.QPushButton(self.centralwidget)
        self.training_button.setGeometry(QtCore.QRect(50, 650, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.training_button.setFont(font)
        self.training_button.setObjectName("training_button")
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(760, 650, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.exit_button.setFont(font)
        self.exit_button.setObjectName("exit_button")
        self.dataset_path = QtWidgets.QTextEdit(self.centralwidget)
        self.dataset_path.setGeometry(QtCore.QRect(220, 420, 681, 41))
        self.dataset_path.setObjectName("dataset_path")
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.exit_button.setFont(font)
        self.training_ac_label = QtWidgets.QTextEdit(self.centralwidget)
        self.training_ac_label.setGeometry(QtCore.QRect(730, 490, 171, 31))
        self.training_ac_label.setObjectName("training_ac_label")
        self.test_ac_label = QtWidgets.QTextEdit(self.centralwidget)
        self.test_ac_label.setGeometry(QtCore.QRect(670, 540, 171, 31))
        self.test_ac_label.setObjectName("test_ac_label")
        self.weight_label = QtWidgets.QTextEdit(self.centralwidget)
        self.weight_label.setGeometry(QtCore.QRect(590, 590, 171, 31))
        self.weight_label.setObjectName("weight_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 954, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.widget = Show_Pic_Widget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, -1, 850, 400))
        self.widget.setObjectName("widget")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dataset_button.setText(_translate("MainWindow", "Dataset"))
        self.label.setText(_translate("MainWindow", "Epoch :"))
        self.label_2.setText(_translate("MainWindow", "Learning rate :"))
        self.label_3.setText(_translate("MainWindow", "Training accuracy :"))
        self.label_4.setText(_translate("MainWindow", "Test accuracy :"))
        self.label_5.setText(_translate("MainWindow", "weight :"))
        self.training_button.setText(_translate("MainWindow", "Training!!"))
        self.exit_button.setText(_translate("MainWindow", "EXIT"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

