# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, uic, QtCore, QtGui, Qt
import CalcClass
import data_fiz
from globalvar import data_word, word_lv
from Fi import Fi


class FormOb(QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        #QtWidgets.QWidget.__init__(self, parent)
        super().__init__(parent, QtCore.Qt.Window)
        uic.loadUi('ObCil.ui', self)

        self.fiWin = None
        self.calcSxema = None
        

        self.steel_cbob.setModel(data_fiz.steelList)

        self.rbf_1.toggled.connect(self.rbf)
        self.rbf_2.toggled.connect(self.rbf)
        self.rbf_3.toggled.connect(self.rbf)
        self.rbf_4.toggled.connect(self.rbf)
        self.rbf_5.toggled.connect(self.rbf)
        self.rbf_6.toggled.connect(self.rbf)
        self.rbf_7.toggled.connect(self.rbf)

        self.vn_rbob.toggled.connect(self.vnnarob)
        self.nagobcalc_rb.toggled.connect(self.nagob)

        self.pbGetSigmaob.clicked.connect(self.getSigma)
        self.pbGetEob.clicked.connect(self.getE)

        self.pbfiob.clicked.connect(self.ShowFi)

        self.pbCancelob.clicked.connect(self.hide)

        self.pbPredob.clicked.connect(self.pred_calcob)

        self.pbCalcob.clicked.connect(self.calcob)


        self.pbShowSxemaob.clicked.connect(self.ShowCalcSxemaOb)

    def getSigma(self):
        pass
        #cc = CalcClass.CalcClass()
        #self.sigma_leob.setText(str(cc.get_sigma(self.steel_cbob.currentText(), int(self.temp_leob.text()))))
        #del cc

    def getE(self):
        pass
        #cc = CalcClass.CalcClass()
        #self.E_leob.setText(str(cc.get_E(self.steel_cbob.currentText(), int(self.temp_leob.text()))))

    def nagob(self):
        if self.nagobcalc_rb.isChecked():
            pass
        else:
            pass


    def vnnarob(self):
        if self.vn_rbob.isChecked():
            self.E_leob.setEnabled(False)
            self.pbGetEob.setEnabled(False)
            self.l_leob.setEnabled(False)
            self.pbGetlob.setEnabled(False)
        else:
            self.E_leob.setEnabled(True)
            self.pbGetEob.setEnabled(True)
            self.l_leob.setEnabled(True)
            self.pbGetlob.setEnabled(True)
        
    def rbf(self):
        s = self.sender().text()
                
        if self.sender().isChecked():
            self.label_rbf.setPixmap(QtGui.QPixmap('pic/PC/PC' + s[0]))

    def ShowFi(self):
        if not self.fiWin:
            self.fiWin = Fi(self)
        self.fiWin.setWindowModality(QtCore.Qt.WindowModal)
        self.fiWin.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        self.fiWin.show()
        #global windowfi
        #windowfi = Fi()
        #windowfi.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        #windowfi.show()

    def ShowCalcSxemaOb(self):
        global windowcalc
        windowcalc = ObCalcSxema()
        windowcalc.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        windowcalc.show()
 
    def pred_calcob(self):
        data_in = CalcClass.data_in() 
        data_out = CalcClass.data_out()

        cc = CalcClass.CalcClass()

        data_inerr = str('')

        try:
            if int(self.temp_leob.text()) in range (20, 1000):
                data_in.temp = int(self.temp_leob.text())
            else:
                data_inerr = data_inerr + 'T должна быть в диапазоне 20 - 1000\n'
        except:
            data_inerr = data_inerr + 'T должна быть в диапазоне 20 - 1000\n'

        data_in.steel = self.steel_cbob.currentText()


        if self.vn_rbob.isChecked():
            data_in.dav = 'vn'
        else:
            data_in.dav = 'nar'
            if data_inerr == '':
                self.E_leob.setReadOnly = False
                self.E_leob.setText(str(cc.get_E(data_in.steel, data_in.temp)))
                data_in.E = float(self.E_leob.text())
                self.E_leob.setReadOnly = True
            else:
                data_inerr = data_inerr + 'E неверные данные\n'

            try:
                if float(self.l_leob.text()) > 0:
                    data_in.l = float(self.l_leob.text())
                else:
                    data_inerr = data_inerr + 'l неверные данные\n'
            except:
                data_inerr = data_inerr + 'l неверные данные\n'

                
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

        
        try:
            if float(self.fi_le.text()) > 0 and float(self.fi_le.text()) <= 1:
                data_in.fi = float(self.fi_le.text())
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
            
            if self.c3_leob.text() == '':
                pass
            elif float(self.c3_leob.text()) >= 0:
                data_in.c_3 = float(self.c3_leob.text())
            else:
                data_inerr = data_inerr + 'c3 неверные данные\n'
        except:
            data_inerr = data_inerr + 'c3 неверные данные\n'
        
        if data_inerr == '':
            self.sigma_leob.setReadOnly = False
            self.sigma_leob.setText(str(cc.get_sigma(data_in.steel, data_in.temp)))
            data_in.sigma_d = float(self.sigma_leob.text())
            self.sigma_leob.setReadOnly = True
            data_out = cc.calc_ob(data_in)
            self.c_leob.setText(str(round(data_out.c, 2)))
            self.s_calc_lob.setText(f'sp={data_out.s_calc:.3f} мм')
        else:
            dialog = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Error', data_inerr)
            result = dialog.exec()

    def calcob(self):
        data_in = CalcClass.data_in()
        data_out = CalcClass.data_out()
     
        data_inerr = str('')
        
        data_in.name = self.name_leob.text()
        try:
            if int(self.temp_leob.text()) in range (20, 1000):
                data_in.temp = int(self.temp_leob.text())
            else:
                data_inerr = data_inerr + 'T должна быть в диапазоне 20 - 1000\n'
        except:
            data_inerr = data_inerr + 'T должна быть в диапазоне 20 - 1000\n'

        if self.vn_rbob.isChecked():
            data_in.dav = 'vn'
            data_in.met = 'obvn'
        else:
            data_in.dav = 'nar'
            data_in.met = 'obnar'
                          
            try:
                if float(self.E_leob.text()) > 0:
                    data_in.E = float(self.E_leob.text())
                else:
                    data_inerr = data_inerr + 'E неверные данные\n'
            except:
                data_inerr = data_inerr + 'E неверные данные\n'

            try:
                if float(self.l_leob.text()) > 0:
                    data_in.l = float(self.l_leob.text())
                else:
                    data_inerr = data_inerr + 'l неверные данные\n'
            except:
                data_inerr = data_inerr + 'l неверные данные\n'

        try:
            if float(self.press_leob.text()) > 0 and float(self.press_leob.text()) < 1000:
                data_in.press = float(self.press_leob.text())
            else:
                data_inerr = data_inerr + 'p должно быть в диапазоне 0 - 1000\n'
        except:
            data_inerr = data_inerr + 'p должно быть в диапазоне 0 - 1000\n'

        data_in.steel = self.steel_cbob.currentText()

        try:
            if float(self.sigma_leob.text()) > 0:
                data_in.sigma_d = float(self.sigma_leob.text())
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
            if self.c3_leob.text() == '':
                pass
            elif float(self.c3_leob.text()) >= 0:
                data_in.c_3 = float(self.c3_leob.text())
            else:
                data_inerr = data_inerr + 'c3 неверные данные\n'
        except:
            data_inerr = data_inerr + 'c3 неверные данные\n'

        
        
        if data_inerr == '':
            cc = CalcClass.CalcClass()
            data_out = cc.calc_ob(data_in)
            #try:
            if float(self.s_leob.text()) >= data_out.s_calc:
                data_in.s_prin = float(self.s_leob.text())
                data_out = cc.calc_ob(data_in)
                data_word.append([data_in, data_out])
                i = word_lv.rowCount()
                word_lv.insertRow(i)
                word_lv.setData(word_lv.index(i),f'{data_in.dia} мм, {data_in.press} МПа, {data_in.temp} C, {data_in.met}')
                self.parent().lvCalc.setModel(word_lv)

                self.s_calc_lob.setText(f'sp={data_out.s_calc:.3f} мм')
                self.press_d_lob.setText(f'[p]={data_out.press_d:.3f} МПа')
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
        self.parent().obWin = None

    
  
class ObCalcSxema(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)

        self.setFixedSize(QtCore.QSize(700, 646))             # Устанавливаем размеры
        self.setWindowTitle('Расчетные схемы обечайек')    # Устанавливаем заголовок окна
          

        h_layout = QtWidgets.QHBoxLayout()            # Создаём QGridLayout
        h_layout.setContentsMargins(QtCore.QMargins(0, 0, 0, 0))
        h_layout.setSpacing(0)
        self.setLayout(h_layout)

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setPixmap(QtGui.QPixmap('pic/ob1.png'))
        h_layout.addWidget(self.label1)

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setPixmap(QtGui.QPixmap('pic/ob2.png'))
        self.label2.setAlignment(QtCore.Qt.AlignTop)
        h_layout.addWidget(self.label2, 1)

        






