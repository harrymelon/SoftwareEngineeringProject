from PyQt5.Qt import *
from CustomerView import Ui_Form
import sys


class customer_window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.isRun = 0
        self.WindSpeed = 0

    def switch_click(self):
        if self.isRun == 0:
            print("开机")
            self.tar_temp.setText("25")
            self.mode.setText("制冷")
            self.tar_speed.setText("低风")
            self.cur_temp.setText("30")
            self.cur_speed.setText("低风")
            self.cost.setText("0")
            self.isRun = 1
        else:
            print("关机")
            self.tar_temp.setText("")
            self.mode.setText("")
            self.tar_speed.setText("")
            self.cur_temp.setText("")
            self.cur_speed.setText("")
            self.isRun = 0

    def button_plus_click(self):
        if self.isRun == 1:
            print("+")
            cur = int(self.tar_temp.text())
            if self.mode.text() == "制冷" and cur < 25:
                cur += 1
                self.tar_temp.setText(str(cur))
            elif self.mode.text() == "制热" and cur < 30:
                cur += 1
                self.tar_temp.setText(str(cur))
            else:
                pass

    def button_sub_click(self):
        if self.isRun == 1:
            print("-")
            cur = int(self.tar_temp.text())
            if self.mode.text() == "制冷" and cur > 18:
                cur -= 1
                self.tar_temp.setText(str(cur))
            elif self.mode.text() == "制热" and cur > 25:
                cur -= 1
                self.tar_temp.setText(str(cur))
            else:
                pass

    def button_mode_click(self):
        if self.isRun == 1:
            print("更改模式")
            if self.mode.text() == "制热":
                self.mode.setText("制冷")
            else:
                self.mode.setText("制热")
            self.tar_temp.setText("25")

    def button_speed_click(self):
        if self.isRun == 1:
            print("更改风速")
            self.WindSpeed = (self.WindSpeed + 1) % 3
            if self.WindSpeed == 0:
                self.tar_speed.setText("低风")
            elif self.WindSpeed == 1:
                self.tar_speed.setText("中风")
            else:
                self.tar_speed.setText("高风")


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = customer_window()
#     window.show()
#     sys.exit(app.exec_())


'''
房间UI界面包含的信息和按键：
按键类：升温，降温，模式，退房，关机/开机，风速（每次调解是mod）
显示的信息：实时温度，设定温度，设定风速，实际风速（低中高和停止送风），计费信息，制冷制热模式
'''
