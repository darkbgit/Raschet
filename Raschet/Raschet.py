# -*- coding: utf-8 -*-
import shutil
import os
import json
import data_fiz
import CalcClass
import docx
import lxml
import makeWord
from PyQt5 import QtWidgets, uic, QtCore, QtGui, Qt
import sys
from Saddle import Saddle
from FormOb import FormOb
from FormEl import FormEl
from globalvar import data_word, word_lv



class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        #QtWidgets.QMainWindow.__init__(parent)
        super().__init__(parent)
        uic.loadUi('MainForm.ui', self)
        
        self.obWin = None
        self.obEl = None
        self.saddle = None
             
        
               
        self.pb_ob.clicked.connect(self.ob_show)
        self.pb_el.clicked.connect(self.el_show)
        
        self.pbMakeWord.clicked.connect(self.makeWord)

        self.pbSaddle.clicked.connect(self.saddle_show)

        
        #self.lvCalc.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.lvCalc.customContextMenuRequested.connect(self.context_lv)
                     

        self.action_about.triggered.connect(self.ShowAbout)
        self.action_close.triggered.connect(self.close)
            


                
    def ShowAbout(self):
        global windowabout
        windowabout = About()
        windowabout.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        windowabout.show()

    def ob_show(self):
        if not self.obWin:
            self.obWin = FormOb(self)
        self.obWin.setWindowModality(QtCore.Qt.WindowModal)
        self.obWin.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        self.obWin.show()

    def el_show(self):
        if not self.obEl:
            self.obEl = FormEl(self)
        self.obEl.setWindowModality(QtCore.Qt.WindowModal)
        self.obEl.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        self.obEl.show()

    def saddle_show(self):
        if not self.saddle:
            self.saddle = Saddle(self)
        self.saddle.setWindowModality(QtCore.Qt.WindowModal)
        self.saddle.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        self.saddle.show()


    def context_lv(self, point):
        #if lvCalc.
        menu = QtWidgets.QMenu()
        #menu_ac = QtWidgets.QAction('Vty.', menu)
        menu.addAction('Верх')
        menu.addAction('Вниз')
        menu.addSeparator()
        menu.addAction('Удалить')
        menu.exec(self.lvCalc.mapToGlobal(point))
   

    def makeWord(self):
        f = self.file_le.text() + '.docx'
        if os.path.isfile(f):
            pass
        else:
            shutil.copy(r'temp.docx', f)
            
        self.pbMakeWord.setEnabled(False)
        for i in range(0, word_lv.rowCount()):
            if data_word[i][0].met == 'obvn' and data_word[i][0].yk == False:
                makeWord.makeWord_obvn(data_word[i][0], data_word[i][1], f)
            elif data_word[i][0].met == 'obnar' and data_word[i][0].yk == False:
                makeWord.makeWord_obnar(data_word[i][0], data_word[i][1], f)
            elif data_word[i][0].met == 'elvn' and data_word[i][0].yk == False:
                makeWord.makeWord_elvn(data_word[i][0], data_word[i][1], f)
            elif data_word[i][0].met == 'elnar' and data_word[i][0].yk == False:
                makeWord.makeWord_elnar(data_word[i][0], data_word[i][1], f)
            elif data_word[i][0].met == 'konvn' and data_word[i][0].yk == False:
                pass
            elif data_word[i][0].met == 'konnar' and data_word[i][0].yk == False:
                pass
            elif data_word[i][0].met == 'obvn' and data_word[i][0].yk == True:
                makeWord.makeWord_obyk(data_word[i][0], data_word[i][1], data_word[i][2], data_word[i][3], f)
            elif data_word[i][0].met == 'obnar' and data_word[i][0].yk == True:
                makeWord.makeWord_obyk(data_word[i][0], data_word[i][1], data_word[i][2], data_word[i][3], f)
            elif data_word[i][0].met == 'elvn' and data_word[i][0].yk == True:
                makeWord.makeWord_elyk(data_word[i][0], data_word[i][1], data_word[i][2], data_word[i][3], f)
            elif data_word[i][0].met == 'elnar' and data_word[i][0].yk == True:
                makeWord.makeWord_elyk(data_word[i][0], data_word[i][1], data_word[i][2], data_word[i][3], f)
            elif data_word[i][0].met == 'konvn' and data_word[i][0].yk == True:
                pass
            elif data_word[i][0].met == 'konnar' and data_word[i][0].yk == True:
                pass
            elif data_word[i][0].met == 'saddle':
                makeWord.makeWord_obsaddle(data_word[i][0], data_word[i][1], f)

        self.pbMakeWord.setEnabled(True)
        dialog = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, 'Ok', 'Complite')
        result = dialog.exec()



class About(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        uic.loadUi('About.ui', self)



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    global mainwindow
    mainwindow = MyWindow()
    mainwindow.show()
    sys.exit(app.exec_())
