from PyQt5 import QtWidgets, uic, QtCore

class Fi(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
       
        self.setMinimumSize(QtCore.QSize(706, 410))             # Устанавливаем размеры
        self.setWindowTitle('Коэффициент прочности сварного шва')    # Устанавливаем заголовок окна
        
        grid_layout = QtWidgets.QGridLayout()             # Создаём QGridLayout
        self.setLayout(grid_layout)   # Устанавливаем данное размещение в центральный виджет
 
        
        self.table = QtWidgets.QTableWidget(self)  # Создаём таблицу
        self.table.setColumnCount(3)     # Устанавливаем три колонки
        self.table.setRowCount(7)        # и одну строку в таблице
 
        # Устанавливаем заголовки таблицы
        self.table.setHorizontalHeaderLabels(['Вид сварного шва\nи способ сварки', 'Коэффициент прочности\nдля сосудов и аппаратов', 'сварных швов\nиз стали и сплавов'])
         
        # Устанавливаем выравнивание на заголовки
        self.table.horizontalHeaderItem(0).setTextAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignHCenter)
        self.table.horizontalHeaderItem(1).setTextAlignment(QtCore.Qt.AlignRight)
        self.table.horizontalHeaderItem(2).setTextAlignment(QtCore.Qt.AlignLeft)
 
        
        # заполняем первую строку
        self.table.setItem(0, 0, QtWidgets.QTableWidgetItem(''))
        self.table.item(0, 0).setFlags(QtCore.Qt.ItemIsEnabled)
        self.table.setItem(0, 1, QtWidgets.QTableWidgetItem('Длина контролируемых\nшвов от общей длины\nсостовляет 100%'))
        self.table.item(0, 1).setFlags(QtCore.Qt.ItemIsEnabled)
        self.table.setItem(0, 2, QtWidgets.QTableWidgetItem('Длина контролируемых\nшвов от общей длины\nсостовляет\nот 10% до 50%'))
        self.table.item(0, 2).setFlags(QtCore.Qt.ItemIsEnabled)

        self.table.setItem(1, 0, QtWidgets.QTableWidgetItem('Стыковой двусторонний с полным проплавлением или угловой\nдвусторонний с полным проплавлением таврового соединения,\nвыполняемый автоматической и полуавтоматической сваркой'))
        self.table.item(1, 0).setFlags(QtCore.Qt.ItemIsEnabled)
        self.table.setItem(1, 1, QtWidgets.QTableWidgetItem('1.0'))
        self.table.item(1, 1).setFlags(QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable)
        self.table.item(1, 1).setTextAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignHCenter)
        self.table.setItem(1, 2, QtWidgets.QTableWidgetItem('0.9'))
        self.table.item(1, 2).setFlags(QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable)
        self.table.item(1, 2).setTextAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignHCenter)

        self.table.setItem(2, 0, QtWidgets.QTableWidgetItem('Стыковой с подваркой корня шва с полным проплавлением или\nугловой двусторонний с полным проплавлением таврового\n соединения, выполняемый вручную'))
        self.table.item(2, 0).setFlags(QtCore.Qt.ItemIsEnabled)
        self.table.setItem(2, 1, QtWidgets.QTableWidgetItem('1.0'))
        self.table.item(2, 1).setFlags(QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable)
        self.table.item(2, 1).setTextAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignHCenter)
        self.table.setItem(2, 2, QtWidgets.QTableWidgetItem('0.9'))
        self.table.item(2, 2).setFlags(QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable)
        self.table.item(2, 2).setTextAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignHCenter)

        self.table.setItem(3, 0, QtWidgets.QTableWidgetItem('Стыковой шов, доступный сварке только с одной стороны и\nимеющий в процессе сварки металлическую подкладку со стороны\n корня шва, прилегающую по всей длине шва к основному металлу'))
        self.table.item(3, 0).setFlags(QtCore.Qt.ItemIsEnabled)
        self.table.setItem(3, 1, QtWidgets.QTableWidgetItem('0.9'))
        self.table.item(3, 1).setFlags(QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable)
        self.table.item(3, 1).setTextAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignHCenter)
        self.table.setItem(3, 2, QtWidgets.QTableWidgetItem('0.8'))
        self.table.item(3, 2).setFlags(QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable)
        self.table.item(3, 2).setTextAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignHCenter)

        self.table.setItem(4, 0, QtWidgets.QTableWidgetItem('Угловой двусторонний с неполным проплавлением\nтаврового соединения'))
        self.table.item(4, 0).setFlags(QtCore.Qt.ItemIsEnabled)
        self.table.setItem(4, 1, QtWidgets.QTableWidgetItem('0.8'))
        self.table.item(4, 1).setFlags(QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable)
        self.table.item(4, 1).setTextAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignHCenter)
        self.table.setItem(4, 2, QtWidgets.QTableWidgetItem('0.65'))
        self.table.item(4, 2).setFlags(QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable)
        self.table.item(4, 2).setTextAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignHCenter)

        self.table.setItem(5, 0, QtWidgets.QTableWidgetItem('Стыковой, выполняемый автоматической и полуавтоматической\nсваркой с одной стороны с флюсовой или керамической\nподкладкой'))
        self.table.item(5, 0).setFlags(QtCore.Qt.ItemIsEnabled)
        self.table.setItem(5, 1, QtWidgets.QTableWidgetItem('0.9'))
        self.table.item(5, 1).setFlags(QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable)
        self.table.item(5, 1).setTextAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignHCenter)
        self.table.setItem(5, 2, QtWidgets.QTableWidgetItem('0.8'))
        self.table.item(5, 2).setFlags(QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable)
        self.table.item(5, 2).setTextAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignHCenter)

        self.table.setItem(6, 0, QtWidgets.QTableWidgetItem('Стыковой, выполняемый вручную с одной стороны'))
        self.table.item(6, 0).setFlags(QtCore.Qt.ItemIsEnabled)
        self.table.setItem(6, 1, QtWidgets.QTableWidgetItem('0.9'))
        self.table.item(6, 1).setFlags(QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable)
        self.table.item(6, 1).setTextAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignHCenter)
        self.table.setItem(6, 2, QtWidgets.QTableWidgetItem('0.65'))
        self.table.item(6, 2).setFlags(QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable)
        self.table.item(6, 2).setTextAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignHCenter)

        self.table.verticalHeader().setVisible(False)
        
 
        # делаем ресайз колонок по содержимому
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
        
        self.table.item(0, 1).setFlags(QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable) 
        
        self.table.itemDoubleClicked.connect(self.dblClick)
 
        grid_layout.addWidget(self.table, 0, 0)   # Добавляем таблицу в сетку

        self.pbCancel = QtWidgets.QPushButton(self)
        self.pbCancel.setMinimumSize(QtCore.QSize(50, 20))
        self.pbCancel.setText('Cancel')
        self.pbCancel.clicked.connect(self.close)
        grid_layout.addWidget(self.pbCancel)



        

    def closeEvent(self, event):
        self.parent().fiWin = None

    def dblClick(self):
        if self.table.currentItem().isSelected():
            self.parent().fi_le.setText(self.table.currentItem().text())
        self.close()
            #print(self.table.item(self.table.currentRow(), self.table.currentColumn()).text())

    
