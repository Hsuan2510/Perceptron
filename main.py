import sys
from PyQt5 import QtWidgets
from UI import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog
import os

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # 創建 UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 連接按鈕的點擊事件到自訂的方法
        self.ui.dataset_button.clicked.connect(self.load_dataset)
        self.ui.training_button.clicked.connect(self.train_model)
        self.ui.exit_button.clicked.connect(self.exit_application)

    def load_dataset(self):
        # 打開資料夾匯入資料集
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "Open .txt File", "", "Text Files (*.txt);;All Files (*)", options=options)
        self.ui.dataset_path.setText(file_path)

        if file_path:
        # 在這裡您可以打開並讀取所選的 .txt 文件
            with open(file_path, 'r') as file:
                data = file.read()
                # 在這裡處理讀取的資料，對應到您的應用程式需求
                print(data)

    def train_model(self):
        # 在這裡處理訓練模型的邏輯
        pass

    def exit_application(self):
        # 在這裡處理退出應用程式的邏輯
        QtWidgets.QApplication.quit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())