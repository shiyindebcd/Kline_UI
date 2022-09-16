# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainFrame.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QComboBox, QFrame, QHBoxLayout, QLabel, QLineEdit, QListView, QPushButton, QSizePolicy, QSlider, QSpacerItem, QVBoxLayout)


class Ui_Form(object):

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1299, 812)
        Form.setStyleSheet(u"\n"
                           "	background-color: rgb(0, 0, 0);\n"
                           "	border-radius: 10px;\n"
                           "	border: none;\n"
                           "\n"
                           "\n"
                           "")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 770))
        self.frame_2.setStyleSheet(u"QFrame {\n"
                                   "	\n"
                                   "	background-color: rgb(0, 0, 0);\n"
                                   "	border-radius: 10px;\n"
                                   "	border: none;\n"
                                   "}\n"
                                   "\n"
                                   "")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setSpacing(3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QFrame {\n"
                                   "	\n"
                                   "	background-color: rgb(0, 0, 0);\n"
                                   "	border-radius: 10px;\n"
                                   "	border: none;\n"
                                   "}\n"
                                   "\n"
                                   "")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 3, 0, 0)
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"	background-color: rgb(13, 9, 27);\n"
                                   "	border-radius: none;\n"
                                   "	border: none;\n"
                                   "")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_6)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setStyleSheet(u"QFrame {		\n"
                                    "	background-color: rgb(0, 0, 0);\n"
                                    "	border-radius: 10px;\n"
                                    "	border: none;\n"
                                    "}\n"
                                    "\n"
                                    "")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_21)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(3, 3, 0, 3)
        self.frame_9 = QFrame(self.frame_21)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 50))
        self.frame_9.setMaximumSize(QSize(16777215, 50))
        self.frame_9.setStyleSheet(u"QFrame {	\n"
                                   "	background-color: rgb(13, 9, 27);\n"
                                   "	border-radius: 10px;\n"
                                   "	border: 1px solid rgb(65, 51, 156);\n"
                                   "}\n"
                                   "\n"
                                   "")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(3, 0, 5, 0)
        self.Btn_draw_line_order = QPushButton(self.frame_9)
        self.Btn_draw_line_order.setObjectName(u"Btn_draw_line_order")
        self.Btn_draw_line_order.setMinimumSize(QSize(100, 40))
        self.Btn_draw_line_order.setMaximumSize(QSize(100, 40))
        self.Btn_draw_line_order.setStyleSheet(u"QPushButton {\n"
                                               "	color: rgb(255, 0, 127);	\n"
                                               "	font: 700 16pt \"\u7b49\u7ebf\";\n"
                                               "	border: 2px solid rgb(65, 51, 156);\n"
                                               "	border-radius: 15px;\n"
                                               "	background-color: rgb(20, 9, 70);\n"
                                               "	text-align: center;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover {\n"
                                               "	border: 2px solid rgb(255, 85, 0);\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:pressed {\n"
                                               "	\n"
                                               "	color: rgb(255, 0, 0);\n"
                                               "}")

        self.horizontalLayout_9.addWidget(self.Btn_draw_line_order)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)

        self.label_kline_info = QLabel(self.frame_9)
        self.label_kline_info.setObjectName(u"label_kline_info")
        self.label_kline_info.setStyleSheet(u"QFrame {\n"
                                            "	background-color: rgba(30, 30, 40, 0);\n"
                                            "	border: none;\n"
                                            "	border-radius: 15px;\n"
                                            "	color: rgb(0, 255, 0);\n"
                                            "	font: 700 14pt \"\u7b49\u7ebf\";\n"
                                            "}\n"
                                            "")

        self.horizontalLayout_9.addWidget(self.label_kline_info)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.label_28 = QLabel(self.frame_9)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(0, 40))
        self.label_28.setMaximumSize(QSize(150, 16777215))
        font = QFont()
        font.setFamilies([u"\u7b49\u7ebf"])
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet(u"QFrame {\n"
                                    "	background-color: rgba(30, 30, 40, 0);\n"
                                    "	border: none;\n"
                                    "	border-radius: 15px;\n"
                                    "	color: rgb(255, 0, 255);\n"
                                    "	font: 700 16pt \"\u7b49\u7ebf\";\n"
                                    "}\n"
                                    "")
        self.label_28.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_28)

        self.comboBox_backtest_exchange = QComboBox(self.frame_9)
        self.comboBox_backtest_exchange.addItem("")
        self.comboBox_backtest_exchange.addItem("")
        self.comboBox_backtest_exchange.addItem("")
        self.comboBox_backtest_exchange.addItem("")
        self.comboBox_backtest_exchange.addItem("")
        self.comboBox_backtest_exchange.setObjectName(u"comboBox_backtest_exchange")
        self.comboBox_backtest_exchange.setMinimumSize(QSize(150, 35))
        self.comboBox_backtest_exchange.setMaximumSize(QSize(150, 35))
        self.comboBox_backtest_exchange.setStyleSheet(u"/* \u672a\u4e0b\u62c9\u65f6\uff0cQComboBox\u7684\u6837\u5f0f */\n"
                                                      "QComboBox {\n"
                                                      "    border: 2px solid gray;   /* \u8fb9\u6846 */\n"
                                                      "    border-radius: 15px;   /* \u5706\u89d2 */\n"
                                                      "    padding: 1px 18px 1px 3px;   /* \u5b57\u4f53\u586b\u886c */\n"
                                                      "    color: rgb(0, 0, 0);    \n"
                                                      "	font: 700 12pt \"\u7b49\u7ebf\";    \n"
                                                      "	background-color: rgb(255, 255, 255);\n"
                                                      "}\n"
                                                      "\n"
                                                      "/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u6837\u5f0f */\n"
                                                      "QComboBox QAbstractItemView {\n"
                                                      "    \n"
                                                      "    border: 1px solid yellow;   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u8fb9\u6846 */\n"
                                                      "    color: black;\n"
                                                      "	border-radius: 3px;\n"
                                                      "    background-color: rgb(225, 225, 225);   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u80cc\u666f\u8272 */\n"
                                                      "    selection-background-color: lightgreen;   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u88ab\u9009\u4e2d\u9879\u7684\u80cc\u666f\u8272 */\n"
                                                      "}\n"
                                                      "/* \u4e0b\u62c9\u7bad\u5934\u6837\u5f0f */\n"
                                                      " QComboBox::down-arrow {\n"
                                                      "	width: 25px; /* \u4e0b\u62c9\u7bad"
                                                      "\u5934\u7684\u5bbd\u5ea6\uff08\u5efa\u8bae\u4e0e\u4e0b\u62c9\u6846drop-down\u7684\u5bbd\u5ea6\u4e00\u81f4\uff09 */ \n"
                                                      "	background: rgb(255, 255, 255); /* \u4e0b\u62c9\u7bad\u5934\u7684\u7684\u80cc\u666f\u8272 */ \n"
                                                      "	padding: 0px 0px 0px 0px; /* \u4e0a\u5185\u8fb9\u8ddd\u3001\u53f3\u5185\u8fb9\u8ddd\u3001\u4e0b\u5185\u8fb9\u8ddd\u3001\u5de6\u5185\u8fb9\u8ddd */\n"
                                                      " } \n"
                                                      "\n"
                                                      "/* \u4e0b\u62c9\u6846\u6837\u5f0f */\n"
                                                      "QComboBox::drop-down {\n"
                                                      "   /* subcontrol-origin: padding;   /* \u5b50\u63a7\u4ef6\u5728\u7236\u5143\u7d20\u4e2d\u7684\u539f\u70b9\u77e9\u5f62\u3002\u5982\u679c\u672a\u6307\u5b9a\u6b64\u5c5e\u6027\uff0c\u5219\u9ed8\u8ba4\u4e3apadding\u3002 */\n"
                                                      "   /* subcontrol-position: top right;   /* \u4e0b\u62c9\u6846\u7684\u4f4d\u7f6e\uff08\u53f3\u4e0a\uff09 */\n"
                                                      "    width: 25px;   /* \u4e0b\u62c9\u6846\u7684\u5bbd\u5ea6 */\n"
                                                      "\n"
                                                      "    border-left-width: 3px;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u5bbd\u5ea6 */\n"
                                                      "    border-left-color: darkgray;   /* \u4e0b\u62c9\u6846\u7684\u5de6"
                                                      "\u8fb9\u754c\u7ebf\u989c\u8272 */\n"
                                                      "    border-left-style: solid;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u4e3a\u5b9e\u7ebf */\n"
                                                      "    border-top-right-radius: 10px;   /* \u4e0b\u62c9\u6846\u7684\u53f3\u4e0a\u8fb9\u754c\u7ebf\u7684\u5706\u89d2\u534a\u5f84\uff08\u5e94\u548c\u6574\u4e2aQComboBox\u53f3\u4e0a\u8fb9\u754c\u7ebf\u7684\u5706\u89d2\u534a\u5f84\u4e00\u81f4\uff09 */\n"
                                                      "    border-bottom-right-radius: 10px;   /* \u540c\u4e0a */\n"
                                                      "}\n"
                                                      "QComboBox:hover {\n"
                                                      "	border: 3px solid rgb(255, 85, 0);\n"
                                                      "}\n"
                                                      "QComboBox:disabled{\n"
                                                      "	color: rgb(0, 0, 0);\n"
                                                      "	border-color: rgb(166, 166, 166);\n"
                                                      "    background-color: rgb(186, 186, 186);\n"
                                                      "}")
        self.comboBox_backtest_exchange.setFrame(True)
        self.comboBox_backtest_exchange.setModelColumn(0)

        self.horizontalLayout_9.addWidget(self.comboBox_backtest_exchange)

        self.optional_contracts = QLineEdit(self.frame_9)
        self.optional_contracts.setObjectName(u"optional_contracts")
        self.optional_contracts.setMinimumSize(QSize(100, 37))
        self.optional_contracts.setMaximumSize(QSize(100, 37))
        self.optional_contracts.setStyleSheet(u"QLineEdit {\n"
                                              "	border: 2px solid rgb(45, 45, 45);\n"
                                              "	border-radius: 15px;\n"
                                              "	padding: 5px;\n"
                                              "	background-color: rgb(255, 255, 255);	\n"
                                              "	color: rgb(0, 0, 0);\n"
                                              "	font: 700 18pt \"\u7b49\u7ebf\";\n"
                                              "}\n"
                                              "QLineEdit:hover {\n"
                                              "	border: 3px solid rgb(255, 85, 0);\n"
                                              "}\n"
                                              "QLineEdit:focus {\n"
                                              "	border: 3px solid rgb(255, 85, 0);\n"
                                              "	color: rgb(255, 0, 0);\n"
                                              "}\n"
                                              "QLineEdit:disabled{\n"
                                              "	color: rgb(0, 0, 0);\n"
                                              "	border-color: rgb(166, 166, 166);\n"
                                              "    background-color: rgb(186, 186, 186);\n"
                                              "}")

        self.horizontalLayout_9.addWidget(self.optional_contracts)

        self.Btn_add_K_charts_i = QPushButton(self.frame_9)
        self.Btn_add_K_charts_i.setObjectName(u"Btn_add_K_charts_i")
        self.Btn_add_K_charts_i.setMinimumSize(QSize(80, 35))
        self.Btn_add_K_charts_i.setMaximumSize(QSize(80, 35))
        self.Btn_add_K_charts_i.setStyleSheet(u"QPushButton{\n"
                                              "	color: rgb(13, 9, 36);\n"
                                              "	background-color:rgb(255, 0, 127);\n"
                                              "	font: 700 16pt \"\u7b49\u7ebf\";\n"
                                              "	border-radius: 15px;\n"
                                              "}\n"
                                              "QPushButton:hover{\n"
                                              "	border: 2px solid rgb(255, 85, 0); \n"
                                              "}\n"
                                              "QPushButton:pressed{\n"
                                              "	color: green;\n"
                                              "	border-color: rgb(255, 0, 0);\n"
                                              "    background-color: rgb(255, 255, 0);\n"
                                              "}\n"
                                              "")

        self.horizontalLayout_9.addWidget(self.Btn_add_K_charts_i)

        self.Btn_add_K_charts_rb = QPushButton(self.frame_9)
        self.Btn_add_K_charts_rb.setObjectName(u"Btn_add_K_charts_rb")
        self.Btn_add_K_charts_rb.setMinimumSize(QSize(80, 35))
        self.Btn_add_K_charts_rb.setMaximumSize(QSize(80, 35))
        self.Btn_add_K_charts_rb.setStyleSheet(u"QPushButton{\n"
                                               "	color: rgb(13, 9, 36);\n"
                                               "	background-color:rgb(255, 0, 127);\n"
                                               "	font: 700 16pt \"\u7b49\u7ebf\";\n"
                                               "	border-radius: 15px;\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               "	border: 2px solid rgb(255, 85, 0); \n"
                                               "}\n"
                                               "QPushButton:pressed{\n"
                                               "	color: green;\n"
                                               "	border-color: rgb(255, 0, 0);\n"
                                               "    background-color: rgb(255, 255, 0);\n"
                                               "}\n"
                                               "")

        self.horizontalLayout_9.addWidget(self.Btn_add_K_charts_rb)

        self.verticalLayout_12.addWidget(self.frame_9)

        self.frame = QFrame(self.frame_21)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {		\n"
                                 "	background-color: rgb(0, 0, 0);\n"
                                 "	border-radius: 10px;\n"
                                 "	border: none;\n"
                                 "}\n"
                                 "\n"
                                 "")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 3, 0, 0)
        self.verticalLayout_klines = QHBoxLayout()
        self.verticalLayout_klines.setObjectName(u"verticalLayout_klines")

        self.horizontalLayout.addLayout(self.verticalLayout_klines)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(30, 0))
        self.frame_7.setMaximumSize(QSize(30, 16777215))
        self.frame_7.setStyleSheet(u"QFrame {		\n"
                                   "	background-color: rgb(0, 0, 0);\n"
                                   "	border-radius: 10px;\n"
                                   "	border: none;\n"
                                   "}\n"
                                   "\n"
                                   "")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.Btn_klines_1min = QPushButton(self.frame_7)
        self.Btn_klines_1min.setObjectName(u"Btn_klines_1min")
        self.Btn_klines_1min.setMinimumSize(QSize(30, 60))
        self.Btn_klines_1min.setMaximumSize(QSize(30, 60))
        self.Btn_klines_1min.setStyleSheet(u"QPushButton {\n"
                                           "	color: rgb(255, 85, 0);	\n"
                                           "	font: 700 10pt \"\u7b49\u7ebf\";\n"
                                           "	border: 2px solid rgb(65, 51, 156);\n"
                                           "	border-radius: 10px;\n"
                                           "	background-color: rgb(20, 9, 70);\n"
                                           "	text-align: center;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover {\n"
                                           "	border: 2px solid rgb(255, 85, 0);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "	\n"
                                           "	color: rgb(255, 0, 0);\n"
                                           "}")

        self.verticalLayout_3.addWidget(self.Btn_klines_1min)

        self.Btn_klines_15min = QPushButton(self.frame_7)
        self.Btn_klines_15min.setObjectName(u"Btn_klines_15min")
        self.Btn_klines_15min.setMinimumSize(QSize(30, 60))
        self.Btn_klines_15min.setMaximumSize(QSize(30, 60))
        self.Btn_klines_15min.setStyleSheet(u"QPushButton {\n"
                                            "	color: rgb(255, 85, 0);	\n"
                                            "	font: 700 10pt \"\u7b49\u7ebf\";\n"
                                            "	border: 2px solid rgb(65, 51, 156);\n"
                                            "	border-radius: 10px;\n"
                                            "	background-color: rgb(20, 9, 70);\n"
                                            "	text-align: center;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover {\n"
                                            "	border: 2px solid rgb(255, 85, 0);\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed {\n"
                                            "	\n"
                                            "	color: rgb(255, 0, 0);\n"
                                            "}")

        self.verticalLayout_3.addWidget(self.Btn_klines_15min)

        self.Btn_klines_30min = QPushButton(self.frame_7)
        self.Btn_klines_30min.setObjectName(u"Btn_klines_30min")
        self.Btn_klines_30min.setMinimumSize(QSize(30, 60))
        self.Btn_klines_30min.setMaximumSize(QSize(30, 60))
        self.Btn_klines_30min.setStyleSheet(u"QPushButton {\n"
                                            "	color: rgb(255, 85, 0);	\n"
                                            "	font: 700 10pt \"\u7b49\u7ebf\";\n"
                                            "	border: 2px solid rgb(65, 51, 156);\n"
                                            "	border-radius: 10px;\n"
                                            "	background-color: rgb(20, 9, 70);\n"
                                            "	text-align: center;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover {\n"
                                            "	border: 2px solid rgb(255, 85, 0);\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed {\n"
                                            "	\n"
                                            "	color: rgb(255, 0, 0);\n"
                                            "}")

        self.verticalLayout_3.addWidget(self.Btn_klines_30min)

        self.Btn_klines_1hour = QPushButton(self.frame_7)
        self.Btn_klines_1hour.setObjectName(u"Btn_klines_1hour")
        self.Btn_klines_1hour.setMinimumSize(QSize(30, 60))
        self.Btn_klines_1hour.setMaximumSize(QSize(30, 60))
        self.Btn_klines_1hour.setStyleSheet(u"QPushButton {\n"
                                            "	color: rgb(255, 85, 0);	\n"
                                            "	font: 700 10pt \"\u7b49\u7ebf\";\n"
                                            "	border: 2px solid rgb(65, 51, 156);\n"
                                            "	border-radius: 10px;\n"
                                            "	background-color: rgb(20, 9, 70);\n"
                                            "	text-align: center;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover {\n"
                                            "	border: 2px solid rgb(255, 85, 0);\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed {\n"
                                            "	\n"
                                            "	color: rgb(255, 0, 0);\n"
                                            "}")

        self.verticalLayout_3.addWidget(self.Btn_klines_1hour)

        self.Btn_klines_2hour = QPushButton(self.frame_7)
        self.Btn_klines_2hour.setObjectName(u"Btn_klines_2hour")
        self.Btn_klines_2hour.setMinimumSize(QSize(30, 60))
        self.Btn_klines_2hour.setMaximumSize(QSize(30, 60))
        self.Btn_klines_2hour.setStyleSheet(u"QPushButton {\n"
                                            "	color: rgb(255, 85, 0);	\n"
                                            "	font: 700 10pt \"\u7b49\u7ebf\";\n"
                                            "	border: 2px solid rgb(65, 51, 156);\n"
                                            "	border-radius: 10px;\n"
                                            "	background-color: rgb(20, 9, 70);\n"
                                            "	text-align: center;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover {\n"
                                            "	border: 2px solid rgb(255, 85, 0);\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed {\n"
                                            "	\n"
                                            "	color: rgb(255, 0, 0);\n"
                                            "}")

        self.verticalLayout_3.addWidget(self.Btn_klines_2hour)

        self.Btn_klines_4hour = QPushButton(self.frame_7)
        self.Btn_klines_4hour.setObjectName(u"Btn_klines_4hour")
        self.Btn_klines_4hour.setMinimumSize(QSize(30, 60))
        self.Btn_klines_4hour.setMaximumSize(QSize(30, 60))
        self.Btn_klines_4hour.setStyleSheet(u"QPushButton {\n"
                                            "	color: rgb(255, 85, 0);	\n"
                                            "	font: 700 10pt \"\u7b49\u7ebf\";\n"
                                            "	border: 2px solid rgb(65, 51, 156);\n"
                                            "	border-radius: 10px;\n"
                                            "	background-color: rgb(20, 9, 70);\n"
                                            "	text-align: center;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover {\n"
                                            "	border: 2px solid rgb(255, 85, 0);\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed {\n"
                                            "	\n"
                                            "	color: rgb(255, 0, 0);\n"
                                            "}")

        self.verticalLayout_3.addWidget(self.Btn_klines_4hour)

        self.Btn_klines_daily = QPushButton(self.frame_7)
        self.Btn_klines_daily.setObjectName(u"Btn_klines_daily")
        self.Btn_klines_daily.setMinimumSize(QSize(30, 60))
        self.Btn_klines_daily.setMaximumSize(QSize(30, 60))
        self.Btn_klines_daily.setStyleSheet(u"QPushButton {\n"
                                            "	color: rgb(255, 85, 0);	\n"
                                            "	font: 700 10pt \"\u7b49\u7ebf\";\n"
                                            "	border: 2px solid rgb(65, 51, 156);\n"
                                            "	border-radius: 10px;\n"
                                            "	background-color: rgb(20, 9, 70);\n"
                                            "	text-align: center;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover {\n"
                                            "	border: 2px solid rgb(255, 85, 0);\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed {\n"
                                            "	\n"
                                            "	color: rgb(255, 0, 0);\n"
                                            "}")

        self.verticalLayout_3.addWidget(self.Btn_klines_daily)

        self.frame_22 = QFrame(self.frame_7)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(30, 0))
        self.frame_22.setMaximumSize(QSize(30, 16777215))
        self.frame_22.setStyleSheet(u"QFrame {	\n"
                                    "	border: 2px solid rgb(65, 51, 156);\n"
                                    "	border-radius: 10px;\n"
                                    "	background-color: rgb(20, 9, 70);\n"
                                    "}\n"
                                    "QFrame:hover {\n"
                                    "	border: 2px solid rgb(255, 85, 0);\n"
                                    "}\n"
                                    "\n"
                                    "")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_22)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_22)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(25, 60))
        self.label.setMaximumSize(QSize(25, 60))
        self.label.setStyleSheet(u"	color: rgb(255, 85, 0);	\n"
                                 "	font: 700 10pt \"\u7b49\u7ebf\";\n"
                                 "	border: none;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label)

        self.verticalSlider = QSlider(self.frame_22)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setMinimumSize(QSize(25, 150))
        self.verticalSlider.setMaximumSize(QSize(25, 200))
        self.verticalSlider.setStyleSheet(u" /*\u6ed1\u52a8\u6761\u69fd\uff08\u6574\u4f53\uff09\u7684\u7f8e\u5316 */\n"
                                          " QSlider::groove:vertical{\n"
                                          "         height: 12px;\n"
                                          "         left: 0px;\n"
                                          "         right: 0px;\n"
                                          "         border:0px;    /*\u6307\u5b9a\u65e0\u8fb9\u6846*/        \n"
                                          "		border-radius:6px;    /*\u6307\u5b9a\u5706\u89d2*/        \n"
                                          "		background:rgba(0,0,0,50); 9  }\n"
                                          "/*\u6ed1\u5757\u7684\u7f8e\u5316*/  \n"
                                          "QSlider::handle:vertical{\n"
                                          "         width:  50px;\n"
                                          "         height: 50px;\n"
                                          "         margin-top: -20px;\n"
                                          "         margin-left: 0px;\n"
                                          "         margin-bottom: -20px;\n"
                                          "         margin-right: 0px;\n"
                                          "         border-image:url(:/res/images/setting_slider_handle.png);\n"
                                          " }\n"
                                          "/*\u5df2\u6ed1\u8fc7\u7684\u8fdb\u5ea6\u7f8e\u5316*/\n"
                                          "QSlider::sub-page:vertical{\n"
                                          "       background:rgba(80,166,234,1);\n"
                                          " }\n"
                                          "QSlider::handle:vertical:hover { \n"
                                          "        width:  50px;\n"
                                          "        height: 50px;\n"
                                          "         margin-top: -20px;\n"
                                          "         margin-left: 0px;\n"
                                          "        margin-bottom: -20px;\n"
                                          "         "
                                          "margin-right: 0px;\n"
                                          "         border-image:url(:/res/images/setting_slider_handle_hover.png); \n"
                                          "}\n"
                                          "QSlider::sub-page:vertical:disabled {\n"
                                          "         background: #BB345F; }\n"
                                          "QSlider::add-page:vertical:disabled {\n"
                                          "        background: #1ADEFF; }\n"
                                          "QSlider::handle:vertical:disabled {\n"
                                          "         background: #EEDDFF; }")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.verticalLayout_14.addWidget(self.verticalSlider)

        self.label_4 = QLabel(self.frame_22)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 30))
        self.label_4.setStyleSheet(u"	color: rgb(255, 85, 0);	\n"
                                   "	font: 700 10pt \"\u7b49\u7ebf\";\n"
                                   "	border: none;")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_4)

        self.label_2 = QLabel(self.frame_22)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 40))
        self.label_2.setStyleSheet(u"	color: rgb(255, 85, 0);	\n"
                                   "	font: 700 10pt \"\u7b49\u7ebf\";\n"
                                   "	border: none;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_2)

        self.verticalLayout_3.addWidget(self.frame_22)

        self.horizontalLayout.addWidget(self.frame_7)

        self.verticalLayout_12.addWidget(self.frame)

        self.verticalLayout_7.addWidget(self.frame_21)

        self.verticalLayout_2.addWidget(self.frame_6)

        self.horizontalLayout_7.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(250, 0))
        self.frame_5.setMaximumSize(QSize(250, 16777215))
        self.frame_5.setStyleSheet(u"QFrame {	\n"
                                   "	background-color: rgb(13, 9, 27);\n"
                                   "	border-radius: 10px;\n"
                                   "	border: none;\n"
                                   "}\n"
                                   "\n"
                                   "")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 5, 5, 3)
        self.frame_3 = QFrame(self.frame_5)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 70))
        self.frame_3.setMaximumSize(QSize(16777215, 70))
        self.frame_3.setStyleSheet(u"QFrame {	\n"
                                   "	background-color: rgb(13, 9, 27);\n"
                                   "	border-radius: 10px;\n"
                                   "	border: 1px solid rgb(65, 51, 156);\n"
                                   "}\n"
                                   "\n"
                                   "")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_instrument_name = QLabel(self.frame_3)
        self.label_instrument_name.setObjectName(u"label_instrument_name")
        self.label_instrument_name.setMinimumSize(QSize(120, 30))
        self.label_instrument_name.setMaximumSize(QSize(16777215, 30))
        self.label_instrument_name.setLayoutDirection(Qt.LeftToRight)
        self.label_instrument_name.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                                 "color: rgb(255, 255, 0);\n"
                                                 "font: 700 18pt \"\u7b49\u7ebf\";\n"
                                                 "border-radius: 15px;\n"
                                                 "border: none;")
        self.label_instrument_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_instrument_name)

        self.label_instrument_id = QLabel(self.frame_3)
        self.label_instrument_id.setObjectName(u"label_instrument_id")
        self.label_instrument_id.setMinimumSize(QSize(0, 30))
        self.label_instrument_id.setMaximumSize(QSize(16777215, 30))
        self.label_instrument_id.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                               "color: rgb(255, 0, 255);\n"
                                               "font: 700 18pt \"\u7b49\u7ebf\";\n"
                                               "border-radius: 15px;\n"
                                               "border: none;")
        self.label_instrument_id.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_instrument_id)

        self.verticalLayout_4.addWidget(self.frame_3)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 60))
        self.frame_8.setMaximumSize(QSize(16777215, 60))
        self.frame_8.setStyleSheet(u"QFrame {	\n"
                                   "	background-color: rgb(13, 9, 27);\n"
                                   "	border-radius: 10px;\n"
                                   "	border: 1px solid rgb(65, 51, 156);\n"
                                   "}\n"
                                   "\n"
                                   "")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.frame_8)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"QFrame {	\n"
                                    "	background-color: rgb(13, 9, 27);\n"
                                    "	border-radius: 10px;\n"
                                    "	border: none;\n"
                                    "}\n"
                                    "\n"
                                    "")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 3, 0, 0)
        self.label_3 = QLabel(self.frame_15)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                   "color: rgb(230, 230, 230);\n"
                                   "font: 12pt \"\u7b49\u7ebf\";\n"
                                   "border-radius: 5px;\n"
                                   "border: none;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_ask_price1 = QLabel(self.frame_15)
        self.label_ask_price1.setObjectName(u"label_ask_price1")
        self.label_ask_price1.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                            "color: rgb(255, 0, 0);\n"
                                            "font: 700 16pt \"\u7b49\u7ebf\";\n"
                                            "border-radius: 5px;\n"
                                            "border: none;")
        self.label_ask_price1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_ask_price1)

        self.label_ask_volume1 = QLabel(self.frame_15)
        self.label_ask_volume1.setObjectName(u"label_ask_volume1")
        self.label_ask_volume1.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                             "color: rgb(255, 255, 0);\n"
                                             "font: 700 16pt \"\u7b49\u7ebf\";\n"
                                             "border-radius: 5px;\n"
                                             "border: none;")
        self.label_ask_volume1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_ask_volume1)

        self.verticalLayout_6.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_8)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"QFrame {	\n"
                                    "	background-color: rgb(13, 9, 27);\n"
                                    "	border-radius: 10px;\n"
                                    "	border: none;\n"
                                    "}\n"
                                    "\n"
                                    "")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 3)
        self.label_6 = QLabel(self.frame_16)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                   "color: rgb(230, 230, 230);\n"
                                   "font: 12pt \"\u7b49\u7ebf\";\n"
                                   "border-radius: 5px;\n"
                                   "border: none;")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.label_bid_price1 = QLabel(self.frame_16)
        self.label_bid_price1.setObjectName(u"label_bid_price1")
        self.label_bid_price1.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                            "color: rgb(255, 0, 0);\n"
                                            "font: 700 16pt \"\u7b49\u7ebf\";\n"
                                            "border-radius: 5px;\n"
                                            "border: none;")
        self.label_bid_price1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_bid_price1)

        self.label_bid_volume1 = QLabel(self.frame_16)
        self.label_bid_volume1.setObjectName(u"label_bid_volume1")
        self.label_bid_volume1.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                             "color: rgb(255, 255, 0);\n"
                                             "font: 700 16pt \"\u7b49\u7ebf\";\n"
                                             "border-radius: 5px;\n"
                                             "border: none;")
        self.label_bid_volume1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_bid_volume1)

        self.verticalLayout_6.addWidget(self.frame_16)

        self.verticalLayout_4.addWidget(self.frame_8)

        self.frame_10 = QFrame(self.frame_5)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 200))
        self.frame_10.setStyleSheet(u"QFrame {	\n"
                                    "	background-color: rgb(13, 9, 27);\n"
                                    "	border-radius: 10px;\n"
                                    "	border: 1px solid rgb(65, 51, 156);\n"
                                    "}\n"
                                    "\n"
                                    "")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_10)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"QFrame {	\n"
                                    "	background-color: rgb(13, 9, 27);\n"
                                    "	border-radius: 10px;\n"
                                    "	border: none;\n"
                                    "}\n"
                                    "\n"
                                    "")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_13)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_17)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.label_12 = QLabel(self.frame_17)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                    "color: rgb(230, 230, 230);\n"
                                    "font: 10pt \"\u7b49\u7ebf\";\n"
                                    "border-radius: 5px;\n"
                                    "border: none;")

        self.verticalLayout_8.addWidget(self.label_12)

        self.label_9 = QLabel(self.frame_17)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                   "color: rgb(230, 230, 230);\n"
                                   "font: 10pt \"\u7b49\u7ebf\";\n"
                                   "border-radius: 5px;\n"
                                   "border: none;")

        self.verticalLayout_8.addWidget(self.label_9)

        self.label_11 = QLabel(self.frame_17)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                    "color: rgb(230, 230, 230);\n"
                                    "font: 10pt \"\u7b49\u7ebf\";\n"
                                    "border-radius: 5px;\n"
                                    "border: none;")

        self.verticalLayout_8.addWidget(self.label_11)

        self.label_13 = QLabel(self.frame_17)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                    "color: rgb(230, 230, 230);\n"
                                    "font: 10pt \"\u7b49\u7ebf\";\n"
                                    "border-radius: 5px;\n"
                                    "border: none;")

        self.verticalLayout_8.addWidget(self.label_13)

        self.label_14 = QLabel(self.frame_17)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                    "color: rgb(230, 230, 230);\n"
                                    "font: 10pt \"\u7b49\u7ebf\";\n"
                                    "border-radius: 5px;\n"
                                    "border: none;")

        self.verticalLayout_8.addWidget(self.label_14)

        self.label_16 = QLabel(self.frame_17)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                    "color: rgb(230, 230, 230);\n"
                                    "font: 10pt \"\u7b49\u7ebf\";\n"
                                    "border-radius: 5px;\n"
                                    "border: none;")

        self.verticalLayout_8.addWidget(self.label_16)

        self.label_18 = QLabel(self.frame_17)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                    "color: rgb(230, 230, 230);\n"
                                    "font: 10pt \"\u7b49\u7ebf\";\n"
                                    "border-radius: 5px;\n"
                                    "border: none;")

        self.verticalLayout_8.addWidget(self.label_18)

        self.horizontalLayout_5.addWidget(self.frame_17, 0, Qt.AlignLeft)

        self.frame_18 = QFrame(self.frame_13)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_18)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.label_percent_increase = QLabel(self.frame_18)
        self.label_percent_increase.setObjectName(u"label_percent_increase")
        self.label_percent_increase.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                                  "color: rgb(255, 0, 0);\n"
                                                  "font: 700 12pt \"\u7b49\u7ebf\";\n"
                                                  "border-radius: 5px;\n"
                                                  "border: none;")
        self.label_percent_increase.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_10.addWidget(self.label_percent_increase)

        self.label_last_price = QLabel(self.frame_18)
        self.label_last_price.setObjectName(u"label_last_price")
        self.label_last_price.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                            "color: rgb(255, 255, 0);\n"
                                            "font: 700 12pt \"\u7b49\u7ebf\";\n"
                                            "border-radius: 5px;\n"
                                            "border: none;")
        self.label_last_price.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_10.addWidget(self.label_last_price)

        self.label_volume = QLabel(self.frame_18)
        self.label_volume.setObjectName(u"label_volume")
        self.label_volume.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                        "color: rgb(255, 255, 0);\n"
                                        "font: 700 12pt \"\u7b49\u7ebf\";\n"
                                        "border-radius: 5px;\n"
                                        "border: none;")
        self.label_volume.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_10.addWidget(self.label_volume)

        self.label_open_interest = QLabel(self.frame_18)
        self.label_open_interest.setObjectName(u"label_open_interest")
        self.label_open_interest.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                               "color: rgb(255, 255, 0);\n"
                                               "font: 700 12pt \"\u7b49\u7ebf\";\n"
                                               "border-radius: 5px;\n"
                                               "border: none;")
        self.label_open_interest.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_10.addWidget(self.label_open_interest)

        self.label_daily_increase = QLabel(self.frame_18)
        self.label_daily_increase.setObjectName(u"label_daily_increase")
        self.label_daily_increase.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                                "color: rgb(255, 255, 0);\n"
                                                "font: 700 12pt \"\u7b49\u7ebf\";\n"
                                                "border-radius: 5px;\n"
                                                "border: none;")
        self.label_daily_increase.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_10.addWidget(self.label_daily_increase)

        self.label_settlement = QLabel(self.frame_18)
        self.label_settlement.setObjectName(u"label_settlement")
        self.label_settlement.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                            "color: rgb(255, 255, 0);\n"
                                            "font: 700 12pt \"\u7b49\u7ebf\";\n"
                                            "border-radius: 5px;\n"
                                            "border: none;")
        self.label_settlement.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_10.addWidget(self.label_settlement)

        self.label_expire_rest_days = QLabel(self.frame_18)
        self.label_expire_rest_days.setObjectName(u"label_expire_rest_days")
        self.label_expire_rest_days.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                                  "color: rgb(255, 255, 0);\n"
                                                  "font: 700 12pt \"\u7b49\u7ebf\";\n"
                                                  "border-radius: 5px;\n"
                                                  "border: none;")
        self.label_expire_rest_days.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_10.addWidget(self.label_expire_rest_days)

        self.horizontalLayout_5.addWidget(self.frame_18)

        self.horizontalLayout_2.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_10)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"QFrame {	\n"
                                    "	background-color: rgb(13, 9, 27);\n"
                                    "	border-radius: 10px;\n"
                                    "	border: none;\n"
                                    "}\n"
                                    "\n"
                                    "")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.frame_14)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_19)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.label_20 = QLabel(self.frame_19)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                    "color: rgb(230, 230, 230);\n"
                                    "font: 10pt \"\u7b49\u7ebf\";\n"
                                    "border-radius: 5px;\n"
                                    "border: none;")

        self.verticalLayout_9.addWidget(self.label_20)

        self.label_19 = QLabel(self.frame_19)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                    "color: rgb(230, 230, 230);\n"
                                    "font: 10pt \"\u7b49\u7ebf\";\n"
                                    "border-radius: 5px;\n"
                                    "border: none;")

        self.verticalLayout_9.addWidget(self.label_19)

        self.label_22 = QLabel(self.frame_19)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                    "color: rgb(230, 230, 230);\n"
                                    "font: 10pt \"\u7b49\u7ebf\";\n"
                                    "border-radius: 5px;\n"
                                    "border: none;")

        self.verticalLayout_9.addWidget(self.label_22)

        self.label_27 = QLabel(self.frame_19)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                    "color: rgb(230, 230, 230);\n"
                                    "font: 10pt \"\u7b49\u7ebf\";\n"
                                    "border-radius: 5px;\n"
                                    "border: none;")

        self.verticalLayout_9.addWidget(self.label_27)

        self.label_24 = QLabel(self.frame_19)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                    "color: rgb(230, 230, 230);\n"
                                    "font: 10pt \"\u7b49\u7ebf\";\n"
                                    "border-radius: 5px;\n"
                                    "border: none;")

        self.verticalLayout_9.addWidget(self.label_24)

        self.label_25 = QLabel(self.frame_19)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                    "color: rgb(230, 230, 230);\n"
                                    "font: 10pt \"\u7b49\u7ebf\";\n"
                                    "border-radius: 5px;\n"
                                    "border: none;")

        self.verticalLayout_9.addWidget(self.label_25)

        self.label_21 = QLabel(self.frame_19)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                    "color: rgb(230, 230, 230);\n"
                                    "font: 10pt \"\u7b49\u7ebf\";\n"
                                    "border-radius: 5px;\n"
                                    "border: none;")

        self.verticalLayout_9.addWidget(self.label_21)

        self.horizontalLayout_6.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_14)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_20)
        self.verticalLayout_11.setSpacing(3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.label_open = QLabel(self.frame_20)
        self.label_open.setObjectName(u"label_open")
        self.label_open.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                      "color: rgb(255, 0, 0);\n"
                                      "font: 700 12pt \"\u7b49\u7ebf\";\n"
                                      "border-radius: 5px;\n"
                                      "border: none;")
        self.label_open.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_11.addWidget(self.label_open)

        self.label_highest = QLabel(self.frame_20)
        self.label_highest.setObjectName(u"label_highest")
        self.label_highest.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                         "color: rgb(255, 0, 0);\n"
                                         "font: 700 12pt \"\u7b49\u7ebf\";\n"
                                         "border-radius: 5px;\n"
                                         "border: none;")
        self.label_highest.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_11.addWidget(self.label_highest)

        self.label_lowest = QLabel(self.frame_20)
        self.label_lowest.setObjectName(u"label_lowest")
        self.label_lowest.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                        "color: rgb(255, 0, 0);\n"
                                        "font: 700 12pt \"\u7b49\u7ebf\";\n"
                                        "border-radius: 5px;\n"
                                        "border: none;")
        self.label_lowest.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_11.addWidget(self.label_lowest)

        self.label_pre_close = QLabel(self.frame_20)
        self.label_pre_close.setObjectName(u"label_pre_close")
        self.label_pre_close.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                           "color: rgb(255, 0, 0);\n"
                                           "font: 700 12pt \"\u7b49\u7ebf\";\n"
                                           "border-radius: 5px;\n"
                                           "border: none;")
        self.label_pre_close.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_11.addWidget(self.label_pre_close)

        self.label_pre_settlement = QLabel(self.frame_20)
        self.label_pre_settlement.setObjectName(u"label_pre_settlement")
        self.label_pre_settlement.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                                "color: rgb(255, 0, 0);\n"
                                                "font: 700 12pt \"\u7b49\u7ebf\";\n"
                                                "border-radius: 5px;\n"
                                                "border: none;")
        self.label_pre_settlement.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_11.addWidget(self.label_pre_settlement)

        self.label_upper_limit = QLabel(self.frame_20)
        self.label_upper_limit.setObjectName(u"label_upper_limit")
        self.label_upper_limit.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                             "color: rgb(255, 0, 0);\n"
                                             "font: 700 12pt \"\u7b49\u7ebf\";\n"
                                             "border-radius: 5px;\n"
                                             "border: none;")
        self.label_upper_limit.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_11.addWidget(self.label_upper_limit)

        self.label_lower_limit = QLabel(self.frame_20)
        self.label_lower_limit.setObjectName(u"label_lower_limit")
        self.label_lower_limit.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
                                             "color: rgb(255, 0, 0);\n"
                                             "font: 700 12pt \"\u7b49\u7ebf\";\n"
                                             "border-radius: 5px;\n"
                                             "border: none;")
        self.label_lower_limit.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_11.addWidget(self.label_lower_limit)

        self.horizontalLayout_6.addWidget(self.frame_20)

        self.horizontalLayout_2.addWidget(self.frame_14)

        self.verticalLayout_4.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_5)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 40))
        self.frame_11.setStyleSheet(u"QFrame {	\n"
                                    "	background-color: rgb(13, 9, 27);\n"
                                    "	border-radius: 10px;\n"
                                    "	border: 1px solid rgb(65, 51, 156);\n"
                                    "}\n"
                                    "\n"
                                    "")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.frame_11)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(0, 40))
        self.label_26.setMaximumSize(QSize(150, 16777215))
        font1 = QFont()
        font1.setFamilies([u"\u7b49\u7ebf"])
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(False)
        self.label_26.setFont(font1)
        self.label_26.setStyleSheet(u"QFrame {\n"
                                    "	background-color: rgba(30, 30, 40, 0);\n"
                                    "	border: none;\n"
                                    "	border-radius: 15px;\n"
                                    "	color: rgb(255, 0, 255);\n"
                                    "	font: 700 14pt \"\u7b49\u7ebf\";\n"
                                    "}\n"
                                    "")
        self.label_26.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_26)

        self.verticalLayout_4.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"QFrame {	\n"
                                    "	background-color: rgb(13, 9, 27);\n"
                                    "	border-radius: 10px;\n"
                                    "	border: none;\n"
                                    "}\n"
                                    "\n"
                                    "")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_12)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.self_selection_listview = QListView(self.frame_12)
        self.self_selection_listview.setObjectName(u"self_selection_listview")
        self.self_selection_listview.setStyleSheet(u"QListView {	\n"
                                                   "	font:  12pt \"\u7b49\u7ebf\";\n"
                                                   "	color: rgb(255, 0, 127);\n"
                                                   "	background-color: rgb(13, 9, 36);\n"
                                                   "	border-radius: 15px;\n"
                                                   "	border: 1px solid rgb(65, 51, 156);\n"
                                                   "	padding:5px;\n"
                                                   "}\n"
                                                   "QListView::item {\n"
                                                   "	min-height:30px;\n"
                                                   "     border-radius: 15px;\n"
                                                   "	padding-left: 5px;\n"
                                                   "	background-color: rgb(13, 9, 36);\n"
                                                   "}\n"
                                                   "\n"
                                                   "QListView::item:selected {   \n"
                                                   "	border: none;\n"
                                                   "	background-color: rgb(170, 0, 255);\n"
                                                   "}\n"
                                                   "\n"
                                                   "QListView::item:hover { \n"
                                                   "	background-color: rgb(0, 70, 0);\n"
                                                   "}\n"
                                                   "QScrollBar:horizontal {\n"
                                                   "    border: none;\n"
                                                   "    background: rgb(52, 59, 72);\n"
                                                   "    height: 8px;\n"
                                                   "    margin: 0px 20px 0 20px;\n"
                                                   "	border-radius: 3px;\n"
                                                   "}\n"
                                                   "QScrollBar::handle:horizontal {\n"
                                                   "    background:rgba(249, 83, 255, 170);\n"
                                                   "    min-width: 30px;\n"
                                                   "	border-radius: 3px\n"
                                                   "}\n"
                                                   "/*\n"
                                                   "\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
                                                   "QScrollBar::handle:hover:horizontal,QScrollBar::handle:pressed:horizontal{\n"
                                                   "background:rgb(150, 0, 150);\n"
                                                   "}\n"
                                                   "QScrol"
                                                   "lBar::add-line:horizontal {\n"
                                                   "    border: none;\n"
                                                   "    background: rgb(55, 63, 77);\n"
                                                   "    width: 20px;\n"
                                                   "	border-top-right-radius: 3px;\n"
                                                   "    border-bottom-right-radius: 3px;\n"
                                                   "    subcontrol-position: right;\n"
                                                   "    subcontrol-origin: margin;\n"
                                                   "}\n"
                                                   "QScrollBar::sub-line:horizontal {\n"
                                                   "    border: none;\n"
                                                   "    background: rgb(55, 63, 77);\n"
                                                   "    width: 20px;\n"
                                                   "	border-top-left-radius: 3px;\n"
                                                   "    border-bottom-left-radius: 3px;\n"
                                                   "    subcontrol-position: left;\n"
                                                   "    subcontrol-origin: margin;\n"
                                                   "}\n"
                                                   "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
                                                   "{\n"
                                                   "     background: none;\n"
                                                   "}\n"
                                                   "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
                                                   "{\n"
                                                   "     background: none;\n"
                                                   "}\n"
                                                   " QScrollBar:vertical {\n"
                                                   "	border: none;\n"
                                                   "    background: rgb(52, 59, 72);\n"
                                                   "    width: 8px;\n"
                                                   "    margin: 20px 0 20px 0;\n"
                                                   "	border-radius: 3px;\n"
                                                   " }\n"
                                                   " QScrollBar::handle:vertical {	\n"
                                                   "	background:rgba(249, 83, 255, 170);\n"
                                                   "    min-height: 30px;\n"
                                                   "	bord"
                                                   "er-radius: 3px\n"
                                                   " }\n"
                                                   "/*\n"
                                                   "\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
                                                   "QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
                                                   "background:rgb(150, 0, 150);\n"
                                                   "}\n"
                                                   " QScrollBar::add-line:vertical {\n"
                                                   "     border: none;\n"
                                                   "    background: rgb(55, 63, 77);\n"
                                                   "     height: 20px;\n"
                                                   "	border-bottom-left-radius: 3px;\n"
                                                   "    border-bottom-right-radius: 3px;\n"
                                                   "     subcontrol-position: bottom;\n"
                                                   "     subcontrol-origin: margin;\n"
                                                   " }\n"
                                                   " QScrollBar::sub-line:vertical {\n"
                                                   "	border: none;\n"
                                                   "    background: rgb(55, 63, 77);\n"
                                                   "     height: 20px;\n"
                                                   "	border-top-left-radius: 3px;\n"
                                                   "    border-top-right-radius: 3px;\n"
                                                   "     subcontrol-position: top;\n"
                                                   "     subcontrol-origin: margin;\n"
                                                   " }\n"
                                                   " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                                   "     background: none;\n"
                                                   " }\n"
                                                   "\n"
                                                   " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                                   "     background: none;\n"
                                                   " }\n"
                                                   "")

        self.verticalLayout_13.addWidget(self.self_selection_listview)

        self.verticalLayout_4.addWidget(self.frame_12)

        self.horizontalLayout_7.addWidget(self.frame_5)

        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)


    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Btn_draw_line_order.setText(QCoreApplication.translate("Form", u"\u753b\u7ebf\u4e0b\u5355", None))
        self.label_kline_info.setText(QCoreApplication.translate("Form", u"15min", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u81ea\u9009\u5408\u7ea6:", None))
        self.comboBox_backtest_exchange.setItemText(0, QCoreApplication.translate("Form", u"\u5927\u5546\u6240 DCE", None))
        self.comboBox_backtest_exchange.setItemText(1, QCoreApplication.translate("Form", u"\u4e0a\u671f\u6240 SHFE", None))
        self.comboBox_backtest_exchange.setItemText(2, QCoreApplication.translate("Form", u"\u90d1\u5546\u6240 CZCE", None))
        self.comboBox_backtest_exchange.setItemText(3, QCoreApplication.translate("Form", u"\u80fd\u6e90\u4ea4\u6613\u6240 INE", None))
        self.comboBox_backtest_exchange.setItemText(4, QCoreApplication.translate("Form", u"\u4e2d\u91d1\u6240 CFFEX", None))

        self.Btn_add_K_charts_i.setText(QCoreApplication.translate("Form", u"\u94c1\u77ff", None))
        self.Btn_add_K_charts_rb.setText(QCoreApplication.translate("Form", u"\u87ba\u7eb9", None))
        self.Btn_klines_1min.setText(QCoreApplication.translate("Form", u"1\n"
                                                                        "\u5206\n"
                                                                        "\u949f", None))
        self.Btn_klines_15min.setText(QCoreApplication.translate("Form", u"15\n"
                                                                         "\u5206\n"
                                                                         "\u949f", None))
        self.Btn_klines_30min.setText(QCoreApplication.translate("Form", u"30\n"
                                                                         "\u5206\n"
                                                                         "\u949f", None))
        self.Btn_klines_1hour.setText(QCoreApplication.translate("Form", u"1\n"
                                                                         "\u5c0f\n"
                                                                         "\u65f6", None))
        self.Btn_klines_2hour.setText(QCoreApplication.translate("Form", u"2\n"
                                                                         "\u5c0f\n"
                                                                         "\u65f6", None))
        self.Btn_klines_4hour.setText(QCoreApplication.translate("Form", u"4\n"
                                                                         "\u5c0f\n"
                                                                         "\u65f6", None))
        self.Btn_klines_daily.setText(QCoreApplication.translate("Form", u"\u65e5\n"
                                                                         "K\n"
                                                                         "\u7ebf", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u81ea\n"
                                                              "\u5b9a\n"
                                                              "\u4e49", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"120", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5206\n"
                                                                "\u949f", None))
        self.label_instrument_name.setText("")
        self.label_instrument_id.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5356\u51fa", None))
        self.label_ask_price1.setText("")
        self.label_ask_volume1.setText("")
        self.label_6.setText(QCoreApplication.translate("Form", u"\u4e70\u5165", None))
        self.label_bid_price1.setText("")
        self.label_bid_volume1.setText("")
        self.label_12.setText(QCoreApplication.translate("Form", u"\u6da8\u5e45", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u6700\u65b0", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u603b\u91cf", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\u6301\u4ed3", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"\u65e5\u589e", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"\u7ed3\u7b97\u4ef7", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"\u5269\u5929\u6570", None))
        self.label_percent_increase.setText("")
        self.label_last_price.setText("")
        self.label_volume.setText("")
        self.label_open_interest.setText("")
        self.label_daily_increase.setText("")
        self.label_settlement.setText("")
        self.label_expire_rest_days.setText("")
        self.label_20.setText(QCoreApplication.translate("Form", u"\u5f00\u76d8", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"\u6700\u9ad8", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"\u6700\u4f4e", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"\u6628\u6536", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"\u6628\u7ed3", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"\u6da8\u505c", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"\u8dcc\u505c", None))
        self.label_open.setText("")
        self.label_highest.setText("")
        self.label_lowest.setText("")
        self.label_pre_close.setText("")
        self.label_pre_settlement.setText("")
        self.label_upper_limit.setText("")
        self.label_lower_limit.setText("")
        self.label_26.setText(QCoreApplication.translate("Form", u"\u81ea\u9009\u5408\u7ea6\u5217\u8868\uff1a", None))  # retranslateUi
