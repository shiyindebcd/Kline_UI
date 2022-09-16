# -*- coding: utf-8 -*-

from collections import deque
from datetime import datetime
from typing import List

import numpy as np
import pandas as pd
import pyqtgraph as pg
from PySide6 import QtCore, QtGui
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from tqsdk.ta import MACD, MV, PUBU

from uiCrosshair import Crosshair


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


    def tickStrings(self, values: List[int], scale: float, spacing: int):
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


########################################################################
# K线图形对象
########################################################################
class CandlestickItem(pg.GraphicsObject):
    """K线图形对象"""


    def __init__(self, data: pd.DataFrame):  # 初始化
        pg.GraphicsObject.__init__(self)

        self.data = data
        # print(type(self.data))
        # 只重画部分图形，大大提高界面更新速度
        self.rect = None
        self.picture = None
        self.setFlag(self.ItemUsesExtendedStyleOption)

        self.offset = 0
        self.low = 0
        self.high = 1
        self.picture = QtGui.QPicture()
        self.pictures = []
        self.generatePicture(self.data)  # 刷新K线


    def generatePicture(self, data=None, redraw=False):  # 画K线
        """重新生成图形对象"""
        if redraw:  # 重画或者只更新最后一个K线
            self.pictures = []
        elif self.pictures:
            self.pictures.pop()
        w = 0.4  # k线一半的宽度

        if len(data) > 0:
            self.low = data['low'].min()
            self.high = data['high'].max()
        else:
            self.low, self.high = (0, 1)

        npic = len(self.pictures)
        for index, row in data.iterrows():
            if index >= npic:
                picture = QtGui.QPicture()
                p = QtGui.QPainter(picture)
                # 画蜡烛图,下跌绿色（实心）, 上涨红色（空心）
                if row['close'] < row['open']:  # 阴线情况
                    p.setPen(pg.mkPen(QtGui.QColor(0, 255, 0), width=2))  # 设置画笔颜色，宽度
                    p.setBrush(pg.mkBrush(QtGui.QColor(0, 255, 0)))
                    p.drawLine(QtCore.QPointF(index, row['low']), QtCore.QPointF(index, row['high']))  # 画上下影线
                    p.drawRect(QtCore.QRectF(index - w, row['open'], w * 2, row['close'] - row['open']))  # 画矩形，实心K线

                elif row['close'] > row['open']:  # 阳线情况
                    p.setPen(pg.mkPen(QtGui.QColor(255, 0, 0), width=2))  # red
                    p.setBrush(pg.mkBrush(QtGui.QColor(255, 0, 0)))  # red
                    if (row['high'] != row['close']):  # 如果最高点不等于收盘价，画上影线
                        p.drawLine(QtCore.QPointF(index, row['high']), QtCore.QPointF(index, row['close']))
                    if (row['low'] != row['open']):  # 如果最低点不等于开盘价，画下影线
                        p.drawLine(QtCore.QPointF(index, row['open']), QtCore.QPointF(index, row['low']))

                    # p.drawRect(QtCore.QRectF(i - w, open, w * 2, close - open)) # 如果画实心阳线，只需画个实心矩形即可
                    # 画空心阳线的时候，需要画四条线

                    p.drawLine(QtCore.QPointF(index - w, row['open']), QtCore.QPointF(index - w, row['close']))  # 画单根K线的左边线
                    p.drawLine(QtCore.QPointF(index + w, row['open']), QtCore.QPointF(index + w, row['close']))  # 画单根K线的右边线
                    p.drawLine(QtCore.QPointF(index - w, row['close']), QtCore.QPointF(index + w, row['close']))  # 画单根K线的上边线
                    p.drawLine(QtCore.QPointF(index - w, row['open']), QtCore.QPointF(index + w, row['open']))  # 画单根K线的下边线

                else:  # 平盘情况
                    p.setPen(pg.mkPen(QtGui.QColor(0, 0, 255), width=2))  # 十字线时设为蓝色
                    p.setBrush(pg.mkBrush(QtGui.QColor(0, 0, 255)))

                    p.drawLine(QtCore.QPointF(index, row['high']), QtCore.QPointF(index, row['low']))  # 画上下影线
                    p.drawLine(QtCore.QPointF(index - w, row['close']), QtCore.QPointF(index + w, row['close']))  # 画一条横线

                p.end()
                self.pictures.append(picture)  # p = QtGui.QPainter(picture)  # p.drawLines()


    def update(self):  # 手动重画
        if not self.scene() is None:
            self.scene().update()


    def paint(self, painter, opt, w):  # 自动重画
        rect = opt.exposedRect
        xmin, xmax = (max(0, int(rect.left())), min(int(len(self.pictures)), int(rect.right())))
        if not self.rect == (rect.left(), rect.right()) or self.picture is None:
            self.rect = (rect.left(), rect.right())
            self.picture = self.createPic(xmin, xmax)
            self.picture.play(painter)
        elif not self.picture is None:
            self.picture.play(painter)


    def createPic(self, xmin, xmax):  # 缓存图片
        picture = QPicture()
        p = QPainter(picture)
        [pic.play(p) for pic in self.pictures[xmin:xmax]]
        p.end()
        return picture


    def boundingRect(self):  # 定义边界
        return QtCore.QRectF(0, self.low, len(self.pictures), (self.high - self.low))


########################################################################
# 成交量图形对象
########################################################################
class VolumeItem(pg.GraphicsObject):
    """K线图形对象"""


    def __init__(self, data: pd.DataFrame):  # 初始化
        """初始化"""
        pg.GraphicsObject.__init__(self)
        self.data = data
        self.rect = None
        self.picture = None
        self.setFlag(self.ItemUsesExtendedStyleOption)  # 只重画部分图形，大大提高界面更新速度

        self.offset = 0
        self.low = 0
        self.high = 1
        self.picture = QtGui.QPicture()
        self.pictures = []
        self.generatePicture(self.data)  # 刷新柱线


    def generatePicture(self, data=None, redraw=False):  # 画柱线
        """重新生成图形对象"""
        # 重画或者只更新最后一个K线
        if redraw:
            self.pictures = []
        elif self.pictures:
            self.pictures.pop()
        w = 0.4  # k线一半的宽度
        self.low = 0
        if len(data) > 0:
            self.high = data['volume'].max()
        else:
            self.high = 1
        npic = len(self.pictures)
        for index, row in data.iterrows():
            if index >= npic:
                picture = QtGui.QPicture()
                p = QtGui.QPainter(picture)

                # 下跌绿色（实心）, 上涨红色（空心）
                if row['close'] < row['open']:  # 阴线情况
                    p.setPen(pg.mkPen(QtGui.QColor(0, 255, 0), width=2))  # 设置画笔颜色，宽度
                    p.setBrush(pg.mkBrush(QtGui.QColor(0, 255, 0)))
                    p.drawRect(QtCore.QRectF(index - w, 0, w * 2, row['volume']))  # 画矩形，实心成交量柱线

                elif row['close'] > row['open']:  # 阳线情况
                    p.setPen(pg.mkPen(QtGui.QColor(255, 0, 0), width=2))  # red
                    p.setBrush(pg.mkBrush(QtGui.QColor(255, 0, 0)))  # red

                    # p.drawRect(QtCore.QRectF(i - w, open, w * 2, close - open)) # 如果画实心阳线，只需画个实心矩形即可
                    # 画空心阳线的时候，需要画四条线

                    p.drawLine(QtCore.QPointF(index - w, 0), QtCore.QPointF(index - w, row['volume']))  # 画单根成交量柱线的左边线
                    p.drawLine(QtCore.QPointF(index + w, 0), QtCore.QPointF(index + w, row['volume']))  # 画单根成交量柱线的右边线
                    p.drawLine(QtCore.QPointF(index - w, row['volume']), QtCore.QPointF(index + w, row['volume']))  # 画单根成交量柱线的下边线
                    p.drawLine(QtCore.QPointF(index - w, 0), QtCore.QPointF(index + w, 0))  # 画单根成交量柱线的上边线

                else:  # 平盘情况
                    p.setPen(pg.mkPen(QtGui.QColor(0, 0, 255), width=2))  # 十字线设为蓝色
                    p.setBrush(pg.mkBrush(QtGui.QColor(0, 0, 255)))  # 十字线设为蓝色

                    p.drawRect(QtCore.QRectF(index - w, 0, w * 2, row['volume']))  # 画矩形，实心成交量柱线

                p.end()
                self.pictures.append(picture)


    def update(self):  # 手动重画
        if not self.scene() is None:
            self.scene().update()


    def paint(self, painter, opt, w):  # 自动重画
        rect = opt.exposedRect
        xmin, xmax = (max(0, int(rect.left())), min(int(len(self.pictures)), int(rect.right())))
        if not self.rect == (rect.left(), rect.right()) or self.picture is None:
            self.rect = (rect.left(), rect.right())
            self.picture = self.createPic(xmin, xmax)
            self.picture.play(painter)
        elif not self.picture is None:
            self.picture.play(painter)


    def createPic(self, xmin, xmax):  # 缓存图片
        picture = QPicture()
        p = QPainter(picture)
        [pic.play(p) for pic in self.pictures[xmin:xmax]]
        p.end()
        return picture


    def boundingRect(self):  # 定义边界
        return QtCore.QRectF(0, self.low, len(self.pictures), (self.high - self.low))


########################################################################
# MACD图形对象
########################################################################
class MACDItem(pg.GraphicsObject):
    """K线图形对象"""


    def __init__(self, data: pd.DataFrame):  # 初始化
        """初始化"""
        pg.GraphicsObject.__init__(self)
        self.data = data
        self.rect = None
        self.picture = None
        self.setFlag(self.ItemUsesExtendedStyleOption)  # 只重画部分图形，大大提高界面更新速度

        self.offset = 0
        self.low = 0
        self.high = 1
        self.picture = QtGui.QPicture()
        self.pictures = []

        self.generatePicture(self.data)


    def generatePicture(self, data=None, redraw=False):  # 画柱线
        """重新生成图形对象"""
        if redraw:  # 重画或者只更新最后一个周期的线
            self.pictures = []
        elif self.pictures:
            self.pictures.pop()

        if len(data) > 0:
            self.low = data['bar'].min()
            self.high = data['bar'].max()
        else:
            self.low, self.high = (0, 1)

        npic = len(self.pictures)

        for index, row in data.iterrows():
            if index >= npic:
                picture = QtGui.QPicture()
                p = QtGui.QPainter(picture)

                if row['bar'] > 0:  # macd 红柱
                    p.setPen(pg.mkPen(QtGui.QColor(255, 0, 0), width=6))  # 设置画笔颜色，宽度
                    p.setBrush(pg.mkBrush(QtGui.QColor(255, 0, 0)))
                    p.drawLine(QtCore.QPointF(index, 0), QtCore.QPointF(index, row['bar']))

                else:  # macd 绿柱

                    p.setPen(pg.mkPen(QtGui.QColor(0, 255, 0), width=6))
                    p.setBrush(pg.mkBrush(QtGui.QColor(0, 255, 0)))
                    p.drawLine(QtCore.QPointF(index, 0), QtCore.QPointF(index, row['bar']))

                p.end()
                self.pictures.append(picture)


    def update(self):  # 手动重画
        if not self.scene() is None:
            self.scene().update()


    def paint(self, painter, opt, w):  # 自动重画
        rect = opt.exposedRect
        xmin, xmax = (max(0, int(rect.left())), min(int(len(self.pictures)), int(rect.right())))
        if not self.rect == (rect.left(), rect.right()) or self.picture is None:
            self.rect = (rect.left(), rect.right())
            self.picture = self.createPic(xmin, xmax)
            self.picture.play(painter)
        elif not self.picture is None:
            self.picture.play(painter)


    def createPic(self, xmin, xmax):  # 缓存图片
        picture = QPicture()
        p = QPainter(picture)
        [pic.play(p) for pic in self.pictures[xmin:xmax]]
        p.end()
        return picture


    # 定义边界
    def boundingRect(self):
        return QtCore.QRectF(0, self.low, len(self.pictures), (self.high - self.low))


########################################################################
#    综合显示k线图对象
########################################################################
class KLineWidget(KeyWraper):
    """用于显示价格走势图"""

    clsId = 0  # 窗口标识

    listOpenInterest = []  # 保存K线数据的列表和Numpy Array对象
    arrows = []
    initCompleted = False  # 是否完成了历史数据的读取标志


    def __init__(self, parent=None):

        self.parent = parent
        super(KLineWidget, self).__init__(parent)

        self.index = None  # 当前序号   # 下标
        self.countK = 100  # 默认显示的Ｋ线根数

        KLineWidget.clsId += 1
        self.windowId = str(KLineWidget.clsId)

        # 画指标线需要的各种数据列表
        self.pb1_list = []
        self.pb2_list = []
        self.pb3_list = []
        self.pb4_list = []
        self.pb5_list = []
        self.pb6_list = []
        self.mv1_list = []
        self.mv2_list = []
        self.diff_list = []
        self.dea_list = []
        self.candle_bar_list = []
        self.macd_bar_list = []

        # 缓存数据
        self.datas = pd.DataFrame()
        self.listSig = []
        self.listOpenInterest = []
        self.arrows = []

        # 所有K线上信号图
        self.allColor = deque(['blue', 'green', 'yellow', 'white'])
        self.sigData = {}
        self.sigColor = {}
        self.sigPlots = {}

        # 所有副图上的信号图
        self.allSubColor = deque(['blue', 'green', 'yellow', 'white'])
        self.subSigData = {}
        self.subSigColor = {}
        self.subSigPlots = {}
        # 初始化完成
        self.initCompleted = False
        self.crosshair = None
        self.initUi()  # 调用函数


    def initUi(self):
        """初始化界面"""
        pg.setConfigOptions(leftButtonPan=True, antialias=True)  # 禁止画框放大，并启用抗锯齿

        # 主图
        self.pw = pg.PlotWidget(background=QtGui.QColor(13, 9, 27))
        self.pw.setContentsMargins(0, 0, 0, 0)  # 去掉边框

        # 界面布局
        self.lay_KL = pg.GraphicsLayout(border=True)
        self.lay_KL.setContentsMargins(0, 0, 1, 1)  # 左、上、右、下的外边距，图形层与窗口边缘的距离
        self.lay_KL.setBorder(color=(255, 0, 0), width=1)  # 设置图层边框红色，粗1
        self.lay_KL.setZValue(0)
        self.lay_KL.setSpacing(3)  # 设置图层内图元间距，多个图元间距
        self.pw.setCentralItem(self.lay_KL)  # 设置主图

        # 初始化子图
        self.initplotKline()  # K线子图
        self.initplotVol()  # 成交量子图
        self.initplotMACD()  # 指标子图
        # 注册十字光标
        self.crosshair = Crosshair(self.pw, self)
        # 设置界面
        self.VboxL = QVBoxLayout()  # 垂直布局
        self.VboxL.setContentsMargins(0, 0, 0, 0)  # Vboxlayout的外边距要去掉,这个非常难找
        self.VboxL.addWidget(self.pw)  # 添加主图
        self.setLayout(self.VboxL)  # 设置布局
        # 初始化完成
        self.initCompleted = True


    def loadData(self, datas):
        """
        传进来pandas.DataFrame格式的k线数据,其中须有datetime, open, close, low, high 这几列
        然后计算瀑布线和macd,合并到这个DataFrame中
        """
        pb1 = PUBU(datas, 3)
        self.pb1_list = pb1['pb'].tolist()
        pb2 = PUBU(datas, 4)
        self.pb2_list = pb2['pb'].tolist()
        pb3 = PUBU(datas, 9)
        self.pb3_list = pb3['pb'].tolist()
        pb4 = PUBU(datas, 13)
        self.pb4_list = pb4['pb'].tolist()
        pb5 = PUBU(datas, 18)
        self.pb5_list = pb5['pb'].tolist()
        pb6 = PUBU(datas, 24)
        self.pb6_list = pb6['pb'].tolist()
        datas['pb1'] = pb1
        datas['pb2'] = pb2
        datas['pb3'] = pb3
        datas['pb4'] = pb4
        datas['pb5'] = pb5
        datas['pb6'] = pb6
        mv_vol = MV(datas, 5, 20)
        self.mv1_list = mv_vol['mv1'].tolist()
        self.mv2_list = mv_vol['mv2'].tolist()
        macd = MACD(datas, 12, 26, 9)
        self.diff_list = macd['diff'].tolist()
        self.dea_list = macd['dea'].tolist()

        self.datas = pd.concat([datas, mv_vol, macd], axis=1)
        self.candle_bar_list = self.datas[['open', 'high', 'low', 'close','volume']].to_records(index=True)
        self.macd_bar_list = macd[['bar']].to_records(index=True)

        # 如果传进来的是从天勤直接获取的klines,前面有可能有无数据的空行,当从天勤请求的k线数量大于该合约原有的k线数量时,前面会以空行填充
        # 需要下面这几句去掉空行,并重建index.因为我传入的数据已经预先把前面空的部分截掉了,所经这里不需要再截一次空行
        # data = pd.concat([datas, mv_vol, macd], axis=1)
        # self.datas = data.drop(data[data['id']<0].index)       # 删除所有没有数据的空行
        # self.datas = self.datas.reset_index(drop=True)         # 删除开头空白的数据行后重建索引
        # print('传入的数据为: ', self.datas)


    def initplotKline(self):
        """初始化蜡烛图子图"""
        self.pwKL = pg.PlotItem(name=('_'.join([self.windowId, 'PlotKL'])), axisItems=None)
        self.pwKL.setXLink('_'.join([self.windowId, 'PlotKL']))  # 设置x轴关联，使两个子图的x坐标一致
        self.pwKL.getViewBox().sigXRangeChanged.connect(self.set_pwKL_yRange)  # 子图的x轴范围改变信号
        self.pwKL.setMenuEnabled(False)  # 隐藏菜单
        self.pwKL.setClipToView(True)  # 在ViewBox可见范围内绘制所有数据
        self.pwKL.hideAxis('left')  # 隐藏左边坐标轴
        self.pwKL.showAxis('right')  # 显示右边坐标轴
        # self.pwKL.hideAxis('bottom')

        self.pwKL.setDownsampling(mode='peak')  # 缩减像素采样,峰值:通过画一个跟随原始数据的最小值和最大值的锯齿波向下采样。# 这种方法可以产生最好的数据可视化表示，但速度较慢。
        self.pwKL.setRange(xRange=(0, 1), yRange=(0, 1))  # 设置x、y轴范围
        self.pwKL.getAxis('right').setWidth(40)  # 设置右边坐标轴宽度
        self.pwKL.showGrid(True, True, alpha=0.3)  # 显示网格,alpha为网格的不透明度,范围0-1.0
        self.pwKL.setMaximumHeight(800)  # 图项最大高度
        self.pwKL.setMinimumHeight(400)  # 图项最小高度
        self.pwKL.hideButtons()  # 隐藏刻度按钮
        self.pwKL.setZValue(0)
        self.pwKL.getAxis('right').setStyle(tickFont=QFont("Arial", 8, QFont.Bold), autoExpandTextSpace=True)  # 设置右边坐标轴刻度字体
        self.pwKL.getAxis('bottom').setStyle(tickFont=QFont("Arial", 8, QFont.Bold), autoExpandTextSpace=True)  # 设置下边坐标轴刻度字体
        self.pwKL.getAxis('right').setPen(QtGui.QColor(255, 0, 0))  # y轴颜色
        self.pwKL.getAxis('bottom').setPen(QtGui.QColor(255, 0, 0))  # x轴颜色
        self.pwKL.getAxis('right').setTextPen(QtGui.QColor(150, 150, 150))  # y轴刻度颜色
        self.pwKL.getAxis('bottom').setTextPen(QtGui.QColor(150, 150, 150))  # x轴刻度颜色

        self.candle = CandlestickItem(self.datas)
        self.candle.setZValue(10)
        self.pwKL.addItem(self.candle)
        self.lay_KL.nextRow()
        self.lay_KL.addItem(self.pwKL)

        #   添加六条pubu线到图上
        self.Curves_pb1 = self.pwKL.plot(self.pb1_list, pen=pg.mkPen(QtGui.QColor(255, 255, 255), width=2))
        self.Curves_pb1.setZValue(15)
        self.Curves_pb2 = self.pwKL.plot(self.pb2_list, pen=pg.mkPen(QtGui.QColor(255, 85, 0), width=2))
        self.Curves_pb2.setZValue(15)
        self.Curves_pb3 = self.pwKL.plot(self.pb3_list, pen=pg.mkPen(QtGui.QColor(255, 0, 127), width=2))
        self.Curves_pb3.setZValue(15)
        self.Curves_pb4 = self.pwKL.plot(self.pb4_list, pen=pg.mkPen(QtGui.QColor(0, 255, 0), width=2))
        self.Curves_pb4.setZValue(15)
        self.Curves_pb5 = self.pwKL.plot(self.pb5_list, pen=pg.mkPen(QtGui.QColor(255, 0, 0), width=2))
        self.Curves_pb5.setZValue(15)
        self.Curves_pb6 = self.pwKL.plot(self.pb6_list, pen=pg.mkPen(QtGui.QColor(60, 60, 255), width=2))
        self.Curves_pb6.setZValue(15)



    def initplotVol(self):
        """初始化成交量子图"""
        self.pwVol = pg.PlotItem(name=('_'.join([self.windowId, 'PlotVol'])), axisItems=None)
        self.pwVol.setXLink('_'.join([self.windowId, 'PlotKL']))  # 设置x轴关联，使两个子图的x坐标一致
        self.pwVol.getViewBox().sigXRangeChanged.connect(self.set_pwVol_yRange)  # 子图的x轴范围改变信号
        self.pwVol.setMenuEnabled(False)  # 隐藏菜单
        self.pwVol.setClipToView(True)  # 在ViewBox可见范围内绘制所有数据
        self.pwVol.hideAxis('left')  # 隐藏左边坐标轴
        self.pwVol.showAxis('right')  # 显示右边坐标轴
        self.pwVol.hideAxis('bottom')

        self.pwVol.setDownsampling(mode='peak')  # 缩减像素采样,峰值:通过画一个跟随原始数据的最小值和最大值的锯齿波向下采样。# 这种方法可以产生最好的数据可视化表示，但速度较慢。
        self.pwVol.setRange(xRange=(0, 1), yRange=(0, 1))  # 设置x、y轴范围
        self.pwVol.getAxis('right').setWidth(40)  # 设置右边坐标轴宽度
        self.pwVol.showGrid(True, True, alpha=0.3)  # 显示网格,alpha为网格的不透明度,范围0-1.0
        self.pwVol.setMinimumHeight(80)  # 图项最小高度
        self.pwVol.setMaximumHeight(130)  # 图项最大高度
        self.pwVol.hideButtons()  # 隐藏刻度按钮
        self.pwVol.setZValue(0)
        self.pwVol.getAxis('right').setStyle(tickFont=QFont("Arial", 8, QFont.Bold), autoExpandTextSpace=True)  # 设置右边坐标轴刻度字体
        self.pwVol.getAxis('bottom').setStyle(tickFont=QFont("Arial", 8, QFont.Bold), autoExpandTextSpace=True)  # 设置下边坐标轴刻度字体
        self.pwVol.getAxis('right').setPen(QtGui.QColor(255, 0, 0))  # y轴颜色
        self.pwVol.getAxis('bottom').setPen(QtGui.QColor(255, 0, 0))  # x轴颜色
        self.pwVol.getAxis('right').setTextPen(QtGui.QColor(150, 150, 150))  # y轴刻度颜色
        self.pwVol.getAxis('bottom').setTextPen(QtGui.QColor(150, 150, 150))  # x轴刻度颜色

        self.volume = VolumeItem(self.datas)
        self.pwVol.addItem(self.volume)
        self.lay_KL.nextRow()
        self.lay_KL.addItem(self.pwVol)

        self.Curves_mv1 = self.pwVol.plot(self.mv1_list, pen=pg.mkPen(QtGui.QColor(255, 255, 0), width=2))
        self.Curves_mv2 = self.pwVol.plot(self.mv2_list, pen=pg.mkPen(QtGui.QColor(255, 255, 255), width=2))
        self.Curves_mv1.setZValue(15)
        self.Curves_mv2.setZValue(15)

    def initplotMACD(self):
        """初始化MACD子图"""
        self.pwMACD = pg.PlotItem(name=('_'.join([self.windowId, 'PlotMACD'])), axisItems=None)
        self.pwMACD.setXLink('_'.join([self.windowId, 'PlotKL']))  # 设置x轴关联，使两个子图的x坐标一致
        self.pwMACD.getViewBox().sigXRangeChanged.connect(self.set_pwMACD_yRange)  # 子图的x轴范围改变信号
        self.pwMACD.setMenuEnabled(False)  # 隐藏菜单
        self.pwMACD.setClipToView(True)  # 在ViewBox可见范围内绘制所有数据
        self.pwMACD.hideAxis('left')  # 隐藏左边坐标轴
        self.pwMACD.showAxis('right')  # 显示右边坐标轴
        self.pwMACD.hideAxis('bottom')

        self.pwMACD.setDownsampling(mode='peak')  # 缩减像素采样,峰值:通过画一个跟随原始数据的最小值和最大值的锯齿波向下采样。# 这种方法可以产生最好的数据可视化表示，但速度较慢。
        self.pwMACD.setRange(xRange=(0, 1), yRange=(0, 1))  # 设置x、y轴范围
        self.pwMACD.getAxis('right').setWidth(40)  # 设置右边坐标轴宽度
        self.pwMACD.showGrid(True, True, alpha=0.3)  # 显示网格,alpha为网格的不透明度,范围0-1.0
        self.pwMACD.setMinimumHeight(80)  # 图项最小高度
        self.pwMACD.setMaximumHeight(130)  # 图项最大高度
        self.pwMACD.hideButtons()  # 隐藏刻度按钮
        self.pwMACD.setZValue(0)
        self.pwMACD.getAxis('right').setStyle(tickFont=QFont("Arial", 8, QFont.Bold), autoExpandTextSpace=True)  # 设置右边坐标轴刻度字体
        self.pwMACD.getAxis('bottom').setStyle(tickFont=QFont("Arial", 8, QFont.Bold), autoExpandTextSpace=True)  # 设置下边坐标轴刻度字体
        self.pwMACD.getAxis('right').setPen(QtGui.QColor(255, 0, 0))  # y轴颜色
        self.pwMACD.getAxis('bottom').setPen(QtGui.QColor(255, 0, 0))  # x轴颜色
        self.pwMACD.getAxis('right').setTextPen(QtGui.QColor(150, 150, 150))  # y轴刻度颜色
        self.pwMACD.getAxis('bottom').setTextPen(QtGui.QColor(150, 150, 150))  # x轴刻度颜色

        self.macd = MACDItem(self.datas)
        self.pwMACD.addItem(self.macd)
        self.lay_KL.nextRow()
        self.lay_KL.addItem(self.pwMACD)

        self.Curves_diff = self.pwMACD.plot(self.diff_list, pen=pg.mkPen(QtGui.QColor(255, 255, 0), width=2))
        self.Curves_dea = self.pwMACD.plot(self.dea_list, pen=pg.mkPen(QtGui.QColor(255, 0, 255), width=2))


    # ----------------------------------------------------------------------
    #  画图相关 
    # ----------------------------------------------------------------------
    def plotKline(self, redraw=False, xmin=0, xmax=-1):
        """重画K线子图"""
        if self.initCompleted:
            self.candle.generatePicture(self.datas.loc[xmin:xmax], redraw)  # 画K线
            self.Curves_pb1.setData(self.pb1_list)
            self.Curves_pb2.setData(self.pb2_list)
            self.Curves_pb3.setData(self.pb3_list)
            self.Curves_pb4.setData(self.pb4_list)
            self.Curves_pb5.setData(self.pb5_list)
            self.Curves_pb6.setData(self.pb6_list)

            self.plotMark()  # 显示开平仓信号位置


    def plotVol(self, redraw=False, xmin=0, xmax=-1):
        """重画成交量子图"""
        if self.initCompleted:
            self.volume.generatePicture(self.datas.loc[xmin:xmax], redraw)  # 画成交量子图
            self.Curves_mv1.setData(self.mv1_list)
            self.Curves_mv2.setData(self.mv2_list)

    def PlotMACD(self, redraw=False, xmin=0, xmax=-1):
        """重画MACD子图"""
        if self.initCompleted:
            self.macd.generatePicture(self.datas.loc[xmin:xmax], redraw)  # 画MACD子图
            self.Curves_diff.setData(self.diff_list)
            self.Curves_dea.setData(self.dea_list)

    def set_pwKL_yRange(self):  # 设置pwKL的y轴显示范围,该函数由sigXRangeChanged信号驱动
        datas = self.datas
        view = self.pwKL.getViewBox()
        vRange = view.viewRange()
        if self.crosshair:
            x = int(self.crosshair.xAxis)
            y = int(self.crosshair.yAxis)
            self.crosshair.signal.emit(x, y)

        xmin = max(0, int(vRange[0][0]))
        xmax = max(0, int(vRange[0][1]))
        try:
            xmax = min(xmax, len(datas) - 1)
        except:
            xmax = xmax
        if len(datas) > 0 and xmax > xmin:
            ymin = min(datas[xmin:xmax]['low'])
            ymax = max(datas[xmin:xmax]['high'])
            if ymin and ymax:
                view.setRange(yRange=(ymin, ymax))
            else:
                pass
        else:
            view.setRange(yRange=(0, 1))


    def set_pwVol_yRange(self):  # 设置pwVol的y轴显示范围,该函数由sigXRangeChanged信号驱动
        datas = self.datas
        view = self.pwVol.getViewBox()
        vRange = view.viewRange()
        xmin = max(0, int(vRange[0][0]))
        xmax = max(0, int(vRange[0][1]))
        try:
            xmax = min(xmax, len(datas) - 1)
        except:
            xmax = xmax
        if len(datas) > 0 and xmax > xmin:
            ymax = max(datas[xmin:xmax]['volume'])
            view.setRange(yRange=(ymax // 13, ymax))
        else:
            view.setRange(yRange=(0, 1))


    def set_pwMACD_yRange(self):  # 设置pwMACD的y轴显示范围,该函数由sigXRangeChanged信号驱动
        datas = self.datas
        view = self.pwMACD.getViewBox()
        vRange = view.viewRange()
        xmin = max(0, int(vRange[0][0]))
        xmax = max(0, int(vRange[0][1]))
        try:
            xmax = min(xmax, len(datas) - 1)
        except:
            xmax = xmax
        if len(datas) > 0 and xmax > xmin:
            ymin = min(min(datas[xmin:xmax]['diff']), min(datas[xmin:xmax]['bar']))
            ymax = max(max(datas[xmin:xmax]['diff']), max(datas[xmin:xmax]['bar']))
            if ymin and ymax:
                view.setRange(yRange=(ymin, ymax))
            else:
                pass
        else:
            view.setRange(yRange=(0, 1))


    def addSig(self, sig, main=True):
        """新增信号图"""
        if main:
            if sig in self.sigPlots:
                self.pwKL.removeItem(self.sigPlots[sig])
            self.sigPlots[sig] = self.pwKL.plot()
            self.sigColor[sig] = self.allColor[0]
            self.allColor.append(self.allColor.popleft())
        else:
            if sig in self.subSigPlots:
                self.pwMACD.removeItem(self.subSigPlots[sig])
            self.subSigPlots[sig] = self.pwMACD.plot()
            self.subSigColor[sig] = self.allSubColor[0]
            self.allSubColor.append(self.allSubColor.popleft())


    # ----------------------------------------------------------------------
    # 信号显示相关
    # ----------------------------------------------------------------------
    def showSig(self, datas, main=True, clear=False):
        """刷新信号图"""
        if clear:
            self.clearSig(main)
            if datas and not main:
                sigDatas = np.array(datas.values()[0])
                self.listOpenInterest = sigDatas
                self.datas['openInterest'] = sigDatas
                self.PlotMACD(0, len(sigDatas))
        if main:
            for sig in datas:
                self.addSig(sig, main)
                self.sigData[sig] = datas[sig]
                self.sigPlots[sig].setData(np.append(datas[sig], 0), pen=self.sigColor[sig][0], name=sig)
        else:
            for sig in datas:
                self.addSig(sig, main)
                self.subSigData[sig] = datas[sig]
                self.subSigPlots[sig].setData(np.append(datas[sig], 0), pen=self.subSigColor[sig][0], name=sig)


    def plotMark(self):
        """显示开平仓信号"""
        # 检查是否有数据
        if len(self.datas) == 0:
            return
        for arrow in self.arrows:
            self.pwKL.removeItem(arrow)
        # 画买卖信号
        for i in range(len(self.listSig)):
            # 无信号
            if self.listSig[i] == 0:
                continue
            # 买信号
            elif self.listSig[i] > 0:
                arrow = pg.ArrowItem(pos=(i, self.datas[i]['low']), angle=90, brush=(255, 0, 0))
            # 卖信号
            elif self.listSig[i] < 0:
                arrow = pg.ArrowItem(pos=(i, self.datas[i]['high']), angle=-90, brush=(0, 255, 0))  # self.pwKL.addItem(arrow)  # self.arrows.append(arrow)


    # ----------------------------------------------------------------------
    #  界面刷新相关
    # ----------------------------------------------------------------------
    def refreshAll(self, redraw=True, update=False):
        """
        更新所有界面
        """
        # 调用画图函数
        self.index = len(self.datas)
        self.crosshair.datas = self.datas
        self.crosshair.signal.emit(None, None)
        # 设置横坐标

        self.axisTime = DatetimeAxis(self.datas, orientation='bottom')  # 时间坐标轴
        self.pwKL.setAxisItems(axisItems={'bottom': self.axisTime})

        self.plotAll(redraw, 0, len(self.datas))
        if not update:
            self.updateAll()


    def plotAll(self, redraw=True, xMin=0, xMax=-1):
        """
        重画所有界面
        redraw ：False=重画最后一根K线; True=重画所有
        xMin,xMax : 数据范围
        """
        if xMax < 0:
            xMax = len(self.datas) - 1
        else:
            xMax = xMax

        self.pwKL.setLimits(xMin=xMin, xMax=xMax)
        self.pwVol.setLimits(xMin=xMin, xMax=xMax)
        self.pwMACD.setLimits(xMin=xMin, xMax=xMax)
        self.plotKline(redraw, xMin, xMax)  # K线图
        self.plotVol(redraw, xMin, xMax)  # K线副图，成交量
        self.PlotMACD(redraw, xMin, xMax)  # K线副图，MACD
        self.refresh()


    def updateAll(self):
        """
        手动更新所有K线图形，K线播放模式下需要
        """
        datas = self.datas
        self.candle.pictrue = None
        self.volume.pictrue = None
        self.macd.picture = None
        self.candle.update()
        self.volume.update()
        self.macd.update()


        def update(view, low, high):
            vRange = view.viewRange()
            xmin = max(0, int(vRange[0][0]))
            xmax = max(0, int(vRange[0][1]))
            try:
                xmax = min(xmax, len(datas) - 1)
            except:
                xmax = xmax
            if len(datas) > 0 and xmax > xmin:
                ymin = min(datas[xmin:xmax][low])
                ymax = max(datas[xmin:xmax][high])
                view.setRange(yRange=(ymin, ymax))
            else:
                view.setRange(yRange=(0, 1))


        update(self.pwKL.getViewBox(), 'low', 'high')
        update(self.pwVol.getViewBox(), 'volume', 'volume')
        update(self.pwMACD.getViewBox(), 'diff', 'diff')


    def refresh(self):
        """
        刷新三个子图的显示范围
        """
        datas = self.datas
        minutes = int(self.countK / 2)
        xmin = max(0, self.index - minutes)
        try:
            if datas:
                xmax = min(xmin + 2 * minutes, len(datas) - 1)
            else:
                xmax = xmin + 2 * minutes
        except:
            xmax = xmin + 2 * minutes
        self.pwKL.setRange(xRange=(xmin, xmax))
        self.pwVol.setRange(xRange=(xmin, xmax))
        self.pwMACD.setRange(xRange=(xmin, xmax))


    # ----------------------------------------------------------------------
    #  快捷键相关 
    # ----------------------------------------------------------------------
    def onNxt(self):
        """跳转到下一个开平仓点"""
        if len(self.listSig) > 0 and not self.index is None:
            datalen = len(self.listSig)
            if self.index < datalen - 2: self.index += 1
            while self.index < datalen - 2 and self.listSig[self.index] == 0:
                self.index += 1
            self.refresh()
            x = self.index
            y = self.datas[x]['close']
            self.crosshair.signal.emit(x, y)


    def onPre(self):
        """跳转到上一个开平仓点"""
        if len(self.listSig) > 0 and not self.index is None:
            if self.index > 0: self.index -= 1
            while self.index > 0 and self.listSig[self.index] == 0:
                self.index -= 1
            self.refresh()
            x = self.index
            y = self.datas[x]['close']
            self.crosshair.signal.emit(x, y)


    def onDown(self):
        """放大显示区间"""
        self.countK = min(len(self.datas), int(self.countK * 1.2) + 1)
        self.refresh()
        if len(self.datas) > 0:
            x = self.index - self.countK / 2 + 2 if int(self.crosshair.xAxis) < self.index - self.countK / 2 + 2 else int(self.crosshair.xAxis)
            x = self.index + self.countK / 2 - 2 if x > self.index + self.countK / 2 - 2 else x
            x = len(self.datas) - 1 if x > len(self.datas) - 1 else int(x)
            y = self.datas.loc[x][2]
            self.crosshair.signal.emit(x, y)


    def onUp(self):
        """缩小显示区间"""
        self.countK = max(3, int(self.countK / 1.2) - 1)
        self.refresh()
        if len(self.datas) > 0:
            x = self.index - self.countK / 2 + 2 if int(self.crosshair.xAxis) < self.index - self.countK / 2 + 2 else int(self.crosshair.xAxis)
            x = self.index + self.countK / 2 - 2 if x > self.index + self.countK / 2 - 2 else x
            x = len(self.datas) - 1 if x > len(self.datas) - 1 else int(x)
            y = self.datas.loc[x]['close']
            self.crosshair.signal.emit(x, y)


    def onLeft(self):
        """向左移动"""
        if len(self.datas) > 0 and int(self.crosshair.xAxis) > 2:
            x = int(self.crosshair.xAxis) - 1
            x = len(self.datas) - 1 if x > len(self.datas) - 1 else int(x)
            y = self.datas.loc[x]['close']
            if x <= self.index - self.countK / 2 + 2 and self.index > 1:
                self.index -= 1
                self.refresh()
            self.crosshair.signal.emit(x, y)


    def onRight(self):
        """向右移动"""
        if len(self.datas) > 0 and int(self.crosshair.xAxis) < len(self.datas) - 1:
            x = int(self.crosshair.xAxis) + 1
            x = len(self.datas) - 1 if x > len(self.datas) - 1 else int(x)
            y = self.datas.loc[x]['close']
            if x >= self.index + int(self.countK / 2) - 2:
                self.index += 1
                self.refresh()
            self.crosshair.signal.emit(x, y)


    # ----------------------------------------------------------------------
    # 界面回调相关
    # ----------------------------------------------------------------------
    def onPaint(self):
        """界面刷新回调"""
        view = self.pwKL.getViewBox()
        vRange = view.viewRange()
        xmin = max(0, int(vRange[0][0]))
        xmax = max(0, int(vRange[0][1]))
        self.index = int((xmin + xmax) / 2) + 1


    # ----------------------------------------------------------------------
    # 数据相关
    # ----------------------------------------------------------------------
    def clearData(self):
        """清空数据"""
        # 清空数据，重新画图

        self.listSig = []
        self.sigData = {}
        self.datas = None


    def clearSig(self, main=True):
        """清空信号图形"""
        # 清空信号图
        if main:
            for sig in self.sigPlots:
                self.pwKL.removeItem(self.sigPlots[sig])
            self.sigData = {}
            self.sigPlots = {}
        else:
            for sig in self.subSigPlots:
                self.pwMACD.removeItem(self.subSigPlots[sig])
            self.subSigData = {}
            self.subSigPlots = {}


    def updateSig(self, sig):
        """刷新买卖信号"""
        self.listSig = sig
        self.plotMark()


    def onBar(self, bar: dict):
        """
        新增K线数据,K线播放模式
        """
        # 是否需要更新K线
        if len(self.datas) > 0 and bar['datetime'] == self.datas.loc[-1].datetime:
            newBar = False
        else:
            newBar = True

        if newBar:
            nrecords = len(self.datas)
        else:
            nrecords = len(self.datas) - 1

        if bar['close'] < bar['open']:
            recordVol = (nrecords, abs(bar['volume']), 0, 0, abs(bar['volume']))
        else:
            recordVol = (nrecords, 0, abs(bar['volume']), 0, abs(bar['volume']))

        if newBar and any(self.datas):
            self.datas.resize(nrecords + 1, refcheck=0)
            self.listBar.resize(nrecords + 1, refcheck=0)
            self.listVol.resize(nrecords + 1, refcheck=0)
        elif any(self.datas):
            self.listLow.pop()
            self.listHigh.pop()
            self.listOpenInterest.pop()
        if any(self.datas):
            self.datas.loc[-1] = (bar['datetime'], bar['open'], bar['close'], bar['low'], bar['high'], bar['volume'], bar['openInterest'])
            self.listBar[-1] = (nrecords, bar['open'], bar['close'], bar['low'], bar['high'])
            self.listVol[-1] = recordVol
        else:
            self.datas = np.rec.array([(bar['datetime'], bar['open'], bar['close'], bar['low'], bar['high'], bar['volume'], bar['openInterest'])], names=('datetime', 'open', 'close', 'low', 'high', 'volume', 'openInterest'))
            self.listBar = np.rec.array([(nrecords, bar['open'], bar['close'], bar['low'], bar['high'])], names=('time_int', 'open', 'close', 'low', 'high'))
            self.listVol = np.rec.array([recordVol], names=('time_int', 'open', 'close', 'low', 'high'))
            self.get_yaxis_range(self.datas)

        self.axisTime.update_xdict({nrecords: bar.datetime})
        self.listLow.append(bar.low)
        self.listHigh.append(bar.high)
        self.listOpenInterest.append(bar.openInterest)
        self.get_yaxis_range(self.datas)

        return newBar
