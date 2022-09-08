# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from functools import partial
from collections import deque
from tqsdk.ta import MACD, PUBU

from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6 import QtGui, QtCore

from uiCrosshair import Crosshair
import pyqtgraph as pg


# 字符串转换
# ---------------------------------------------------------------------------------------
# try:
#     _fromUtf8 = QtCore.QString.fromUtf8
# except AttributeError:
#     def _fromUtf8(s):
#         return s

########################################################################
# 键盘鼠标功能
########################################################################
class KeyWraper(QWidget):
    """键盘鼠标功能支持的元类"""

    # 初始化
    # ----------------------------------------------------------------------
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setMouseTracking(True)  # 设置鼠标跟踪
        self.autoFillBackground()

    # 重载方法keyPressEvent(self,event),即按键按下事件方法
    # ----------------------------------------------------------------------
    def keyPressEvent(self, event):
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

    # 重载方法mousePressEvent(self,event),即鼠标点击事件方法
    # ----------------------------------------------------------------------
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.RightButton:
            self.onRClick(event.pos())
        elif event.button() == QtCore.Qt.LeftButton:
            self.onLClick(event.pos())

    # 重载方法mouseReleaseEvent(self,event),即鼠标点击事件方法
    # ----------------------------------------------------------------------
    def mouseRelease(self, event):
        if event.button() == QtCore.Qt.RightButton:
            self.onRRelease(event.pos())
        elif event.button() == QtCore.Qt.LeftButton:
            self.onLRelease(event.pos())
        self.releaseMouse()

    # 重载方法wheelEvent(self,event),即滚轮事件方法
    # ----------------------------------------------------------------------
    def wheelEvent(self, event):
        return

    # 重载方法paintEvent(self,event),即拖动事件方法
    # ----------------------------------------------------------------------
    def paintEvent(self, event):
        self.onPaint()

    # PgDown键
    # ----------------------------------------------------------------------
    def onNxt(self):
        pass

    # PgUp键
    # ----------------------------------------------------------------------
    def onPre(self):
        pass

    # 向上键和滚轮向上
    # ----------------------------------------------------------------------
    def onUp(self):
        pass

    # 向下键和滚轮向下
    # ----------------------------------------------------------------------
    def onDown(self):
        pass

    # 向左键
    # ----------------------------------------------------------------------
    def onLeft(self):
        pass

    # 向右键
    # ----------------------------------------------------------------------
    def onRight(self):
        pass

    # 鼠标左单击
    # ----------------------------------------------------------------------
    def onLClick(self, pos):
        pass

    # 鼠标右单击
    # ----------------------------------------------------------------------
    def onRClick(self, pos):
        pass

    # 鼠标左释放
    # ----------------------------------------------------------------------
    def onLRelease(self, pos):
        pass

    # 鼠标右释放
    # ----------------------------------------------------------------------
    def onRRelease(self, pos):
        pass

    # 画图
    # ----------------------------------------------------------------------
    def onPaint(self):
        pass


########################################################################
# 选择缩放功能支持
########################################################################
class CustomViewBox(pg.ViewBox):
    # ----------------------------------------------------------------------
    def __init__(self, *args, **kwds):
        pg.ViewBox.__init__(self, *args, **kwds)

    ## 右键自适应
    def mouseClickEvent(self, ev):
        if ev.button() == QtCore.Qt.RightButton:
            self.autoRange()


########################################################################
# 时间序列，横坐标支持
########################################################################
class MyStringAxis(pg.AxisItem):
    """时间序列横坐标支持"""

    # 初始化 
    # ----------------------------------------------------------------------
    def __init__(self, xdict, *args, **kwargs):
        pg.AxisItem.__init__(self, *args, **kwargs)
        self.minVal = 0
        self.maxVal = 0
        self.xdict = xdict
        self.x_values = np.asarray(xdict.keys())
        self.x_strings = xdict.values()
        self.setPen(color=(255, 255, 255, 255), width=0.8)
        # self.setStyle(tickFont=QFont("Arial", 6, QFont.Bold), autoExpandTextSpace=True)

    # 更新坐标映射表
    # ----------------------------------------------------------------------
    def update_xdict(self, xdict):
        self.xdict.update(xdict)
        self.x_values = np.asarray(self.xdict.keys())
        self.x_strings = self.xdict.values()

    # 将原始横坐标转换为时间字符串,第一个坐标包含日期
    # ----------------------------------------------------------------------
    def tickStrings(self, values, scale, spacing):
        strings = []
        for v in values:
            vs = v * scale
            if vs in self.x_values:
                vstr = self.x_strings[np.abs(self.x_values - vs).argmin()]
                vstr = vstr.strftime('%Y-%m-%d %H:%M:%S')
            else:
                vstr = ""
            strings.append(vstr)
        return strings


########################################################################
# K线图形对象
########################################################################
class CandlestickItem(pg.GraphicsObject):
    """K线图形对象"""

    # 初始化
    # ----------------------------------------------------------------------
    def __init__(self, data: pd.DataFrame):
        """初始化"""
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

        # 刷新K线
        self.generatePicture(self.data)

        # 画K线

    # ----------------------------------------------------------------------
    def generatePicture(self, data=None, redraw=False):
        """重新生成图形对象"""
        # 重画或者只更新最后一个K线
        if redraw:
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
                # 下跌绿色（实心）, 上涨红色（空心）
                if row['close'] < row['open']:  # 阴线情况
                    p.setPen(pg.mkPen('g', width=2))  # 设置画笔颜色，宽度
                    p.setBrush(pg.mkBrush('g'))
                    p.drawLine(QtCore.QPointF(index, row['low']), QtCore.QPointF(index, row['high']))  # 画上下影线
                    p.drawRect(QtCore.QRectF(index - w, row['open'], w * 2, row['close'] - row['open']))  # 画矩形，实心K线

                elif row['close'] > row['open']:  # 阳线情况
                    p.setPen(pg.mkPen('r', width=2))  # red
                    p.setBrush(pg.mkBrush('r'))  # red
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
                    p.setPen(pg.mkPen('b', width=2))  # 十字线设为蓝色
                    p.setBrush(pg.mkBrush('b'))  # 十字线设为蓝色

                    p.drawLine(QtCore.QPointF(index, row['high']), QtCore.QPointF(index, row['low']))  # 画上下影线
                    p.drawLine(QtCore.QPointF(index - w, row['close']), QtCore.QPointF(index + w, row['close']))  # 画一条横线

                p.end()
                self.pictures.append(picture)

    # 手动重画
    # ----------------------------------------------------------------------
    def update(self):
        if not self.scene() is None:
            self.scene().update()

    # 自动重画
    # ----------------------------------------------------------------------
    def paint(self, painter, opt, w):
        rect = opt.exposedRect
        xmin, xmax = (max(0, int(rect.left())), min(int(len(self.pictures)), int(rect.right())))
        if not self.rect == (rect.left(), rect.right()) or self.picture is None:
            self.rect = (rect.left(), rect.right())
            self.picture = self.createPic(xmin, xmax)
            self.picture.play(painter)
        elif not self.picture is None:
            self.picture.play(painter)

    # 缓存图片
    # ----------------------------------------------------------------------
    def createPic(self, xmin, xmax):
        picture = QPicture()
        p = QPainter(picture)
        [pic.play(p) for pic in self.pictures[xmin:xmax]]
        p.end()
        return picture

    # 定义边界
    # ----------------------------------------------------------------------
    def boundingRect(self):
        return QtCore.QRectF(0, self.low, len(self.pictures), (self.high - self.low))




########################################################################
# 成交量图形对象
########################################################################
class VolumeItem(pg.GraphicsObject):
    """K线图形对象"""

    # 初始化
    # ----------------------------------------------------------------------
    def __init__(self, data: pd.DataFrame):
        """初始化"""
        pg.GraphicsObject.__init__(self)
        self.data = data
        # 只重画部分图形，大大提高界面更新速度
        self.rect = None
        self.picture = None
        self.setFlag(self.ItemUsesExtendedStyleOption)

        self.offset = 0
        self.low = 0
        self.high = 1
        self.picture = QtGui.QPicture()
        self.pictures = []

        # 刷新柱线
        self.generatePicture(self.data)

        # 画柱线

    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------
    def generatePicture(self, data=None, redraw=False):
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
                    p.setPen(pg.mkPen('g', width=2))  # 设置画笔颜色，宽度
                    p.setBrush(pg.mkBrush('g'))
                    p.drawRect(QtCore.QRectF(index - w, 0, w * 2, row['volume']))  # 画矩形，实心成交量柱线

                elif row['close'] > row['open']:  # 阳线情况
                    p.setPen(pg.mkPen('r', width=2))  # red
                    p.setBrush(pg.mkBrush('r'))  # red

                    # p.drawRect(QtCore.QRectF(i - w, open, w * 2, close - open)) # 如果画实心阳线，只需画个实心矩形即可
                    # 画空心阳线的时候，需要画四条线

                    p.drawLine(QtCore.QPointF(index - w, 0), QtCore.QPointF(index - w, row['volume']))  # 画单根成交量柱线的左边线
                    p.drawLine(QtCore.QPointF(index + w, 0), QtCore.QPointF(index + w, row['volume']))  # 画单根成交量柱线的右边线
                    p.drawLine(QtCore.QPointF(index - w, row['volume']), QtCore.QPointF(index + w, row['volume']))  # 画单根成交量柱线的下边线
                    p.drawLine(QtCore.QPointF(index - w, 0), QtCore.QPointF(index + w, 0))  # 画单根成交量柱线的上边线

                else:  # 平盘情况
                    p.setPen(pg.mkPen('b', width=2))  # 十字线设为蓝色
                    p.setBrush(pg.mkBrush('b'))  # 十字线设为蓝色

                    p.drawRect(QtCore.QRectF(index - w, 0, w * 2, row['volume']))  # 画矩形，实心成交量柱线

                p.end()
                self.pictures.append(picture)

    # 手动重画
    # ----------------------------------------------------------------------
    def update(self):
        if not self.scene() is None:
            self.scene().update()

    # 自动重画
    # ----------------------------------------------------------------------
    def paint(self, painter, opt, w):
        rect = opt.exposedRect
        xmin, xmax = (max(0, int(rect.left())), min(int(len(self.pictures)), int(rect.right())))
        if not self.rect == (rect.left(), rect.right()) or self.picture is None:
            self.rect = (rect.left(), rect.right())
            self.picture = self.createPic(xmin, xmax)
            self.picture.play(painter)
        elif not self.picture is None:
            self.picture.play(painter)

    # 缓存图片
    # ----------------------------------------------------------------------
    def createPic(self, xmin, xmax):
        picture = QPicture()
        p = QPainter(picture)
        [pic.play(p) for pic in self.pictures[xmin:xmax]]
        p.end()
        return picture

    # 定义边界
    # ----------------------------------------------------------------------
    def boundingRect(self):
        return QtCore.QRectF(0, self.low, len(self.pictures), (self.high - self.low))



########################################################################
# MACD图形对象
########################################################################
class MACDItem(pg.GraphicsObject):
    """K线图形对象"""

    # 初始化
    # ----------------------------------------------------------------------
    def __init__(self, data: pd.DataFrame):
        """初始化"""
        pg.GraphicsObject.__init__(self)
        self.data = data
        # 只重画部分图形，大大提高界面更新速度
        self.rect = None
        self.picture = None
        self.setFlag(self.ItemUsesExtendedStyleOption)

        self.offset = 0
        self.low = 0
        self.high = 1
        self.picture = QtGui.QPicture()
        self.pictures = []

        self.generatePicture(self.data)

    # 画柱线
    # ----------------------------------------------------------------------
    def generatePicture(self, data=None, redraw=False):
        """重新生成图形对象"""
        if redraw:          # 重画或者只更新最后一个K线
            self.pictures = []
        elif self.pictures:
            self.pictures.pop()

        if len(data) > 0:
            self.low = data['bar'].min()
            self.high = data['bar'].max()
        else:
            self.low, self.high = (0, 1)

        npic = len(self.pictures)
        diff_cache = (self.high + self.low) / 2
        dea_cache = (self.high + self.low) / 2

        for index, row in data.iterrows():
            if index >= npic:
                picture = QtGui.QPicture()
                p = QtGui.QPainter(picture)
                if index > 0:
                    p.setPen(pg.mkPen('y', width=2))
                    p.drawLine(QtCore.QPointF(index-1,diff_cache), QtCore.QPointF(index, row['diff']))
                    diff_cache = row['diff']
                    p.setPen(pg.mkPen('w', width=2))
                    p.drawLine(QtCore.QPointF(index-1, dea_cache), QtCore.QPointF(index, row['dea']))
                    dea_cache = row['dea']

                if row['bar'] > 0:      # macd红柱
                    p.setPen(pg.mkPen('r', width=6))  # 设置画笔颜色，宽度
                    p.setBrush(pg.mkBrush('r'))
                    p.drawLine(QtCore.QPointF(index, 0), QtCore.QPointF(index, row['bar']))

                else:           # macd 绿柱

                    p.setPen(pg.mkPen('g', width=6))
                    p.setBrush(pg.mkBrush('g'))
                    p.drawLine(QtCore.QPointF(index, 0), QtCore.QPointF(index, row['bar']))

                p.end()
                self.pictures.append(picture)

    # 手动重画
    # ----------------------------------------------------------------------
    def update(self):
        if not self.scene() is None:
            self.scene().update()

    # 自动重画
    # ----------------------------------------------------------------------
    def paint(self, painter, opt, w):
        rect = opt.exposedRect
        xmin, xmax = (max(0, int(rect.left())), min(int(len(self.pictures)), int(rect.right())))
        if not self.rect == (rect.left(), rect.right()) or self.picture is None:
            self.rect = (rect.left(), rect.right())
            self.picture = self.createPic(xmin, xmax)
            self.picture.play(painter)
        elif not self.picture is None:
            self.picture.play(painter)

    # 缓存图片
    # ----------------------------------------------------------------------
    def createPic(self, xmin, xmax):
        picture = QPicture()
        p = QPainter(picture)
        [pic.play(p) for pic in self.pictures[xmin:xmax]]
        p.end()
        return picture

    # 定义边界
    # ----------------------------------------------------------------------
    def boundingRect(self):
        return QtCore.QRectF(0, self.low, len(self.pictures), (self.high - self.low))


########################################################################
class KLineWidget(KeyWraper):
    """用于显示价格走势图"""

    clsId = 0           # 窗口标识

    listOpenInterest = []       # 保存K线数据的列表和Numpy Array对象
    arrows = []
    initCompleted = False       # 是否完成了历史数据的读取标志

    def __init__(self, parent=None):

        self.parent = parent
        super(KLineWidget, self).__init__(parent)

        self.index = None  # 当前序号   # 下标
        self.countK = 100  # 默认显示的Ｋ线根数

        KLineWidget.clsId += 1
        self.windowId = str(KLineWidget.clsId)

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
        self.initUi()   # 调用函数

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
        self.lay_KL.setSpacing(2)  # 设置图层内图元间距，多个图元间距
        # self.KLtitle = self.lay_KL.addLabel(u'')  # 设置标题标签,默认不需要
        self.pw.setCentralItem(self.lay_KL)  # 设置主图
        # 设置横坐标
        xdict = {}
        self.axisTime = MyStringAxis(xdict, orientation='bottom')  # 时间坐标轴
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

    # ----------------------------------------------------------------------

    def makePlotItem(self, name):
        """生成PlotItem对象"""
        self.vb = CustomViewBox()
        self.plotItem = pg.PlotItem(viewBox=self.vb, name=name, axisItems=None)
        # plotItem = pg.PlotItem(viewBox = vb, name=name ,axisItems={'bottom': self.axisTime})

        self.plotItem.setMenuEnabled(False)  # 隐藏菜单
        self.plotItem.setClipToView(True)  # 在ViewBox可见范围内绘制所有数据
        self.plotItem.hideAxis('left')  # 隐藏左边坐标轴
        self.plotItem.showAxis('right')  # 显示右边坐标轴

        self.plotItem.setDownsampling(mode='peak')  # 缩减像素采样,峰值:通过画一个跟随原始数据的最小值和最大值的锯齿波向下采样。
        # 这种方法可以产生最好的数据可视化表示，但速度较慢。

        self.plotItem.setRange(xRange=(0, 1), yRange=(0, 1))  # 设置x、y轴范围
        self.plotItem.getAxis('right').setWidth(40)  # 设置右边坐标轴宽度
        self.plotItem.showGrid(True, True)  # 显示网格
        self.plotItem.setMinimumHeight(80)  # 图项最小高度
        self.plotItem.hideButtons()  # 隐藏刻度按钮
        # plotItem.setMouseEnabled(x=True, y=True)                       # 禁止鼠标拖动
        # self.plotItem.getAxis('right').setStyle(tickFont=QFont("Roman times", 10, QFont.Bold))  # 设置右边坐标轴刻度字体
        # self.plotItem.getAxis('bottom').setStyle(tickFont=QFont("Roman times", 10, QFont.Bold))  # 设置下边坐标轴刻度字体
        self.plotItem.getAxis('right').setPen(QtGui.QColor(255, 0, 0))  # y轴颜色
        self.plotItem.getAxis('bottom').setPen(QtGui.QColor(255, 0, 0))  # x轴颜色
        self.plotItem.getAxis('right').setTextPen(QtGui.QColor(150, 150, 150))  # y轴刻度颜色
        self.plotItem.getAxis('bottom').setTextPen(QtGui.QColor(150, 150, 150))  # x轴刻度颜色

        return self.plotItem

    # ----------------------------------------------------------------------
    def initplotKline(self):
        """初始化蜡烛图子图"""
        self.pwKL = self.makePlotItem('_'.join([self.windowId, 'PlotKL']))
        self.candle = CandlestickItem(self.datas)
        self.pwKL.addItem(self.candle)
        self.pwKL.setMinimumHeight(350)
        self.pwKL.setXLink('_'.join([self.windowId, 'PlotKL']))  # 设置x轴关联，使两个子图的x坐标一致
        self.pwKL.hideAxis('bottom')
        self.pwKL.getViewBox().sigXRangeChanged.connect(self.set_pwKL_yRange)  # 子图的x轴范围改变信号

        self.lay_KL.nextRow()
        self.lay_KL.addItem(self.pwKL)

    # ----------------------------------------------------------------------
    def initplotVol(self):
        """初始化成交量子图"""
        self.pwVol = self.makePlotItem('_'.join([self.windowId, 'PlotVOL']))
        self.volume = VolumeItem(self.datas)
        self.pwVol.addItem(self.volume)
        self.pwVol.setMaximumHeight(150)
        self.pwVol.setXLink('_'.join([self.windowId, 'PlotKL']))  # 设置x轴关联，使两个子图的x坐标一致
        self.pwVol.hideAxis('bottom')
        self.pwVol.setContentsMargins(1,0,1,0)

        self.pwKL.getViewBox().sigXRangeChanged.connect(self.set_pwVol_yRange)  # 子图的x轴范围改变信号

        self.lay_KL.nextRow()
        self.lay_KL.addItem(self.pwVol)

    # ----------------------------------------------------------------------
    def initplotMACD(self):
        """初始化MACD子图"""
        self.pwMACD = self.makePlotItem('_'.join([self.windowId, 'PlotMACD']))
        self.macd = MACDItem(self.datas)
        self.pwMACD.addItem(self.macd)
        self.pwMACD.setMaximumHeight(150)
        self.pwMACD.setXLink('_'.join([self.windowId, 'PlotKL']))  # 设置x轴关联，使两个子图的x坐标一致
        self.pwKL.hideAxis('bottom')
        self.pwKL.getViewBox().sigXRangeChanged.connect(self.set_pwMACD_yRange)  # 子图的x轴范围改变信号

        self.lay_KL.nextRow()
        self.lay_KL.addItem(self.pwMACD)

    # ----------------------------------------------------------------------
    #  画图相关 
    # ----------------------------------------------------------------------
    def plotKline(self, redraw=False, xmin=0, xmax=-1):
        """重画K线子图"""
        if self.initCompleted:
            self.candle.generatePicture(self.datas.loc[xmin:xmax], redraw)  # 画K线
            self.plotMark()  # 显示开平仓信号位置

    # ----------------------------------------------------------------------
    def plotVol(self, redraw=False, xmin=0, xmax=-1):
        """重画成交量子图"""
        if self.initCompleted:
            self.volume.generatePicture(self.datas.loc[xmin:xmax], redraw)  # 画成交量子图

    # ----------------------------------------------------------------------
    def PlotMACD(self, redraw=False, xmin=0, xmax=-1):
        """重画MACD子图"""
        if self.initCompleted:
            self.macd.generatePicture(self.datas.loc[xmin:xmax], redraw)  # 画MACD子图

    # ----------------------------------------------------------------------

    def set_pwKL_yRange(self):      # 设置pwKL的y轴显示范围,该函数由sigXRangeChanged信号驱动
        datas = self.datas
        view = self.pwKL.getViewBox()
        vRange = view.viewRange()
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
            view.setRange(yRange=(0, ymax))
        else:
            view.setRange(yRange=(0, 1))

    def set_pwMACD_yRange(self):      # 设置pwMACD的y轴显示范围,该函数由sigXRangeChanged信号驱动
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
            ymin = min(datas[xmin:xmax]['diff'])
            ymax = max(datas[xmin:xmax]['diff'])
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

    # ----------------------------------------------------------------------
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
                arrow = pg.ArrowItem(pos=(i, self.datas[i]['high']), angle=-90, brush=(0, 255, 0))
            self.pwKL.addItem(arrow)
            self.arrows.append(arrow)

    # ----------------------------------------------------------------------
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

    # ----------------------------------------------------------------------
    def plotAll(self, redraw=True, xMin=0, xMax=-1):
        """
        重画所有界面
        redraw ：False=重画最后一根K线; True=重画所有
        xMin,xMax : 数据范围
        """
        xMax = len(self.datas) - 1 if xMax < 0 else xMax

        self.pwKL.setLimits(xMin=xMin, xMax=xMax)
        self.pwVol.setLimits(xMin=xMin, xMax=xMax)
        self.pwMACD.setLimits(xMin=xMin, xMax=xMax)
        self.plotKline(redraw, xMin, xMax)  # K线图
        self.plotVol(redraw, xMin, xMax)  # K线副图，成交量
        self.PlotMACD(redraw, xMin, xMax)  # K线副图，MACD
        self.refresh()

    # ----------------------------------------------------------------------

    def refresh(self):
        """
        刷新三个子图的显示范围
        """
        minutes = int(self.countK / 2)
        xmin = max(0, self.index - minutes)
        try:
            xmax = min(xmin + 2 * minutes, len(self.datas) - 1) if self.datas else xmin + 2 * minutes
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
            self.crosshair.signal.emit((x, y))

    # ----------------------------------------------------------------------
    def onPre(self):
        """跳转到上一个开平仓点"""
        if len(self.listSig) > 0 and not self.index is None:
            if self.index > 0: self.index -= 1
            while self.index > 0 and self.listSig[self.index] == 0:
                self.index -= 1
            self.refresh()
            x = self.index
            y = self.datas[x]['close']
            self.crosshair.signal.emit((x, y))

    # ----------------------------------------------------------------------
    def onDown(self):
        """放大显示区间"""
        self.countK = min(len(self.datas), int(self.countK * 1.2) + 1)
        self.refresh()
        if len(self.datas) > 0:
            x = self.index - self.countK / 2 + 2 if int(self.crosshair.xAxis) < self.index - self.countK / 2 + 2 else int(self.crosshair.xAxis)
            x = self.index + self.countK / 2 - 2 if x > self.index + self.countK / 2 - 2 else x
            x = len(self.datas) - 1 if x > len(self.datas) - 1 else int(x)
            y = self.datas[x][2]
            self.crosshair.signal.emit((x, y))

    # ----------------------------------------------------------------------
    def onUp(self):
        """缩小显示区间"""
        self.countK = max(3, int(self.countK / 1.2) - 1)
        self.refresh()
        if len(self.datas) > 0:
            x = self.index - self.countK / 2 + 2 if int(self.crosshair.xAxis) < self.index - self.countK / 2 + 2 else int(self.crosshair.xAxis)
            x = self.index + self.countK / 2 - 2 if x > self.index + self.countK / 2 - 2 else x
            x = len(self.datas) - 1 if x > len(self.datas) - 1 else int(x)
            y = self.datas[x]['close']
            self.crosshair.signal.emit((x, y))

    # ----------------------------------------------------------------------
    def onLeft(self):
        """向左移动"""
        if len(self.datas) > 0 and int(self.crosshair.xAxis) > 2:
            x = int(self.crosshair.xAxis) - 1
            x = len(self.datas) - 1 if x > len(self.datas) - 1 else int(x)
            y = self.datas[x]['close']
            if x <= self.index - self.countK / 2 + 2 and self.index > 1:
                self.index -= 1
                self.refresh()
            self.crosshair.signal.emit((x, y))

    # ----------------------------------------------------------------------
    def onRight(self):
        """向右移动"""
        if len(self.datas) > 0 and int(self.crosshair.xAxis) < len(self.datas) - 1:
            x = int(self.crosshair.xAxis) + 1
            x = len(self.datas) - 1 if x > len(self.datas) - 1 else int(x)
            y = self.datas[x]['close']
            if x >= self.index + int(self.countK / 2) - 2:
                self.index += 1
                self.refresh()
            self.crosshair.signal.emit((x, y))

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


    # #----------------------------------------------------------------------
    # 数据相关
    # ----------------------------------------------------------------------
    def clearData(self):
        """清空数据"""
        # 清空数据，重新画图

        self.listSig = []
        self.sigData = {}
        self.datas = None

    # ----------------------------------------------------------------------
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

    # ----------------------------------------------------------------------
    def updateSig(self, sig):
        """刷新买卖信号"""
        self.listSig = sig
        self.plotMark()

    # ----------------------------------------------------------------------
    def onBar(self, bar):
        """
        新增K线数据,K线播放模式
        """
        # 是否需要更新K线
        if len(self.datas) > 0 and bar.datetime == self.datas[-1].datetime:
            newBar = False
        else:
            newBar = True

        if newBar:
            nrecords = len(self.datas)
        else:
            nrecords = len(self.datas) - 1

        if bar.openInterest == np.inf or bar.openInterest == -np.inf:
            bar.openInterest = np.random.randint(0, 3)
        else:
            bar.openInterest

        if bar.close < bar.open:
            recordVol = (nrecords, abs(bar.volume), 0, 0, abs(bar.volume))
        else:
            recordVol = (nrecords, 0, abs(bar.volume), 0, abs(bar.volume))

        if newBar and any(self.datas):
            self.datas.resize(nrecords + 1, refcheck=0)
            self.listBar.resize(nrecords + 1, refcheck=0)
            self.listVol.resize(nrecords + 1, refcheck=0)
        elif any(self.datas):
            self.listLow.pop()
            self.listHigh.pop()
            self.listOpenInterest.pop()
        if any(self.datas):
            self.datas[-1] = (bar.datetime, bar.open, bar.close, bar.low, bar.high, bar.volume, bar.openInterest)
            self.listBar[-1] = (nrecords, bar.open, bar.close, bar.low, bar.high)
            self.listVol[-1] = recordVol
        else:
            self.datas = np.rec.array([(bar.datetime, bar.open, bar.close, bar.low, bar.high, bar.volume, bar.openInterest)],
                                      names=('datetime', 'open', 'close', 'low', 'high', 'volume', 'openInterest'))
            self.listBar = np.rec.array([(nrecords, bar.open, bar.close, bar.low, bar.high)],
                                        names=('time_int', 'open', 'close', 'low', 'high'))
            self.listVol = np.rec.array([recordVol], names=('time_int', 'open', 'close', 'low', 'high'))
            self.get_yaxis_range(self.datas)

        self.axisTime.update_xdict({nrecords: bar.datetime})
        self.listLow.append(bar.low)
        self.listHigh.append(bar.high)
        self.listOpenInterest.append(bar.openInterest)
        self.get_yaxis_range(self.datas)
        return newBar

    # ----------------------------------------------------------------------
    def loadData(self, datas):
        """
        传进来pandas.DataFrame格式的k线数据,其中须有datetime, open, close, low, high 这几列
        然后计算瀑布线和macd,合并到这个DataFrame中
        """
        pb1 = PUBU(datas, 3)
        pb2 = PUBU(datas, 4)
        pb3 = PUBU(datas, 9)
        pb4 = PUBU(datas, 13)
        pb5 = PUBU(datas, 18)
        pb6 = PUBU(datas, 24)
        datas['pb1'] = pb1
        datas['pb2'] = pb2
        datas['pb3'] = pb3
        datas['pb4'] = pb4
        datas['pb5'] = pb5
        datas['pb6'] = pb6
        macd = MACD(datas, 12, 26, 9)

        self.datas = pd.concat([datas, macd], axis=1)
        # print('传入的数据为: ', self.datas)



    # ----------------------------------------------------------------------
    def refreshAll(self, redraw=True, update=False):
        """
        更新所有界面
        """
        # 调用画图函数
        self.index = len(self.datas)
        self.plotAll(redraw, 0, len(self.datas))
        if not update:
            self.updateAll()
        self.crosshair.signal.emit((None, None))
