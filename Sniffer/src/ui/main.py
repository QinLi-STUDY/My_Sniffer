# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSplitter, QTableWidget, QTableWidgetItem,
    QTextEdit, QTreeWidget, QTreeWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(955, 600)
        font = QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionExit.setFont(font)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionAbout.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.interfaceBox = QComboBox(self.centralwidget)
        self.interfaceBox.setObjectName(u"interfaceBox")

        self.gridLayout.addWidget(self.interfaceBox, 0, 1, 1, 1)

        self.filterEdit = QLineEdit(self.centralwidget)
        self.filterEdit.setObjectName(u"filterEdit")
        self.filterEdit.setFont(font)

        self.gridLayout.addWidget(self.filterEdit, 1, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.packetTable = QTableWidget(self.splitter)
        if (self.packetTable.columnCount() < 7):
            self.packetTable.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.packetTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.packetTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.packetTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.packetTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.packetTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.packetTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.packetTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.packetTable.setObjectName(u"packetTable")
        font1 = QFont()
        font1.setFamilies([u"Fira Code"])
        font1.setPointSize(11)
        self.packetTable.setFont(font1)
        self.splitter.addWidget(self.packetTable)
        self.treeWidget = QTreeWidget(self.splitter)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setAnimated(True)
        self.splitter.addWidget(self.treeWidget)
        self.treeWidget.header().setVisible(False)
        self.contentEdit = QTextEdit(self.splitter)
        self.contentEdit.setObjectName(u"contentEdit")
        font2 = QFont()
        font2.setFamilies([u"Fira Code"])
        font2.setPointSize(14)
        self.contentEdit.setFont(font2)
        self.contentEdit.setReadOnly(True)
        self.splitter.addWidget(self.contentEdit)

        self.gridLayout.addWidget(self.splitter, 2, 0, 1, 3)

        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")

        self.gridLayout.addWidget(self.startButton, 1, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"sniffer", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Network Card:", None))
        self.filterEdit.setText(QCoreApplication.translate("MainWindow", u"Please input the BPF expression to filter packets", None))
        self.filterEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pleast input the BPF expression to filter packets", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Setting Filter:", None))
        ___qtablewidgetitem = self.packetTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"No.", None));
        ___qtablewidgetitem1 = self.packetTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"time", None));
        ___qtablewidgetitem2 = self.packetTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"s_port", None));
        ___qtablewidgetitem3 = self.packetTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"d_port", None));
        ___qtablewidgetitem4 = self.packetTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Protocol", None));
        ___qtablewidgetitem5 = self.packetTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Len", None));
        ___qtablewidgetitem6 = self.packetTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"informa", None));
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"Begin", None))
    # retranslateUi

