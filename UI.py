import sys
from array import *
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize, Qt


class Window(QMainWindow):
    
    def __init__(self, parent = None):
        
        super().__init__(parent)
        self.main_widget = MAIN(parent=self)
        self.setCentralWidget(self.main_widget)
        self._createMenuBar()

    def _createMenuBar(self):
        menuBar = self.menuBar()
        
        self.fileMenu = QMenu("Меню", self)
        menuBar.addMenu(self.fileMenu)
        rec_action = QAction('Выдача рекомендаций', self)
        save_action = QAction('Сохраненные рекомендации', self)
        report_action = QAction('Сообщить об ошибках', self)
        
        self.fileMenu.addAction(rec_action)
        self.fileMenu.addAction(save_action)
        self.fileMenu.addAction(report_action)
        
        rec_action.triggered.connect(self.Main_menu)
        save_action.triggered.connect(self.Save_menu)
        report_action.triggered.connect(self.Report_menu)
        
        self.setGeometry(250, 200, 800, 720)
        self.setWindowTitle('ЭС')
        self.show()
        
    def Main_menu(self):
        self.main_widget = MAIN(parent=self)
        self.setCentralWidget(self.main_widget)
        
    def Save_menu(self):
        self.main_widget = SAVE(parent=self)
        self.setCentralWidget(self.main_widget)
         
    def Report_menu(self):
        self.main_widget = REPORT(parent=self)
        self.setCentralWidget(self.main_widget)
        
        
class SAVE(QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.initUI()
        

    def initUI(self):

        title = QLabel('                  \
                                   Сохраненные рекомендации')
        title.setFont(QFont('Times new roman', 16))

        space = QLabel('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        
        self.table = QTableWidget(self)  
        self.table.setColumnCount(5)     
        self.table.setRowCount(1)
        self.table.setHorizontalHeaderLabels(["Пол","Возраст","Заболевания","Показания", "Противопоказания"])
        self.table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(3).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(4).setTextAlignment(Qt.AlignHCenter)
        self.table.resizeColumnsToContents()

        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        
        self.hbox1.addWidget(title)
        self.hbox2.addWidget(self.table)
        self.hbox3.addWidget(space)
       
        self.vbox = QVBoxLayout()
        
      
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        
        self.setLayout(self.vbox)

class REPORT(QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.initUI()
        
    def initUI(self):

        title = QLabel('                  \
                                       Сообщить об ошибке')
        title.setFont(QFont('Times new roman', 16))

        space = QLabel('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\
                        \n\n\n\n\n\n\n\n\n\n\n\n')
        
        self.report = QLineEdit(self)
        self.report_btn = QPushButton('Отправить', self)

        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        
        self.hbox1.addWidget(title)
        self.hbox2.addWidget(self.report)
        self.hbox3.addWidget(self.report_btn)
        self.hbox3.addStretch(1)
        self.hbox4.addWidget(space)
       
        self.vbox = QVBoxLayout()
        
      
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)
        
        self.setLayout(self.vbox)



class DISEASES(QWidget):

    
    def __init__(self):
        super().__init__()

        self.DISEASES_UI()

    def DISEASES_UI(self):
        
        title = []
    
        self.vbox = QVBoxLayout()
        
        for i in range(count_d):

            title.append("Заболевание №{:d}: ".format(i+1))

            hbox = QHBoxLayout()
            label = QLabel(title[i])
            label.setFont(QFont('Times new roman', 14))
            hbox.addWidget(label)
            edit = QLineEdit(self)
            hbox.addWidget(edit)
            self.vbox.addLayout(hbox)
    
        self.setLayout(self.vbox)


class MAIN(QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.initUI()
        

    def initUI(self):
        
   
        title = QLabel('    \
                                   Расчет рекомендаций витаминов и добавок')
        title.setFont(QFont('Times new roman', 16))

        space = QLabel('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        
        gender = QLabel('Ваш пол: ')
        gender.setFont(QFont('Times new roman', 16))
        space1 = QLabel('                           \
                                                    \
                                                    \
                                                    ')
        space2 = QLabel('      \
                              \
                              \
                            ')
        
        age = QLabel('Ваш возраст: ')
        age.setFont(QFont('Times new roman', 16))
        age_n = QLineEdit(self)
        
        disease = QLabel('Количество хронических заболеваний: ')
        disease.setFont(QFont('Times new roman', 16))
        self.disease_n = QLineEdit(self)
        disease_btn = QPushButton('Принять', self)
        disease_btn.clicked.connect(self.count_disease)

        gender1 = QRadioButton('муж')
        gender1.setChecked(True)

        gender2 = QRadioButton('жен')

        button_group = QButtonGroup()
        button_group.addButton(gender1)
        button_group.addButton(gender2)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(gender)
        hbox1.addWidget(gender1)
        hbox1.addWidget(gender2)
        hbox1.addWidget(space1)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(age)
        hbox2.addWidget(age_n)
        hbox2.addWidget(space1)
        
        hbox3 = QHBoxLayout()
        hbox3.addWidget(disease)
        hbox3.addWidget(self.disease_n)
        hbox3.addWidget(disease_btn)
        hbox3.addWidget(space2)


        self.hbox4 = QHBoxLayout()
        self.mw = QScrollArea()
        self.hbox4.addWidget(self.mw)

      
        self.hbox5 = QHBoxLayout()
        self.hbox6 = QHBoxLayout()
        self.hbox7 = QHBoxLayout()
        self.hbox7.addStretch(1)

       
        self.vbox = QVBoxLayout()
        
        self.vbox.addWidget(title)
      
        self.vbox.addLayout(hbox1)
        self.vbox.addLayout(hbox2)
        self.vbox.addLayout(hbox3)
        self.vbox.addLayout(self.hbox4)
        self.vbox.addLayout(self.hbox5)
        self.vbox.addLayout(self.hbox6)
        self.vbox.addLayout(self.hbox7)
        
        self.vbox.addWidget(space)
        
        self.setLayout(self.vbox)
        
    def count_disease(self):

        global count_d
        count_d = int(self.disease_n.text())
        
        self.mw.setWidget(DISEASES())
         
        self.recomend = QPushButton('Выдать рекомендации', self)
        self.hbox5.addWidget(self.recomend)
        
        self.recomend.clicked.connect(self.rec_table)

    def rec_table(self):

        self.table = QTableWidget(self)  
        self.table.setColumnCount(2)     
        self.table.setRowCount(1)
        self.table.setHorizontalHeaderLabels(["Показания", "Противопоказания"])
        self.table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        self.table.resizeColumnsToContents()
        self.save = QPushButton('Сохранить рекомендации', self)
        
        self.hbox6.addWidget(self.table)
        self.hbox7.addWidget(self.save) 
                     

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
