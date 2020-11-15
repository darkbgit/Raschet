# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, uic, QtCore, QtGui, Qt
import CalcClass
import data_fiz


class FormEl(QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        uic.loadUi('ElForm.ui', self)

        

        self.steel_cbel.setModel(data_fiz.steelList)

        
        self.vn_rbel.toggled.connect(self.vnnarel)
        

        self.pbGetSigmael.clicked.connect(self.getSigma)
        self.pbGetEel.clicked.connect(self.getE)

        self.pbfiel.clicked.connect(self.ShowFi)

        self.pbCancelel.clicked.connect(self.hide)

        self.pbPredel.clicked.connect(self.pred_calcob)

        #self.pbCalcob.clicked.connect(self.calcob)


        self.pbShowSxemael.clicked.connect(self.ShowCalcSxemaEl)

    def getSigma(self):
        cc = CalcClass.CalcClass()
        self.sigma_leob.setText(str(cc.get_sigma(self.steel_cbob.currentText(), int(self.temp_leob.text()))))

    def getE(self):
        cc = CalcClass.CalcClass()
        self.E_leob.setText(str(cc.get_E(self.steel_cbob.currentText(), int(self.temp_leob.text()))))

    
    def vnnarel(self):
        if self.vn_rbel.isChecked():
            self.E_leel.setEnabled(False)
            self.pbGetEel.setEnabled(False)
        else:
            self.E_leel.setEnabled(True)
            self.pbGetE.setEnabled(True)
            
        
    def rbf(self):
        s = self.sender().text()
                
        if self.sender().isChecked():
            self.label_rbf.setPixmap(QtGui.QPixmap('pic/PC/PC' + s[0]))

    def ShowFi(self):
        global windowfi
        windowfi = Fi()
        windowfi.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        windowfi.show()

    def ShowCalcSxemaEl(self):
        global windowcalc
        windowcalc = ElCalcSxema()
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
            try:
                data_in.E = float(self.E_leob.text())
            except:
                data_inerr = data_inerr + 'E неверные данные\n'

            try:
                if float(self.l_leob.text()) >= 0:
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

  
class ElCalcSxema(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        uic.loadUi('ObSxema.ui', self)


class Fi(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        uic.loadUi('FiForm.ui', self)

        self.pb1.clicked.connect(self.push)

    def push(self):
        windowob.rbf_2.setChecked()








