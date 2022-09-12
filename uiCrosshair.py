# -*- coding: utf-8 -*-
import datetime as dt

import pyqtgraph as pg
from pyqtgraph.Point import Point
from PySide6 import QtCore
from tqsdk import tafunc


########################################################################
# 十字光标类
########################################################################
class Crosshair(QtCore.QObject):
    """
    此类给pg.PlotWidget()添加crossHair功能,PlotWidget实例需要初始化时传入
    """
    signal = QtCore.Signal()
    signalInfo = QtCore.Signal(float, float)


    # ----------------------------------------------------------------------
    def __init__(self, parent, master):
        """Constructor"""
        self.__view = parent
        self.master = master
        super(Crosshair, self).__init__()

        self.xAxis = 0
        self.yAxis = 0

        self.datas = None

        self.yAxises = [0 for i in range(3)]
        self.leftX = [0 for i in range(3)]
        self.showHLine = [False for i in range(3)]
        self.textPrices = [pg.TextItem('', anchor=(1, 1)) for i in range(3)]
        self.views = [parent.centralWidget.getItem(i + 1, 0) for i in range(3)]
        self.rects = [self.views[i].sceneBoundingRect() for i in range(3)]
        self.vLines = [pg.InfiniteLine(angle=90, movable=False) for i in range(3)]
        self.hLines = [pg.InfiniteLine(angle=0, movable=False) for i in range(3)]

        # mid 在y轴动态跟随最新价显示最新价和最新时间
        self.__textDate = pg.TextItem('date', anchor=(1, 1))
        self.__textInfo = pg.TextItem('lastBarInfo')
        self.__textInd = pg.TextItem('lastIndInfo', anchor=(1, 0))
        self.__textMACD = pg.TextItem('lastMACDInfo', anchor=(1, 0))
        self.__textVolume = pg.TextItem('lastBarVolume', anchor=(1, 0))

        self.__textDate.setZValue(20)
        self.__textInfo.setZValue(20)
        self.__textInd.setZValue(20)
        self.__textMACD.setZValue(20)
        self.__textVolume.setZValue(20)
        self.__textInfo.border = pg.mkPen(color=(230, 255, 0, 255), width=1.2)

        for i in range(3):
            self.textPrices[i].setZValue(2)
            self.vLines[i].setPos(0)
            self.hLines[i].setPos(0)
            self.vLines[i].setZValue(0)
            self.hLines[i].setZValue(0)
            self.views[i].addItem(self.vLines[i])
            self.views[i].addItem(self.hLines[i])
            self.views[i].addItem(self.textPrices[i])

        self.views[0].addItem(self.__textInfo, ignoreBounds=True)
        self.views[0].addItem(self.__textInd, ignoreBounds=True)
        self.views[1].addItem(self.__textVolume, ignoreBounds=True)
        self.views[2].addItem(self.__textDate, ignoreBounds=True)
        self.views[2].addItem(self.__textMACD, ignoreBounds=True)
        self.proxy = pg.SignalProxy(self.__view.scene().sigMouseMoved, rateLimit=360, slot=self.__mouseMoved)
        # self.proxy2 = pg.SignalProxy(self.__view.scene().wheelEvent,rateLimit=360, slot=self.__mouseMoved)
        # 跨线程刷新界面支持
        self.signal.connect(self.update)
        self.signalInfo.connect(self.plotInfo)


    # ----------------------------------------------------------------------
    def update(self, pos):
        """刷新界面显示"""
        print('运行到这里了')
        xAxis, yAxis = pos
        xAxis, yAxis = (self.xAxis, self.yAxis) if xAxis is None else (xAxis, yAxis)
        self.moveTo(xAxis, yAxis)
        # self.rects = [self.views[i].sceneBoundingRect() for i in range(3)]

        # self.set_pos()
    # ----------------------------------------------------------------------
    def __mouseMoved(self, evt):
        """鼠标移动回调"""
        pos = evt[0]
        self.rects = [self.views[i].sceneBoundingRect() for i in range(3)]
        for i in range(3):
            self.showHLine[i] = False
            if self.rects[i].contains(pos):
                mousePoint = self.views[i].vb.mapSceneToView(pos)
                xAxis = mousePoint.x()
                yAxis = mousePoint.y()
                self.yAxises[i] = yAxis
                self.showHLine[i] = True
                self.moveTo(xAxis, yAxis)


    # ----------------------------------------------------------------------
    def moveTo(self, xAxis, yAxis):
        if xAxis is None:
            xAxis, yAxis = (self.xAxis, self.yAxis)
        else:
            xAxis, yAxis = (int(xAxis), yAxis)
        self.rects = [self.views[i].sceneBoundingRect() for i in range(3)]

        if not xAxis or not yAxis:
            return
        self.xAxis = xAxis
        self.yAxis = yAxis
        self.vhLinesSetXY(xAxis, yAxis)
        self.plotInfo(xAxis, yAxis)
        self.master.candle.update()


    # ----------------------------------------------------------------------
    def vhLinesSetXY(self, xAxis, yAxis):
        """水平和竖线位置设置"""
        for i in range(3):
            self.vLines[i].setPos(xAxis)
            if self.showHLine[i]:
                self.hLines[i].setPos(yAxis if i == 0 else self.yAxises[i])
                self.hLines[i].show()
            else:
                self.hLines[i].hide()


    # ----------------------------------------------------------------------
    def plotInfo(self, xAxis, yAxis):
        """
        被嵌入的plotWidget在需要的时候通过调用此方法显示K线信息
        """
        if self.datas is None:
            return
        try:
            # 获取K线数据
            data = self.datas.loc[xAxis]
            lastdata = self.datas.loc[xAxis - 1]

            # 用天勤自带的时间转换函数将时间截转换成datetime格式
            tickDatetime = tafunc.time_to_datetime(data['datetime'])
            openPrice = data['open']
            closePrice = data['close']
            lowPrice = data['low']
            highPrice = data['high']
            volume = int(data['volume'])
            preClosePrice = lastdata['close']
            diff = data['diff']
            dea = data['dea']
            bar = data['bar']
            mv1 = data['mv1']
            mv2 = data['mv2']
            pb1 = data['pb1']
            pb2 = data['pb2']
            pb3 = data['pb3']
            pb4 = data['pb4']
            pb5 = data['pb5']
            pb6 = data['pb6']

        except Exception as e:
            print(e)
            return

        if (isinstance(tickDatetime, dt.datetime)):
            datetimeText = dt.datetime.strftime(tickDatetime, '%m-%d %H:%M')
            dateText = dt.datetime.strftime(tickDatetime, '%m-%d')
            timeText = dt.datetime.strftime(tickDatetime, '%H:%M')
        else:
            datetimeText = ""
            dateText = ""
            timeText = ""



        # 显示高开低收及日期
        # 和上一个收盘价比较，决定K线信息的字符颜色
        cOpen = 'red' if openPrice > preClosePrice else 'green'
        cClose = 'red' if closePrice > preClosePrice else 'green'
        cHigh = 'red' if highPrice > preClosePrice else 'green'
        cLow = 'red' if lowPrice > preClosePrice else 'green'

        self.__textInfo.setHtml(u'<div style="text-align: center; background-color:rgb(13,9,27)">\
                                <span style="color: rgb(255,255,255);  font-size: 14px;">日期</span><br>\
                                <span style="color: rgb(0,255,255); font-size: 16px;">%s</span><br>\
                                <span style="color: white;  font-size: 14px;">时间</span><br>\
                                <span style="color: rgb(0,255,255); font-size: 16px;">%s</span><br>\
                                <span style="color: rgb(255,255,255);  font-size: 14px;">价格</span><br>\
                                <span style="color: %s;     font-size: 12px;">开:%.1f</span><br>\
                                <span style="color: %s;     font-size: 12px;">高:%.1f</span><br>\
                                <span style="color: %s;     font-size: 12px;">低:%.1f</span><br>\
                                <span style="color: %s;     font-size: 12px;">收:%.1f</span><br>\
                                <span style="color: rgb(255,255,255);  font-size: 14px;">成交量:</span><br>\
                                <span style="color: rgb(0,255,255); font-size: 14px;">%d</span><br>\
                            </div>' % (dateText, timeText, cOpen, openPrice, cHigh, highPrice, cLow, lowPrice, cClose, closePrice, volume))
        # 显示纵轴时间
        # 显示所有的主图技术指标,六条瀑布线
        self.__textInd.setHtml(u'<div style="text-align: center; background-color:rgb(13,9,27)">\
                                <span style="color: rgb(255,255,255);  font-size: 14px;">  PB1: %.1f   </span>\
                                <span style="color: rgb(255,85,0);  font-size: 14px;">  PB2: %.1f   </span>\
                                <span style="color: rgb(255,0,127);  font-size: 14px;">  PB3: %.1f   </span>\
                                <span style="color: rgb(0,255,0);  font-size: 14px;">  PB4: %.1f   </span>\
                                <span style="color: rgb(255,0,0);  font-size: 14px;">  PB5: %.1f   </span>\
                                <span style="color: rgb(0,0,255);  font-size: 14px;">  PB6: %.1f   </span>'
                               '</div>' % (pb1, pb2, pb3, pb4, pb5, pb6))

        # 显示macd技术指标
        self.__textMACD.setHtml(u'<div style="text-align: center; background-color:#000">\
                                <span style="color: white;  font-size: 14px;">  diff: %.1f   </span>\
                                <span style="color: yellow;  font-size: 14px;">  dea: %.1f   </span>\
                                <span style="color: pink;  font-size: 14px;">  bar: %.1f   </span>'
                                '</div>' % (diff, dea, bar))


        # 显示成交量及均量
        self.__textVolume.setHtml(u'<div style="text-align: center; background-color:#000">\
                                <span style="color: white;  font-size: 14px;">  Vol: %.1f   </span>\
                                <span style="color: yellow;  font-size: 14px;">  ma5: %.1f   </span>\
                                <span style="color: pink;  font-size: 14px;">  ma20: %.1f   </span>'
                                  '</div>' % (volume, mv1, mv2))

        # 坐标轴宽度
        rightAxisWidth = self.views[0].getAxis('right').width()
        bottomAxisHeight = self.views[2].getAxis('bottom').height()
        offset = QtCore.QPointF(rightAxisWidth, bottomAxisHeight)

        # 各个顶点
        tl = [self.views[i].vb.mapSceneToView(self.rects[i].topLeft()) for i in range(3)]
        # 调试中获得的值为:
        # [PySide6.QtCore.QPointF(3493.702783, 727.623408),
        # PySide6.QtCore.QPointF(3493.702783, 110144.265625),
        # PySide6.QtCore.QPointF(3493.702783, 7.519954)]

        br = [self.views[i].vb.mapSceneToView(self.rects[i].bottomRight() - offset) for i in range(3)]
        # 调试中获得的值为:
        # [PySide6.QtCore.QPointF(3602.111762, 667.376592),
        # PySide6.QtCore.QPointF(3602.111762, 2612.734375),
        # PySide6.QtCore.QPointF(3602.111762, -3.606918)]

        # 显示X轴价格
        for i in range(3):
            if self.showHLine[i]:
                self.textPrices[i].setHtml('<div style="text-align: right">\
                             <span style="color: yellow; font-size: 16px;">%0.1f</span>\
                                </div>' % (yAxis if i == 0 else self.yAxises[i]))
                self.textPrices[i].setPos(br[i].x(), yAxis if i == 0 else self.yAxises[i])
                self.textPrices[i].show()
            else:
                self.textPrices[i].hide()

        # 显示Y轴时间
        self.__textDate.setHtml('<div style="text-align: center">\
                                <span style="color: yellow; font-size: 16px;">%s</span>\
                                </div>' % (datetimeText))




        # 设置坐标
        # def set_pos(self):
        self.__textInfo.setPos(tl[0].x(),tl[0].y())
        self.__textInd.setPos(br[0].x(), tl[0].y())
        self.__textVolume.setPos(br[0].x(), tl[1].y())
        self.__textMACD.setPos(br[0].x(), tl[2].y())
        # view= self.views[0]
        # top_left = view.mapRectToView(view.sceneBoundingRect().topLeft())
        # self.__textInfo.setPos(top_left)

        # 修改对称方式防止遮挡
        if xAxis > self.master.index:
            self.__textDate.anchor = Point((1, 1))
        else:
            self.__textDate.anchor = Point((0, 1))

        self.__textDate.setPos(xAxis, br[2].y())
