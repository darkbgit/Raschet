from PyQt5 import QtWidgets, uic, QtCore, QtGui
import data_fiz
import CalcClass
import globalvar

class Saddle(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        uic.loadUi('SaddleForm.ui', self)

        self.gostWin = None


        self.steel_cb.setModel(data_fiz.steelList)


        self.type_group = QtWidgets.QButtonGroup()
        self.type_group.addButton(self.saddletyperb_1, 1)
        self.type_group.addButton(self.saddletyperb_2, 2)
        self.type_group.addButton(self.saddletyperb_3, 3)

        self.type_group.buttonToggled.connect(self.typeChange)

        self.dav_group  = QtWidgets.QButtonGroup()
        self.dav_group.addButton(self.vn_rb, 1)
        self.dav_group.addButton(self.nar_rb, 2)

        self.rebro_group = QtWidgets.QButtonGroup()
        self.rebro_group.addButton(self.rebrono_rb, 1)
        self.rebro_group.addButton(self.rebro1_rb, 2)
        self.rebro_group.addButton(self.rebro3_rb, 3)

        self.ring_group  = QtWidgets.QButtonGroup()
        self.ring_group.addButton(self.ringin_rb, 1)
        self.ring_group.addButton(self.ringout_rb, 2)

        #self.ring_gb.hide()

        self.ring_group.buttonToggled.connect(self.ringChange)

        self.pbPred.clicked.connect(self.pred_calc)
        self.pbCancel.clicked.connect(self.close)


        self.pbGetLea.clicked.connect(self.getLea)
        #self.type_group.buttonToggled['bool'].emit(False)
        
    def getLea(self):
        if not self.gostWin:
            self.gostWin = GostEl(self)
        self.gostWin.setWindowModality(QtCore.Qt.WindowModal)
        self.gostWin.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        self.gostWin.show()

    def ringChange(self):
        if self.ring_group.checkedId() == 1:
            self.pic.setPixmap(QtGui.QPixmap('pic/Saddle/SaddleRingInElem'))
        elif self.ring_group.checkedId() == 2:
            self.pic.setPixmap(QtGui.QPixmap('pic/Saddle/SaddleRingOutElem'))
            

    def typeChange(self):
        if self.type_group.checkedId() == 1:
            self.ring_gb.hide()
            self.pic.setPixmap(QtGui.QPixmap('pic/Saddle/SaddleNothingElem'))
            self.removeLay(self.grid1)
            self.grid.update()

        elif self.type_group.checkedId() == 2:
            self.ring_gb.hide()
            self.pic.setPixmap(QtGui.QPixmap('pic/Saddle/SaddleSheetElem'))
            self.removeLay(self.grid1)
            self.grid.update()
                   
            self.lab1_1 = QtWidgets.QLabel('Толщина листа, s2:')
            self.s2_le = QtWidgets.QLineEdit('10')
            self.s2_le.setMaximumHeight(20)
            self.lab1_2 = QtWidgets.QLabel('мм')

            self.lab2_1 = QtWidgets.QLabel('Ширина листа, b2:')
            self.b2_le = QtWidgets.QLineEdit('300')
            self.b2_le.setMaximumHeight(20)
            self.lab2_2 = QtWidgets.QLabel('мм')

            self.lab3_1 = QtWidgets.QLabel('Угол охвата листа, δ2:')
            self.delta2_le = QtWidgets.QLineEdit('140')
            self.delta2_le.setMaximumHeight(20)
            self.lab3_2 = QtWidgets.QLabel('°')

            self.lab4_1 = QtWidgets.QLabel('Длина выступающей части листа, f:')
            self.f_le = QtWidgets.QLineEdit()
            self.f_le.setMaximumHeight(20)
            self.lab4_2 = QtWidgets.QLabel('мм')

            self.grid1.addWidget(self.lab1_1, 0, 0)
            self.grid1.addWidget(self.s2_le, 0, 1)
            self.grid1.addWidget(self.lab1_2, 0, 2)

            self.grid1.addWidget(self.lab2_1, 1, 0)
            self.grid1.addWidget(self.b2_le, 1, 1)
            self.grid1.addWidget(self.lab2_2, 1, 2)

            self.grid1.addWidget(self.lab3_1, 2, 0)
            self.grid1.addWidget(self.delta2_le, 2, 1)
            self.grid1.addWidget(self.lab3_2, 2, 2)

            self.grid1.addWidget(self.lab4_1, 3, 0)
            self.grid1.addWidget(self.f_le, 3, 1)
            self.grid1.addWidget(self.lab4_2, 3, 2)

            self.fr = QtWidgets.QFrame()
            self.grid1.addWidget(self.fr, 4, 0, 1, 3)
        

        elif self.type_group.checkedId() == 3:
            self.ring_gb.show()
            if self.ringin_rb.isChecked():
                self.pic.setPixmap(QtGui.QPixmap('pic/Saddle/SaddleRingInElem'))
            else:
                self.pic.setPixmap(QtGui.QPixmap('pic/Saddle/SaddleRingOutElem'))

    def pred_calc(self):
        
        
        data_in = CalcClass.data_saddlein()
        data_out = CalcClass.data_saddleout()

        cc = CalcClass.CalcClass()

        data_inerr = str('')

        #try:
        #    if int(self.temp_le.text()) in range (20, 1000):
        #        data_in.temp = int(self.temp_le.text())
        #    else:
        #        data_inerr = data_inerr + 'T должна быть в диапазоне 20 - 1000\n'
        #except:
        #    data_inerr = data_inerr + 'T должна быть в диапазоне 20 - 1000\n'
        data_in.met = 'saddle'

        data_in.name = self.name_le.text()

        data_in.nameob = self.nameob_le.text()

        try:
            if int(self.D_le.text()) > 0:
                data_in.D = int(self.D_le.text())
            else:
                data_inerr = data_inerr + 'D неверные данные\n'
        except:
            data_inerr = data_inerr + 'D неверные данные\n'

        try:
            if float(self.s_le.text()) > 0:
                data_in.s = float(self.s_le.text())
            else:
                data_inerr = data_inerr + 's неверные данные\n'
        except:
            data_inerr = data_inerr + 's неверные данные\n'

        try:
            if float(self.c_le.text()) >= 0:
                data_in.c = float(self.c_le.text())
            else:
                data_inerr = data_inerr + 'c неверные данные\n'
        except:
            data_inerr = data_inerr + 'c неверные данные\n'

        try:
            if float(self.Lob_le.text()) > 0:
                data_in.Lob = float(self.Lob_le.text())
            else:
                data_inerr = data_inerr + 'Lob неверные данные\n'
        except:
            data_inerr = data_inerr + 'Lob неверные данные\n'

        try:
            if float(self.fi_le.text()) > 0 and float(self.fi_le.text()) <= 1:
                data_in.fi = float(self.fi_le.text())
            else:
                data_inerr = data_inerr + 'fi должен быть в диапазоне 0 - 1\n'
        except:
            data_inerr = data_inerr + 'fi должен быть в диапазоне 0 - 1\n'

        data_in.steel = self.steel_cb.currentText()

        try:
            if int(self.temp_le.text()) in range (20, 1000):
                data_in.temp = int(self.temp_le.text())
            else:
                data_inerr = data_inerr + 'T должна быть в диапазоне 20 - 1000\n'
        except:
            data_inerr = data_inerr + 'T должна быть в диапазоне 20 - 1000\n'

        try:
            if int(self.G_le.text()) > 0:
                data_in.G = int(self.G_le.text())
            else:
                data_inerr = data_inerr + 'G неверные данные\n'
        except:
            data_inerr = data_inerr + 'G неверные данные\n'

        try:
            if float(self.p_le.text()) > 0 and float(self.p_le.text()) < 1000:
                data_in.p = float(self.p_le.text())
            else:
                data_inerr = data_inerr + 'p должно быть в диапазоне 0 - 1000\n'
        except:
            data_inerr = data_inerr + 'p должно быть в диапазоне 0 - 1000\n'

        if self.vn_rb.isChecked():
            data_in.dav = 'vn'
        else:
            data_in.dav = 'nar'

        try:
            if float(self.b_le.text()) > 0:
                data_in.b = int(self.b_le.text())
            else:
                data_inerr = data_inerr + 'b неверные данные\n'
        except:
            data_inerr = data_inerr + 'b неверные данные\n'

        try:
            if int(self.delta1_le.text()) > 0:
                data_in.delta1 = int(self.delta1_le.text())
            else:
                data_inerr = data_inerr + 'δ1 неверные данные\n'
        except:
            data_inerr = data_inerr + 'δ1 неверные данные\n'

        try:
            if int(self.l0_le.text()) > 0:
                data_in.l0 = int(self.l0_le.text())
            else:
                data_inerr = data_inerr + 'l0 неверные данные\n'
        except:
            data_inerr = data_inerr + 'l0 неверные данные\n'

        try:
            if float(self.H_le.text()) > 0:
                data_in.H = int(self.H_le.text())
            else:
                data_inerr = data_inerr + 'H неверные данные\n'
        except:
            data_inerr = data_inerr + 'H неверные данные\n'

        try:
            if int(self.L_le.text()) > 0:
                data_in.L = int(self.L_le.text())
            else:
                data_inerr = data_inerr + 'L неверные данные\n'
        except:
            data_inerr = data_inerr + 'L неверные данные\n'

        try:
            if int(self.e_le.text()) > 0:
                data_in.e = int(self.e_le.text())
            else:
                data_inerr = data_inerr + 'e неверные данные\n'
        except:
            data_inerr = data_inerr + 'e неверные данные\n'
            
        try:
            if float(self.a_le.text()) > 0:
                data_in.a = float(self.a_le.text())
            else:
                data_inerr = data_inerr + 'a неверные данные\n'
        except:
            data_inerr = data_inerr + 'a неверные данные\n'

        

        
            
            
        data_in.type = self.type_group.checkedId()

        if data_in.type == 1:
            pass
        elif data_in.type == 2:
            try:
                if float(self.s2_le.text()) > 0:
                    data_in.s2 = float(self.s2_le.text())
                else:
                    data_inerr = data_inerr + 's2 неверные данные\n'
            except:
                data_inerr = data_inerr + 's2 неверные данные\n'

            try:
                if float(self.b2_le.text()) > 0:
                    data_in.b2 = int(self.b2_le.text())
                else:
                    data_inerr = data_inerr + 'b2 неверные данные\n'
            except:
                data_inerr = data_inerr + 'b2 неверные данные\n'

            try:
                if int(self.delta2_le.text()) > 0:
                    data_in.delta2 = int(self.delta2_le.text())
                else:
                    data_inerr = data_inerr + 'δ2 неверные данные\n'
            except:
                data_inerr = data_inerr + 'δ2 неверные данные\n'

        elif data_in.type == 3:
            pass

               
        if data_inerr == '':
            
            data_out = cc.calc_saddle(data_in)
            #self.d0_l.setText(f'd0={data_nozzleout.d0:.2f} мм')
            #self.pressd_l.setText(f'[p]={data_nozzleout.press_d:.2f} МПа')
            #self.b_l.setText(f'b={data_nozzleout.b:.2f} мм')
            #globalvar.elementdatayk.append(data_nozzlein)
            #globalvar.elementdatayk.append(data_nozzleout)
            globalvar.data_word.append([data_in, data_out])
            i = globalvar.word_lv.rowCount()
            globalvar.word_lv.insertRow(i)
            globalvar.word_lv.setData(globalvar.word_lv.index(i),f'{data_in.D} мм, {data_in.p} МПа, {data_in.temp} C, {data_in.met}')
            self.parent().lvCalc.setModel(globalvar.word_lv)
            self.pbCalc.setEnabled(True)
        else:
            dialog = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Error', data_inerr)
            result = dialog.exec()

                 

        
                   

    def closeEvent(self, event):
        self.parent().saddle = None

    def removeLay(self, lay):
        for i in reversed(range(lay.count())):
            widgetToRemove = lay.itemAt(i).widget()
            lay.removeWidget(widgetToRemove)
            widgetToRemove.setParent(None)

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

        self.diagostel_cb.setCurrentText(self.parent().D_le.text())
        self.diachange()

        self.sgostel_cb.setCurrentText(self.parent().s_le.text())
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
        l0 = int(self.parent().l0_le.text())
        self.parent().L_le.setText(str(2*int(self.h1gostel_le.text())+int(self.parent().Lob_le.text())))
        self.parent().e_le.setText(str(l0+int(self.h1gostel_le.text())))
        self.parent().a_le.setText(str(round(l0+int(self.h1gostel_le.text())+2/3*int(self.Hgostel_le.text()), 2)))
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
