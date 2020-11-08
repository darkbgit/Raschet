# -*- coding: utf-8 -*-

import json
import data_fiz
import CalcClass
import docx
import lxml
import makeWord
from PyQt5 import QtWidgets, uic, QtCore
import sys

data_word = []
word_lv = QtCore.QStringListModel()

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        uic.loadUi('MainForm.ui', self)
        
        
        steelList = QtCore.QStringListModel()
        steelList.insertRows(0, len(data_fiz.sigma_list.keys()))
        i = 0
        for k in data_fiz.sigma_list.keys():
            steelList.setData(steelList.index(i), k)
            i = i + 1
        del i
        self.steel_cbov.setModel(steelList)
        self.steel_cbon.setModel(steelList)
        self.steel_cbev.setModel(steelList)
        self.steel_cben.setModel(steelList)
        
        self.pbPredov.clicked.connect(self.pred_calcov)
        self.pbPredon.clicked.connect(self.pred_calcon)
        self.pbPredev.clicked.connect(self.pred_calcev)
        

        self.pbCalcov.clicked.connect(self.calcov)
        self.pbCalcon.clicked.connect(self.calcon)
        #self.pbCalcev.clicked.connect(self.calcev)


        self.pbfiov.clicked.connect(self.fishow)

        self.pbMakeWord.clicked.connect(self.makeWord)

        self.pbHev.clicked.connect(self.elGOSTshow)



        #self.lvCalc.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.lvCalc.customContextMenuRequested.connect(self.context_lv)

        self.pbShowSxemaov.clicked.connect(self.ShowCalcSxemaOv)

    #def getHel(self):
    #    try:
    #       dia = dia_leev.text()

    def elGOSTshow(self):
        global windowgostel
        windowgostel = GostEl()
        windowgostel.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        windowgostel.show()

    def fishow(self):
        global windowfi
        windowfi = Fi()
        windowfi.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        windowfi.show()

    def ShowCalcSxemaOv(self):
        global windowcalc
        windowcalc = ObCalcSxema()
        windowcalc.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        windowcalc.show()


    def context_lv(self, point):
        #if lvCalc.
        menu = QtWidgets.QMenu()
        #menu_ac = QtWidgets.QAction('Vty.', menu)
        menu.addAction('Верх')
        menu.addAction('Вниз')
        menu.addSeparator()
        menu.addAction('Удалить')
        menu.exec(self.lvCalc.mapToGlobal(point))


    def pred_calcov(self):
        data_in = CalcClass.data_in() 
        data_out = CalcClass.data_out()
        data_in.dav = 'vn'
        data_inerr = str('')
        try:
            if int(self.temp_leov.text()) in range (20, 1000):
                data_in.temp = int(self.temp_leov.text())
            else:
                data_inerr = data_inerr + 'T должна быть в диапазоне 20 - 1000\n'
        except:
            data_inerr = data_inerr + 'T должна быть в диапазоне 20 - 1000\n'
        try:
            if float(self.press_leov.text()) > 0 and float(self.press_leov.text()) < 1000:
                data_in.press = float(self.press_leov.text())
            else:
                data_inerr = data_inerr + 'p должно быть в диапазоне 0 - 1000\n'
        except:
            data_inerr = data_inerr + 'p должно быть в диапазоне 0 - 1000\n'

        data_in.steel = self.steel_cbov.currentText()

        try:
            if float(self.fi_leov.text()) > 0 and float(self.fi_leov.text()) <= 1:
                data_in.fi = float(self.fi_leov.text())
            else:
                data_inerr = data_inerr + 'fi должен быть в диапазоне 0 - 1\n'
        except:
            data_inerr = data_inerr + 'fi должен быть в диапазоне 0 - 1\n'
        
        try:
            if int(self.dia_leov.text()) > 0:
                data_in.dia = int(self.dia_leov.text())
            else:
                data_inerr = data_inerr + 'D неверные данные\n'
        except:
            data_inerr = data_inerr + 'D неверные данные\n'

        try:
            if float(self.c1_leov.text()) >= 0:
                data_in.c_kor = float(self.c1_leov.text())
            else:
                data_inerr = data_inerr + 'c1 неверные данные\n'
        except:
            data_inerr = data_inerr + 'c1 неверные данные\n'

        try:
            if float(self.c2_leov.text()) >= 0:
                data_in.c_minus = float(self.c2_leov.text())
            else:
                data_inerr = data_inerr + 'c2 неверные данные\n'
        except:
            data_inerr = data_inerr + 'c2 неверные данные\n'
        
        if data_inerr == '':
            cc = CalcClass.CalcClass()
            self.sigma_leov.setReadOnly = False
            self.sigma_leov.setText(str(cc.get_sigma(data_in.steel, data_in.temp)))
            data_in.sigma_d = float(self.sigma_leov.text())#cc.get_sigma(data_in.steel, data_in.temp)#
            self.sigma_leov.setReadOnly = True
            data_out = cc.calc_ob(data_in)
            self.c_leov.setText(str(round(data_out.c, 2)))
            self.statusBar().showMessage(f'sp={data_out.s_calc:.3f} мм')
            self.s_calc_lov.setText(f'sp={data_out.s_calc:.3f} мм')
        else:
            dialog = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Error', data_inerr)
            result = dialog.exec()

    def pred_calcon(self):
        data_in = CalcClass.data_in()
        data_out = CalcClass.data_out()
        data_in.dav = 'nar'
        data_inerr = str('')
        try:
            if int(self.temp_leon.text()) in range (20, 1000):
                data_in.temp = int(self.temp_leon.text())
            else:
                data_inerr = data_inerr + 'T должна быть в диапазоне 20 - 1000\n'
        except:
            data_inerr = data_inerr + 'T должна быть в диапазоне 20 - 1000\n'
        try:
            if float(self.press_leon.text()) > 0 and float(self.press_leon.text()) < 1000:
                data_in.press = float(self.press_leon.text())
            else:
                data_inerr = data_inerr + 'p должно быть в диапазоне 0 - 1000\n'
        except:
            data_inerr = data_inerr + 'p должно быть в диапазоне 0 - 1000\n'

        data_in.steel = self.steel_cbon.currentText()

        try:
            if float(self.fi_leon.text()) > 0 and float(self.fi_leon.text()) <= 1:
                data_in.fi = float(self.fi_leon.text())
            else:
                data_inerr = data_inerr + 'fi должен быть в диапазоне 0 - 1\n'
        except:
            data_inerr = data_inerr + 'fi должен быть в диапазоне 0 - 1\n'
        
        try:
            if int(self.dia_leon.text()) > 0:
                data_in.dia = int(self.dia_leon.text())
            else:
                data_inerr = data_inerr + 'D неверные данные\n'
        except:
            data_inerr = data_inerr + 'D неверные данные\n'

        try:
            if float(self.c1_leon.text()) >= 0:
                data_in.c_kor = float(self.c1_leon.text())
            else:
                data_inerr = data_inerr + 'c1 неверные данные\n'
        except:
            data_inerr = data_inerr + 'c1 неверные данные\n'

        try:
            if float(self.c2_leon.text()) >= 0:
                data_in.c_minus = float(self.c2_leon.text())
            else:
                data_inerr = data_inerr + 'c2 неверные данные\n'
        except:
            data_inerr = data_inerr + 'c2 неверные данные\n'
        
        try:
            if float(self.l_leon.text()) >= 0:
                data_in.l = float(self.l_leon.text())
            else:
                data_inerr = data_inerr + 'l неверные данные\n'
        except:
            data_inerr = data_inerr + 'l неверные данные\n'


        if data_inerr == '':
            cc = CalcClass.CalcClass()
            self.sigma_leon.setReadOnly = False
            self.sigma_leon.setText(str(cc.get_sigma(data_in.steel, data_in.temp)))
            data_in.sigma_d = float(self.sigma_leon.text())#cc.get_sigma(data_in.steel, data_in.temp)#
            self.sigma_leon.setReadOnly = True
            self.E_leon.setReadOnly = False
            self.E_leon.setText(str(cc.get_E('Carbon', data_in.temp)))
            data_in.E = float(self.E_leon.text())#cc.get_sigma(data_in.steel, data_in.temp)#
            self.E_leon.setReadOnly = True
            data_out = cc.calc_ob(data_in)
            self.c_leon.setText(str(round(data_out.c, 2)))
            self.statusBar().showMessage(f'sp={data_out.s_calc:.3f} мм')
            self.s_calc_lon.setText(f'sp={data_out.s_calc:.3f} мм')
        else:
            dialog = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Error', data_inerr)
            result = dialog.exec()

    def pred_calcev(self):
        data_in = CalcClass.data_in() 
        data_out = CalcClass.data_out()
        data_in.dav = 'vn'
        data_inerr = str('')
        try:
            if int(self.temp_leev.text()) in range (20, 1000):
                data_in.temp = int(self.temp_leev.text())
            else:
                data_inerr = data_inerr + 'T должна быть в диапазоне 20 - 1000\n'
        except:
            data_inerr = data_inerr + 'T должна быть в диапазоне 20 - 1000\n'
        try:
            if float(self.press_leev.text()) > 0 and float(self.press_leev.text()) < 1000:
                data_in.press = float(self.press_leev.text())
            else:
                data_inerr = data_inerr + 'p должно быть в диапазоне 0 - 1000\n'
        except:
            data_inerr = data_inerr + 'p должно быть в диапазоне 0 - 1000\n'

        data_in.steel = self.steel_cbev.currentText()

        try:
            if float(self.fi_leev.text()) > 0 and float(self.fi_leev.text()) <= 1:
                data_in.fi = float(self.fi_leev.text())
            else:
                data_inerr = data_inerr + 'fi должен быть в диапазоне 0 - 1\n'
        except:
            data_inerr = data_inerr + 'fi должен быть в диапазоне 0 - 1\n'
        
        try:
            if int(self.dia_leev.text()) > 0:
                data_in.dia = int(self.dia_leev.text())
            else:
                data_inerr = data_inerr + 'D неверные данные\n'
        except:
            data_inerr = data_inerr + 'D неверные данные\n'

        try:
            if float(self.c1_leev.text()) >= 0:
                data_in.c_kor = float(self.c1_leev.text())
            else:
                data_inerr = data_inerr + 'c1 неверные данные\n'
        except:
            data_inerr = data_inerr + 'c1 неверные данные\n'

        try:
            if float(self.c2_leev.text()) >= 0:
                data_in.c_minus = float(self.c2_leev.text())
            else:
                data_inerr = data_inerr + 'c2 неверные данные\n'
        except:
            data_inerr = data_inerr + 'c2 неверные данные\n'
        
        if data_inerr == '':
            cc = CalcClass.CalcClass()
            self.sigma_leev.setReadOnly = False
            self.sigma_leev.setText(str(cc.get_sigma(data_in.steel, data_in.temp)))
            data_in.sigma_d = float(self.sigma_leev.text())#cc.get_sigma(data_in.steel, data_in.temp)#
            self.sigma_leev.setReadOnly = True
            data_out = cc.calc_el(data_in)
            self.c_leev.setText(str(round(data_out.c, 2)))
            self.statusBar().showMessage(f'sp={data_out.s_calc:.3f} мм')
            self.s_calc_lev.setText(f'sp={data_out.s_calc:.3f} мм')
        else:
            dialog = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Error', data_inerr)
            result = dialog.exec()


    def calcov(self):
        data_in = CalcClass.data_in()
        data_out = CalcClass.data_out()
        data_in.met = 'obvn'
        data_inerr = str('')
        
        data_in.name = self.name_leov.text()
        try:
            if int(self.temp_leov.text()) in range (20, 1000):
                data_in.temp = int(self.temp_leov.text())
            else:
                data_inerr = data_inerr + 'T должна быть в диапазоне 20 - 1000\n'
        except:
            data_inerr = data_inerr + 'T должна быть в диапазоне 20 - 1000\n'
        try:
            if float(self.press_leov.text()) > 0 and float(self.press_leov.text()) < 1000:
                data_in.press = float(self.press_leov.text())
            else:
                data_inerr = data_inerr + 'p должно быть в диапазоне 0 - 1000\n'
        except:
            data_inerr = data_inerr + 'p должно быть в диапазоне 0 - 1000\n'

        data_in.steel = self.steel_cbov.currentText()

        try:
            data_in.sigma_d = float(self.sigma_leov.text())
        except:
            data_inerr = data_inerr + '[σ] неверные данные\n'

        try:
            if float(self.fi_leov.text()) > 0 and float(self.fi_leov.text()) <= 1:
                data_in.fi = float(self.fi_leov.text())
            else:
                data_inerr = data_inerr + 'fi должен быть в диапазоне 0 - 1\n'
        except:
            data_inerr = data_inerr + 'fi должен быть в диапазоне 0 - 1\n'
        
        try:
            if int(self.dia_leov.text()) > 0:
                data_in.dia = int(self.dia_leov.text())
            else:
                data_inerr = data_inerr + 'D неверные данные\n'
        except:
            data_inerr = data_inerr + 'D неверные данные\n'

        try:
            if float(self.c1_leov.text()) >= 0:
                data_in.c_kor = float(self.c1_leov.text())
            else:
                data_inerr = data_inerr + 'c1 неверные данные\n'
        except:
            data_inerr = data_inerr + 'c1 неверные данные\n'

        try:
            if float(self.c2_leov.text()) >= 0:
                data_in.c_minus = float(self.c2_leov.text())
            else:
                data_inerr = data_inerr + 'c2 неверные данные\n'
        except:
            data_inerr = data_inerr + 'c2 неверные данные\n'

        
        
        if data_inerr == '':
            cc = CalcClass.CalcClass()
            data_out = cc.calc_ob(data_in)
            try:
                if float(self.s_leov.text()) >= data_out.s_calc:
                    data_in.s_prin = float(self.s_leov.text())
                    data_out = cc.calc_ob(data_in)
                    data_word.append([data_in, data_out])
                    i = word_lv.rowCount()
                    word_lv.insertRow(i)
                    word_lv.setData(word_lv.index(i),f'{data_in.dia} мм, {data_in.press} МПа, {data_in.temp} C, {data_in.met}')
                    self.lvCalc.setModel(word_lv)

                    self.statusBar().showMessage(f'sp={data_out.s_calc:.3f} мм, [p]={data_out.press_d:.3f} МПа')
                    self.s_calc_lov.setText(f'sp={data_out.s_calc:.3f} мм')
                    self.press_d_lov.setText(f'[p]={data_out.press_d:.3f} МПа')
                else:
                    dialog = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Error', 's должно быть больше или равно sp')
                    result = dialog.exec()
            except:
                self.statusBar().showMessage('')
                dialog = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Error', 's неверные данные')
                result = dialog.exec()
            
        else:
            dialog = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Error', data_inerr)
            result = dialog.exec()

    def calcon(self):
        data_in = CalcClass.data_in()
        data_out = CalcClass.data_out()
        data_in.dav = 'nar'
        data_in.met = 'obnar'
        data_inerr = str('')
        
        data_in.name = self.name_leon.text()
        try:
            if int(self.temp_leon.text()) in range (20, 1000):
                data_in.temp = int(self.temp_leon.text())
            else:
                data_inerr = data_inerr + 'T должна быть в диапазоне 20 - 1000\n'
        except:
            data_inerr = data_inerr + 'T должна быть в диапазоне 20 - 1000\n'
        try:
            if float(self.press_leon.text()) > 0 and float(self.press_leon.text()) < 1000:
                data_in.press = float(self.press_leon.text())
            else:
                data_inerr = data_inerr + 'p должно быть в диапазоне 0 - 1000\n'
        except:
            data_inerr = data_inerr + 'p должно быть в диапазоне 0 - 1000\n'

        data_in.steel = self.steel_cbon.currentText()

        try:
            data_in.sigma_d = float(self.sigma_leon.text())
        except:
            data_inerr = data_inerr + '[σ] неверные данные\n'

        try:
            data_in.E = float(self.E_leon.text())
        except:
            data_inerr = data_inerr + 'E неверные данные\n'

        try:
            if float(self.fi_leon.text()) > 0 and float(self.fi_leon.text()) <= 1:
                data_in.fi = float(self.fi_leon.text())
            else:
                data_inerr = data_inerr + 'fi должен быть в диапазоне 0 - 1\n'
        except:
            data_inerr = data_inerr + 'fi должен быть в диапазоне 0 - 1\n'
        
        try:
            if int(self.dia_leon.text()) > 0:
                data_in.dia = int(self.dia_leon.text())
            else:
                data_inerr = data_inerr + 'D неверные данные\n'
        except:
            data_inerr = data_inerr + 'D неверные данные\n'

        try:
            if float(self.c1_leon.text()) >= 0:
                data_in.c_kor = float(self.c1_leon.text())
            else:
                data_inerr = data_inerr + 'c1 неверные данные\n'
        except:
            data_inerr = data_inerr + 'c1 неверные данные\n'

        try:
            if float(self.c2_leon.text()) >= 0:
                data_in.c_minus = float(self.c2_leon.text())
            else:
                data_inerr = data_inerr + 'c2 неверные данные\n'
        except:
            data_inerr = data_inerr + 'c2 неверные данные\n'

        try:
            if float(self.l_leon.text()) >= 0:
                data_in.l = float(self.l_leon.text())
            else:
                data_inerr = data_inerr + 'l неверные данные\n'
        except:
            data_inerr = data_inerr + 'l неверные данные\n'

        
        
        if data_inerr == '':
            cc = CalcClass.CalcClass()
            data_out = cc.calc_ob(data_in)
            try:
                if float(self.s_leon.text()) >= data_out.s_calc:
                    data_in.s_prin = float(self.s_leon.text())
                    data_out = cc.calc_ob(data_in)
                    data_word.append([data_in, data_out])
                    i = word_lv.rowCount()
                    word_lv.insertRow(i)
                    word_lv.setData(word_lv.index(i),f'{data_in.dia} мм, {data_in.press} МПа, {data_in.temp} C, {data_in.met}')
                    self.lvCalc.setModel(word_lv)

                    self.statusBar().showMessage(f'sp={data_out.s_calc:.3f} мм, [p]={data_out.press_d:.3f} МПа')
                    self.s_calc_lon.setText(f'sp={data_out.s_calc:.3f} мм')
                    self.press_d_lon.setText(f'[p]={data_out.press_d:.3f} МПа')
                else:
                    dialog = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Error', 's должно быть больше или равно sp')
                    result = dialog.exec()
            except:
                self.statusBar().showMessage('')
                dialog = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Error', 's неверные данные')
                result = dialog.exec()
            
        else:
            dialog = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Error', data_inerr)
            result = dialog.exec()



    def makeWord(self):
        self.pbMakeWord.setEnabled(False)
        for i in range(0, word_lv.rowCount()):
            if data_word[i][0].met == 'obvn':
                makeWord.makeWord_obvn(data_word[i][0], data_word[i][1], '1.docx')
            elif data_word[i][0].met == 'obnar':
                makeWord.makeWord_obnar(data_word[i][0], data_word[i][1], '1.docx')
            elif data_word[i][0].met == 'elvn':
                pass
            elif data_word[i][0].met == 'elnar':
                pass
            elif data_word[i][0].met == 'konvn':
                pass
            elif data_word[i][0].met == 'konnar':
                pass

        self.pbMakeWord.setEnabled(True)


class ObCalcSxema(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        uic.loadUi('obvn.ui', self)

class Fi(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        uic.loadUi('FiForm.ui', self)
    
class GostEl(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        uic.loadUi('GostEl.ui', self)

        diaList = QtCore.QStringListModel()
        diaList.insertRows(0, len(data_fiz.el025_list.keys()))
        i = 0
        for k in data_fiz.el025_list.keys():
            diaList.setData(diaList.index(i), k)
            i += 1
        del i
        self.diagostel_cb.setModel(diaList)
        self.diagostel_cb.currentIndexChanged.connect(self.diachange)
        self.sgostel_cb.currentIndexChanged.connect(self.schange)

         
    #    self.pbGostElOK.connect(self.getdata_el)

    #def getdata_el(self):

    def diachange(self):
        sList = QtCore.QStringListModel()
        if data_fiz.el025_list[self.diagostel_cb.currentText()][-1] == 'a':
            sList.insertRows(0, len(data_fiz.el025_list[self.diagostel_cb.currentText()]) - 2)
            i = 0
            for k in data_fiz.el025_list[self.diagostel_cb.currentText()]:
                if type(k) == int:
                    sList.setData(sList.index(i), k)
                    i += 1
            del i
        else:
            sList.insertRows(0, len(data_fiz.el025_list[self.diagostel_cb.currentText()]) - 2 - len(data_fiz.el025_list[self.diagostel_cb.currentText()][-1].split('-')))
            i = 0
            for k in data_fiz.el025_list[self.diagostel_cb.currentText()]:
                if type(k) == int:
                    sList.setData(sList.index(i), k)
                    i += 1
            del i

        self.sgostel_cb.setModel(sList)


    def schange(self):
        if data_fiz.el025_list[self.diagostel_cb.currentText()][-1] == 'a':
            H = data_fiz.el025_list[self.diagostel_cb.currentText()][-2][1]
            h1 = data_fiz.el025_list[self.diagostel_cb.currentText()][-2][0]
        else:
            ind =  data_fiz.el025_list[self.diagostel_cb.currentText()].index(int(self.sgostel_cb.currentText()))

            if ind >= int(data_fiz.el025_list[self.diagostel_cb.currentText()][-1].split('-')[-1]):
                H = data_fiz.el025_list[self.diagostel_cb.currentText()][-2][1]
                h1 = data_fiz.el025_list[self.diagostel_cb.currentText()][-2][0]
            elif ind >= int(data_fiz.el025_list[self.diagostel_cb.currentText()][-1].split('-')[-2]) or len(data_fiz.el025_list[self.diagostel_cb.currentText()][-1].split('-')) == 1:
                H = data_fiz.el025_list[self.diagostel_cb.currentText()][-3][1]
                h1 = data_fiz.el025_list[self.diagostel_cb.currentText()][-3][0]
            elif ind >= int(data_fiz.el025_list[self.diagostel_cb.currentText()][-1].split('-')[-3]) or len(data_fiz.el025_list[self.diagostel_cb.currentText()][-1].split('-')) == 2:
                H = data_fiz.el025_list[self.diagostel_cb.currentText()][-4][1]
                h1 = data_fiz.el025_list[self.diagostel_cb.currentText()][-4][0]
            else:
                H =''
                h1 = ''

        self.Hgostel_le.setText(str(H))
        self.h1gostel_le.setText(str(h1))

        



        #st = QtCore.QStringListModel()
        #st.insertRow(0)

        #st.setData(st.index(0), data_in.temp)
        #self.lvCalc.setModel(st)

    #return super().__init__(parent=parent, flags=flags)




   

def main():
    cc = CalcClass.CalcClass()
    #st = input('Steel:')
    #temp = int(input('Temp:'))
    #dop1 = input('Dop1:')
    #dop2 = input('Dop2:')
    data_in = CalcClass.data_in()
    data_in.name = '000-000000-Н-0000.00.00'
    data_in.steel = 'Ст3'
    data_in.press = 0.8
    data_in.temp = 200
    data_in.sigma_d = cc.get_sigma(data_in.steel, data_in.temp)
    data_in.E = cc.get_E('Carbon', data_in.temp)
    data_in.dia = 1200
    data_in.c_kor = 2.0
    data_in.c_minus = 0.8
    data_in.fi = 1.0
    data_in.s_prin = 11.0
    data_in.dav = 'nar'
    data_in.c_kor = 2.0
    data_in.l = 1000

    data_out = CalcClass.data_out()
         
    data_out = cc.calc_ob(data_in)

    makeWord.makeWord_obnar(data_in, data_out, 'temp.docx')


   #formula = lxml.etree._Element.makeelement(_tag='{http://schemas.openxmlformats.org/officeDocument/2006/math}oMathPara', attrib= )
   # formula = lxml.etree._Element('<m:oMathPara><m:oMath><m:sSub><m:sSubPr><m:ctrlPr><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/><w:i/></w:rPr></m:ctrlPr></m:sSubPr><m:e><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>s</m:t></m:r></m:e><m:sub><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>p</m:t></m:r></m:sub></m:sSub><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>=</m:t></m:r><m:f><m:fPr><m:ctrlPr><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/><w:i/></w:rPr></m:ctrlPr></m:fPr><m:num><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>pD</m:t></m:r></m:num><m:den><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>p-d</m:t></m:r></m:den></m:f></m:oMath></m:oMathPara>')
   # formyla = '<m:oMathPara><m:oMath><m:sSub><m:sSubPr><m:ctrlPr><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/><w:i/></w:rPr></m:ctrlPr></m:sSubPr><m:e><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>s</m:t></m:r></m:e><m:sub><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>p</m:t></m:r></m:sub></m:sSub><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>=</m:t></m:r><m:f><m:fPr><m:ctrlPr><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/><w:i/></w:rPr></m:ctrlPr></m:fPr><m:num><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>pD</m:t></m:r></m:num><m:den><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/></w:rPr><m:t>p-d</m:t></m:r></m:den></m:f></m:oMath></m:oMathPara>'
   # doc.add_paragraph()._element.append(formula)
    
    
    #paragraph_format = paragraph.paragraph_format

    #paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    #paragraph_format.alignment
    #d = docx.Document("f.docx")

    #new_doc = docx.Document()
    #new_para = new_doc.add_paragraph()
    #new_para_elem = new_para._element

    #para_with_formula = d.paragraphs[0]

    ## Это уже объект типа CT_P, родителем которого является lxml.Element
    #elem = para_with_formula._element
    ## Пространство имен `m` xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math"
    #tmp_ns = {"m": "http://schemas.openxmlformats.org/officeDocument/2006/math"}

    #math_tag_with_namespace = "{" + tmp_ns["m"] + "}oMathPara"

    #for p in d.paragraphs:
    #    print(p.text())

    #for i in elem.getiterator():
        
       
    #    if i.tag == math_tag_with_namespace:
    #        print(i.nsmap)
    #        for b in i.tag:
    #            print(i.tag)
    #        print(i.tag)
    #        print("OH! A formula!")
    #        new_para_elem.append(i)
    #        #doc.add_paragraph()._element.append(i)

    #new_doc.save("NEW_DOC.docx")

    #doc.add_paragraph()._element.append
    #doc.save('2.docx')





if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
