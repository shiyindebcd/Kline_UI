# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainFrame.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QListView, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1306, 830)
        Form.setStyleSheet(u"\n"
"	background-color: rgb(0, 0, 0);\n"
"	border-radius: 10px;\n"
"	border: none;\n"
"\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(Form)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 770))
        self.frame_16.setStyleSheet(u"QFrame {\n"
"	border-radius: 10px;\n"
"	border: none;\n"
"}\n"
"\n"
"")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_19.setSpacing(3)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.frame_16)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setStyleSheet(u"QFrame {\n"
"	border-radius: 10px;\n"
"	border: none;\n"
"}\n"
"\n"
"")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_23)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 3, 0, 0)
        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_24)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_36 = QFrame(self.frame_24)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setStyleSheet(u"")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_36)
        self.verticalLayout_32.setSpacing(3)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.frame_39 = QFrame(self.frame_36)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMinimumSize(QSize(0, 30))
        self.frame_39.setMaximumSize(QSize(16777215, 35))
        self.frame_39.setStyleSheet(u"QFrame {	\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"}\n"
"\n"
"")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_20.setSpacing(2)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(2, 0, 0, 0)
        self.Btn_draw_line_order = QPushButton(self.frame_39)
        self.Btn_draw_line_order.setObjectName(u"Btn_draw_line_order")
        self.Btn_draw_line_order.setMinimumSize(QSize(60, 30))
        self.Btn_draw_line_order.setMaximumSize(QSize(100, 40))
        self.Btn_draw_line_order.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 0, 127);	\n"
"	font: 700 14pt \"\u7b49\u7ebf\";\n"
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

        self.horizontalLayout_20.addWidget(self.Btn_draw_line_order, 0, Qt.AlignVCenter)

        self.Btn_draw_line_style = QPushButton(self.frame_39)
        self.Btn_draw_line_style.setObjectName(u"Btn_draw_line_style")
        self.Btn_draw_line_style.setMinimumSize(QSize(60, 30))
        self.Btn_draw_line_style.setMaximumSize(QSize(60, 30))
        self.Btn_draw_line_style.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 0, 127);	\n"
"	font: 700 14pt \"\u7b49\u7ebf\";\n"
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

        self.horizontalLayout_20.addWidget(self.Btn_draw_line_style)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_7)

        self.label_kline_info = QLabel(self.frame_39)
        self.label_kline_info.setObjectName(u"label_kline_info")
        self.label_kline_info.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(30, 30, 40, 0);\n"
"	border: none;\n"
"	border-radius: 15px;\n"
"	color: rgb(0, 255, 0);\n"
"	font: 700 14pt \"\u7b49\u7ebf\";\n"
"}\n"
"")

        self.horizontalLayout_20.addWidget(self.label_kline_info)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_8)

        self.label_28 = QLabel(self.frame_39)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(0, 30))
        self.label_28.setMaximumSize(QSize(150, 16777215))
        font = QFont()
        font.setFamilies([u"\u7b49\u7ebf"])
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(30, 30, 40, 0);\n"
"	border: none;\n"
"	border-radius: 15px;\n"
"	color: rgb(255, 0, 255);\n"
"	font: 700 14pt \"\u7b49\u7ebf\";\n"
"}\n"
"")
        self.label_28.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.label_28)

        self.comboBox_add_quote_exchange = QComboBox(self.frame_39)
        self.comboBox_add_quote_exchange.addItem("")
        self.comboBox_add_quote_exchange.addItem("")
        self.comboBox_add_quote_exchange.addItem("")
        self.comboBox_add_quote_exchange.addItem("")
        self.comboBox_add_quote_exchange.addItem("")
        self.comboBox_add_quote_exchange.setObjectName(u"comboBox_add_quote_exchange")
        self.comboBox_add_quote_exchange.setMinimumSize(QSize(120, 30))
        self.comboBox_add_quote_exchange.setMaximumSize(QSize(120, 30))
        self.comboBox_add_quote_exchange.setStyleSheet(u"/* \u672a\u4e0b\u62c9\u65f6\uff0cQComboBox\u7684\u6837\u5f0f */\n"
"QComboBox {\n"
"    border: 2px solid gray;   /* \u8fb9\u6846 */\n"
"    border-radius: 15px;   /* \u5706\u89d2 */\n"
"    padding: 1px 1px 1px 5px;   /* \u5b57\u4f53\u586b\u886c */\n"
"    color: rgb(0, 0, 0);    \n"
"	font: 700 10pt \"\u7b49\u7ebf\";    \n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u6837\u5f0f */\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid rgb(65, 51, 156);   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u8fb9\u6846 */\n"
"    color: rgb(200, 200, 200);\n"
"	border-radius: 0px;\n"
"    background-color: rgb(13, 9, 36);   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u80cc\u666f\u8272 */\n"
"}\n"
"QComboBox QAbstractItemView::item {\n"
"	border:none;\n"
"    height: 25px; \n"
"}\n"
"QComboBox QAbstractItemView::item:hover{\n"
"	border: none;	\n"
"	color: rgb(255, 0, 0);\n"
"	background-color: rgb(65, 49, 188);\n"
"\n"
"}\n"
"QComboBox"
                        " QAbstractItemView::item:selected{\n"
"	border: none;\n"
"}\n"
"/* \u4e0b\u62c9\u7bad\u5934\u6837\u5f0f */\n"
" QComboBox::down-arrow {\n"
"	\n"
"	image: url(:/icon/ProcessTrader/icons/\u53cc\u4e0b\u62c9\u7bad\u5934.svg);\n"
"	width: 10px; /* \u4e0b\u62c9\u7bad\u5934\u7684\u5bbd\u5ea6\uff08\u5efa\u8bae\u4e0e\u4e0b\u62c9\u6846drop-down\u7684\u5bbd\u5ea6\u4e00\u81f4\uff09 */ \n"
"	background: rgb(255, 255, 255); /* \u4e0b\u62c9\u7bad\u5934\u7684\u7684\u80cc\u666f\u8272 */ \n"
"	padding: 0px 0px 0px 0px; /* \u4e0a\u5185\u8fb9\u8ddd\u3001\u53f3\u5185\u8fb9\u8ddd\u3001\u4e0b\u5185\u8fb9\u8ddd\u3001\u5de6\u5185\u8fb9\u8ddd */\n"
" } \n"
"\n"
"/* \u4e0b\u62c9\u6846\u6837\u5f0f */\n"
"QComboBox::drop-down {\n"
"   /* subcontrol-origin: padding;   /* \u5b50\u63a7\u4ef6\u5728\u7236\u5143\u7d20\u4e2d\u7684\u539f\u70b9\u77e9\u5f62\u3002\u5982\u679c\u672a\u6307\u5b9a\u6b64\u5c5e\u6027\uff0c\u5219\u9ed8\u8ba4\u4e3apadding\u3002 */\n"
"   /* subcontrol-position: top right;   /* \u4e0b\u62c9\u6846\u7684\u4f4d\u7f6e\uff08\u53f3"
                        "\u4e0a\uff09 */\n"
"    width: 20px;   /* \u4e0b\u62c9\u6846\u7684\u5bbd\u5ea6 */\n"
"\n"
"    border-left-width: 3px;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u5bbd\u5ea6 */\n"
"    border-left-color: darkgray;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u989c\u8272 */\n"
"    border-left-style: solid;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u4e3a\u5b9e\u7ebf */\n"
"    border-top-right-radius: 10px;   /* \u4e0b\u62c9\u6846\u7684\u53f3\u4e0a\u8fb9\u754c\u7ebf\u7684\u5706\u89d2\u534a\u5f84\uff08\u5e94\u548c\u6574\u4e2aQComboBox\u53f3\u4e0a\u8fb9\u754c\u7ebf\u7684\u5706\u89d2\u534a\u5f84\u4e00\u81f4\uff09 */\n"
"    border-bottom-right-radius: 10px;   /* \u540c\u4e0a */\n"
"}\n"
"QComboBox:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/*\u53f3\u8fb9\u7684\u6ed1\u52a8\u6761*/\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: transparent;\n"
"    width: 8px;\n"
"    margin: 17px 0 17px 0;\n"
"	border-radius: 0px;\n"
" }\n"
""
                        " QScrollBar::handle:vertical {	\n"
"	background:rgba(249, 83, 255, 170);\n"
"    min-height: 30px;\n"
"	border-radius: 0px\n"
" }\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"	background-color: transparent;\n"
"     height: 15px;\n"
"	border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"     height: 15px;\n"
"	border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: transparent;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical "
                        "{\n"
"     background: transparent;\n"
" }\n"
"QScrollBar::add-line:vertical:pressed, QScrollBar::sub-line:vertical:pressed\n"
"{	\n"
"	background-color: transparent;\n"
"}\n"
"")
        self.comboBox_add_quote_exchange.setFrame(True)
        self.comboBox_add_quote_exchange.setModelColumn(0)

        self.horizontalLayout_20.addWidget(self.comboBox_add_quote_exchange, 0, Qt.AlignVCenter)

        self.comboBox_contract_type = QComboBox(self.frame_39)
        self.comboBox_contract_type.addItem("")
        self.comboBox_contract_type.addItem("")
        self.comboBox_contract_type.addItem("")
        self.comboBox_contract_type.addItem("")
        self.comboBox_contract_type.addItem("")
        self.comboBox_contract_type.setObjectName(u"comboBox_contract_type")
        self.comboBox_contract_type.setMinimumSize(QSize(140, 30))
        self.comboBox_contract_type.setMaximumSize(QSize(140, 16777215))
        self.comboBox_contract_type.setStyleSheet(u"/* \u672a\u4e0b\u62c9\u65f6\uff0cQComboBox\u7684\u6837\u5f0f */\n"
"QComboBox {\n"
"    border: 2px solid gray;   /* \u8fb9\u6846 */\n"
"    border-radius: 15px;   /* \u5706\u89d2 */\n"
"    padding: 1px 1px 1px 5px;   /* \u5b57\u4f53\u586b\u886c */\n"
"    color: rgb(0, 0, 0);    \n"
"	font: 700 10pt \"\u7b49\u7ebf\";    \n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u6837\u5f0f */\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid rgb(65, 51, 156);   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u8fb9\u6846 */\n"
"    color: rgb(200, 200, 200);\n"
"	border-radius: 0px;\n"
"    background-color: rgb(13, 9, 36);   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u80cc\u666f\u8272 */\n"
"}\n"
"QComboBox QAbstractItemView::item {\n"
"	border:none;\n"
"    height: 25px; \n"
"}\n"
"QComboBox QAbstractItemView::item:hover{\n"
"	border: none;	\n"
"	color: rgb(255, 0, 0);\n"
"	background-color: rgb(65, 49, 188);\n"
"\n"
"}\n"
"QComboBox"
                        " QAbstractItemView::item:selected{\n"
"	border: none;\n"
"}\n"
"/* \u4e0b\u62c9\u7bad\u5934\u6837\u5f0f */\n"
" QComboBox::down-arrow {\n"
"	\n"
"	image: url(:/icon/ProcessTrader/icons/\u53cc\u4e0b\u62c9\u7bad\u5934.svg);\n"
"	width: 10px; /* \u4e0b\u62c9\u7bad\u5934\u7684\u5bbd\u5ea6\uff08\u5efa\u8bae\u4e0e\u4e0b\u62c9\u6846drop-down\u7684\u5bbd\u5ea6\u4e00\u81f4\uff09 */ \n"
"	background: rgb(255, 255, 255); /* \u4e0b\u62c9\u7bad\u5934\u7684\u7684\u80cc\u666f\u8272 */ \n"
"	padding: 0px 0px 0px 0px; /* \u4e0a\u5185\u8fb9\u8ddd\u3001\u53f3\u5185\u8fb9\u8ddd\u3001\u4e0b\u5185\u8fb9\u8ddd\u3001\u5de6\u5185\u8fb9\u8ddd */\n"
" } \n"
"\n"
"/* \u4e0b\u62c9\u6846\u6837\u5f0f */\n"
"QComboBox::drop-down {\n"
"   /* subcontrol-origin: padding;   /* \u5b50\u63a7\u4ef6\u5728\u7236\u5143\u7d20\u4e2d\u7684\u539f\u70b9\u77e9\u5f62\u3002\u5982\u679c\u672a\u6307\u5b9a\u6b64\u5c5e\u6027\uff0c\u5219\u9ed8\u8ba4\u4e3apadding\u3002 */\n"
"   /* subcontrol-position: top right;   /* \u4e0b\u62c9\u6846\u7684\u4f4d\u7f6e\uff08\u53f3"
                        "\u4e0a\uff09 */\n"
"    width: 20px;   /* \u4e0b\u62c9\u6846\u7684\u5bbd\u5ea6 */\n"
"\n"
"    border-left-width: 3px;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u5bbd\u5ea6 */\n"
"    border-left-color: darkgray;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u989c\u8272 */\n"
"    border-left-style: solid;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u4e3a\u5b9e\u7ebf */\n"
"    border-top-right-radius: 10px;   /* \u4e0b\u62c9\u6846\u7684\u53f3\u4e0a\u8fb9\u754c\u7ebf\u7684\u5706\u89d2\u534a\u5f84\uff08\u5e94\u548c\u6574\u4e2aQComboBox\u53f3\u4e0a\u8fb9\u754c\u7ebf\u7684\u5706\u89d2\u534a\u5f84\u4e00\u81f4\uff09 */\n"
"    border-bottom-right-radius: 10px;   /* \u540c\u4e0a */\n"
"}\n"
"QComboBox:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/*\u53f3\u8fb9\u7684\u6ed1\u52a8\u6761*/\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: transparent;\n"
"    width: 8px;\n"
"    margin: 17px 0 17px 0;\n"
"	border-radius: 0px;\n"
" }\n"
""
                        " QScrollBar::handle:vertical {	\n"
"	background:rgba(249, 83, 255, 170);\n"
"    min-height: 30px;\n"
"	border-radius: 0px\n"
" }\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"	background-color: transparent;\n"
"     height: 15px;\n"
"	border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"     height: 15px;\n"
"	border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: transparent;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical "
                        "{\n"
"     background: transparent;\n"
" }\n"
"QScrollBar::add-line:vertical:pressed, QScrollBar::sub-line:vertical:pressed\n"
"{	\n"
"	background-color: transparent;\n"
"}\n"
"")
        self.comboBox_contract_type.setEditable(False)

        self.horizontalLayout_20.addWidget(self.comboBox_contract_type)

        self.comboBox_symbol = QComboBox(self.frame_39)
        self.comboBox_symbol.setObjectName(u"comboBox_symbol")
        self.comboBox_symbol.setMinimumSize(QSize(150, 30))
        self.comboBox_symbol.setStyleSheet(u"/* \u672a\u4e0b\u62c9\u65f6\uff0cQComboBox\u7684\u6837\u5f0f */\n"
"QComboBox {\n"
"    border: 2px solid gray;   /* \u8fb9\u6846 */\n"
"    border-radius: 15px;   /* \u5706\u89d2 */\n"
"    padding: 1px 1px 1px 5px;   /* \u5b57\u4f53\u586b\u886c */\n"
"    color: rgb(0, 0, 0);    \n"
"	font: 700 10pt \"\u7b49\u7ebf\";    \n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u6837\u5f0f */\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid rgb(65, 51, 156);   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u8fb9\u6846 */\n"
"    color: rgb(200, 200, 200);\n"
"	border-radius: 0px;\n"
"    background-color: rgb(13, 9, 36);   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u80cc\u666f\u8272 */\n"
"}\n"
"QComboBox QAbstractItemView::item {\n"
"	border:none;\n"
"    height: 25px; \n"
"}\n"
"QComboBox QAbstractItemView::item:hover{\n"
"	border: none;	\n"
"	color: rgb(255, 0, 0);\n"
"	background-color: rgb(65, 49, 188);\n"
"\n"
"}\n"
"QComboBox"
                        " QAbstractItemView::item:selected{\n"
"	border: none;\n"
"}\n"
"/* \u4e0b\u62c9\u7bad\u5934\u6837\u5f0f */\n"
" QComboBox::down-arrow {\n"
"	\n"
"	image: url(:/icon/ProcessTrader/icons/\u53cc\u4e0b\u62c9\u7bad\u5934.svg);\n"
"	width: 10px; /* \u4e0b\u62c9\u7bad\u5934\u7684\u5bbd\u5ea6\uff08\u5efa\u8bae\u4e0e\u4e0b\u62c9\u6846drop-down\u7684\u5bbd\u5ea6\u4e00\u81f4\uff09 */ \n"
"	background: rgb(255, 255, 255); /* \u4e0b\u62c9\u7bad\u5934\u7684\u7684\u80cc\u666f\u8272 */ \n"
"	padding: 0px 0px 0px 0px; /* \u4e0a\u5185\u8fb9\u8ddd\u3001\u53f3\u5185\u8fb9\u8ddd\u3001\u4e0b\u5185\u8fb9\u8ddd\u3001\u5de6\u5185\u8fb9\u8ddd */\n"
" } \n"
"\n"
"/* \u4e0b\u62c9\u6846\u6837\u5f0f */\n"
"QComboBox::drop-down {\n"
"   /* subcontrol-origin: padding;   /* \u5b50\u63a7\u4ef6\u5728\u7236\u5143\u7d20\u4e2d\u7684\u539f\u70b9\u77e9\u5f62\u3002\u5982\u679c\u672a\u6307\u5b9a\u6b64\u5c5e\u6027\uff0c\u5219\u9ed8\u8ba4\u4e3apadding\u3002 */\n"
"   /* subcontrol-position: top right;   /* \u4e0b\u62c9\u6846\u7684\u4f4d\u7f6e\uff08\u53f3"
                        "\u4e0a\uff09 */\n"
"    width: 20px;   /* \u4e0b\u62c9\u6846\u7684\u5bbd\u5ea6 */\n"
"\n"
"    border-left-width: 3px;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u5bbd\u5ea6 */\n"
"    border-left-color: darkgray;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u989c\u8272 */\n"
"    border-left-style: solid;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u4e3a\u5b9e\u7ebf */\n"
"    border-top-right-radius: 10px;   /* \u4e0b\u62c9\u6846\u7684\u53f3\u4e0a\u8fb9\u754c\u7ebf\u7684\u5706\u89d2\u534a\u5f84\uff08\u5e94\u548c\u6574\u4e2aQComboBox\u53f3\u4e0a\u8fb9\u754c\u7ebf\u7684\u5706\u89d2\u534a\u5f84\u4e00\u81f4\uff09 */\n"
"    border-bottom-right-radius: 10px;   /* \u540c\u4e0a */\n"
"}\n"
"QComboBox:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/*\u53f3\u8fb9\u7684\u6ed1\u52a8\u6761*/\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: transparent;\n"
"    width: 8px;\n"
"    margin: 17px 0 17px 0;\n"
"	border-radius: 0px;\n"
" }\n"
""
                        " QScrollBar::handle:vertical {	\n"
"	background:rgba(249, 83, 255, 170);\n"
"    min-height: 30px;\n"
"	border-radius: 0px\n"
" }\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"	background-color: transparent;\n"
"     height: 15px;\n"
"	border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"     height: 15px;\n"
"	border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: transparent;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical "
                        "{\n"
"     background: transparent;\n"
" }\n"
"QScrollBar::add-line:vertical:pressed, QScrollBar::sub-line:vertical:pressed\n"
"{	\n"
"	background-color: transparent;\n"
"}\n"
"")
        self.comboBox_symbol.setMaxVisibleItems(30)

        self.horizontalLayout_20.addWidget(self.comboBox_symbol)

        self.Btn_add_self_selection_contracts = QPushButton(self.frame_39)
        self.Btn_add_self_selection_contracts.setObjectName(u"Btn_add_self_selection_contracts")
        self.Btn_add_self_selection_contracts.setMinimumSize(QSize(60, 30))
        self.Btn_add_self_selection_contracts.setMaximumSize(QSize(60, 30))
        self.Btn_add_self_selection_contracts.setStyleSheet(u"QPushButton{\n"
"	color: rgb(13, 9, 36);\n"
"	background-color:rgb(255, 0, 127);\n"
"	font: 700 14pt \"\u7b49\u7ebf\";\n"
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

        self.horizontalLayout_20.addWidget(self.Btn_add_self_selection_contracts, 0, Qt.AlignVCenter)


        self.verticalLayout_32.addWidget(self.frame_39)

        self.frame_40 = QFrame(self.frame_36)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setStyleSheet(u"QFrame {		\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: none;\n"
"	border: none;\n"
"}\n"
"\n"
"")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_21.setSpacing(2)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_klines = QVBoxLayout()
        self.verticalLayout_klines.setSpacing(0)
        self.verticalLayout_klines.setObjectName(u"verticalLayout_klines")

        self.horizontalLayout_21.addLayout(self.verticalLayout_klines)

        self.frame_45 = QFrame(self.frame_40)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(20, 0))
        self.frame_45.setMaximumSize(QSize(20, 16777215))
        self.frame_45.setStyleSheet(u"QFrame {		\n"
"	border-radius: 10px;\n"
"	border: none;\n"
"}\n"
"\n"
"")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_45)
        self.verticalLayout_33.setSpacing(5)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 10, 0, -1)
        self.Btn_klines_1min = QPushButton(self.frame_45)
        self.Btn_klines_1min.setObjectName(u"Btn_klines_1min")
        self.Btn_klines_1min.setMinimumSize(QSize(20, 60))
        self.Btn_klines_1min.setMaximumSize(QSize(20, 60))
        self.Btn_klines_1min.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 85, 0);	\n"
"	font: 700 9pt \"\u7b49\u7ebf\";\n"
"	border: 2px solid rgb(65, 51, 156);\n"
"	border-radius: 8px;\n"
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

        self.verticalLayout_33.addWidget(self.Btn_klines_1min)

        self.Btn_klines_15min = QPushButton(self.frame_45)
        self.Btn_klines_15min.setObjectName(u"Btn_klines_15min")
        self.Btn_klines_15min.setMinimumSize(QSize(20, 60))
        self.Btn_klines_15min.setMaximumSize(QSize(20, 60))
        self.Btn_klines_15min.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 85, 0);	\n"
"	font: 700 9pt \"\u7b49\u7ebf\";\n"
"	border: 2px solid rgb(65, 51, 156);\n"
"	border-radius: 8px;\n"
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

        self.verticalLayout_33.addWidget(self.Btn_klines_15min)

        self.Btn_klines_30min = QPushButton(self.frame_45)
        self.Btn_klines_30min.setObjectName(u"Btn_klines_30min")
        self.Btn_klines_30min.setMinimumSize(QSize(20, 60))
        self.Btn_klines_30min.setMaximumSize(QSize(20, 60))
        self.Btn_klines_30min.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 85, 0);	\n"
"	font: 700 9pt \"\u7b49\u7ebf\";\n"
"	border: 2px solid rgb(65, 51, 156);\n"
"	border-radius: 8px;\n"
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

        self.verticalLayout_33.addWidget(self.Btn_klines_30min)

        self.Btn_klines_1hour = QPushButton(self.frame_45)
        self.Btn_klines_1hour.setObjectName(u"Btn_klines_1hour")
        self.Btn_klines_1hour.setMinimumSize(QSize(20, 60))
        self.Btn_klines_1hour.setMaximumSize(QSize(20, 60))
        self.Btn_klines_1hour.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 85, 0);	\n"
"	font: 700 9pt \"\u7b49\u7ebf\";\n"
"	border: 2px solid rgb(65, 51, 156);\n"
"	border-radius: 8px;\n"
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

        self.verticalLayout_33.addWidget(self.Btn_klines_1hour)

        self.Btn_klines_2hour = QPushButton(self.frame_45)
        self.Btn_klines_2hour.setObjectName(u"Btn_klines_2hour")
        self.Btn_klines_2hour.setMinimumSize(QSize(20, 60))
        self.Btn_klines_2hour.setMaximumSize(QSize(20, 60))
        self.Btn_klines_2hour.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 85, 0);	\n"
"	font: 700 9pt \"\u7b49\u7ebf\";\n"
"	border: 2px solid rgb(65, 51, 156);\n"
"	border-radius: 8px;\n"
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

        self.verticalLayout_33.addWidget(self.Btn_klines_2hour)

        self.Btn_klines_4hour = QPushButton(self.frame_45)
        self.Btn_klines_4hour.setObjectName(u"Btn_klines_4hour")
        self.Btn_klines_4hour.setMinimumSize(QSize(20, 60))
        self.Btn_klines_4hour.setMaximumSize(QSize(20, 60))
        self.Btn_klines_4hour.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 85, 0);	\n"
"	font: 700 9pt \"\u7b49\u7ebf\";\n"
"	border: 2px solid rgb(65, 51, 156);\n"
"	border-radius: 8px;\n"
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

        self.verticalLayout_33.addWidget(self.Btn_klines_4hour)

        self.Btn_klines_daily = QPushButton(self.frame_45)
        self.Btn_klines_daily.setObjectName(u"Btn_klines_daily")
        self.Btn_klines_daily.setMinimumSize(QSize(20, 60))
        self.Btn_klines_daily.setMaximumSize(QSize(20, 60))
        self.Btn_klines_daily.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 85, 0);	\n"
"	font: 700 9pt \"\u7b49\u7ebf\";\n"
"	border: 2px solid rgb(65, 51, 156);\n"
"	border-radius: 8px;\n"
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

        self.verticalLayout_33.addWidget(self.Btn_klines_daily)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer_6)


        self.horizontalLayout_21.addWidget(self.frame_45)


        self.verticalLayout_32.addWidget(self.frame_40)


        self.verticalLayout_20.addWidget(self.frame_36)


        self.verticalLayout_3.addWidget(self.frame_24)


        self.horizontalLayout_19.addWidget(self.frame_23)

        self.frame_56 = QFrame(self.frame_16)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMinimumSize(QSize(250, 0))
        self.frame_56.setMaximumSize(QSize(250, 16777215))
        self.frame_56.setStyleSheet(u"QFrame {	\n"
"	background-color: rgb(13, 9, 27);\n"
"	border-radius: 10px;\n"
"	border: none;\n"
"}\n"
"\n"
"")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_56)
        self.verticalLayout_38.setSpacing(3)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 3, 5, 0)
        self.frame_57 = QFrame(self.frame_56)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setMinimumSize(QSize(0, 70))
        self.frame_57.setMaximumSize(QSize(16777215, 70))
        self.frame_57.setStyleSheet(u"QFrame {	\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"}\n"
"\n"
"")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_57)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_instrument_name = QLabel(self.frame_57)
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

        self.verticalLayout_39.addWidget(self.label_instrument_name)

        self.label_instrument_id = QLabel(self.frame_57)
        self.label_instrument_id.setObjectName(u"label_instrument_id")
        self.label_instrument_id.setMinimumSize(QSize(0, 30))
        self.label_instrument_id.setMaximumSize(QSize(16777215, 30))
        self.label_instrument_id.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(255, 0, 255);\n"
"font: 700 18pt \"\u7b49\u7ebf\";\n"
"border-radius: 15px;\n"
"border: none;")
        self.label_instrument_id.setAlignment(Qt.AlignCenter)

        self.verticalLayout_39.addWidget(self.label_instrument_id)


        self.verticalLayout_38.addWidget(self.frame_57)

        self.frame_58 = QFrame(self.frame_56)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setMinimumSize(QSize(0, 60))
        self.frame_58.setMaximumSize(QSize(16777215, 60))
        self.frame_58.setStyleSheet(u"QFrame {	\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"}\n"
"\n"
"")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_58)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.frame_59 = QFrame(self.frame_58)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setStyleSheet(u"QFrame {	\n"
"	border-radius: 10px;\n"
"	border: none;\n"
"}\n"
"\n"
"")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_26.setSpacing(20)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 3, 0, 0)
        self.label_3 = QLabel(self.frame_59)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(230, 230, 230);\n"
"font: 12pt \"\u7b49\u7ebf\";\n"
"border-radius: 5px;\n"
"border: none;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_3)

        self.label_ask_price1 = QLabel(self.frame_59)
        self.label_ask_price1.setObjectName(u"label_ask_price1")
        self.label_ask_price1.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(255, 0, 0);\n"
"font: 700 16pt \"\u7b49\u7ebf\";\n"
"border-radius: 5px;\n"
"border: none;")
        self.label_ask_price1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_ask_price1)

        self.label_ask_volume1 = QLabel(self.frame_59)
        self.label_ask_volume1.setObjectName(u"label_ask_volume1")
        self.label_ask_volume1.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(255, 255, 0);\n"
"font: 700 16pt \"\u7b49\u7ebf\";\n"
"border-radius: 5px;\n"
"border: none;")
        self.label_ask_volume1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_ask_volume1)


        self.verticalLayout_41.addWidget(self.frame_59)

        self.frame_77 = QFrame(self.frame_58)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setStyleSheet(u"QFrame {	\n"
"	border-radius: 10px;\n"
"	border: none;\n"
"}\n"
"\n"
"")
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_77)
        self.horizontalLayout_30.setSpacing(20)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 3)
        self.label_17 = QLabel(self.frame_77)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(230, 230, 230);\n"
"font: 12pt \"\u7b49\u7ebf\";\n"
"border-radius: 5px;\n"
"border: none;")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.label_17)

        self.label_bid_price1 = QLabel(self.frame_77)
        self.label_bid_price1.setObjectName(u"label_bid_price1")
        self.label_bid_price1.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(255, 0, 0);\n"
"font: 700 16pt \"\u7b49\u7ebf\";\n"
"border-radius: 5px;\n"
"border: none;")
        self.label_bid_price1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.label_bid_price1)

        self.label_bid_volume1 = QLabel(self.frame_77)
        self.label_bid_volume1.setObjectName(u"label_bid_volume1")
        self.label_bid_volume1.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(255, 255, 0);\n"
"font: 700 16pt \"\u7b49\u7ebf\";\n"
"border-radius: 5px;\n"
"border: none;")
        self.label_bid_volume1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.label_bid_volume1)


        self.verticalLayout_41.addWidget(self.frame_77)


        self.verticalLayout_38.addWidget(self.frame_58)

        self.frame_78 = QFrame(self.frame_56)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setMaximumSize(QSize(16777215, 200))
        self.frame_78.setStyleSheet(u"QFrame {	\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"}\n"
"\n"
"")
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_78)
        self.horizontalLayout_31.setSpacing(10)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_79 = QFrame(self.frame_78)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setStyleSheet(u"QFrame {	\n"
"	border: none;\n"
"}\n"
"\n"
"")
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_79)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.frame_90 = QFrame(self.frame_79)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_90)
        self.verticalLayout_48.setSpacing(5)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(5, 5, 5, 5)
        self.label_18 = QLabel(self.frame_90)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(230, 230, 230);\n"
"font: 10pt \"\u7b49\u7ebf\";\n"
"border-radius: 5px;\n"
"border: none;")

        self.verticalLayout_48.addWidget(self.label_18)

        self.label_19 = QLabel(self.frame_90)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(230, 230, 230);\n"
"font: 10pt \"\u7b49\u7ebf\";\n"
"border-radius: 5px;\n"
"border: none;")

        self.verticalLayout_48.addWidget(self.label_19)

        self.label_20 = QLabel(self.frame_90)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(230, 230, 230);\n"
"font: 10pt \"\u7b49\u7ebf\";\n"
"border-radius: 5px;\n"
"border: none;")

        self.verticalLayout_48.addWidget(self.label_20)

        self.label_21 = QLabel(self.frame_90)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(230, 230, 230);\n"
"font: 10pt \"\u7b49\u7ebf\";\n"
"border-radius: 5px;\n"
"border: none;")

        self.verticalLayout_48.addWidget(self.label_21)

        self.label_25 = QLabel(self.frame_90)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(230, 230, 230);\n"
"font: 10pt \"\u7b49\u7ebf\";\n"
"border-radius: 5px;\n"
"border: none;")

        self.verticalLayout_48.addWidget(self.label_25)

        self.label_27 = QLabel(self.frame_90)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(230, 230, 230);\n"
"font: 10pt \"\u7b49\u7ebf\";\n"
"border-radius: 5px;\n"
"border: none;")

        self.verticalLayout_48.addWidget(self.label_27)

        self.label_29 = QLabel(self.frame_90)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(230, 230, 230);\n"
"font: 10pt \"\u7b49\u7ebf\";\n"
"border-radius: 5px;\n"
"border: none;")

        self.verticalLayout_48.addWidget(self.label_29)


        self.horizontalLayout_38.addWidget(self.frame_90, 0, Qt.AlignLeft)

        self.frame_93 = QFrame(self.frame_79)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_93)
        self.verticalLayout_52.setSpacing(5)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(5, 5, 5, 5)
        self.label_percent_increase = QLabel(self.frame_93)
        self.label_percent_increase.setObjectName(u"label_percent_increase")
        self.label_percent_increase.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(255, 0, 0);\n"
"font: 700 12pt \"\u7b49\u7ebf\";\n"
"border-radius: 5px;\n"
"border: none;")
        self.label_percent_increase.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_52.addWidget(self.label_percent_increase)

        self.label_last_price = QLabel(self.frame_93)
        self.label_last_price.setObjectName(u"label_last_price")
        self.label_last_price.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(255, 255, 0);\n"
"font: 700 12pt \"\u7b49\u7ebf\";\n"
"border-radius: 5px;\n"
"border: none;")
        self.label_last_price.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_52.addWidget(self.label_last_price)

        self.label_volume = QLabel(self.frame_93)
        self.label_volume.setObjectName(u"label_volume")
        self.label_volume.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(255, 255, 0);\n"
"font: 700 12pt \"\u7b49\u7ebf\";\n"
"border-radius: 5px;\n"
"border: none;")
        self.label_volume.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_52.addWidget(self.label_volume)

        self.label_open_interest = QLabel(self.frame_93)
        self.label_open_interest.setObjectName(u"label_open_interest")
        self.label_open_interest.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(255, 255, 0);\n"
"font: 700 12pt \"\u7b49\u7ebf\";\n"
"border-radius: 5px;\n"
"border: none;")
        self.label_open_interest.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_52.addWidget(self.label_open_interest)

        self.label_daily_increase = QLabel(self.frame_93)
        self.label_daily_increase.setObjectName(u"label_daily_increase")
        self.label_daily_increase.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(255, 255, 0);\n"
"font: 700 12pt \"\u7b49\u7ebf\";\n"
"border-radius: 5px;\n"
"border: none;")
        self.label_daily_increase.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_52.addWidget(self.label_daily_increase)

        self.label_settlement = QLabel(self.frame_93)
        self.label_settlement.setObjectName(u"label_settlement")
        self.label_settlement.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(255, 255, 0);\n"
"font: 700 12pt \"\u7b49\u7ebf\";\n"
"border-radius: 5px;\n"
"border: none;")
        self.label_settlement.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_52.addWidget(self.label_settlement)

        self.label_expire_rest_days = QLabel(self.frame_93)
        self.label_expire_rest_days.setObjectName(u"label_expire_rest_days")
        self.label_expire_rest_days.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(255, 255, 0);\n"
"font: 700 12pt \"\u7b49\u7ebf\";\n"
"border-radius: 5px;\n"
"border: none;")
        self.label_expire_rest_days.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_52.addWidget(self.label_expire_rest_days)


        self.horizontalLayout_38.addWidget(self.frame_93)


        self.horizontalLayout_31.addWidget(self.frame_79)

        self.frame_94 = QFrame(self.frame_78)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setStyleSheet(u"QFrame {	\n"
"	border: none;\n"
"}\n"
"\n"
"")
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_94)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.frame_95 = QFrame(self.frame_94)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_95)
        self.verticalLayout_54.setSpacing(5)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(5, 5, 5, 5)
        self.label_30 = QLabel(self.frame_95)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(230, 230, 230);\n"
"font: 10pt \"\u7b49\u7ebf\";\n"
"border-radius: 5px;\n"
"border: none;")

        self.verticalLayout_54.addWidget(self.label_30)

        self.label_31 = QLabel(self.frame_95)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(230, 230, 230);\n"
"font: 10pt \"\u7b49\u7ebf\";\n"
"border-radius: 5px;\n"
"border: none;")

        self.verticalLayout_54.addWidget(self.label_31)

        self.label_32 = QLabel(self.frame_95)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(230, 230, 230);\n"
"font: 10pt \"\u7b49\u7ebf\";\n"
"border-radius: 5px;\n"
"border: none;")

        self.verticalLayout_54.addWidget(self.label_32)

        self.label_33 = QLabel(self.frame_95)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(230, 230, 230);\n"
"font: 10pt \"\u7b49\u7ebf\";\n"
"border-radius: 5px;\n"
"border: none;")

        self.verticalLayout_54.addWidget(self.label_33)

        self.label_34 = QLabel(self.frame_95)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(230, 230, 230);\n"
"font: 10pt \"\u7b49\u7ebf\";\n"
"border-radius: 5px;\n"
"border: none;")

        self.verticalLayout_54.addWidget(self.label_34)

        self.label_35 = QLabel(self.frame_95)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(230, 230, 230);\n"
"font: 10pt \"\u7b49\u7ebf\";\n"
"border-radius: 5px;\n"
"border: none;")

        self.verticalLayout_54.addWidget(self.label_35)

        self.label_36 = QLabel(self.frame_95)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(230, 230, 230);\n"
"font: 10pt \"\u7b49\u7ebf\";\n"
"border-radius: 5px;\n"
"border: none;")

        self.verticalLayout_54.addWidget(self.label_36)


        self.horizontalLayout_44.addWidget(self.frame_95)

        self.frame_96 = QFrame(self.frame_94)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_96)
        self.verticalLayout_55.setSpacing(3)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(5, 5, 5, 5)
        self.label_open = QLabel(self.frame_96)
        self.label_open.setObjectName(u"label_open")
        self.label_open.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(255, 0, 0);\n"
"font: 700 12pt \"\u7b49\u7ebf\";\n"
"border-radius: 5px;\n"
"border: none;")
        self.label_open.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_55.addWidget(self.label_open)

        self.label_highest = QLabel(self.frame_96)
        self.label_highest.setObjectName(u"label_highest")
        self.label_highest.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(255, 0, 0);\n"
"font: 700 12pt \"\u7b49\u7ebf\";\n"
"border-radius: 5px;\n"
"border: none;")
        self.label_highest.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_55.addWidget(self.label_highest)

        self.label_lowest = QLabel(self.frame_96)
        self.label_lowest.setObjectName(u"label_lowest")
        self.label_lowest.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(255, 0, 0);\n"
"font: 700 12pt \"\u7b49\u7ebf\";\n"
"border-radius: 5px;\n"
"border: none;")
        self.label_lowest.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_55.addWidget(self.label_lowest)

        self.label_pre_close = QLabel(self.frame_96)
        self.label_pre_close.setObjectName(u"label_pre_close")
        self.label_pre_close.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(255, 0, 0);\n"
"font: 700 12pt \"\u7b49\u7ebf\";\n"
"border-radius: 5px;\n"
"border: none;")
        self.label_pre_close.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_55.addWidget(self.label_pre_close)

        self.label_pre_settlement = QLabel(self.frame_96)
        self.label_pre_settlement.setObjectName(u"label_pre_settlement")
        self.label_pre_settlement.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(255, 0, 0);\n"
"font: 700 12pt \"\u7b49\u7ebf\";\n"
"border-radius: 5px;\n"
"border: none;")
        self.label_pre_settlement.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_55.addWidget(self.label_pre_settlement)

        self.label_upper_limit = QLabel(self.frame_96)
        self.label_upper_limit.setObjectName(u"label_upper_limit")
        self.label_upper_limit.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(255, 0, 0);\n"
"font: 700 12pt \"\u7b49\u7ebf\";\n"
"border-radius: 5px;\n"
"border: none;")
        self.label_upper_limit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_55.addWidget(self.label_upper_limit)

        self.label_lower_limit = QLabel(self.frame_96)
        self.label_lower_limit.setObjectName(u"label_lower_limit")
        self.label_lower_limit.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(255, 0, 0);\n"
"font: 700 12pt \"\u7b49\u7ebf\";\n"
"border-radius: 5px;\n"
"border: none;")
        self.label_lower_limit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_55.addWidget(self.label_lower_limit)


        self.horizontalLayout_44.addWidget(self.frame_96)


        self.horizontalLayout_31.addWidget(self.frame_94)


        self.verticalLayout_38.addWidget(self.frame_78)

        self.frame_97 = QFrame(self.frame_56)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setMaximumSize(QSize(16777215, 40))
        self.frame_97.setStyleSheet(u"QFrame {	\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"}\n"
"\n"
"")
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_97)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.frame_97)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(0, 40))
        self.label_37.setMaximumSize(QSize(150, 16777215))
        self.label_37.setFont(font)
        self.label_37.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(30, 30, 40, 0);\n"
"	border: none;\n"
"	border-radius: 15px;\n"
"	color: rgb(255, 0, 255);\n"
"	font: 700 14pt \"\u7b49\u7ebf\";\n"
"}\n"
"")
        self.label_37.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_49.addWidget(self.label_37)


        self.verticalLayout_38.addWidget(self.frame_97)

        self.frame_98 = QFrame(self.frame_56)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setStyleSheet(u"")
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_98)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.self_selection_listview = QListView(self.frame_98)
        self.self_selection_listview.setObjectName(u"self_selection_listview")
        self.self_selection_listview.setMaximumSize(QSize(16777215, 16777215))
        self.self_selection_listview.setStyleSheet(u"QListView {	\n"
"	font:  10pt \"\u7b49\u7ebf\";	\n"
"	color: rgb(255, 0, 127);\n"
"	background-color: rgb(13,9,36);\n"
"	alternate-background-color:rgba(36, 27, 102, 100);\n"
"	border-radius: 15px;\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	padding-top: 5px;\n"
"	padding-bottom: 5px;\n"
"	padding-left: 0;\n"
"	padding-right: 0;\n"
"}\n"
"QListView::item {\n"
"	min-height:30px;\n"
"     border-radius: 14px;\n"
"	padding-left: 15px;\n"
"}\n"
"\n"
"QListView::item:selected {  	 \n"
"	color: rgb(0, 255, 0);\n"
"	border: none;\n"
"	background-color: rgba(170, 0, 255,150);\n"
"}\n"
"\n"
"QListView::item:hover { \n"
"	background-color: rgba(0, 70, 0, 200);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/*\u4e0b\u8fb9\u548c\u53f3\u8fb9\u7684\u6ed1\u52a8\u6761*/\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background:rgb(26, 19, 75);\n"
"    height: 8px;\n"
"    margin: 0px 17px 0 17px;\n"
"	border-radius: 3px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background:rgba(249, 83, 255, 170);\n"
"    min-width: "
                        "30px;\n"
"	border-radius: 3px\n"
"}\n"
"/*\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:horizontal,QScrollBar::handle:pressed:horizontal{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(0, 50, 135);\n"
"    width: 15px;\n"
"	border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(0, 50, 135);\n"
"    width: 15px;\n"
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
"QScrollBar::add-line:horizontal:pressed, QScrollBar::sub-li"
                        "ne:horizontal:pressed\n"
"{	\n"
"	background-color: rgb(85, 0, 255);\n"
"}\n"
"\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(26, 19, 75);\n"
"    width: 8px;\n"
"    margin: 17px 0 17px 0;\n"
"	border-radius: 3px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background:rgba(249, 83, 255, 170);\n"
"    min-height: 30px;\n"
"	border-radius: 3px\n"
" }\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(0, 50, 135);\n"
"     height: 15px;\n"
"	border-bottom-left-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(0, 50, 135);\n"
"     height: 15px;\n"
"	border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    "
                        " subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"QScrollBar::add-line:vertical:pressed, QScrollBar::sub-line:vertical:pressed\n"
"{	\n"
"	background-color: rgb(85, 0, 255);\n"
"}\n"
"\n"
"")
        self.self_selection_listview.setAlternatingRowColors(True)

        self.verticalLayout_56.addWidget(self.self_selection_listview)


        self.verticalLayout_38.addWidget(self.frame_98)

        self.label_TQ_services_info = QLabel(self.frame_56)
        self.label_TQ_services_info.setObjectName(u"label_TQ_services_info")
        self.label_TQ_services_info.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 12pt \"\u7b49\u7ebf\";")

        self.verticalLayout_38.addWidget(self.label_TQ_services_info)

        self.frame_115 = QFrame(self.frame_56)
        self.frame_115.setObjectName(u"frame_115")
        self.frame_115.setMinimumSize(QSize(0, 100))
        self.frame_115.setStyleSheet(u"QFrame {	\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"}\n"
"\n"
"")
        self.frame_115.setFrameShape(QFrame.StyledPanel)
        self.frame_115.setFrameShadow(QFrame.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.frame_115)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.frame_116 = QFrame(self.frame_115)
        self.frame_116.setObjectName(u"frame_116")
        self.frame_116.setStyleSheet(u"QFrame {	\n"
"	border-radius: 10px;\n"
"	border: none;\n"
"}\n"
"\n"
"")
        self.frame_116.setFrameShape(QFrame.StyledPanel)
        self.frame_116.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_116)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.Btn_start_TQ_services = QPushButton(self.frame_116)
        self.Btn_start_TQ_services.setObjectName(u"Btn_start_TQ_services")
        self.Btn_start_TQ_services.setMinimumSize(QSize(0, 30))
        self.Btn_start_TQ_services.setMaximumSize(QSize(180, 16777215))
        self.Btn_start_TQ_services.setStyleSheet(u"QPushButton{\n"
"	color: rgb(13, 9, 36);\n"
"	background-color:rgb(255, 0, 127);\n"
"	font: 700 14pt \"\u7b49\u7ebf\";\n"
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

        self.horizontalLayout_54.addWidget(self.Btn_start_TQ_services)


        self.verticalLayout_68.addWidget(self.frame_116)

        self.frame_117 = QFrame(self.frame_115)
        self.frame_117.setObjectName(u"frame_117")
        self.frame_117.setStyleSheet(u"QFrame {	\n"
"	border-radius: 10px;\n"
"	border: none;\n"
"}\n"
"\n"
"")
        self.frame_117.setFrameShape(QFrame.StyledPanel)
        self.frame_117.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_117)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.Btn_stop_TQ_services = QPushButton(self.frame_117)
        self.Btn_stop_TQ_services.setObjectName(u"Btn_stop_TQ_services")
        self.Btn_stop_TQ_services.setMinimumSize(QSize(0, 30))
        self.Btn_stop_TQ_services.setMaximumSize(QSize(180, 16777215))
        self.Btn_stop_TQ_services.setStyleSheet(u"QPushButton{\n"
"	color: rgb(13, 9, 36);\n"
"	background-color:rgb(0, 255, 0);\n"
"	font: 700 14pt \"\u7b49\u7ebf\";\n"
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

        self.horizontalLayout_55.addWidget(self.Btn_stop_TQ_services)


        self.verticalLayout_68.addWidget(self.frame_117)


        self.verticalLayout_38.addWidget(self.frame_115)


        self.horizontalLayout_19.addWidget(self.frame_56)


        self.horizontalLayout.addWidget(self.frame_16)


        self.retranslateUi(Form)

        self.comboBox_add_quote_exchange.setCurrentIndex(0)
        self.comboBox_contract_type.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Btn_draw_line_order.setText(QCoreApplication.translate("Form", u"\u753b\u7ebf", None))
        self.Btn_draw_line_style.setText(QCoreApplication.translate("Form", u"\u6837\u5f0f", None))
        self.label_kline_info.setText("")
        self.label_28.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u81ea\u9009:", None))
        self.comboBox_add_quote_exchange.setItemText(0, QCoreApplication.translate("Form", u"\u5927\u5546\u6240 DCE", None))
        self.comboBox_add_quote_exchange.setItemText(1, QCoreApplication.translate("Form", u"\u4e0a\u671f\u6240 SHFE", None))
        self.comboBox_add_quote_exchange.setItemText(2, QCoreApplication.translate("Form", u"\u90d1\u5546\u6240 CZCE", None))
        self.comboBox_add_quote_exchange.setItemText(3, QCoreApplication.translate("Form", u"\u80fd\u6e90\u4ea4\u6613\u6240 INE", None))
        self.comboBox_add_quote_exchange.setItemText(4, QCoreApplication.translate("Form", u"\u4e2d\u91d1\u6240 CFFEX", None))

        self.comboBox_contract_type.setItemText(0, QCoreApplication.translate("Form", u"\u4e3b\u529b\u5408\u7ea6 Main", None))
        self.comboBox_contract_type.setItemText(1, QCoreApplication.translate("Form", u"\u6240\u6709\u5408\u7ea6 Future", None))
        self.comboBox_contract_type.setItemText(2, QCoreApplication.translate("Form", u"\u4e3b\u529b\u8fde\u7eed Cont", None))
        self.comboBox_contract_type.setItemText(3, QCoreApplication.translate("Form", u"\u5408\u7ea6\u6307\u6570 Index", None))
        self.comboBox_contract_type.setItemText(4, QCoreApplication.translate("Form", u"\u671f\u6743\u5408\u7ea6 Option", None))

        self.Btn_add_self_selection_contracts.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0", None))
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
        self.label_instrument_name.setText("")
        self.label_instrument_id.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5356\u51fa", None))
        self.label_ask_price1.setText("")
        self.label_ask_volume1.setText("")
        self.label_17.setText(QCoreApplication.translate("Form", u"\u4e70\u5165", None))
        self.label_bid_price1.setText("")
        self.label_bid_volume1.setText("")
        self.label_18.setText(QCoreApplication.translate("Form", u"\u6da8\u5e45", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"\u6700\u65b0", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"\u603b\u91cf", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"\u6301\u4ed3", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"\u65e5\u589e", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"\u7ed3\u7b97\u4ef7", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"\u5269\u5929\u6570", None))
        self.label_percent_increase.setText("")
        self.label_last_price.setText("")
        self.label_volume.setText("")
        self.label_open_interest.setText("")
        self.label_daily_increase.setText("")
        self.label_settlement.setText("")
        self.label_expire_rest_days.setText("")
        self.label_30.setText(QCoreApplication.translate("Form", u"\u5f00\u76d8", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"\u6700\u9ad8", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"\u6700\u4f4e", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"\u6628\u6536", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"\u6628\u7ed3", None))
        self.label_35.setText(QCoreApplication.translate("Form", u"\u6da8\u505c", None))
        self.label_36.setText(QCoreApplication.translate("Form", u"\u8dcc\u505c", None))
        self.label_open.setText("")
        self.label_highest.setText("")
        self.label_lowest.setText("")
        self.label_pre_close.setText("")
        self.label_pre_settlement.setText("")
        self.label_upper_limit.setText("")
        self.label_lower_limit.setText("")
        self.label_37.setText(QCoreApplication.translate("Form", u"\u81ea\u9009\u5408\u7ea6\u5217\u8868\uff1a", None))
        self.label_TQ_services_info.setText(QCoreApplication.translate("Form", u"\u5929\u52e4\u884c\u60c5\u6570\u636e\u670d\u52a1\u672a\u542f\u52a8", None))
        self.Btn_start_TQ_services.setText(QCoreApplication.translate("Form", u"\u5f00\u542f\u5929\u52e4\u884c\u60c5\u670d\u52a1", None))
        self.Btn_stop_TQ_services.setText(QCoreApplication.translate("Form", u"\u5173\u95ed\u5929\u52e4\u884c\u60c5\u670d\u52a1", None))
    # retranslateUi

