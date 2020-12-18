# -*- coding: utf-8 -*-
import re
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
            
        self.proekt_le.textEdited.connect(self.proektLe)

        self.menu = QtWidgets.QMenu()
        self.menu_up = QtWidgets.QAction('Вверх', self.menu)
        self.menu_up.triggered.connect(self.menuUpLv)
        self.menu_down = QtWidgets.QAction('Вниз', self.menu)
        self.menu_down.triggered.connect(self.menuDownLv)
        self.menu_del = QtWidgets.QAction('Удалить', self.menu)
        self.menu_del.triggered.connect(self.menuDelLv)
        self.menu_delall = QtWidgets.QAction('Удалить все', self.menu)
        self.menu_delall.triggered.connect(self.menuDelAllLv)
        self.menu.addAction(self.menu_up)
        self.menu.addAction(self.menu_down)
        self.menu.addSeparator()
        self.menu.addAction(self.menu_del)
        self.menu.addAction(self.menu_delall)

    def proektLe(self):
        t = self.proekt_le.text()
        p = re.compile(r'(?<=Н-)(\d{4})')
        m = p.search(t)
        if m:
            self.file_le.setText(m.group(0))

                
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
        if self.lvCalc.model():
            self.menu_up.setEnabled(True)
            self.menu_down.setEnabled(True)
            if self.lvCalc.selectedIndexes()[0].row() == 0:
                self.menu_up.setDisabled(True)
            if self.lvCalc.selectedIndexes()[0].row() == self.lvCalc.model().rowCount() - 1:
                self.menu_down.setDisabled(True)
            self.menu.exec(self.lvCalc.mapToGlobal(point))
   
    def menuUpLv(self):
        i = self.lvCalc.selectedIndexes()[0].row()
        data_word[i], data_word[i-1] = data_word[i-1], data_word[i]
        d = self.lvCalc.model().data(self.lvCalc.model().index(i), 0)
        d1 = self.lvCalc.model().data(self.lvCalc.model().index(i-1), 0)
        self.lvCalc.model().setData(self.lvCalc.model().index(i-1), d1)
        self.lvCalc.model().setData(self.lvCalc.model().index(i), d)
        del d, d1

    def menuDownLv(self):
        i = self.lvCalc.selectedIndexes()[0].row()
        data_word[i], data_word[i+1] = data_word[i+1], data_word[i]
        d = self.lvCalc.model().data(self.lvCalc.model().index(i), 0)
        d1 = self.lvCalc.model().data(self.lvCalc.model().index(i+1), 0)
        self.lvCalc.model().setData(self.lvCalc.model().index(i), d1)
        self.lvCalc.model().setData(self.lvCalc.model().index(i+1), d)
        del d, d1

    def menuDelLv(self):
        if self.lvCalc.model().rowCount() == 0:
            self.lvCalc.setModel(None)
            data_word.clear()

        data_word.pop(self.lvCalc.selectedIndexes()[0].row())
        self.lvCalc.model().removeRow(self.lvCalc.selectedIndexes()[0].row())



    def menuDelAllLv(self):
        data_word.clear()
        self.lvCalc.setModel(None)
        
        #self.lvCalc.rowsAboutToBeRemoved(0, self.lvCalc.rowCount())
        #word_lv.rowsAboutToBeRemoved(0)
        #self.lvCalc.setModel(word_lv)

    def makeWord(self):
        f = self.file_le.text() + '.docx'
        if os.path.isfile(f):
            try:
                with open(f,"r+") as fi:
                    fi.close()
            except IOError:
                dialog = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Error', f'закройте файл {f} и нажмите OK')
                result = dialog.exec()
        else:
            shutil.copy(r'temp.docx', f)
            if self.proekt_le.text() != '':
                doc = docx.Document(f)
                if doc.core_properties.subject != self.proekt_le.text() + 'РР':
                    doc.core_properties.subject = self.proekt_le.text() + ' РР'
                doc.save(f)
            
        self.pbMakeWord.setEnabled(False)
        for i in range(0, word_lv.rowCount()):
            if (data_word[i][0].met == 'obvn' or data_word[i][0].met == 'obnar') and data_word[i][0].yk == False:
                makeWord.makeWord_ob(data_word[i][0], data_word[i][1], f)
            elif (data_word[i][0].met == 'elvn' or data_word[i][0].met == 'elnar') and data_word[i][0].yk == False:
                makeWord.makeWord_el(data_word[i][0], data_word[i][1], f)
            elif data_word[i][0].met == 'konvn' and data_word[i][0].yk == False:
                pass
            elif data_word[i][0].met == 'konnar' and data_word[i][0].yk == False:
                pass
            elif (data_word[i][0].met == 'obvn' or data_word[i][0].met == 'obnar') and data_word[i][0].yk == True:
                makeWord.makeWord_obyk(data_word[i][0], data_word[i][1], data_word[i][2], data_word[i][3], f)
            elif (data_word[i][0].met == 'elvn' or  data_word[i][0].met == 'elnar') and data_word[i][0].yk == True:
                makeWord.makeWord_elyk(data_word[i][0], data_word[i][1], data_word[i][2], data_word[i][3], f)
            elif data_word[i][0].met == 'konvn' and data_word[i][0].yk == True:
                pass
            elif data_word[i][0].met == 'konnar' and data_word[i][0].yk == True:
                pass
            elif data_word[i][0].met == 'saddle':
                makeWord.makeWord_obsaddle(data_word[i][0], data_word[i][1], f)
            elif data_word[i][0].met == 'heat':
                makeWord.makeWord_heat()

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
