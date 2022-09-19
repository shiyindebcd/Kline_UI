# -*- coding: utf-8 -*-

from datetime import datetime
import pyqtgraph as pg
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import *


########################################################################
# 键盘鼠标功能
########################################################################
class KeyWraper(QWidget):
    """键盘鼠标功能支持的元类"""


    def __init__(self, parent=None):  # 初始化
        QWidget.__init__(self, parent)
        self.setMouseTracking(True)  # 设置鼠标跟踪
        self.autoFillBackground()


    def keyPressEvent(self, event):  # 重载方法keyPressEvent(self,event),即按键按下事件方法
        if event.key() == QtCore.Qt.Key_Up:
            self.onUp()
        elif event.key() == QtCore.Qt.Key_Down:
            self.onDown()
        elif event.key() == QtCore.Qt.Key_Left:
            self.onLeft()
        elif event.key() == QtCore.Qt.Key_Right:
            self.onRight()
        elif event.key() == QtCore.Qt.Key_PageUp:
            self.onPre()
        elif event.key() == QtCore.Qt.Key_PageDown:
            self.onNxt()


    def mousePressEvent(self, event):  # 重载方法mousePressEvent(self,event),即鼠标点击事件方法
        if event.button() == QtCore.Qt.RightButton:
            self.onRClick(event.pos())
        elif event.button() == QtCore.Qt.LeftButton:
            self.onLClick(event.pos())


    def mouseRelease(self, event):  # 重载方法mouseReleaseEvent(self,event),即鼠标点击事件方法
        if event.button() == QtCore.Qt.RightButton:
            self.onRRelease(event.pos())
        elif event.button() == QtCore.Qt.LeftButton:
            self.onLRelease(event.pos())
        self.releaseMouse()


    def wheelEvent(self, event):  # 重载方法wheelEvent(self,event),即滚轮事件方法
        return


    def paintEvent(self, event):  # 重载方法paintEvent(self,event),即拖动事件方法
        self.onPaint()


    def onNxt(self):  # PgDown键
        pass


    def onPre(self):  # PgUp键
        pass


    def onUp(self):  # 向上键和滚轮向上
        pass


    def onDown(self):  # 向下键和滚轮向下
        pass


    def onLeft(self):  # 向左键
        pass


    def onRight(self):  # 向右键
        pass


    def onLClick(self, pos):  # 鼠标左单击
        pass


    def onRClick(self, pos):  # 鼠标右单击
        pass


    def onLRelease(self, pos):  # 鼠标左释放
        pass


    def onRRelease(self, pos):  # 鼠标右释放
        pass


    def onPaint(self):  # 画图
        pass


########################################################################
# 时间序列，横坐标支持
########################################################################
class DatetimeAxis(pg.AxisItem):

    def __init__(self, datas, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.data = datas  # 传入k线数据
        self.setPen(pg.mkPen(QtGui.QColor(255, 0, 0), width=1))  # 设置时间轴边框颜色
        self.tickFont = QtGui.QFont("Arial", 6)  # 时间轴刻度字体


    def tickStrings(self, values: list[int], scale: float, spacing: int):
        """
        Convert original index to datetime string.
        values自动传入x坐标
        """
        # 行索引和时间组合字典，行索引和x轴对应
        datetime_index_map = dict(zip(self.data.index, self.data.datetime))
        strings = []
        for ix in values:
            dt = datetime_index_map.get(ix, None)  # x轴对应的时间
            if not dt:
                s = ""
            else:
                dt = datetime.fromtimestamp(dt / 1e9)  # 转换成datetime格式
                if dt.hour:  # 日内周期
                    s = dt.strftime("%m-%d %H:%M")
                else:
                    s = dt.strftime("%Y-%m-%d")
            strings.append(s)
        return strings


# 绘制时，线条属性设置弹出框

class DrawLineStyleWidget(QtWidgets.QWidget):
    sinout_signal = QtCore.Signal(object)
    def __init__(self):
        super().__init__()
        self.default_color: str = '#ff557f'
        self.init_ui()
        pass
    def init_ui(self):
        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.WindowCloseButtonHint)
        self.setWindowTitle('绘制趋势线')
        self.setMinimumHeight(80)
        self.setMinimumWidth(200)
        self.current_color_label = QtWidgets.QLabel('当前颜色')
        self.current_color_label.setAlignment(QtCore.Qt.AlignCenter)
        self.current_color_label.setStyleSheet('QLabel{font-size:16px;color:'+self.default_color+';font-weight:bold}')
        change_color_btn = QtWidgets.QPushButton('线段颜色')
        change_color_btn.clicked.connect(self.change_color_btn_clicked)
        layout_color = QtWidgets.QVBoxLayout()
        layout_color.addWidget(self.current_color_label)
        layout_color.addWidget(change_color_btn)
        layout_color.addStretch(1)
        tip_linewidth_label = QtWidgets.QLabel('线段粗细')
        self.linewidth_spin = QtWidgets.QSpinBox()
        self.linewidth_spin.setValue(4)
        linewidth_check_btn = QtWidgets.QPushButton('确定')
        linewidth_check_btn.clicked.connect(self.linewidth_check_btn_clicked)
        layout_linewidth = QtWidgets.QHBoxLayout()
        layout_linewidth.addWidget(self.linewidth_spin)
        layout_linewidth.addWidget(linewidth_check_btn)
        layout_linewidth_00 = QtWidgets.QVBoxLayout()
        layout_linewidth_00.addWidget(tip_linewidth_label)
        layout_linewidth_00.addLayout(layout_linewidth)
        layout_linewidth_00.addStretch(1)
        previous_step_btn = QtWidgets.QPushButton('撤销')
        previous_step_btn.clicked.connect(self.previous_step_btn_clicked)
        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(layout_color)
        layout.addLayout(layout_linewidth_00)
        layout.addWidget(previous_step_btn)
        self.setLayout(layout)
        pass
    def change_color_btn_clicked(self):
        col = QtWidgets.QColorDialog.getColor()
        if col.isValid():
            pal = self.current_color_label.palette()
            pal.setColor(QtGui.QPalette.WindowText,col)
            self.current_color_label.setPalette(pal)
            pre_map = {
                'change_type':'color',
                'data':col.name()
            }
            self.sinout_signal.emit(pre_map)
        pass
    def previous_step_btn_clicked(self):
        pre_map = {
            'change_type': 'pre_step',
            'data': None
        }
        self.sinout_signal.emit(pre_map)
        pass
    def linewidth_check_btn_clicked(self):
        line_width = self.linewidth_spin.value()
        if int(line_width)<=0:
            QtWidgets.QMessageBox.information(
                self,
                '提示',
                '线条粗细必须大于0',
                QtWidgets.QMessageBox.Yes
            )
            return
        # linewidth
        pre_map = {
            'change_type':'linewidth',
            'data':int(line_width)
        }
        self.sinout_signal.emit(pre_map)
        pass
