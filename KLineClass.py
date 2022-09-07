# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from functools import partial
from collections import deque

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
        # 拖动放大模式
        # self.setMouseMode(self.RectMode)
        # self.setBackgroundColor(QtGui.QColor(255, 255, 255))  # 设置ViewBox的背景颜色

    ## 右键自适应
    # ----------------------------------------------------------------------
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
        # 画笔和画刷
        w = 0.4
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
            self.low, self.high = (np.min(data['low']), np.max(data['high']))
        else:
            self.low, self.high = (0, 1)
        npic = len(self.pictures)
        for (t, _open, _close, _low, _high) in data:
            if t >= npic:
                picture = QtGui.QPicture()
                p = QtGui.QPainter(picture)
                # 下跌绿色（实心）, 上涨红色（空心）
                if _close < _open:  # 阴线情况
                    p.setPen(pg.mkPen('g', width=2))  # 设置画笔颜色，宽度
                    p.setBrush(pg.mkBrush('g'))
                    p.drawLine(QtCore.QPointF(t, _low), QtCore.QPointF(t, _high))  # 画上下影线
                    p.drawRect(QtCore.QRectF(t - w, _open, w * 2, _close - _open))  # 画矩形，实心K线

                elif _close > _open:  # 阳线情况
                    p.setPen(pg.mkPen('r', width=2))  # red
                    p.setBrush(pg.mkBrush('r'))  # red
                    if (_high != _close):  # 如果最高点不等于收盘价，画上影线
                        p.drawLine(QtCore.QPointF(t, _high), QtCore.QPointF(t, _close))
                    if (_low != _open):  # 如果最低点不等于开盘价，画下影线
                        p.drawLine(QtCore.QPointF(t, _open), QtCore.QPointF(t, _low))

                    # p.drawRect(QtCore.QRectF(i - w, open, w * 2, close - open)) # 如果画实心阳线，只需画个实心矩形即可
                    # 画空心阳线的时候，需要画四条线

                    p.drawLine(QtCore.QPointF(t - w, _open), QtCore.QPointF(t - w, _close))  # 画单根K线的左边线
                    p.drawLine(QtCore.QPointF(t + w, _open), QtCore.QPointF(t + w, _close))  # 画单根K线的右边线
                    p.drawLine(QtCore.QPointF(t - w, _close), QtCore.QPointF(t + w, _close))  # 画单根K线的上边线
                    p.drawLine(QtCore.QPointF(t - w, _open), QtCore.QPointF(t + w, _open))  # 画单根K线的下边线

                else:  # 平盘情况
                    p.setPen(pg.mkPen('b', width=2))  # 十字线设为蓝色
                    p.setBrush(pg.mkBrush('b'))  # 十字线设为蓝色

                    p.drawLine(QtCore.QPointF(t, _high), QtCore.QPointF(t, _low))  # 画上下影线
                    p.drawLine(QtCore.QPointF(t - w, _close), QtCore.QPointF(t + w, _close))  # 画一条横线

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

    # 计算y轴显示的范围
    # ----------------------------------------------------------------------
    def get_y_range(self, min_ix: int = None, max_ix: int = None) -> tuple[float, float]:
        print(self.data)
        min_price = self.data.loc[min_ix:max_ix].low.min()
        max_price = self.data.loc[min_ix:max_ix].high.max()
        print('当前显示k线范围: ', min_price, max_price)

        return min_price, max_price


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
        # 画笔和画刷
        w = 0.4
        self.offset = 0
        self.low = 0
        self.high = 1
        self.picture = QtGui.QPicture()
        self.pictures = []

        # 刷新K线
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

        if len(data) > 0:
            self.low, self.high = (np.min(data['low']), np.max(data['high']))
        else:
            self.low, self.high = (0, 1)
        npic = len(self.pictures)
        for (t, open, close, low, high) in data:
            if t >= npic:
                picture = QtGui.QPicture()
                p = QtGui.QPainter(picture)
                # 下跌绿色（实心）, 上涨红色（空心）
                if close < open:  # 阴线情况
                    p.setPen(pg.mkPen('g', width=2))  # 设置画笔颜色，宽度
                    p.setBrush(pg.mkBrush('g'))
                    p.drawLine(QtCore.QPointF(t, low), QtCore.QPointF(t, high))  # 画上下影线                
                    p.drawRect(QtCore.QRectF(t - w, open, w * 2, close - open))  # 画矩形，实心K线

                elif close > open:  # 阳线情况
                    p.setPen(pg.mkPen('r', width=2))  # red
                    p.setBrush(pg.mkBrush('r'))  # red
                    if (high != close):  # 如果最高点不等于收盘价，画上影线
                        p.drawLine(QtCore.QPointF(t, high), QtCore.QPointF(t, close))
                    if (low != open):  # 如果最低点不等于开盘价，画下影线
                        p.drawLine(QtCore.QPointF(t, open), QtCore.QPointF(t, low))

                    # p.drawRect(QtCore.QRectF(i - w, open, w * 2, close - open)) # 如果画实心阳线，只需画个实心矩形即可
                    # 画空心阳线的时候，需要画四条线

                    p.drawLine(QtCore.QPointF(t - w, open), QtCore.QPointF(t - w, close))  # 画单根K线的左边线
                    p.drawLine(QtCore.QPointF(t + w, open), QtCore.QPointF(t + w, close))  # 画单根K线的右边线
                    p.drawLine(QtCore.QPointF(t - w, close), QtCore.QPointF(t + w, close))  # 画单根K线的上边线
                    p.drawLine(QtCore.QPointF(t - w, open), QtCore.QPointF(t + w, open))  # 画单根K线的下边线

                else:  # 平盘情况
                    p.setPen(pg.mkPen('b', width=2))  # 十字线设为蓝色
                    p.setBrush(pg.mkBrush('b'))  # 十字线设为蓝色

                    p.drawLine(QtCore.QPointF(t, high), QtCore.QPointF(t, low))  # 画上下影线
                    p.drawLine(QtCore.QPointF(t - w, close), QtCore.QPointF(t + w, close))  # 画一条横线

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

    # 计算y轴显示的范围
    # ----------------------------------------------------------------------
    def get_y_range(self, min_ix: int = None, max_ix: int = None) -> tuple[float, float]:

        min_price = self.datas.loc[min_ix:max_ix].low.min()
        max_price = self.datas.loc[min_ix:max_ix].high.max()

        return min_price, max_price


########################################################################
class KLineWidget(KeyWraper):
    """用于显示价格走势图"""

    # 窗口标识
    clsId = 0

    # 保存K线数据的列表和Numpy Array对象
    listBar = []
    listVol = []
    listHigh = []
    listLow = []
    listSig = []
    listOpenInterest = []
    arrows = []

    # 是否完成了历史数据的读取
    initCompleted = False

    # ----------------------------------------------------------------------
    def __init__(self, parent=None):
        """Constructor"""
        self.curveOI = None
        self.pwInd = None
        self.volume = None
        self.pwVol = None
        self.candle = None
        self.plotItem = None
        self.vb = None
        self.pwKL = None
        self.VboxL = None
        self.crosshair = None
        self.axisTime = None
        self.pw = None
        self.lay_KL = None
        self.time_index = None
        self.parent = parent
        super(KLineWidget, self).__init__(parent)

        # 当前序号
        self.index = None  # 下标
        self.countK = 100  # 默认显示的Ｋ线根数

        KLineWidget.clsId += 1
        self.windowId = str(KLineWidget.clsId)

        # 缓存数据
        self.datas = pd.DataFrame()
        self.listBar = []
        self.listVol = []
        self.listHigh = []
        self.listLow = []
        self.listSig = []
        self.listOpenInterest = []
        self.arrows = []

        # 所有K线上信号图
        self.allColor = deque(['blue', 'green', 'yellow', 'white'])
        self.sigData = {}
        self.sigColor = {}
        self.sigPlots = {}

        # 所副图上信号图
        self.allSubColor = deque(['blue', 'green', 'yellow', 'white'])
        self.subSigData = {}
        self.subSigColor = {}
        self.subSigPlots = {}

        # 初始化完成
        self.initCompleted = False

        # 调用函数
        self.initUi()

    # ----------------------------------------------------------------------
    #  初始化相关 
    # ----------------------------------------------------------------------
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
        self.initplotIndicators()  # 指标子图
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
        """初始化K线子图"""
        self.pwKL = self.makePlotItem('_'.join([self.windowId, 'PlotKL']))
        self.candle = CandlestickItem(self.datas)
        self.pwKL.addItem(self.candle)
        self.pwKL.setMinimumHeight(350)
        self.pwKL.setXLink('_'.join([self.windowId, 'PlotKL']))  # 设置x轴关联，使两个子图的x坐标一致
        self.pwKL.hideAxis('bottom')

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

        self.lay_KL.nextRow()
        self.lay_KL.addItem(self.pwVol)

    # ----------------------------------------------------------------------
    def initplotIndicators(self):  # 原函数名：initplotOI
        """初始化指标子图"""
        self.pwInd = self.makePlotItem('_'.join([self.windowId, 'PlotInd']))
        self.pwInd.setMaximumHeight(150)
        self.pwInd.setXLink('_'.join([self.windowId, 'PlotKL']))  # 设置x轴关联，使两个子图的x坐标一致
        self.curveOI = self.pwInd.plot()

        self.lay_KL.nextRow()
        self.lay_KL.addItem(self.pwInd)

    # ----------------------------------------------------------------------
    #  画图相关 
    # ----------------------------------------------------------------------
    def plotKline(self, redraw=False, xmin=0, xmax=-1):
        """重画K线子图"""
        if self.initCompleted:
            self.candle.generatePicture(self.listBar[xmin:xmax], redraw)  # 画K线
            self.plotMark()  # 显示开平仓信号位置

    # ----------------------------------------------------------------------
    def plotVol(self, redraw=False, xmin=0, xmax=-1):
        """重画成交量子图"""
        if self.initCompleted:
            self.volume.generatePicture(self.listVol[xmin:xmax], redraw)  # 画成交量子图

    # ----------------------------------------------------------------------
    def PlotInd(self, xmin=0, xmax=-1):
        """重画指标子图"""
        if self.initCompleted:
            self.curveOI.setData(np.append(self.listOpenInterest[xmin:xmax], 0), pen='w', name="OpenInterest")

            # ----------------------------------------------------------------------

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
                self.pwInd.removeItem(self.subSigPlots[sig])
            self.subSigPlots[sig] = self.pwInd.plot()
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
                self.PlotInd(0, len(sigDatas))
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
        self.volume.pictrue = None
        self.candle.pictrue = None
        self.volume.update()
        self.candle.update()

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

    # ----------------------------------------------------------------------
    def plotAll(self, redraw=True, xMin=0, xMax=-1):
        """
        重画所有界面
        redraw ：False=重画最后一根K线; True=重画所有
        xMin,xMax : 数据范围
        """
        # if xMax < 0:
        #     xMax = len(self.datas) - 1
        # else:
        #     xMax
        xMax = len(self.datas) - 1 if xMax < 0 else xMax
        # self.countK = xMax-xMin
        # self.index = int((xMax+xMin)/2)
        self.pwKL.setLimits(xMin=xMin, xMax=xMax)
        self.pwVol.setLimits(xMin=xMin, xMax=xMax)
        self.pwInd.setLimits(xMin=xMin, xMax=xMax)
        self.plotKline(redraw, xMin, xMax)  # K线图
        self.plotVol(redraw, xMin, xMax)  # K线副图，成交量
        self.PlotInd(0, len(self.datas))  # K线副图，指标
        self.refresh()

    # ----------------------------------------------------------------------
    def get_item_y_range(self):
        if self.candle:
            self.candle.get_y_range()

    def refresh(self):
        """
        刷新三个子图的显示范围
        """
        datas = self.datas
        # minutes = int(self.countK / 2)
        try:
            xmin = max(0, self.index - self.countK)
            if self.datas:
                xmax = min(xmin + self.countK, len(self.datas) - 1)
            else:
                xmax = xmin + self.countK
        except:
            xmax = xmin + self.countK
        self.pwKL.setRange(xRange=(xmin, xmax))
        self.pwVol.setRange(xRange=(xmin, xmax))
        self.pwInd.setRange(xRange=(xmin, xmax))

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

    # ----------------------------------------------------------------------

    def get_yaxis_range(self, datas):
        """设置y轴范围"""
        view = self.pwKL.getViewBox()
        vRange = view.viewRange()
        xmin = max(0, int(vRange[0][0]))
        xmax = max(0, int(vRange[0][1]))
        print('datas的类型是：', type(datas))
        print('datas为', datas)
        print('x的取值范围为:', xmin, xmax)
        if len(datas) > 0 and xmax > xmin:
            ymin = min(datas.loc[xmin:xmax]['low'])
            print('y的最小值为:', ymin)
            ymax = max(datas.loc[xmin:xmax]['high'])
            print('y的最大值为:', ymax)

        self.refresh()

    def resignData(self, datas):
        """更新数据，用于Y坐标自适应"""

        # self.crosshair.datas = datas
        def viewXRangeChanged(low, high):
            vRange = view.viewRange()
            xmin = max(0, int(vRange[0][0]))
            xmax = max(0, int(vRange[0][1]))
            xmax = min(xmax, len(datas))

            if len(datas) > 0 and xmax > xmin:
                ymin = min(datas.loc[xmin:xmax]['low'])
                print('y的最小值为:', ymin)
                ymax = max(datas.loc[xmin:xmax]['high'])
                print('y的最大值为:', ymax)

                if ymin == ymax:
                    view.setRange(yRange=(-1, 1))
                else:
                    view.setRange(yRange=(ymin, ymax))

            else:
                view.setRange(yRange=(0, 1))

        view = self.pwKL.getViewBox()
        view.sigXRangeChanged.connect(partial(viewXRangeChanged, ('low', 'high')))

        view = self.pwVol.getViewBox()
        view.sigXRangeChanged.connect(partial(viewXRangeChanged, ('volume', 'volume')))

        view = self.pwInd.getViewBox()
        view.sigXRangeChanged.connect(partial(viewXRangeChanged, ('openInterest', 'openInterest')))

    # #----------------------------------------------------------------------
    # 数据相关
    # ----------------------------------------------------------------------
    def clearData(self):
        """清空数据"""
        # 清空数据，重新画图
        self.time_index = []
        self.listBar = []
        self.listVol = []
        self.listLow = []
        self.listHigh = []
        self.listOpenInterest = []
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
                self.pwInd.removeItem(self.subSigPlots[sig])
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
    def loadData(self, datas, sigs=None):
        """
        载入pandas.DataFrame数据
        datas : 数据格式，cols : datetime, open, close, low, high
        """
        # 设置中心点时间
        # 绑定数据，更新横坐标映射，更新Y轴自适应函数，更新十字光标映射
        self.datas = datas
        self.datas['time_int'] = np.array(range(len(self.datas.index)))
        # for index, row in self.datas.iterrows():
        #     row['times'] = tafunc.time_to_datetime(row['datetime'])
        # self.datas['times'] = self.datas.strftime('%Y-%M-%D')

        self.axisTime.xdict = {}
        xdict = dict(enumerate(self.datas.datetime.tolist()))
        self.axisTime.update_xdict(xdict)
        # self.get_yaxis_range(self.datas)
        # 更新画图用到的数据
        self.listBar = self.datas[['time_int', 'open', 'close', 'low', 'high']].to_records(False)
        self.listHigh = list(self.datas['high'])
        self.listLow = list(self.datas['low'])
        # self.listOpenInterest = list(datas['openInterest'])
        self.listSig = [0] * (len(self.datas) - 1) if sigs is None else sigs
        # 成交量颜色和涨跌同步，K线方向由涨跌决定
        datas0 = pd.DataFrame()
        datas0['open'] = self.datas.apply(lambda x: 0 if x['close'] >= x['open'] else x['volume'], axis=1)
        datas0['close'] = self.datas.apply(lambda x: 0 if x['close'] < x['open'] else x['volume'], axis=1)
        datas0['low'] = 0
        datas0['high'] = self.datas['volume']
        datas0['time_int'] = np.array(range(len(self.datas.index)))
        self.listVol = datas0[['time_int', 'open', 'close', 'low', 'high']].to_records(False)

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
