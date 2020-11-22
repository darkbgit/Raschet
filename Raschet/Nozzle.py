from PyQt5 import QtWidgets, uic, QtCore, QtGui
import data_fiz
import CalcClass
import globalvar

class Nozzle(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        uic.loadUi('NozzleForm.ui', self)

        self.vid_group = QtWidgets.QButtonGroup()
        self.vid_group.addButton(self.ykrb_1, 1)
        self.vid_group.addButton(self.ykrb_2, 2)
        self.vid_group.addButton(self.ykrb_3, 3)
        self.vid_group.addButton(self.ykrb_4, 4)
        self.vid_group.addButton(self.ykrb_5, 5)
        self.vid_group.addButton(self.ykrb_6, 6)
        self.vid_group.addButton(self.ykrb_7, 7)
        self.vid_group.addButton(self.ykrb_8, 8)

        self.vid_group.buttonToggled.connect(self.ykrb)

        self.steel1_cb.setModel(data_fiz.steelList)
        self.steel2_cb.setModel(data_fiz.steelList)
        self.steel3_cb.setModel(data_fiz.steelList)

        
        

        self.pbCancel.clicked.connect(self.hide)
        self.pbPredCalc.clicked.connect(self.pred_calc)
        self.pbCalc.clicked.connect(self.calc)
        

        if self.parent().typeElement == 'ob':
            self.placerb_1 = QtWidgets.QRadioButton('Радиальный')
            self.placerb_1.setChecked(True)
            self.placerb_1.toggled[bool].emit(False)
            self.placerb_2 = QtWidgets.QRadioButton('В плоскости\nпопер. сечения')
            self.placerb_3 = QtWidgets.QRadioButton('Смещенный')
            self.placerb_4 = QtWidgets.QRadioButton('Наклонный')
            self.placerb_group = QtWidgets.QButtonGroup()
            self.placerb_group.addButton(self.placerb_1, 1)
            self.placerb_group.addButton(self.placerb_2, 2)
            self.placerb_group.addButton(self.placerb_3, 3)
            self.placerb_group.addButton(self.placerb_4, 4)
            self.pic = QtWidgets.QLabel()
            self.pic.setScaledContents(True)
            self.grid = QtWidgets.QGridLayout()
            self.fr = QtWidgets.QFrame()
            self.grid.addWidget(self.placerb_1, 0, 0)
            self.grid.addWidget(self.placerb_2, 1, 0)
            self.grid.addWidget(self.placerb_3, 2, 0)
            self.grid.addWidget(self.placerb_4, 3, 0)
            self.grid.addWidget(self.fr, 4, 0)
            self.grid.addWidget(self.pic, 0, 1, 6, 1)
            self.grid1 = QtWidgets.QGridLayout()
            self.place_gb.setLayout(self.grid)
                        
            self.grid.addLayout(self.grid1, 5, 0)
            #self.placerb_group.buttonToggled.connect(self.place)
            self.placerb_1.toggled.connect(self.place)
            self.placerb_2.toggled.connect(self.place)
            self.placerb_3.toggled.connect(self.place)
            self.placerb_4.toggled.connect(self.place)

        elif self.parent().typeElement == 'kon':
            pass

        elif self.parent().typeElement == 'el':
            self.labsis = QtWidgets.QLabel('Система координат:')
            self.placepolar_rb = QtWidgets.QRadioButton('Полярная')
            self.placepolar_rb.setChecked(True)
            self.placedekart_rb = QtWidgets.QRadioButton('Декартова')
            self.rb_group1 = QtWidgets.QButtonGroup()
            self.rb_group1.addButton(self.placepolar_rb)
            self.rb_group1.addButton(self.placedekart_rb)
            

            self.placerb_1 = QtWidgets.QRadioButton('Радиальный')
            self.placerb_1.setChecked(True)
            self.placerb_1.toggled[bool].emit(False)
            self.placerb_2 = QtWidgets.QRadioButton('Вдоль оси')
            self.placerb_3 = QtWidgets.QRadioButton('Наклонный')
            self.placerb_group = QtWidgets.QButtonGroup()
            self.placerb_group.addButton(self.placerb_1, 1)
            self.placerb_group.addButton(self.placerb_2, 2)
            self.placerb_group.addButton(self.placerb_3, 3)
            
            self.pic = QtWidgets.QLabel()
            self.pic.setScaledContents(True)
            self.grid = QtWidgets.QGridLayout()
            self.fr = QtWidgets.QFrame()
            self.grid.addWidget(self.labsis, 0, 1)
            self.grid.addWidget(self.placepolar_rb, 0, 2)
            self.grid.addWidget(self.placedekart_rb, 0, 3)

            self.grid.addWidget(self.placerb_1, 1, 0)
            self.grid.addWidget(self.placerb_2, 2, 0)
            self.grid.addWidget(self.placerb_3, 3, 0)
            self.grid.addWidget(self.fr, 4, 0)
            self.grid.addWidget(self.pic, 1, 1, 6, 3)
            self.grid1 = QtWidgets.QGridLayout()
            self.place_gb.setLayout(self.grid)
                        
            self.grid.addLayout(self.grid1, 5, 0)

            #self.placerb_group.buttonToggled.connect(self.place)
            self.placerb_1.toggled.connect(self.place)
            self.placerb_2.toggled.connect(self.place)
            self.placerb_3.toggled.connect(self.place)

            self.placepolar_rb.toggled.connect(self.place)
            self.placedekart_rb.toggled.connect(self.place)
            



        
        self.placerb_1.toggled[bool].emit(False)

    def place(self):
        if self.parent().typeElement == 'ob':
            s = self.sender().text()
            if self.sender().isChecked():
               if s == 'Радиальный':
                   self.pic.setPixmap(QtGui.QPixmap('pic/Nozzle/CylRadial'))
                   
                   self.removeLay(self.grid1)
                   self.grid.update()
                   
                   lab1_1 = QtWidgets.QLabel('Смещение, Lш:')
                   lineEdit1 = QtWidgets.QLineEdit()
                   lineEdit1.setMaximumHeight(20)
                   lab1_2 = QtWidgets.QLabel('м')

                   lab2_1 = QtWidgets.QLabel('Угол смещения оси, θ:')
                   lineEdit2 = QtWidgets.QLineEdit()
                   lineEdit2.setMaximumHeight(20)
                   lab2_2 = QtWidgets.QLabel('°')

                   self.grid1.addWidget(lab1_1, 0, 0, 1, 2)
                   self.grid1.addWidget(lineEdit1, 1, 0)
                   self.grid1.addWidget(lab1_2, 1, 1)

                   self.grid1.addWidget(lab2_1, 2, 0, 1, 2)
                   self.grid1.addWidget(lineEdit2, 3, 0)
                   self.grid1.addWidget(lab2_2, 3, 1)
                                                        
               elif s == 'В плоскости\nпопер. сечения':
                   self.pic.setPixmap(QtGui.QPixmap('pic/Nozzle/CylAxial'))

                   self.removeLay(self.grid1)
                   self.grid.update()

                   lab1_1 = QtWidgets.QLabel('Смещение, Lш:')
                   lineEdit1 = QtWidgets.QLineEdit()
                   lineEdit1.setMaximumHeight(20)
                   lab1_2 = QtWidgets.QLabel('м')

                   lab2_1 = QtWidgets.QLabel('Угол смещения оси, θ:')
                   lineEdit2 = QtWidgets.QLineEdit()
                   lineEdit2.setMaximumHeight(20)
                   lab2_2 = QtWidgets.QLabel('°')

                   lab3_1 = QtWidgets.QLabel('Угол, ψ:')
                   lineEdit3 = QtWidgets.QLineEdit()
                   lineEdit3.setMaximumHeight(20)
                   lab3_2 = QtWidgets.QLabel('°')

                   lab4_1 = QtWidgets.QLabel('Смещение, t:')
                   lineEdit4 = QtWidgets.QLineEdit()
                   lineEdit4.setMaximumHeight(20)
                   lab4_2 = QtWidgets.QLabel('мм')

                   self.grid1.addWidget(lab1_1, 0, 0, 1, 2)
                   self.grid1.addWidget(lineEdit1, 1, 0)
                   self.grid1.addWidget(lab1_2, 1, 1)

                   self.grid1.addWidget(lab2_1, 2, 0, 1, 2)
                   self.grid1.addWidget(lineEdit2, 3, 0)
                   self.grid1.addWidget(lab2_2, 3, 1)

                   self.grid1.addWidget(lab3_1, 4, 0, 1, 2)
                   self.grid1.addWidget(lineEdit3, 5, 0)
                   self.grid1.addWidget(lab3_2, 5, 1)

                   self.grid1.addWidget(lab4_1, 6, 0, 1, 2)
                   self.grid1.addWidget(lineEdit4, 7, 0)
                   self.grid1.addWidget(lab4_2, 7, 1)

               elif s == 'Смещенный':
                   self.pic.setPixmap(QtGui.QPixmap('pic/Nozzle/CylOffset'))
                   
                   self.removeLay(self.grid1)
                   self.grid.update()

                   lab1_1 = QtWidgets.QLabel('Смещение, Lш:')
                   lineEdit1 = QtWidgets.QLineEdit()
                   lineEdit1.setMaximumHeight(20)
                   lab1_2 = QtWidgets.QLabel('м')

                   lab2_1 = QtWidgets.QLabel('Угол смещения оси, θ:')
                   lineEdit2 = QtWidgets.QLineEdit()
                   lineEdit2.setMaximumHeight(20)
                   lab2_2 = QtWidgets.QLabel('°')

                   lab3_1 = QtWidgets.QLabel('Смещение, lсм:')
                   lineEdit3 = QtWidgets.QLineEdit()
                   lineEdit3.setMaximumHeight(20)
                   lab3_2 = QtWidgets.QLabel('мм')

                   self.grid1.addWidget(lab1_1, 0, 0, 1, 2)
                   self.grid1.addWidget(lineEdit1, 1, 0)
                   self.grid1.addWidget(lab1_2, 1, 1)

                   self.grid1.addWidget(lab2_1, 2, 0, 1, 2)
                   self.grid1.addWidget(lineEdit2, 3, 0)
                   self.grid1.addWidget(lab2_2, 3, 1)

                   self.grid1.addWidget(lab3_1, 4, 0, 1, 2)
                   self.grid1.addWidget(lineEdit3, 5, 0)
                   self.grid1.addWidget(lab3_2, 5, 1)

                   
               elif s == 'Наклонный':
                   self.pic.setPixmap(QtGui.QPixmap('pic/Nozzle/CylTilted'))
                   
                   self.removeLay(self.grid1)
                   self.grid.update()

                   lab1_1 = QtWidgets.QLabel('Смещение, Lш:')
                   lineEdit1 = QtWidgets.QLineEdit()
                   lineEdit1.setMaximumHeight(20)
                   lab1_2 = QtWidgets.QLabel('м')

                   lab2_1 = QtWidgets.QLabel('Угол смещения оси, θ:')
                   lineEdit2 = QtWidgets.QLineEdit()
                   lineEdit2.setMaximumHeight(20)
                   lab2_2 = QtWidgets.QLabel('°')

                   lab3_1 = QtWidgets.QLabel('Угол наклона оси, γ:')
                   lineEdit3 = QtWidgets.QLineEdit()
                   lineEdit3.setMaximumHeight(20)
                   lab3_2 = QtWidgets.QLabel('°')

                   lab4_1 = QtWidgets.QLabel('Угол отклонения оси, ω:')
                   lineEdit4 = QtWidgets.QLineEdit()
                   lineEdit4.setMaximumHeight(20)
                   lab4_2 = QtWidgets.QLabel('°')

                   self.grid1.addWidget(lab1_1, 0, 0, 1, 2)
                   self.grid1.addWidget(lineEdit1, 1, 0)
                   self.grid1.addWidget(lab1_2, 1, 1)

                   self.grid1.addWidget(lab2_1, 2, 0, 1, 2)
                   self.grid1.addWidget(lineEdit2, 3, 0)
                   self.grid1.addWidget(lab2_2, 3, 1)

                   self.grid1.addWidget(lab3_1, 4, 0, 1, 2)
                   self.grid1.addWidget(lineEdit3, 5, 0)
                   self.grid1.addWidget(lab3_2, 5, 1)

                   self.grid1.addWidget(lab4_1, 6, 0, 1, 2)
                   self.grid1.addWidget(lineEdit4, 7, 0)
                   self.grid1.addWidget(lab4_2, 7, 1)

        elif self.parent().typeElement == 'kon':
            pass

        elif self.parent().typeElement == 'el':
            s = self.sender().text()
            if self.sender().isChecked():
                self.removeLay(self.grid1)
                self.grid.update()
                if s == 'Радиальный':
                    if self.placepolar_rb.isChecked():
                        self.ellRadial()
                    else:
                        self.ellRadialDekart()
                                                       
                elif s == 'Вдоль оси':
                    if self.placepolar_rb.isChecked():
                        self.ellVert()
                    else:
                        self.ellVertDekart()
                                                        
                elif s == 'Наклонный':
                    if self.placepolar_rb.isChecked():
                        self.ellTilted()
                    else:
                        self.ellTitledDekart()

                elif s == 'Полярная':
                    if self.placerb_1.isChecked():
                        self.ellRadial()
                    elif self.placerb_2.isChecked():
                        self.ellVert()
                    elif self.placerb_3.isChecked():
                        self.ellTilted()

                elif s == 'Декартова':
                    if self.placerb_1.isChecked():
                        self.ellRadialDekart()
                    elif self.placerb_2.isChecked():
                        self.ellVertDekart()
                    elif self.placerb_3.isChecked():
                        self.ellTiltedDekart()
                   

    def ykrb(self, int):
        self.yk_l.setPixmap(QtGui.QPixmap('pic/Nozzle/Nozzle' + str(self.vid_group.checkedId())))

    def removeLay(self, lay):
        for i in reversed(range(lay.count())):
            widgetToRemove = lay.itemAt(i).widget()
            lay.removeWidget(widgetToRemove)
            widgetToRemove.setParent(None)


    def closeEvent(self, event):
        self.parent().nozzleWin = None

    def pred_calc(self):
        self.data[0].yk = True
        data_in = self.data[0]
        data_out = self.data[1]
        data_nozzlein = CalcClass.data_nozzlein()
        data_nozzleout = CalcClass.data_nozzleout()

        cc = CalcClass.CalcClass()

        data_inerr = str('')

        #try:
        #    if int(self.temp_le.text()) in range (20, 1000):
        #        data_in.temp = int(self.temp_le.text())
        #    else:
        #        data_inerr = data_inerr + 'T должна быть в диапазоне 20 - 1000\n'
        #except:
        #    data_inerr = data_inerr + 'T должна быть в диапазоне 20 - 1000\n'

        data_nozzlein.steel1 = self.steel1_cb.currentText()

        if data_inerr == '':
            self.sigma1_le.setReadOnly = False
            self.sigma1_le.setText(str(cc.get_sigma(data_nozzlein.steel1, data_in.temp)))
            self.sigma1_le.setReadOnly = True
            try:
                data_nozzlein.sigma_d1 = float(self.sigma1_le.text())
            except:
                data_inerr = data_inerr + '[σ] неверные данные\n'

            if self.vn_rbyk.isChecked():
                data_nozzlein.dav = 'vn'
            else:
                data_nozzlein.dav = 'nar'
                
                self.E1_le.setReadOnly = False
                self.E1_le.setText(str(cc.get_E(data_nozzlein.steel1, data_in.temp)))
                self.E1_le.setReadOnly = True
                
                try:
                    data_nozzlein.E1 = float(self.E1_le.text())
                except:
                    data_inerr = data_inerr + 'E неверные данные\n'
        

                #try:
                #    if float(self.l_leob.text()) > 0:
                #        data_in.l = float(self.l_leob.text())
                #    else:
                #        data_inerr = data_inerr + 'l неверные данные\n'
                #except:
                #    data_inerr = data_inerr + 'l неверные данные\n'

               
        #try:
        #    if float(self.press_le.text()) > 0 and float(self.press_le.text()) < 1000:
        #        data_in.press = float(self.press_le.text())
        #    else:
        #        data_inerr = data_inerr + 'p должно быть в диапазоне 0 - 1000\n'
        #except:
        #    data_inerr = data_inerr + 'p должно быть в диапазоне 0 - 1000\n'

        
        try:
            if int(self.dia_le.text()) > 0:
                data_nozzlein.dia = int(self.dia_le.text())
            else:
                data_inerr = data_inerr + 'D неверные данные\n'
        except:
            data_inerr = data_inerr + 'D неверные данные\n'

        try:
            if float(self.s1_le.text()) > 0:
                data_nozzlein.s1 = float(self.s1_le.text())
            else:
                data_inerr = data_inerr + 's1 неверные данные\n'
        except:
            data_inerr = data_inerr + 's1 неверные данные\n'

        try:
            if float(self.cs_le.text()) >= 0:
                data_nozzlein.cs = float(self.cs_le.text())
            else:
                data_inerr = data_inerr + 'cs неверные данные\n'
        except:
            data_inerr = data_inerr + 'cs неверные данные\n'

        try:
            if float(self.cs1_le.text()) >= 0:
                data_nozzlein.cs1 = float(self.cs1_le.text())
            else:
                data_inerr = data_inerr + 'cs1 неверные данные\n'
        except:
            data_inerr = data_inerr + 'cs1 неверные данные\n'

        try:
            if int(self.l1_le.text()) >= 0:
                data_nozzlein.l1 = int(self.l1_le.text())
            else:
                data_inerr = data_inerr + 'l1 неверные данные\n'
        except:
            data_inerr = data_inerr + 'l1 неверные данные\n'

        data_nozzlein.steel2 = self.steel2_cb.currentText()

        try:
            if int(self.l2_le.text()) >= 0:
                data_nozzlein.l2 = int(self.l2_le.text())
            else:
                data_inerr = data_inerr + 'l2 неверные данные\n'
        except:
            data_inerr = data_inerr + 'l2 неверные данные\n'

        try:
            if float(self.s2_le.text()) >= 0:
                data_nozzlein.s2 = float(self.s2_le.text())
            else:
                data_inerr = data_inerr + 's2 неверные данные\n'
        except:
            data_inerr = data_inerr + 's2 неверные данные\n'

        data_nozzlein.steel3 = self.steel3_cb.currentText()

        try:
            if int(self.l3_le.text()) >= 0:
                data_nozzlein.l3 = int(self.l3_le.text())
            else:
                data_inerr = data_inerr + 'l3 неверные данные\n'
        except:
            data_inerr = data_inerr + 'l3 неверные данные\n'

        try:
            if float(self.s3_le.text()) >= 0:
                data_nozzlein.s3 = float(self.s3_le.text())
            else:
                data_inerr = data_inerr + 's3 неверные данные\n'
        except:
            data_inerr = data_inerr + 's3 неверные данные\n'

        try:
            if float(self.fi_le.text()) > 0 and float(self.fi_le.text()) <= 1:
                data_nozzlein.fi = float(self.fi_le.text())
            else:
                data_inerr = data_inerr + 'fi должен быть в диапазоне 0 - 1\n'
        except:
            data_inerr = data_inerr + 'fi должен быть в диапазоне 0 - 1\n'

        try:
            if float(self.fi1_le.text()) > 0 and float(self.fi1_le.text()) <= 1:
                data_nozzlein.fi1 = float(self.fi1_le.text())
            else:
                data_inerr = data_inerr + 'fi1 должен быть в диапазоне 0 - 1\n'
        except:
            data_inerr = data_inerr + 'fi1 должен быть в диапазоне 0 - 1\n'

        try:
            if float(self.delta_le.text()) >= 0:
                data_nozzlein.delta = int(self.delta_le.text())
            else:
                data_inerr = data_inerr + 'delta должен быть в диапазоне 0 - \n'
        except:
            data_inerr = data_inerr + 'delta должен быть в диапазоне 0 - 1\n'

        try:
            if float(self.delta1_le.text()) >= 0:
                data_nozzlein.delta1 = int(self.delta1_le.text())
            else:
                data_inerr = data_inerr + 'delta1 должен быть в диапазоне 0 - \n'
        except:
            data_inerr = data_inerr + 'delta1 должен быть в диапазоне 0 - 1\n'

        try:
            if float(self.delta2_le.text()) >= 0:
                data_nozzlein.delta2 = int(self.delta2_le.text())
            else:
                data_inerr = data_inerr + 'delta2 должен быть в диапазоне 0 - \n'
        except:
            data_inerr = data_inerr + 'delta2 должен быть в диапазоне 0 - 1\n'

        data_nozzlein.vid = self.vid_group.checkedId()
        data_nozzlein.place = self.placerb_group.checkedId()
        
        if data_inerr == '':
            
            data_nozzleout = cc.calc_nozzle(data_in, data_out, data_nozzlein)
            self.d0_l.setText(f'd0={data_nozzleout.d0:.2f} мм')
            self.pressd_l.setText(f'[p]={data_nozzleout.press_d:.2f} МПа')
            self.b_l.setText(f'b={data_nozzleout.b:.2f} мм')
            #globalvar.elementdatayk.append(data_nozzlein)
            #globalvar.elementdatayk.append(data_nozzleout)
            globalvar.data_word.append([data_in, data_out, data_nozzlein, data_nozzleout])
            i = globalvar.word_lv.rowCount()
            globalvar.word_lv.insertRow(i)
            globalvar.word_lv.setData(globalvar.word_lv.index(i),f'{data_in.dia} мм, {data_in.press} МПа, {data_in.temp} C, {data_in.met}, {data_in.yk}')
            self.parent().parent().lvCalc.setModel(globalvar.word_lv)
            self.pbCalc.setEnabled(True)
        else:
            dialog = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Error', data_inerr)
            result = dialog.exec()

    def calc(self):
        pass

    def ellRadial(self):
        self.pic.setPixmap(QtGui.QPixmap('pic/Nozzle/EllRadial'))

        lab1_1 = QtWidgets.QLabel('Смещение, Rш:')
        lineEdit1 = QtWidgets.QLineEdit()
        lineEdit1.setMaximumHeight(20)
        lab1_2 = QtWidgets.QLabel('мм')

        lab2_1 = QtWidgets.QLabel('Угол смещения\nоси, θ:')
        lineEdit2 = QtWidgets.QLineEdit()
        lineEdit2.setMaximumHeight(20)
        lab2_2 = QtWidgets.QLabel('°')

        self.grid1.addWidget(lab1_1, 0, 0, 1, 2)
        self.grid1.addWidget(lineEdit1, 1, 0)
        self.grid1.addWidget(lab1_2, 1, 1)

        self.grid1.addWidget(lab2_1, 2, 0, 1, 2)
        self.grid1.addWidget(lineEdit2, 3, 0)
        self.grid1.addWidget(lab2_2, 3, 1)

    def ellRadialDekart(self):
        self.pic.setPixmap(QtGui.QPixmap('pic/Nozzle/EllRadialDekart'))

        lab1_1 = QtWidgets.QLabel('Координата, x0:')
        lineEdit1 = QtWidgets.QLineEdit()
        lineEdit1.setMaximumHeight(20)
        lab1_2 = QtWidgets.QLabel('мм')

        lab2_1 = QtWidgets.QLabel('Координата, y0:')
        lineEdit2 = QtWidgets.QLineEdit()
        lineEdit2.setMaximumHeight(20)
        lab2_2 = QtWidgets.QLabel('°')

        self.grid1.addWidget(lab1_1, 0, 0, 1, 2)
        self.grid1.addWidget(lineEdit1, 1, 0)
        self.grid1.addWidget(lab1_2, 1, 1)

        self.grid1.addWidget(lab2_1, 2, 0, 1, 2)
        self.grid1.addWidget(lineEdit2, 3, 0)
        self.grid1.addWidget(lab2_2, 3, 1)

    def ellVert(self):
        self.pic.setPixmap(QtGui.QPixmap('pic/Nozzle/EllVert'))

        lab1_1 = QtWidgets.QLabel('Смещение, Rш:')
        lineEdit1 = QtWidgets.QLineEdit()
        lineEdit1.setMaximumHeight(20)
        lab1_2 = QtWidgets.QLabel('мм')

        lab2_1 = QtWidgets.QLabel('Угол смещения\nоси, θ:')
        lineEdit2 = QtWidgets.QLineEdit()
        lineEdit2.setMaximumHeight(20)
        lab2_2 = QtWidgets.QLabel('°')

        self.grid1.addWidget(lab1_1, 0, 0, 1, 2)
        self.grid1.addWidget(lineEdit1, 1, 0)
        self.grid1.addWidget(lab1_2, 1, 1)

        self.grid1.addWidget(lab2_1, 2, 0, 1, 2)
        self.grid1.addWidget(lineEdit2, 3, 0)
        self.grid1.addWidget(lab2_2, 3, 1)

    def ellVertDekart(self):
        self.pic.setPixmap(QtGui.QPixmap('pic/Nozzle/EllVertDekart'))

        lab1_1 = QtWidgets.QLabel('Координата, x0:')
        lineEdit1 = QtWidgets.QLineEdit()
        lineEdit1.setMaximumHeight(20)
        lab1_2 = QtWidgets.QLabel('мм')

        lab2_1 = QtWidgets.QLabel('Координата, y0:')
        lineEdit2 = QtWidgets.QLineEdit()
        lineEdit2.setMaximumHeight(20)
        lab2_2 = QtWidgets.QLabel('°')

        self.grid1.addWidget(lab1_1, 0, 0, 1, 2)
        self.grid1.addWidget(lineEdit1, 1, 0)
        self.grid1.addWidget(lab1_2, 1, 1)

        self.grid1.addWidget(lab2_1, 2, 0, 1, 2)
        self.grid1.addWidget(lineEdit2, 3, 0)
        self.grid1.addWidget(lab2_2, 3, 1)

    def ellTilted(self):
        self.pic.setPixmap(QtGui.QPixmap('pic/Nozzle/EllTilted'))

        lab1_1 = QtWidgets.QLabel('Смещение, Rш:')
        lineEdit1 = QtWidgets.QLineEdit()
        lineEdit1.setMaximumHeight(20)
        lab1_2 = QtWidgets.QLabel('мм')

        lab2_1 = QtWidgets.QLabel('Угол смещения\nоси, θ:')
        lineEdit2 = QtWidgets.QLineEdit()
        lineEdit2.setMaximumHeight(20)
        lab2_2 = QtWidgets.QLabel('°')

        lab3_1 = QtWidgets.QLabel('Угол наклона\nоси, γ:')
        lineEdit3 = QtWidgets.QLineEdit()
        lineEdit3.setMaximumHeight(20)
        lab3_2 = QtWidgets.QLabel('°')

        self.grid1.addWidget(lab1_1, 0, 0, 1, 2)
        self.grid1.addWidget(lineEdit1, 1, 0)
        self.grid1.addWidget(lab1_2, 1, 1)

        self.grid1.addWidget(lab2_1, 2, 0, 1, 2)
        self.grid1.addWidget(lineEdit2, 3, 0)
        self.grid1.addWidget(lab2_2, 3, 1)

        self.grid1.addWidget(lab3_1, 4, 0, 1, 2)
        self.grid1.addWidget(lineEdit3, 5, 0)
        self.grid1.addWidget(lab3_2, 5, 1)

    def ellTiltedDekart(self):
        self.pic.setPixmap(QtGui.QPixmap('pic/Nozzle/EllTiltedDekart'))

        lab1_1 = QtWidgets.QLabel('Координата, x0:')
        lineEdit1 = QtWidgets.QLineEdit()
        lineEdit1.setMaximumHeight(20)
        lab1_2 = QtWidgets.QLabel('мм')

        lab2_1 = QtWidgets.QLabel('Координата, y0:')
        lineEdit2 = QtWidgets.QLineEdit()
        lineEdit2.setMaximumHeight(20)
        lab2_2 = QtWidgets.QLabel('°')
                       
        lab3_1 = QtWidgets.QLabel('Угол наклона\nоси, γ:')
        lineEdit3 = QtWidgets.QLineEdit()
        lineEdit3.setMaximumHeight(20)
        lab3_2 = QtWidgets.QLabel('°')

        self.grid1.addWidget(lab1_1, 0, 0, 1, 2)
        self.grid1.addWidget(lineEdit1, 1, 0)
        self.grid1.addWidget(lab1_2, 1, 1)

        self.grid1.addWidget(lab2_1, 2, 0, 1, 2)
        self.grid1.addWidget(lineEdit2, 3, 0)
        self.grid1.addWidget(lab2_2, 3, 1)

        self.grid1.addWidget(lab3_1, 4, 0, 1, 2)
        self.grid1.addWidget(lineEdit3, 5, 0)
        self.grid1.addWidget(lab3_2, 5, 1)
