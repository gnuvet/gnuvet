# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aebasecol.ui'
#
# Created: Mon Dec 22 21:53:13 2014
#      by: PyQt4 UI code generator 4.11.2
#

from PyQt4.QtGui import (QApplication, QCheckBox, QFont, QFrame, QLabel,
                         QLineEdit, QPixmap, QPushButton, QRadioButton,
                         QScrollArea)

import gv_qrc

class Ui_Aebasecol(object):
    devels = 0
    
    def setupUi(self, Aebasecol):
        Aebasecol.resize(400, 469)
        Aebasecol.setMinimumSize(400, 469)
        Aebasecol.setMaximumSize(400, 470)
        ## self.centralwidget = QtGui.QWidget(Aebasecol) # elim centralwidget?
        self.menubar = Aebasecol.menuBar()
        self.statusbar = Aebasecol.statusBar()
        self.statusbar.setSizeGripEnabled(False)
        self.no_dbconn = QLabel(self.statusbar)
        font = QFont()
        font.setBold(True)
        self.no_dbconn.setFont(font)
        self.statusbar.addPermanentWidget(self.no_dbconn, 0)
        self.no_dbconn.hide()
        self.aeFr = QFrame(Aebasecol)
        self.aeFr.setGeometry(10, 10, 380, 340)
        self.aeFr.setAutoFillBackground(True)
        self.aeFr.setFrameShape(6) # StyledPanel
        self.aeFr.setFrameShadow(20) # Raised
        self.bcnameLb = QLabel(self.aeFr)
        self.bcnameLb.setGeometry(31, 10, 115, 19)
        self.bcnameLe = QLineEdit(self.aeFr)
        self.bcnameLe.setGeometry(30, 30, 231, 27)
        self.bcnameLe.setMaxLength(25)
        self.combLb = QLabel(self.aeFr)
        self.combLb.setGeometry(31, 70, 240, 24)
        self.possRb = QRadioButton(self.aeFr)
        self.possRb.setGeometry(30, 95, 78, 23)
        self.possRb.setChecked(True)
        self.oblRb = QRadioButton(self.aeFr)
        self.oblRb.setGeometry(30, 115, 91, 23)
        self.noRb = QRadioButton(self.aeFr)
        self.noRb.setGeometry(30, 135, 58, 23)
        self.specLb = QLabel(self.aeFr)
        self.specLb.setGeometry(31, 170, 231, 37)
        ## self.specLb.setFrameShape(1)
        self.specLb.setWordWrap(True)
        self.scrollA = QScrollArea(self.aeFr)
        self.scrollA.setGeometry(30, 220, 231, 101)
        ## self.scrollA.setFrameShape(1)
        self.specFr = QFrame(self.scrollA) # aeFr?
        self.specFr.setGeometry(0, 0, 230, 110)
        self.specFr.setFrameShape(6)
        self.specFr.setFrameShadow(30)
        self.allCb = QCheckBox(
            QApplication.translate("Aebasecol", "Select All", None, 1),
            self.specFr)
        self.allCb.setGeometry(20, 10, 200, 21)
        self.line = QFrame(self.specFr)
        self.line.setGeometry(20, 36, 180, 2)
        self.line.setFrameShape(6)
        self.togglePb = QPushButton(self.aeFr)
        self.togglePb.setGeometry(280, 255, 80, 30)
        self.errFr = QFrame(Aebasecol)
        self.errFr.setGeometry(10, 10, 380, 340)
        self.errFr.setAutoFillBackground(True)
        self.errFr.setFrameShape(6)
        self.errFr.setFrameShadow(20)
        self.warnLb = QLabel(self.errFr)
        self.warnLb.setGeometry(10, 130, 40, 39)
        self.warnLb.setPixmap(QPixmap(":/images/warning.png"))
        self.errmsgLb = QLabel(self.errFr)
        self.errmsgLb.setGeometry(70, 69, 210, 175)
        self.errmsgLb.setWordWrap(True)
        self.confFr = QFrame(Aebasecol)
        self.confFr.setGeometry(10, 10, 380, 340)
        self.confFr.setAutoFillBackground(True)
        self.confFr.setFrameShape(6)
        self.confFr.setFrameShadow(20)
        self.qLb = QLabel(self.confFr)
        self.qLb.setGeometry(20, 148, 32, 32)
        self.qLb.setPixmap(QPixmap(":/images/question.png"))
        self.confmsgLb = QLabel(self.confFr)
        self.confmsgLb.setGeometry(79, 24, 261, 281)
        self.okPb = QPushButton(Aebasecol)
        self.okPb.setGeometry(70, 358, 80, 30)
        self.backPb = QPushButton(Aebasecol)
        self.backPb.setGeometry(160, 358, 80, 30)
        self.cancelPb = QPushButton(Aebasecol)
        self.cancelPb.setGeometry(250, 358, 80, 30)
        self.cancelPb.setAutoDefault(True)
        self.bcnameLb.setBuddy(self.bcnameLe)

        self.retranslateUi(Aebasecol)

    def retranslateUi(self, Aebasecol):
        Aebasecol.setWindowTitle(
            QApplication.translate(
                "Aebasecol", "GnuVet: Add Basecolour", None, 1))
        self.no_dbconn.setText(
            QApplication.translate("Aebasecol", "No db connection...", None, 1))
        self.bcnameLb.setText(
            QApplication.translate("Aebasecol", "BaseC&olour Name:", None, 1))
        self.okPb.setText(
            QApplication.translate("Aebasecol", "OK", None, 1))
        self.backPb.setText(
            QApplication.translate("Aebasecol", "Bac&k", None, 1))
        self.cancelPb.setText(
            QApplication.translate("Aebasecol", "Cancel", None, 1))
        self.cancelPb.setShortcut(
            QApplication.translate("Aebasecol", "Esc", None, 1))
        ## self.groupBox.setTitle(
        ##    _translate("Aebasecol", "Combinations with other 
        ## Basecolours", None))
        self.combLb.setText(
            QApplication.translate(
                "Aebasecol", "Combinations with other Basecolours:", None, 1))
        self.possRb.setText(
            QApplication.translate("Aebasecol", "&possible", None, 1))
        self.possRb.setToolTip(
            QApplication.translate(
                "Aebasecol", "This Basecolour can be combined with others",
                None, 1))
        self.possRb.setStatusTip(
            QApplication.translate(
                "Aebasecol", "Combination possible", None, 1))
        self.oblRb.setText(
            QApplication.translate("Aebasecol", "n&ecessary", None, 1))
        self.oblRb.setToolTip(
            QApplication.translate(
                "Aebasecol", "This Basecolour has to be combined with another",
                None, 1))
        self.oblRb.setStatusTip(
            QApplication.translate(
                "Aebasecol", "Combination required", None, 1))
        self.noRb.setText(
            QApplication.translate("Aebasecol", "&none", None, 1))
        self.noRb.setToolTip(
            QApplication.translate(
                "Aebasecol", "This Basecolour can not be combined with others",
                None, 1))
        self.noRb.setStatusTip(
            QApplication.translate("Aebasecol", "No combination possible",
                                   None, 1))
        self.specLb.setText(
            QApplication.translate(
                "Aebasecol",
                "Please select species for which new basecolour applies:",
                None, 1))
        self.togglePb.setText(
            QApplication.translate("Aebasecol", "Toggle &All", None, 1))

    def develf(self):
        if self.devels == 0:
            self.aeFr.hide()
            self.confFr.hide()
            self.errFr.show()
            self.devels = 1
        elif self.devels == 1:
            self.confFr.hide()
            self.errFr.hide()
            self.aeFr.show()
            self.devels = 2
        elif self.devels == 2:
            self.aeFr.hide()
            self.errFr.hide()
            self.confFr.show()
            self.devels = 0

if __name__ == '__main__':
    from PyQt4.QtGui import QAction, QApplication, QMainWindow, QShortcut
    a = QApplication([])
    a.setStyle('plastique')
    b = Ui_Aebasecol()
    w = QMainWindow()
    b.setupUi(w)
    develA = QAction(w)
    develA.setShortcut('Ctrl+D')
    develA.triggered.connect(b.develf)
    w.addAction(develA)
    QShortcut('Ctrl+Q', w, quit)
    b.cancelPb.clicked.connect(quit)
    w.show()
    exit(a.exec_())
