# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Fri Nov 14 23:37:40 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(618, 474)
        MainWindow.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeCluster = QtGui.QTreeWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeCluster.sizePolicy().hasHeightForWidth())
        self.treeCluster.setSizePolicy(sizePolicy)
        self.treeCluster.setMinimumSize(QtCore.QSize(150, 0))
        self.treeCluster.setMaximumSize(QtCore.QSize(200, 16777215))
        self.treeCluster.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.treeCluster.setObjectName("treeCluster")
        self.horizontalLayout.addWidget(self.treeCluster)
        self.tabsMain = QtGui.QTabWidget(self.centralwidget)
        self.tabsMain.setMinimumSize(QtCore.QSize(325, 0))
        self.tabsMain.setObjectName("tabsMain")
        self.MTasks = QtGui.QWidget()
        self.MTasks.setObjectName("MTasks")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.MTasks)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gbClearKey = QtGui.QGroupBox(self.MTasks)
        self.gbClearKey.setFlat(False)
        self.gbClearKey.setObjectName("gbClearKey")
        self.gridLayout_2 = QtGui.QGridLayout(self.gbClearKey)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblCacheKeys = QtGui.QLabel(self.gbClearKey)
        self.lblCacheKeys.setObjectName("lblCacheKeys")
        self.gridLayout_2.addWidget(self.lblCacheKeys, 0, 0, 1, 1)
        self.txtCacheKeys = QtGui.QLineEdit(self.gbClearKey)
        self.txtCacheKeys.setObjectName("txtCacheKeys")
        self.gridLayout_2.addWidget(self.txtCacheKeys, 0, 1, 1, 1)
        self.btnCacheKeys = QtGui.QPushButton(self.gbClearKey)
        self.btnCacheKeys.setObjectName("btnCacheKeys")
        self.gridLayout_2.addWidget(self.btnCacheKeys, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.gbClearKey)
        self.gbTasks = QtGui.QGroupBox(self.MTasks)
        self.gbTasks.setObjectName("gbTasks")
        self.gridLayout = QtGui.QGridLayout(self.gbTasks)
        self.gridLayout.setObjectName("gridLayout")
        self.btnFlushCache = QtGui.QPushButton(self.gbTasks)
        self.btnFlushCache.setObjectName("btnFlushCache")
        self.gridLayout.addWidget(self.btnFlushCache, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.gbTasks)
        self.tabsMain.addTab(self.MTasks, "")
        self.SKInfo = QtGui.QWidget()
        self.SKInfo.setObjectName("SKInfo")
        self.tabsMain.addTab(self.SKInfo, "")
        self.Stats = QtGui.QWidget()
        self.Stats.setObjectName("Stats")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.Stats)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabsStats = QtGui.QTabWidget(self.Stats)
        self.tabsStats.setObjectName("tabsStats")
        self.CacheInfo = QtGui.QWidget()
        self.CacheInfo.setObjectName("CacheInfo")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.CacheInfo)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.scrollArea_2 = QtGui.QScrollArea(self.CacheInfo)
        self.scrollArea_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtGui.QWidget(self.scrollArea_2)
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, -229, 335, 476))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gbTotals = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.gbTotals.setObjectName("gbTotals")
        self.gridLayout_3 = QtGui.QGridLayout(self.gbTotals)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lblCurrentItemsTxt = QtGui.QLabel(self.gbTotals)
        self.lblCurrentItemsTxt.setObjectName("lblCurrentItemsTxt")
        self.gridLayout_3.addWidget(self.lblCurrentItemsTxt, 1, 0, 1, 1)
        self.lblCurrentItems = QtGui.QLabel(self.gbTotals)
        self.lblCurrentItems.setObjectName("lblCurrentItems")
        self.gridLayout_3.addWidget(self.lblCurrentItems, 1, 1, 1, 1)
        self.lblHitsTxt = QtGui.QLabel(self.gbTotals)
        self.lblHitsTxt.setObjectName("lblHitsTxt")
        self.gridLayout_3.addWidget(self.lblHitsTxt, 4, 0, 1, 1)
        self.lblHits = QtGui.QLabel(self.gbTotals)
        self.lblHits.setObjectName("lblHits")
        self.gridLayout_3.addWidget(self.lblHits, 4, 1, 1, 1)
        self.lblMissesTxt = QtGui.QLabel(self.gbTotals)
        self.lblMissesTxt.setObjectName("lblMissesTxt")
        self.gridLayout_3.addWidget(self.lblMissesTxt, 5, 0, 1, 1)
        self.lblMisses = QtGui.QLabel(self.gbTotals)
        self.lblMisses.setObjectName("lblMisses")
        self.gridLayout_3.addWidget(self.lblMisses, 5, 1, 1, 1)
        self.lblFreeTxt = QtGui.QLabel(self.gbTotals)
        self.lblFreeTxt.setObjectName("lblFreeTxt")
        self.gridLayout_3.addWidget(self.lblFreeTxt, 9, 0, 1, 1)
        self.lblFree = QtGui.QLabel(self.gbTotals)
        self.lblFree.setObjectName("lblFree")
        self.gridLayout_3.addWidget(self.lblFree, 9, 1, 1, 1)
        self.lblUsedTxt = QtGui.QLabel(self.gbTotals)
        self.lblUsedTxt.setObjectName("lblUsedTxt")
        self.gridLayout_3.addWidget(self.lblUsedTxt, 10, 0, 1, 1)
        self.lblUsed = QtGui.QLabel(self.gbTotals)
        self.lblUsed.setObjectName("lblUsed")
        self.gridLayout_3.addWidget(self.lblUsed, 10, 1, 1, 1)
        self.lblItemsTxt = QtGui.QLabel(self.gbTotals)
        self.lblItemsTxt.setObjectName("lblItemsTxt")
        self.gridLayout_3.addWidget(self.lblItemsTxt, 0, 0, 1, 1)
        self.lblItems = QtGui.QLabel(self.gbTotals)
        self.lblItems.setObjectName("lblItems")
        self.gridLayout_3.addWidget(self.lblItems, 0, 1, 1, 1)
        self.lblConnectionsTxt = QtGui.QLabel(self.gbTotals)
        self.lblConnectionsTxt.setObjectName("lblConnectionsTxt")
        self.gridLayout_3.addWidget(self.lblConnectionsTxt, 2, 0, 1, 1)
        self.lblConnections = QtGui.QLabel(self.gbTotals)
        self.lblConnections.setObjectName("lblConnections")
        self.gridLayout_3.addWidget(self.lblConnections, 2, 1, 1, 1)
        self.lblCurrentConnectionsTxt = QtGui.QLabel(self.gbTotals)
        self.lblCurrentConnectionsTxt.setFrameShape(QtGui.QFrame.NoFrame)
        self.lblCurrentConnectionsTxt.setObjectName("lblCurrentConnectionsTxt")
        self.gridLayout_3.addWidget(self.lblCurrentConnectionsTxt, 3, 0, 1, 1)
        self.lblCurrentConnections = QtGui.QLabel(self.gbTotals)
        self.lblCurrentConnections.setObjectName("lblCurrentConnections")
        self.gridLayout_3.addWidget(self.lblCurrentConnections, 3, 1, 1, 1)
        self.lblGetsTxt = QtGui.QLabel(self.gbTotals)
        self.lblGetsTxt.setObjectName("lblGetsTxt")
        self.gridLayout_3.addWidget(self.lblGetsTxt, 6, 0, 1, 1)
        self.lblGets = QtGui.QLabel(self.gbTotals)
        self.lblGets.setObjectName("lblGets")
        self.gridLayout_3.addWidget(self.lblGets, 6, 1, 1, 1)
        self.lblSetsTxt = QtGui.QLabel(self.gbTotals)
        self.lblSetsTxt.setObjectName("lblSetsTxt")
        self.gridLayout_3.addWidget(self.lblSetsTxt, 7, 0, 1, 1)
        self.lblSets = QtGui.QLabel(self.gbTotals)
        self.lblSets.setObjectName("lblSets")
        self.gridLayout_3.addWidget(self.lblSets, 7, 1, 1, 1)
        self.lblSpaceTxt = QtGui.QLabel(self.gbTotals)
        self.lblSpaceTxt.setObjectName("lblSpaceTxt")
        self.gridLayout_3.addWidget(self.lblSpaceTxt, 8, 0, 1, 1)
        self.lblSpace = QtGui.QLabel(self.gbTotals)
        self.lblSpace.setObjectName("lblSpace")
        self.gridLayout_3.addWidget(self.lblSpace, 8, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.gbTotals)
        self.gbRates = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.gbRates.setObjectName("gbRates")
        self.gridLayout_4 = QtGui.QGridLayout(self.gbRates)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lblRequestRateTxt = QtGui.QLabel(self.gbRates)
        self.lblRequestRateTxt.setObjectName("lblRequestRateTxt")
        self.gridLayout_4.addWidget(self.lblRequestRateTxt, 0, 0, 1, 1)
        self.lblRequestRate = QtGui.QLabel(self.gbRates)
        self.lblRequestRate.setObjectName("lblRequestRate")
        self.gridLayout_4.addWidget(self.lblRequestRate, 0, 1, 1, 1)
        self.lblHitRateTxt = QtGui.QLabel(self.gbRates)
        self.lblHitRateTxt.setObjectName("lblHitRateTxt")
        self.gridLayout_4.addWidget(self.lblHitRateTxt, 1, 0, 1, 1)
        self.lblHitRate = QtGui.QLabel(self.gbRates)
        self.lblHitRate.setObjectName("lblHitRate")
        self.gridLayout_4.addWidget(self.lblHitRate, 1, 1, 1, 1)
        self.lblMissRateTxt = QtGui.QLabel(self.gbRates)
        self.lblMissRateTxt.setObjectName("lblMissRateTxt")
        self.gridLayout_4.addWidget(self.lblMissRateTxt, 2, 0, 1, 1)
        self.lblMissRate = QtGui.QLabel(self.gbRates)
        self.lblMissRate.setObjectName("lblMissRate")
        self.gridLayout_4.addWidget(self.lblMissRate, 2, 1, 1, 1)
        self.lblSetRateTxt = QtGui.QLabel(self.gbRates)
        self.lblSetRateTxt.setObjectName("lblSetRateTxt")
        self.gridLayout_4.addWidget(self.lblSetRateTxt, 4, 0, 1, 1)
        self.lblGetRateTxt = QtGui.QLabel(self.gbRates)
        self.lblGetRateTxt.setObjectName("lblGetRateTxt")
        self.gridLayout_4.addWidget(self.lblGetRateTxt, 3, 0, 1, 1)
        self.lblSetRate = QtGui.QLabel(self.gbRates)
        self.lblSetRate.setObjectName("lblSetRate")
        self.gridLayout_4.addWidget(self.lblSetRate, 4, 1, 1, 1)
        self.lblGetRate = QtGui.QLabel(self.gbRates)
        self.lblGetRate.setObjectName("lblGetRate")
        self.gridLayout_4.addWidget(self.lblGetRate, 3, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.gbRates)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_4.addWidget(self.scrollArea_2)
        self.tabsStats.addTab(self.CacheInfo, "")
        self.Diagrams = QtGui.QWidget()
        self.Diagrams.setObjectName("Diagrams")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.Diagrams)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scrollArea = QtGui.QScrollArea(self.Diagrams)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 350, 247))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblCacheUsageGraph = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblCacheUsageGraph.setObjectName("lblCacheUsageGraph")
        self.verticalLayout.addWidget(self.lblCacheUsageGraph)
        self.lblHitsMissesGraph = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblHitsMissesGraph.setObjectName("lblHitsMissesGraph")
        self.verticalLayout.addWidget(self.lblHitsMissesGraph)
        self.lblGetSetGraph = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblGetSetGraph.setObjectName("lblGetSetGraph")
        self.verticalLayout.addWidget(self.lblGetSetGraph)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.addWidget(self.scrollArea)
        self.tabsStats.addTab(self.Diagrams, "")
        self.ServerInfo = QtGui.QWidget()
        self.ServerInfo.setObjectName("ServerInfo")
        self.tabsStats.addTab(self.ServerInfo, "")
        self.verticalLayout_4.addWidget(self.tabsStats)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnRefresh = QtGui.QPushButton(self.Stats)
        self.btnRefresh.setObjectName("btnRefresh")
        self.horizontalLayout_2.addWidget(self.btnRefresh)
        self.btnWatch = QtGui.QPushButton(self.Stats)
        self.btnWatch.setObjectName("btnWatch")
        self.horizontalLayout_2.addWidget(self.btnWatch)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.pbStats = QtGui.QProgressBar(self.Stats)
        self.pbStats.setProperty("value", QtCore.QVariant(0))
        self.pbStats.setAlignment(QtCore.Qt.AlignCenter)
        self.pbStats.setObjectName("pbStats")
        self.verticalLayout_4.addWidget(self.pbStats)
        self.tabsMain.addTab(self.Stats, "")
        self.horizontalLayout.addWidget(self.tabsMain)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 618, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menu_Servers = QtGui.QMenu(self.menubar)
        self.menu_Servers.setObjectName("menu_Servers")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAddServer = QtGui.QAction(MainWindow)
        self.actionAddServer.setObjectName("actionAddServer")
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAddCluster = QtGui.QAction(MainWindow)
        self.actionAddCluster.setObjectName("actionAddCluster")
        self.actionTest_Sub_Item = QtGui.QAction(MainWindow)
        self.actionTest_Sub_Item.setObjectName("actionTest_Sub_Item")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionQuit)
        self.menu_Servers.addAction(self.actionAddServer)
        self.menu_Servers.addAction(self.actionAddCluster)
        self.menu_Servers.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu_Servers.menuAction())

        self.retranslateUi(MainWindow)
        self.tabsMain.setCurrentIndex(0)
        self.tabsStats.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL("activated()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Memcached Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.treeCluster.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Clusters", None, QtGui.QApplication.UnicodeUTF8))
        self.gbClearKey.setTitle(QtGui.QApplication.translate("MainWindow", "Delete Key(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCacheKeys.setText(QtGui.QApplication.translate("MainWindow", "Cache Key(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.txtCacheKeys.setToolTip(QtGui.QApplication.translate("MainWindow", "Seperate Keys with \';\'", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCacheKeys.setText(QtGui.QApplication.translate("MainWindow", "Delete Key(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.gbTasks.setTitle(QtGui.QApplication.translate("MainWindow", "Server Admin Tasks", None, QtGui.QApplication.UnicodeUTF8))
        self.btnFlushCache.setToolTip(QtGui.QApplication.translate("MainWindow", "Flush Keys from All Servers in Cluster", None, QtGui.QApplication.UnicodeUTF8))
        self.btnFlushCache.setText(QtGui.QApplication.translate("MainWindow", "Flush Cache Keys", None, QtGui.QApplication.UnicodeUTF8))
        self.tabsMain.setTabText(self.tabsMain.indexOf(self.MTasks), QtGui.QApplication.translate("MainWindow", "Management Tasks", None, QtGui.QApplication.UnicodeUTF8))
        self.tabsMain.setTabToolTip(self.tabsMain.indexOf(self.MTasks), QtGui.QApplication.translate("MainWindow", "Cluster Management Tasks", None, QtGui.QApplication.UnicodeUTF8))
        self.tabsMain.setTabText(self.tabsMain.indexOf(self.SKInfo), QtGui.QApplication.translate("MainWindow", "Slab && Key Info", None, QtGui.QApplication.UnicodeUTF8))
        self.tabsMain.setTabToolTip(self.tabsMain.indexOf(self.SKInfo), QtGui.QApplication.translate("MainWindow", "Slabs, Keys, & Values", None, QtGui.QApplication.UnicodeUTF8))
        self.gbTotals.setTitle(QtGui.QApplication.translate("MainWindow", "Totals", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCurrentItemsTxt.setText(QtGui.QApplication.translate("MainWindow", "Current Items:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCurrentItems.setText(QtGui.QApplication.translate("MainWindow", "n/a", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHitsTxt.setText(QtGui.QApplication.translate("MainWindow", "Hits:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHits.setText(QtGui.QApplication.translate("MainWindow", "n/a", None, QtGui.QApplication.UnicodeUTF8))
        self.lblMissesTxt.setText(QtGui.QApplication.translate("MainWindow", "Misses:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblMisses.setText(QtGui.QApplication.translate("MainWindow", "n/a", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFreeTxt.setText(QtGui.QApplication.translate("MainWindow", "Free Space:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFree.setText(QtGui.QApplication.translate("MainWindow", "n/a", None, QtGui.QApplication.UnicodeUTF8))
        self.lblUsedTxt.setText(QtGui.QApplication.translate("MainWindow", "Used Space:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblUsed.setText(QtGui.QApplication.translate("MainWindow", "n/a", None, QtGui.QApplication.UnicodeUTF8))
        self.lblItemsTxt.setText(QtGui.QApplication.translate("MainWindow", "All Time Items:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblItems.setText(QtGui.QApplication.translate("MainWindow", "n/a", None, QtGui.QApplication.UnicodeUTF8))
        self.lblConnectionsTxt.setText(QtGui.QApplication.translate("MainWindow", "All Time Connections:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblConnections.setText(QtGui.QApplication.translate("MainWindow", "n/a", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCurrentConnectionsTxt.setText(QtGui.QApplication.translate("MainWindow", "Current Connections:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCurrentConnections.setText(QtGui.QApplication.translate("MainWindow", "n/a", None, QtGui.QApplication.UnicodeUTF8))
        self.lblGetsTxt.setText(QtGui.QApplication.translate("MainWindow", "Gets:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblGets.setText(QtGui.QApplication.translate("MainWindow", "n/a", None, QtGui.QApplication.UnicodeUTF8))
        self.lblSetsTxt.setText(QtGui.QApplication.translate("MainWindow", "Sets:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblSets.setText(QtGui.QApplication.translate("MainWindow", "n/a", None, QtGui.QApplication.UnicodeUTF8))
        self.lblSpaceTxt.setText(QtGui.QApplication.translate("MainWindow", "Space:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblSpace.setText(QtGui.QApplication.translate("MainWindow", "n/a", None, QtGui.QApplication.UnicodeUTF8))
        self.gbRates.setTitle(QtGui.QApplication.translate("MainWindow", "Cache Rates", None, QtGui.QApplication.UnicodeUTF8))
        self.lblRequestRateTxt.setText(QtGui.QApplication.translate("MainWindow", "Request Rate:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblRequestRate.setText(QtGui.QApplication.translate("MainWindow", "n/a", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHitRateTxt.setText(QtGui.QApplication.translate("MainWindow", "Hit Rate:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHitRate.setText(QtGui.QApplication.translate("MainWindow", "n/a", None, QtGui.QApplication.UnicodeUTF8))
        self.lblMissRateTxt.setText(QtGui.QApplication.translate("MainWindow", "Miss Rate:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblMissRate.setText(QtGui.QApplication.translate("MainWindow", "n/a", None, QtGui.QApplication.UnicodeUTF8))
        self.lblSetRateTxt.setText(QtGui.QApplication.translate("MainWindow", "Set Rate:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblGetRateTxt.setText(QtGui.QApplication.translate("MainWindow", "Get Rate:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblSetRate.setText(QtGui.QApplication.translate("MainWindow", "n/a", None, QtGui.QApplication.UnicodeUTF8))
        self.lblGetRate.setText(QtGui.QApplication.translate("MainWindow", "n/a", None, QtGui.QApplication.UnicodeUTF8))
        self.tabsStats.setTabText(self.tabsStats.indexOf(self.CacheInfo), QtGui.QApplication.translate("MainWindow", "Cache Info", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCacheUsageGraph.setText(QtGui.QApplication.translate("MainWindow", "Cache Usage", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHitsMissesGraph.setText(QtGui.QApplication.translate("MainWindow", "Hits & Misses Graph", None, QtGui.QApplication.UnicodeUTF8))
        self.lblGetSetGraph.setText(QtGui.QApplication.translate("MainWindow", "Gets & Set Graph", None, QtGui.QApplication.UnicodeUTF8))
        self.tabsStats.setTabText(self.tabsStats.indexOf(self.Diagrams), QtGui.QApplication.translate("MainWindow", "Diagrams", None, QtGui.QApplication.UnicodeUTF8))
        self.tabsStats.setTabText(self.tabsStats.indexOf(self.ServerInfo), QtGui.QApplication.translate("MainWindow", "Server Information", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRefresh.setText(QtGui.QApplication.translate("MainWindow", "Refresh Stats", None, QtGui.QApplication.UnicodeUTF8))
        self.btnWatch.setText(QtGui.QApplication.translate("MainWindow", "Watch Live Stats", None, QtGui.QApplication.UnicodeUTF8))
        self.tabsMain.setTabText(self.tabsMain.indexOf(self.Stats), QtGui.QApplication.translate("MainWindow", "Statistics", None, QtGui.QApplication.UnicodeUTF8))
        self.tabsMain.setTabToolTip(self.tabsMain.indexOf(self.Stats), QtGui.QApplication.translate("MainWindow", "Memcached Server Stats", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Servers.setTitle(QtGui.QApplication.translate("MainWindow", "&Servers", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddServer.setText(QtGui.QApplication.translate("MainWindow", "&Add Server", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Sa&ve", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddCluster.setText(QtGui.QApplication.translate("MainWindow", "Add &Cluster", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTest_Sub_Item.setText(QtGui.QApplication.translate("MainWindow", "Test Sub Item", None, QtGui.QApplication.UnicodeUTF8))

