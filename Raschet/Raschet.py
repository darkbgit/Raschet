# -*- coding: utf-8 -*-

import json
import data_fiz
import CalcClass
import docx
import lxml
import makeWord
from PyQt5 import QtWidgets, uic, QtCore, QtGui, Qt
import sys
from FormOb import FormOb
from FormEl import FormEl
from globalvar import data_word, word_lv



##global data_word
#data_word = []
#global word_lv
#word_lv = QtCore.QStringListModel()

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        #QtWidgets.QMainWindow.__init__(parent)
        super().__init__(parent)
        uic.loadUi('MainForm.ui', self)
        
        self.obWin = None
        self.obEl = None
        
              
        self.steel_cbob.setModel(data_fiz.steelList)
        self.steel_cbel.setModel(data_fiz.steelList)
        self.steel_cbobyk.setModel(data_fiz.steelList)
        
        
        self.pbPredob.clicked.connect(self.pred_calcob)
        self.pbPredel.clicked.connect(self.pred_calcel)

        self.pb_ob.clicked.connect(self.ob_show)
        self.pb_el.clicked.connect(self.el_show)
        

        self.pbCalcob.clicked.connect(self.calcob)
        self.pbCalcel.clicked.connect(self.calcel)


        self.pbfiob.clicked.connect(self.fishow)
        self.pbfiel.clicked.connect(self.fishow)

        self.pbMakeWord.clicked.connect(self.makeWord)

        self.pbHel.clicked.connect(self.ShowGOSTel)

        self.vn_rbob.toggled.connect(self.vnnarob)
        self.vn_rbobyk.toggled.connect(self.vnnarobyk)
        self.vn_rbel.toggled.connect(self.vnnarel)

        self.obykrb_1.toggled.connect(self.ykobrb)
        self.obykrb_2.toggled.connect(self.ykobrb)
        self.obykrb_3.toggled.connect(self.ykobrb)
        self.obykrb_4.toggled.connect(self.ykobrb)
        self.obykrb_5.toggled.connect(self.ykobrb)
        self.obykrb_6.toggled.connect(self.ykobrb)
        self.obykrb_7.toggled.connect(self.ykobrb)
        self.obykrb_8.toggled.connect(self.ykobrb)

        #self.verticalLayout.clicked.connect(self.ykobrb)


        #self.lvCalc.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.lvCalc.customContextMenuRequested.connect(self.context_lv)

        
        self.pbShowSxemael.clicked.connect(self.ShowCalcSxemaEl)

        self.action_about.triggered.connect(self.ShowAbout)
        self.action_close.triggered.connect(self.close)

        self.pbobtoobyk.clicked.connect(self.obtoobyk)

    #def getHel(self):
    #    try:
    #       dia = dia_leev.text()

    def obtoobyk(self):
        self.name_leobyk.setText(self.name_leob.text())
        self.temp_leobyk.setText(self.temp_leob.text())
        self.press_leobyk.setText(self.press_leob.text())
        if self.vn_rbob.isChecked() == True:
            self.vn_rbobyk.toggle()
        else:
            self.nar_rbobyk.toggle()
        self.tabWidget.setCurrentIndex(1)

    def vnnarob(self):
        if self.vn_rbob.isChecked() == True:
            self.E_leob.setEnabled(False)
            self.pbGetEob.setEnabled(False)
            self.l_leob.setEnabled(False)
            self.pbGetlob.setEnabled(False)
        else:
            self.E_leob.setEnabled(True)
            self.pbGetEob.setEnabled(True)
            self.l_leob.setEnabled(True)
            self.pbGetlob.setEnabled(True)

    def vnnarobyk(self):
        if self.vn_rbobyk.isChecked() == True:
            self.E_leobyk.setEnabled(False)
            self.pbGetEobyk.setEnabled(False)
            self.l_leobyk.setEnabled(False)
            self.pbGetlobyk.setEnabled(False)
        else:
            self.E_leobyk.setEnabled(True)
            self.pbGetEobyk.setEnabled(True)
            self.l_leobyk.setEnabled(True)
            self.pbGetlobyk.setEnabled(True)

    def ykobrb(self, sender):
        s = self.sender().text() 
        if self.sender().isChecked():
            self.yk_leob.setPixmap(QtGui.QPixmap('pic/Nozzle/Nozzle' + s[0]))
                
    def vnnarel(self):
        if self.vn_rbel.isChecked() == True:
            self.E_leel.setEnabled(False)
            self.pbGetEel.setEnabled(False)
        else:
            self.E_leel.setEnabled(True)
            self.pbGetEel.setEnabled(True)
            
        
    
    def ShowGOSTel(self):
        global windowgostel
        windowgostel = GostEl()
        windowgostel.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        windowgostel.show()

    def fishow(self):
        global windowfi
        windowfi = Fi()
        windowfi.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        windowfi.show()

    

    def ShowCalcSxemaEl(self):
        global windowcalcel
        windowcalcel = ElCalcSxema()
        windowcalcel.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        windowcalcel.show()

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



    def context_lv(self, point):
        #if lvCalc.
        menu = QtWidgets.QMenu()
        #menu_ac = QtWidgets.QAction('Vty.', menu)
        menu.addAction('Верх')
        menu.addAction('Вниз')
        menu.addSeparator()
        menu.addAction('Удалить')
        menu.exec(self.lvCalc.mapToGlobal(point))

    def pred_calcob(self):
        if self.vn_rbob.isChecked() == True:
            self.pred_calcov()
        else:
            self.pred_calcon()

    def pred_calcov(self):
        data_in = CalcClass.data_in() 
        data_out = CalcClass.data_out()
        data_in.dav = 'vn'
        data_inerr = str('')
        try:
            if int(self.temp_leob.text()) in range (20, 1000):
                data_in.temp = int(self.temp_leob.text())
            else:
                data_inerr = data_inerr + 'T должна быть в диапазоне 20 - 1000\n'
        except:
            data_inerr = data_inerr + 'T должна быть в диапазоне 20 - 1000\n'
        try:
            if float(self.press_leob.text()) > 0 and float(self.press_leob.text()) < 1000:
                data_in.press = float(self.press_leob.text())
            else:
                data_inerr = data_inerr + 'p должно быть в диапазоне 0 - 1000\n'
        except:
            data_inerr = data_inerr + 'p должно быть в диапазоне 0 - 1000\n'

        data_in.steel = self.steel_cbob.currentText()

        try:
            if float(self.fi_leob.text()) > 0 and float(self.fi_leob.text()) <= 1:
                data_in.fi = float(self.fi_leob.text())
            else:
                data_inerr = data_inerr + 'fi должен быть в диапазоне 0 - 1\n'
        except:
            data_inerr = data_inerr + 'fi должен быть в диапазоне 0 - 1\n'
        
        try:
            if int(self.dia_leob.text()) > 0:
                data_in.dia = int(self.dia_leob.text())
            else:
                data_inerr = data_inerr + 'D неверные данные\n'
        except:
            data_inerr = data_inerr + 'D неверные данные\n'

        try:
            if float(self.c1_leob.text()) >= 0:
                data_in.c_kor = float(self.c1_leob.text())
            else:
                data_inerr = data_inerr + 'c1 неверные данные\n'
        except:
            data_inerr = data_inerr + 'c1 неверные данные\n'

        try:
            if float(self.c2_leob.text()) >= 0:
                data_in.c_minus = float(self.c2_leob.text())
            else:
                data_inerr = data_inerr + 'c2 неверные данные\n'
        except:
            data_inerr = data_inerr + 'c2 неверные данные\n'
        
        if data_inerr == '':
            cc = CalcClass.CalcClass()
            self.sigma_leob.setReadOnly = False
            self.sigma_leob.setText(str(cc.get_sigma(data_in.steel, data_in.temp)))
            data_in.sigma_d = float(self.sigma_leob.text())#cc.get_sigma(data_in.steel, data_in.temp)#
            self.sigma_leob.setReadOnly = True
            data_out = cc.calc_ob(data_in)
            self.c_leob.setText(str(round(data_out.c, 2)))
            self.statusBar().showMessage(f'sp={data_out.s_calc:.3f} мм')
            self.s_calc_lob.setText(f'sp={data_out.s_calc:.3f} мм')
        else:
            dialog = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Error', data_inerr)
            result = dialog.exec()

    def pred_calcon(self):
        data_in = CalcClass.data_in()
        data_out = CalcClass.data_out()
        data_in.dav = 'nar'
        data_inerr = str('')
        try:
            if int(self.temp_leob.text()) in range (20, 1000):
                data_in.temp = int(self.temp_leob.text())
            else:
                data_inerr = data_inerr + 'T должна быть в диапазоне 20 - 1000\n'
        except:
            data_inerr = data_inerr + 'T должна быть в диапазоне 20 - 1000\n'
        try:
            if float(self.press_leob.text()) > 0 and float(self.press_leob.text()) < 1000:
                data_in.press = float(self.press_leob.text())
            else:
                data_inerr = data_inerr + 'p должно быть в диапазоне 0 - 1000\n'
        except:
            data_inerr = data_inerr + 'p должно быть в диапазоне 0 - 1000\n'

        data_in.steel = self.steel_cbob.currentText()

        try:
            if float(self.fi_leob.text()) > 0 and float(self.fi_leob.text()) <= 1:
                data_in.fi = float(self.fi_leob.text())
            else:
                data_inerr = data_inerr + 'fi должен быть в диапазоне 0 - 1\n'
        except:
            data_inerr = data_inerr + 'fi должен быть в диапазоне 0 - 1\n'
        
        try:
            if int(self.dia_leob.text()) > 0:
                data_in.dia = int(self.dia_leob.text())
            else:
                data_inerr = data_inerr + 'D неверные данные\n'
        except:
            data_inerr = data_inerr + 'D неверные данные\n'

        try:
            if float(self.c1_leob.text()) >= 0:
                data_in.c_kor = float(self.c1_leob.text())
            else:
                data_inerr = data_inerr + 'c1 неверные данные\n'
        except:
            data_inerr = data_inerr + 'c1 неверные данные\n'

        try:
            if float(self.c2_leob.text()) >= 0:
                data_in.c_minus = float(self.c2_leob.text())
            else:
                data_inerr = data_inerr + 'c2 неверные данные\n'
        except:
            data_inerr = data_inerr + 'c2 неверные данные\n'
        
        try:
            if float(self.l_leob.text()) >= 0:
                data_in.l = float(self.l_leob.text())
            else:
                data_inerr = data_inerr + 'l неверные данные\n'
        except:
            data_inerr = data_inerr + 'l неверные данные\n'


        if data_inerr == '':
            cc = CalcClass.CalcClass()
            self.sigma_leob.setReadOnly = False
            self.sigma_leob.setText(str(cc.get_sigma(data_in.steel, data_in.temp)))
            data_in.sigma_d = float(self.sigma_leob.text())#cc.get_sigma(data_in.steel, data_in.temp)#
            self.sigma_leob.setReadOnly = True
            self.E_leob.setReadOnly = False
            self.E_leob.setText(str(cc.get_E('Carbon', data_in.temp)))
            data_in.E = float(self.E_leob.text())#cc.get_sigma(data_in.steel, data_in.temp)#
            self.E_leob.setReadOnly = True
            data_out = cc.calc_ob(data_in)
            self.c_leob.setText(str(round(data_out.c, 2)))
            self.statusBar().showMessage(f'sp={data_out.s_calc:.3f} мм')
            self.s_calc_lob.setText(f'sp={data_out.s_calc:.3f} мм')
        else:
            dialog = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Error', data_inerr)
            result = dialog.exec()

    

    def pred_calcel(self):
        data_in = CalcClass.data_in() 
        data_out = CalcClass.data_out()

        cc = CalcClass.CalcClass()

                
        data_inerr = str('')

        try:
            if int(self.temp_leel.text()) in range (20, 1000):
                data_in.temp = int(self.temp_leel.text())
            else:
                data_inerr = data_inerr + 'T должна быть в диапазоне 20 - 1000\n'
        except:
            data_inerr = data_inerr + 'T должна быть в диапазоне 20 - 1000\n'
        try:
            if float(self.press_leel.text()) > 0 and float(self.press_leel.text()) < 1000:
                data_in.press = float(self.press_leel.text())
            else:
                data_inerr = data_inerr + 'p должно быть в диапазоне 0 - 1000\n'
        except:
            data_inerr = data_inerr + 'p должно быть в диапазоне 0 - 1000\n'

        data_in.steel = self.steel_cbel.currentText()

        if self.vn_rbel.isChecked() == True:
            data_in.dav = 'vn'
        else:
            data_in.dav = 'nar'
            self.E_leel.setReadOnly = False
            self.E_leel.setText(str(cc.get_E('Carbon', data_in.temp)))
            data_in.E = float(self.E_leel.text())#cc.get_sigma(data_in.steel, data_in.temp)#
            self.E_leel.setReadOnly = True
            try:
                data_in.E = float(self.E_leel.text())
            except:
                data_inerr = data_inerr + 'E неверные данные\n'

        try:
            if float(self.fi_leel.text()) > 0 and float(self.fi_leel.text()) <= 1:
                data_in.fi = float(self.fi_leel.text())
            else:
                data_inerr = data_inerr + 'fi должен быть в диапазоне 0 - 1\n'
        except:
            data_inerr = data_inerr + 'fi должен быть в диапазоне 0 - 1\n'
        
        try:
            if int(self.dia_leel.text()) > 0:
                data_in.dia = int(self.dia_leel.text())
            else:
                data_inerr = data_inerr + 'D неверные данные\n'
        except:
            data_inerr = data_inerr + 'D неверные данные\n'

        try:
            if int(self.H_leel.text()) > 0:
                data_in.elH = int(self.H_leel.text())
            else:
                data_inerr = data_inerr + 'H неверные данные\n'
        except:
            data_inerr = data_inerr + 'H неверные данные\n'

        try:
            if int(self.h1_leel.text()) > 0:
                data_in.elh1 = int(self.h1_leel.text())
            else:
                data_inerr = data_inerr + 'h1 неверные данные\n'
        except:
            data_inerr = data_inerr + 'h1 неверные данные\n'

        try:
            if float(self.c1_leel.text()) >= 0:
                data_in.c_kor = float(self.c1_leel.text())
            else:
                data_inerr = data_inerr + 'c1 неверные данные\n'
        except:
            data_inerr = data_inerr + 'c1 неверные данные\n'

        try:
            if float(self.c2_leel.text()) >= 0:
                data_in.c_minus = float(self.c2_leel.text())
            else:
                data_inerr = data_inerr + 'c2 неверные данные\n'
        except:
            data_inerr = data_inerr + 'c2 неверные данные\n'

        try:
            if float(self.c3_leel.text()) >= 0:
                data_in.c_3 = float(self.c3_leel.text())
            else:
                data_inerr = data_inerr + 'c3 неверные данные\n'
        except:
            data_inerr = data_inerr + 'c3 неверные данные\n'
        
        if data_inerr == '':
            
            self.sigma_leel.setReadOnly = False
            self.sigma_leel.setText(str(cc.get_sigma(data_in.steel, data_in.temp)))
            data_in.sigma_d = float(self.sigma_leel.text())#cc.get_sigma(data_in.steel, data_in.temp)#
            self.sigma_leel.setReadOnly = True
            data_out = cc.calc_el(data_in)
            self.c_leel.setText(str(round(data_out.c, 2)))
            self.statusBar().showMessage(f'sp={data_out.s_calc:.3f} мм')
            self.s_calc_lel.setText(f'sp={data_out.s_calc:.3f} мм')
        else:
            dialog = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Error', data_inerr)
            result = dialog.exec()

    def pred_calcen(self):
        pass

    def calcob(self):
        if self.vn_rbob.isChecked() == True:
            self.calcov()
        else:
            self.calcon()
           
    def calcov(self):
        data_in = CalcClass.data_in()
        data_out = CalcClass.data_out()
        data_in.met = 'obvn'
        data_inerr = str('')
        
        data_in.name = self.name_leob.text()
        try:
            if int(self.temp_leob.text()) in range (20, 1000):
                data_in.temp = int(self.temp_leob.text())
            else:
                data_inerr = data_inerr + 'T должна быть в диапазоне 20 - 1000\n'
        except:
            data_inerr = data_inerr + 'T должна быть в диапазоне 20 - 1000\n'
        try:
            if float(self.press_leob.text()) > 0 and float(self.press_leob.text()) < 1000:
                data_in.press = float(self.press_leob.text())
            else:
                data_inerr = data_inerr + 'p должно быть в диапазоне 0 - 1000\n'
        except:
            data_inerr = data_inerr + 'p должно быть в диапазоне 0 - 1000\n'

        data_in.steel = self.steel_cbob.currentText()

        try:
            data_in.sigma_d = float(self.sigma_leob.text())
        except:
            data_inerr = data_inerr + '[σ] неверные данные\n'

        try:
            if float(self.fi_leob.text()) > 0 and float(self.fi_leob.text()) <= 1:
                data_in.fi = float(self.fi_leob.text())
            else:
                data_inerr = data_inerr + 'fi должен быть в диапазоне 0 - 1\n'
        except:
            data_inerr = data_inerr + 'fi должен быть в диапазоне 0 - 1\n'
        
        try:
            if int(self.dia_leob.text()) > 0:
                data_in.dia = int(self.dia_leob.text())
            else:
                data_inerr = data_inerr + 'D неверные данные\n'
        except:
            data_inerr = data_inerr + 'D неверные данные\n'

        try:
            if float(self.c1_leob.text()) >= 0:
                data_in.c_kor = float(self.c1_leob.text())
            else:
                data_inerr = data_inerr + 'c1 неверные данные\n'
        except:
            data_inerr = data_inerr + 'c1 неверные данные\n'

        try:
            if float(self.c2_leob.text()) >= 0:
                data_in.c_minus = float(self.c2_leob.text())
            else:
                data_inerr = data_inerr + 'c2 неверные данные\n'
        except:
            data_inerr = data_inerr + 'c2 неверные данные\n'

        
        
        if data_inerr == '':
            cc = CalcClass.CalcClass()
            data_out = cc.calc_ob(data_in)
            try:
                if float(self.s_leob.text()) >= data_out.s_calc:
                    data_in.s_prin = float(self.s_leob.text())
                    data_out = cc.calc_ob(data_in)
                    data_word.append([data_in, data_out])
                    i = word_lv.rowCount()
                    word_lv.insertRow(i)
                    word_lv.setData(word_lv.index(i),f'{data_in.dia} мм, {data_in.press} МПа, {data_in.temp} C, {data_in.met}')
                    self.lvCalc.setModel(word_lv)

                    self.statusBar().showMessage(f'sp={data_out.s_calc:.3f} мм, [p]={data_out.press_d:.3f} МПа')
                    self.s_calc_lob.setText(f'sp={data_out.s_calc:.3f} мм')
                    self.press_d_lob.setText(f'[p]={data_out.press_d:.3f} МПа')
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
        
        data_in.name = self.name_leob.text()
        try:
            if int(self.temp_leob.text()) in range (20, 1000):
                data_in.temp = int(self.temp_leob.text())
            else:
                data_inerr = data_inerr + 'T должна быть в диапазоне 20 - 1000\n'
        except:
            data_inerr = data_inerr + 'T должна быть в диапазоне 20 - 1000\n'
        try:
            if float(self.press_leob.text()) > 0 and float(self.press_leob.text()) < 1000:
                data_in.press = float(self.press_leob.text())
            else:
                data_inerr = data_inerr + 'p должно быть в диапазоне 0 - 1000\n'
        except:
            data_inerr = data_inerr + 'p должно быть в диапазоне 0 - 1000\n'

        data_in.steel = self.steel_cbob.currentText()

        try:
            data_in.sigma_d = float(self.sigma_leob.text())
        except:
            data_inerr = data_inerr + '[σ] неверные данные\n'

        try:
            data_in.E = float(self.E_leob.text())
        except:
            data_inerr = data_inerr + 'E неверные данные\n'

        try:
            if float(self.fi_leob.text()) > 0 and float(self.fi_leob.text()) <= 1:
                data_in.fi = float(self.fi_leob.text())
            else:
                data_inerr = data_inerr + 'fi должен быть в диапазоне 0 - 1\n'
        except:
            data_inerr = data_inerr + 'fi должен быть в диапазоне 0 - 1\n'
        
        try:
            if int(self.dia_leob.text()) > 0:
                data_in.dia = int(self.dia_leob.text())
            else:
                data_inerr = data_inerr + 'D неверные данные\n'
        except:
            data_inerr = data_inerr + 'D неверные данные\n'

        try:
            if float(self.c1_leob.text()) >= 0:
                data_in.c_kor = float(self.c1_leob.text())
            else:
                data_inerr = data_inerr + 'c1 неверные данные\n'
        except:
            data_inerr = data_inerr + 'c1 неверные данные\n'

        try:
            if float(self.c2_leob.text()) >= 0:
                data_in.c_minus = float(self.c2_leob.text())
            else:
                data_inerr = data_inerr + 'c2 неверные данные\n'
        except:
            data_inerr = data_inerr + 'c2 неверные данные\n'

        try:
            if float(self.l_leob.text()) >= 0:
                data_in.l = float(self.l_leob.text())
            else:
                data_inerr = data_inerr + 'l неверные данные\n'
        except:
            data_inerr = data_inerr + 'l неверные данные\n'

        
        
        if data_inerr == '':
            cc = CalcClass.CalcClass()
            data_out = cc.calc_ob(data_in)
            try:
                if float(self.s_leob.text()) >= data_out.s_calc:
                    data_in.s_prin = float(self.s_leob.text())
                    data_out = cc.calc_ob(data_in)
                    data_word.append([data_in, data_out])
                    i = word_lv.rowCount()
                    word_lv.insertRow(i)
                    word_lv.setData(word_lv.index(i),f'{data_in.dia} мм, {data_in.press} МПа, {data_in.temp} C, {data_in.met}')
                    self.lvCalc.setModel(word_lv)

                    self.statusBar().showMessage(f'sp={data_out.s_calc:.3f} мм, [p]={data_out.press_d:.3f} МПа')
                    self.s_calc_lob.setText(f'sp={data_out.s_calc:.3f} мм')
                    self.press_d_lob.setText(f'[p]={data_out.press_d:.3f} МПа')
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

    def calcel(self):
        data_in = CalcClass.data_in()
        data_out = CalcClass.data_out()

        cc = CalcClass.CalcClass()

        data_inerr = str('')

        
                        
        data_in.name = self.name_leel.text()
        try:
            if int(self.temp_leel.text()) in range (20, 1000):
                data_in.temp = int(self.temp_leel.text())
            else:
                data_inerr = data_inerr + 'T должна быть в диапазоне 20 - 1000\n'
        except:
            data_inerr = data_inerr + 'T должна быть в диапазоне 20 - 1000\n'
        try:
            if float(self.press_leel.text()) > 0 and float(self.press_leel.text()) < 1000:
                data_in.press = float(self.press_leel.text())
            else:
                data_inerr = data_inerr + 'p должно быть в диапазоне 0 - 1000\n'
        except:
            data_inerr = data_inerr + 'p должно быть в диапазоне 0 - 1000\n'

        data_in.steel = self.steel_cbel.currentText()

        if self.vn_rbel.isChecked() == True:
            data_in.dav = 'vn'
            data_in.met = 'elvn'
        else:
            data_in.dav = 'nar'
            data_in.met = 'elnar'
            self.E_leel.setReadOnly = False
            self.E_leel.setText(str(cc.get_E('Carbon', data_in.temp)))
            data_in.E = float(self.E_leel.text())#cc.get_sigma(data_in.steel, data_in.temp)#
            self.E_leel.setReadOnly = True
            try:
                data_in.E = float(self.E_leel.text())
            except:
                data_inerr = data_inerr + 'E неверные данные\n'

        try:
            data_in.sigma_d = float(self.sigma_leel.text())
        except:
            data_inerr = data_inerr + '[σ] неверные данные\n'
                    
        try:
            if float(self.fi_leel.text()) > 0 and float(self.fi_leel.text()) <= 1:
                data_in.fi = float(self.fi_leel.text())
            else:
                data_inerr = data_inerr + 'fi должен быть в диапазоне 0 - 1\n'
        except:
            data_inerr = data_inerr + 'fi должен быть в диапазоне 0 - 1\n'
        
        try:
            if int(self.dia_leel.text()) > 0:
                data_in.dia = int(self.dia_leel.text())
            else:
                data_inerr = data_inerr + 'D неверные данные\n'
        except:
            data_inerr = data_inerr + 'D неверные данные\n'

        try:
            if int(self.H_leel.text()) > 0:
                data_in.elH = int(self.H_leel.text())
            else:
                data_inerr = data_inerr + 'H неверные данные\n'
        except:
            data_inerr = data_inerr + 'H неверные данные\n'

        try:
            if int(self.h1_leel.text()) > 0:
                data_in.elh1 = int(self.h1_leel.text())
            else:
                data_inerr = data_inerr + 'h1 неверные данные\n'
        except:
            data_inerr = data_inerr + 'h1 неверные данные\n'

        try:
            if float(self.c1_leel.text()) >= 0:
                data_in.c_kor = float(self.c1_leel.text())
            else:
                data_inerr = data_inerr + 'c1 неверные данные\n'
        except:
            data_inerr = data_inerr + 'c1 неверные данные\n'

        try:
            if float(self.c2_leel.text()) >= 0:
                data_in.c_minus = float(self.c2_leel.text())
            else:
                data_inerr = data_inerr + 'c2 неверные данные\n'
        except:
            data_inerr = data_inerr + 'c2 неверные данные\n'

        try:
            if float(self.c3_leel.text()) >= 0:
                data_in.c_3 = float(self.c3_leel.text())
            else:
                data_inerr = data_inerr + 'c3 неверные данные\n'
        except:
            data_inerr = data_inerr + 'c3 неверные данные\n'

        
        
        
        if data_inerr == '':
            
            data_out = cc.calc_el(data_in)
            try:
                if float(self.s_leel.text()) >= data_out.s_calc:
                    data_in.s_prin = float(self.s_leel.text())
                    data_out = cc.calc_el(data_in)
                    data_word.append([data_in, data_out])
                    i = word_lv.rowCount()
                    word_lv.insertRow(i)
                    word_lv.setData(word_lv.index(i),f'{data_in.dia} мм, {data_in.press} МПа, {data_in.temp} C, {data_in.met}')
                    self.lvCalc.setModel(word_lv)

                    self.statusBar().showMessage(f'sp={data_out.s_calc:.3f} мм, [p]={data_out.press_d:.3f} МПа')
                    self.s_calc_lel.setText(f'sp={data_out.s_calc:.3f} мм')
                    self.press_d_lel.setText(f'[p]={data_out.press_d:.3f} МПа')
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
                makeWord.makeWord_elvn(data_word[i][0], data_word[i][1], '1.docx')
            elif data_word[i][0].met == 'elnar':
                makeWord.makeWord_elnar(data_word[i][0], data_word[i][1], '1.docx')
            elif data_word[i][0].met == 'konvn':
                pass
            elif data_word[i][0].met == 'konnar':
                pass

        self.pbMakeWord.setEnabled(True)




class ElCalcSxema(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        uic.loadUi('elsxema.ui', self)

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

        self.pbGostElOK.clicked.connect(self.pressOK)
        self.pbGostElCancel.clicked.connect(self.close)

         
    #    self.pbGostElOK.connect(self.getdata_el)

    #def getdata_el(self):

    def pressOK(self):
        mainwindow.dia_leel.setText(self.diagostel_cb.currentText())
        mainwindow.H_leel.setText(self.Hgostel_le.text())
        mainwindow.h1_leel.setText(self.h1gostel_le.text())
        mainwindow.s_leel.setText(self.sgostel_cb.currentText())
        mainwindow.c3_leel.setText(f'{float(self.sgostel_cb.currentText()) * 0.15:.2f}')
        mainwindow.name_leel.setText(f'Днище {self.diagostel_cb.currentText()}-{self.sgostel_cb.currentText()}-{self.Hgostel_le.text()} ГОСТ 6533-78')
        self.close()

    


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
            elif ind < int(data_fiz.el025_list[self.diagostel_cb.currentText()][-1].split('-')[-1]) and len(data_fiz.el025_list[self.diagostel_cb.currentText()][-1].split('-')) == 1:
                H = data_fiz.el025_list[self.diagostel_cb.currentText()][-3][1]
                h1 = data_fiz.el025_list[self.diagostel_cb.currentText()][-3][0]
            elif ind >= int(data_fiz.el025_list[self.diagostel_cb.currentText()][-1].split('-')[-2]):
                H = data_fiz.el025_list[self.diagostel_cb.currentText()][-3][1]
                h1 = data_fiz.el025_list[self.diagostel_cb.currentText()][-3][0]
            elif ind < int(data_fiz.el025_list[self.diagostel_cb.currentText()][-1].split('-')[-2]) and len(data_fiz.el025_list[self.diagostel_cb.currentText()][-1].split('-')) == 2:
                H = data_fiz.el025_list[self.diagostel_cb.currentText()][-4][1]
                h1 = data_fiz.el025_list[self.diagostel_cb.currentText()][-4][0]
            else:
                H =''
                h1 = ''

        self.Hgostel_le.setText(str(H))
        self.h1gostel_le.setText(str(h1))

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
