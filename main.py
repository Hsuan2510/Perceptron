import sys
import numpy as np
from PyQt5 import QtGui, QtWidgets
from UI import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog
import matplotlib.pyplot as plt

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # 創建 UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.pts = np.empty([0, 2], float)
        self.pts_group = np.array([], int)
        self.groupID = np.array([], int)
        self.pred = np.array([], int)
        self.train_accuracy = 0
        


        # 連接按鈕的點擊事件到自訂的方法
        self.ui.dataset_button.clicked.connect(self.load_dataset)
        self.ui.training_button.clicked.connect(self.train_model)
        self.ui.exit_button.clicked.connect(self.exit_application)

    def reset(self):
        self.pts = np.empty([0, 2], float)
        self.pts_group = np.array([], int)
        self.groupID = np.array([], int)
        self.train_accuracy = 0
        self.pred = np.array([], int)
        self.epoch = 0
        self.learning_rate = 0
        self.train_accuracy = 0
        self.test_accuracy = 0

    def load_dataset(self):
        # 打開資料夾匯入資料集
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        self.file_path, _ = QFileDialog.getOpenFileName(self, "Open .txt File", "", "Text Files (*.txt);;All Files (*)", options=options)
        self.ui.dataset_path.setText(self.file_path)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.ui.dataset_path.setFont(font)

    def train_model(self):
        self.reset()
        self.epoch = self.ui.epoch_spinBox.value()
        self.learning_rate = self.ui.learing_rate_spinBox.value()

        # print("epoch: ", self.epoch)
        # print("learning rate: ", self.learning_rate)

        # 讀取資料集
        with open(self.file_path, 'r') as file:
            datas = file.readlines()
            for data in datas:
                coord_x, coord_y, d = data.split(" ")
                # 把coord_x, coord_y 存成np.array
                self.pts = np.append(self.pts, np.array([[coord_x, coord_y]], dtype="float64"), axis=0)
                self.pts_group = np.append(self.pts_group, int(d))
                if int(d) not in self.groupID:
                    self.groupID = np.append(self.groupID, int(d))
        self.groupID = np.sort(self.groupID)
        

        # 隨機將2/3的資料分成訓練集，1/3的資料分成測試集
        idx = np.random.permutation(len(self.pts)) # 打散順序
        self.train_size = int(len(self.pts) * (2 / 3))
        self.train_idx = idx[:self.train_size]  # 前2/3的資料當訓練集
        self.test_idx = idx[self.train_size:]  # 後1/3的資料當測試集

        # 預測訓練結果
        w = window.train_predict()
        self.test_predict(w)

        # 畫圖
        self.train_pic(w)
        # self.test_pic(w)
        self.ui.widget.canvas.draw()

    def Activate_function(self,x): # 活化函數
        if x >= 0:
            return self.groupID[0]
        else:
            return self.groupID[1]
        
    def train_predict(self):
        w = np.random.uniform(-1, 1, size=len(self.pts[0])) # 初始化權重 -1~1
        theta = 0
        w = np.concatenate(([theta], w), axis=0)
        print("w: ", w)
        
        for i in range(self.epoch): # 要迭代幾次
            print("epoch: ", i)
            for j in self.train_idx:
                print(j)
                input = self.pts[j]
                input = np.concatenate(([-1], input), axis=0)
                label = self.pts_group[j]
                output = np.dot(input,w)
                pred_result = self.Activate_function(output)
                w = w + self.learning_rate * (label - pred_result) * input

        return w

    def test_predict(self, w):
        for i in self.train_idx:
            input = self.pts[i]
            input = np.concatenate(([-1], input), axis=0)
            output = np.dot(input,w)
            pred_result = self.Activate_function(output)
            self.pred = np.append(self.pred, pred_result)

        for i in self.test_idx:
            input = self.pts[i]
            input = np.concatenate(([-1], input), axis=0)
            output = np.dot(input,w)
            pred_result = self.Activate_function(output)
            self.pred = np.append(self.pred, pred_result)

        return
    
    def train_pic(self, w):
        self.ui.widget.canvas.train.cla() # 清除畫布
        for i in range(len(self.train_idx)):
            j = self.train_idx[i]
            if self.pred[i] == 1:
                print(self.pts[j, 0], self.pts[j, 1])
                print("---")
                self.ui.widget.canvas.train.scatter(self.pts[j, 0], self.pts[j, 1], s=5, color='r')
            else:
                self.ui.widget.canvas.train.scatter(self.pts[j, 0], self.pts[j, 1], s=5, color='b')

            if self.pred[i] == self.pts_group[j]:
                self.train_accuracy += 1

        self.train_accuracy = self.train_accuracy / len(self.train_idx)

        slope = -w[1] / w[2]
        intercept = -w[0] / w[2]
        x = np.array([min(self.pts[:, 0]) - 1, max(self.pts[:, 0]) + 1])
        y = slope * x + intercept

        # 绘制直线
        self.ui.widget.canvas.train.plot(x, y, color='k', lw=3)

        # 设置坐标轴范围
        self.ui.widget.canvas.train.axis(xmin=min(self.pts[:, 0]) - 1, xmax=max(self.pts[:, 0]) + 1)  # 設定x軸顯示範圍
        self.ui.widget.canvas.train.axis(ymin=min(self.pts[:, 1]) - 1, ymax=max(self.pts[:, 1]) + 1)  # 設定y軸顯示範圍
        self.ui.widget.canvas.train.set_xlabel("X")
        self.ui.widget.canvas.train.set_ylabel("Y")
        self.ui.widget.canvas.train.set_title("Train")

        # plt.show()  # 如果需要显示图形，不要忘记这一行

    def exit_application(self):
        # 在這裡處理退出應用程式的邏輯
        QtWidgets.QApplication.quit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())