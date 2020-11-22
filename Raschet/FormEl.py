# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, uic, QtCore, QtGui, Qt
import CalcClass
import data_fiz
from Fi import Fi
import globalvar
from globalvar import data_word, word_lv
from Nozzle import Nozzle

global elementdatayk


class FormEl(QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        uic.loadUi('ElForm.ui', self)

        self.fiWin = None
        self.calcSxema = None
        self.gostWin = None
        self.nozzleWin = None
        self.typeElement = 'el'
        

        self.steel_cbel.setModel(data_fiz.steelList)

        
        self.vn_rbel.toggled.connect(self.vnnarel)
        

        self.pbGetSigmael.clicked.connect(self.getSigma)
        self.pbGetEel.clicked.connect(self.getE)

        self.pbfiel.clicked.connect(self.ShowFi)

        self.pbCancelel.clicked.connect(self.hide)

        self.pbPredel.clicked.connect(self.pred_calcel)

        self.pbCalcel.clicked.connect(self.calcel)

        self.pbElToNozzle.clicked.connect(self.ShowNozzle)


        self.pbShowSxemael.clicked.connect(self.ShowCalcSxemaEl)

        self.pbDimGostEl.clicked.connect(self.getDimEl)

    def getDimEl(self):
        if not self.gostWin:
            self.gostWin = GostEl(self)
        self.gostWin.setWindowModality(QtCore.Qt.WindowModal)
        self.gostWin.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        self.gostWin.show()

    def getSigma(self):
        pass


    def getE(self):
        pass

    
    def vnnarel(self):
        if self.vn_rbel.isChecked():
            self.E_leel.setEnabled(False)
            self.pbGetEel.setEnabled(False)
        else:
            self.E_leel.setEnabled(True)
            self.pbGetEel.setEnabled(True)
            
    def ShowFi(self):
        if not self.fiWin:
            self.fiWin = Fi(self)
        self.fiWin.setWindowModality(QtCore.Qt.WindowModal)
        self.fiWin.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        self.fiWin.show()

    def ShowCalcSxemaEl(self):
        global windowcalc
        windowcalc = ElCalcSxema()
        windowcalc.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        windowcalc.show()
 
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

        data_in.steel = self.steel_cbel.currentText()

        if data_inerr == '':
            self.sigma_leel.setReadOnly = False
            self.sigma_leel.setText(str(cc.get_sigma(data_in.steel, data_in.temp)))
            self.sigma_leel.setReadOnly = True
            try:
                data_in.sigma_d = float(self.sigma_leel.text())
            except:
                data_inerr = data_inerr + '[σ] неверные данные\n'

            if self.vn_rbel.isChecked():
                data_in.dav = 'vn'
            else:
                data_in.dav = 'nar'
                
                self.E_leel.setReadOnly = False
                self.E_leel.setText(str(cc.get_E(data_in.steel, data_in.temp)))
                self.E_leel.setReadOnly = True
                
                try:
                    data_in.E = float(self.E_leel.text())
                except:
                    data_inerr = data_inerr + 'E неверные данные\n'

        
        try:
            if float(self.press_leel.text()) > 0 and float(self.press_leel.text()) < 1000:
                data_in.press = float(self.press_leel.text())
            else:
                data_inerr = data_inerr + 'p должно быть в диапазоне 0 - 1000\n'
        except:
            data_inerr = data_inerr + 'p должно быть в диапазоне 0 - 1000\n'

        
        try:
            if float(self.fi_le.text()) > 0 and float(self.fi_le.text()) <= 1:
                data_in.fi = float(self.fi_le.text())
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
            
            if self.c3_leel.text() == '':
                pass
            elif float(self.c3_leel.text()) >= 0:
                data_in.c_3 = float(self.c3_leel.text())
            else:
                data_inerr = data_inerr + 'c3 неверные данные\n'
        except:
            data_inerr = data_inerr + 'c3 неверные данные\n'
        
        if data_inerr == '':
           
            data_out = cc.calc_el(data_in)
            self.c_leel.setText(str(round(data_out.c, 2)))
            self.s_calc_lel.setText(f'sp={data_out.s_calc:.3f} мм')
            self.pbCalcel.setEnabled(True)
        else:
            dialog = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Error', data_inerr)
            result = dialog.exec()

    def calcel(self):
        data_in = CalcClass.data_in()
        data_out = CalcClass.data_out()
     
        data_inerr = str('')
        
        data_in.name = self.name_leel.text()
        try:
            if int(self.temp_leel.text()) in range (20, 1000):
                data_in.temp = int(self.temp_leel.text())
            else:
                data_inerr = data_inerr + 'T должна быть в диапазоне 20 - 1000\n'
        except:
            data_inerr = data_inerr + 'T должна быть в диапазоне 20 - 1000\n'

        if self.vn_rbel.isChecked():
            data_in.dav = 'vn'
            data_in.met = 'elvn'
        else:
            data_in.dav = 'nar'
            data_in.met = 'elnar'
                          
            try:
                if float(self.E_leel.text()) > 0:
                    data_in.E = float(self.E_leel.text())
                else:
                    data_inerr = data_inerr + 'E неверные данные\n'
            except:
                data_inerr = data_inerr + 'E неверные данные\n'
            

        try:
            if float(self.press_leel.text()) > 0 and float(self.press_leel.text()) < 1000:
                data_in.press = float(self.press_leel.text())
            else:
                data_inerr = data_inerr + 'p должно быть в диапазоне 0 - 1000\n'
        except:
            data_inerr = data_inerr + 'p должно быть в диапазоне 0 - 1000\n'

        data_in.steel = self.steel_cbel.currentText()

        try:
            if float(self.sigma_leel.text()) > 0:
                data_in.sigma_d = float(self.sigma_leel.text())
            else:
                data_inerr = data_inerr + '[σ] неверные данные\n'
        except:
            data_inerr = data_inerr + '[σ] неверные данные\n'

        try:
            if float(self.fi_le.text()) > 0 and float(self.fi_le.text()) <= 1:
                data_in.fi = float(self.fi_le.text())
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
            if self.c3_leel.text() == '':
                pass
            elif float(self.c3_leel.text()) >= 0:
                data_in.c_3 = float(self.c3_leel.text())
            else:
                data_inerr = data_inerr + 'c3 неверные данные\n'
        except:
            data_inerr = data_inerr + 'c3 неверные данные\n'

        
        
        if data_inerr == '':
            cc = CalcClass.CalcClass()
            data_out = cc.calc_el(data_in)
            #try:
            if float(self.s_leel.text()) >= data_out.s_calc:
                data_in.s_prin = float(self.s_leel.text())
                data_out = cc.calc_el(data_in)
                data_word.append([data_in, data_out])
                globalvar.elementdatayk = [data_in, data_out]
                i = word_lv.rowCount()
                word_lv.insertRow(i)
                word_lv.setData(word_lv.index(i),f'{data_in.dia} мм, {data_in.press} МПа, {data_in.temp} C, {data_in.met}')
                self.parent().lvCalc.setModel(word_lv)

                self.s_calc_lel.setText(f'sp={data_out.s_calc:.3f} мм')
                self.press_d_lel.setText(f'[p]={data_out.press_d:.3f} МПа')
                self.pbElToNozzle.setEnabled(True)
                if (((data_in.s_prin - data_out.c)/data_in.dia <= 0.1) and ((data_in.s_prin - data_out.c)/data_in.dia >= 0.002)) and ((data_in.elH/data_in.dia < 0.5) and (data_in.elH/data_in.dia >= 0.2)):
                    data_out.ypf = True
                else:
                    data_out.ypf = True
                    self.ypf_l.setText('Условия применения формул не выполняется')
            else:
                dialog = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Error', 's должно быть больше или равно sp')
                result = dialog.exec()
            #except:
                
            #    dialog = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Error', 's неверные данные')
            #    result = dialog.exec()
            
        else:
            dialog = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Error', data_inerr)
            result = dialog.exec()


    def closeEvent(self, event):
        self.parent().obEl = None

    def ShowNozzle(self):
        if not self.nozzleWin:
            self.nozzleWin = Nozzle(self)
        self.nozzleWin.setWindowModality(QtCore.Qt.WindowModal)
        self.nozzleWin.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        self.nozzleWin.show()
        self.nozzleWin.elem_le.setText(self.name_leel.text())
        self.nozzleWin.temp_le.setText(self.temp_leel.text())
        self.nozzleWin.press_le.setText(self.press_leel.text())
        if self.vn_rbel.isChecked():
            self.nozzleWin.vn_rbyk.setChecked(True)
        else:
            self.nozzleWin.nar_rbyk.setChecked(True)

        globalvar.elementdatayk[0].yk = True
        self.nozzleWin.data = globalvar.elementdatayk

        

  
class ElCalcSxema(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)

        self.setFixedSize(QtCore.QSize(533, 400))             # Устанавливаем размеры
        self.setWindowTitle('Расчетные схемы выпуклых днищ')    # Устанавливаем заголовок окна
          

        h_layout = QtWidgets.QHBoxLayout()            # Создаём QGridLayout
        h_layout.setContentsMargins(QtCore.QMargins(0, 0, 0, 0))
        h_layout.setSpacing(0)
        self.setLayout(h_layout)

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setPixmap(QtGui.QPixmap('pic/elSxema.png'))
        self.label1.setScaledContents(True)
        h_layout.addWidget(self.label1)

        
class GostEl(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        uic.loadUi('GostEl.ui', self)

        self.diaList = QtCore.QStringListModel()

        self.listDim = None

        self.diaList.insertRows(0, 100)
        
        self.diagostel_cb.setModel(self.diaList)
        self.typegostel_cb.setCurrentIndex(1)
        self.typechange()
        self.diachange()
        self.schange()
        self.typegostel_cb.currentIndexChanged.connect(self.typechange)
        self.diagostel_cb.currentIndexChanged.connect(self.diachange)
        self.sgostel_cb.currentIndexChanged.connect(self.schange)

        self.pbGostElOK.clicked.connect(self.pressOK)
        self.pbGostElCancel.clicked.connect(self.close)
   

    def typechange(self):
        if self.typegostel_cb.currentIndex() == 0:
            self.listDim = data_fiz.el025n_list
        elif self.typegostel_cb.currentIndex() == 1:
            self.listDim = data_fiz.el025v_list
        elif self.typegostel_cb.currentIndex() == 2:
            self.listDim = data_fiz.el02v_list
        

        #self.diaList.insertRows(0, 100)        
        i = 0
        for k in self.listDim.keys():
            self.diaList.setData(self.diaList.index(i), k)
            i += 1
        
        self.diaList.removeRows(i, self.diaList.rowCount()-i)

        self.diaList.insertRows(0, 100)        
        i = 0
        for k in self.listDim.keys():
            self.diaList.setData(self.diaList.index(i), k)
            i += 1
        
        self.diaList.removeRows(i, self.diaList.rowCount()-i)
        
        self.diaList.endResetModel()
       
    def pressOK(self):
        self.parent().dia_leel.setText(self.diagostel_cb.currentText())
        self.parent().H_leel.setText(self.Hgostel_le.text())
        self.parent().h1_leel.setText(self.h1gostel_le.text())
        self.parent().s_leel.setText(self.sgostel_cb.currentText())
        self.parent().c3_leel.setText(f'{float(self.sgostel_cb.currentText()) * 0.15:.2f}')
        self.parent().name_leel.setText(f'Днище {self.diagostel_cb.currentText()}-{self.sgostel_cb.currentText()}-{self.Hgostel_le.text()} ГОСТ 6533-78')
        self.close()

    def diachange(self):
        sList = QtCore.QStringListModel()
        if self.listDim[self.diagostel_cb.currentText()][-1] == 'a':
            sList.insertRows(0, len(self.listDim[self.diagostel_cb.currentText()]) - 2)
            i = 0
            for k in self.listDim[self.diagostel_cb.currentText()]:
                if type(k) == int:
                    sList.setData(sList.index(i), k)
                    i += 1
            del i
        else:
            sList.insertRows(0, len(self.listDim[self.diagostel_cb.currentText()]) - 2 - len(self.listDim[self.diagostel_cb.currentText()][-1].split('-')))
            i = 0
            for k in self.listDim[self.diagostel_cb.currentText()]:
                if type(k) == int:
                    sList.setData(sList.index(i), k)
                    i += 1
            del i

        self.sgostel_cb.setModel(sList)

    def schange(self):
        if self.listDim[self.diagostel_cb.currentText()][-1] == 'a':
            H = self.listDim[self.diagostel_cb.currentText()][-2][1]
            h1 = self.listDim[self.diagostel_cb.currentText()][-2][0]
        else:
            ind =  self.listDim[self.diagostel_cb.currentText()].index(int(self.sgostel_cb.currentText()))

            if ind >= int(self.listDim[self.diagostel_cb.currentText()][-1].split('-')[-1]):
                H = self.listDim[self.diagostel_cb.currentText()][-2][1]
                h1 = self.listDim[self.diagostel_cb.currentText()][-2][0]
            elif ind < int(self.listDim[self.diagostel_cb.currentText()][-1].split('-')[-1]) and len(self.listDim[self.diagostel_cb.currentText()][-1].split('-')) == 1:
                H = self.listDim[self.diagostel_cb.currentText()][-3][1]
                h1 = self.listDim[self.diagostel_cb.currentText()][-3][0]
            elif ind >= int(self.listDim[self.diagostel_cb.currentText()][-1].split('-')[-2]):
                H = self.listDim[self.diagostel_cb.currentText()][-3][1]
                h1 = self.listDim[self.diagostel_cb.currentText()][-3][0]
            elif ind < int(self.listDim[self.diagostel_cb.currentText()][-1].split('-')[-2]) and len(self.listDim[self.diagostel_cb.currentText()][-1].split('-')) == 2:
                H = self.listDim[self.diagostel_cb.currentText()][-4][1]
                h1 = self.listDim[self.diagostel_cb.currentText()][-4][0]
            else:
                H =''
                h1 = ''

        self.Hgostel_le.setText(str(H))
        self.h1gostel_le.setText(str(h1))

    def closeEvent(self, event):
        self.parent().gostWin = None













