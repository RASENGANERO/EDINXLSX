import sys
import os
from PyQt5 import Qt
from PyQt5.QtWidgets import (QWidget,QTextBrowser,QMessageBox,QGridLayout,QApplication,QPushButton,QFileDialog)
from PyQt5.QtCore import *
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.openFileButton = QPushButton("Открыть файлы")
        self.openFileButton.clicked.connect(self.getOpenFiles)
        self.FileHACK = QPushButton("Объединить и распарсить")
        self.FileHACK.clicked.connect(self.fileHack)
        self.grid = QGridLayout()
        self.setGeometry(250,250,777,257)
        self.setLayout(self.grid)
        self.br=QTextBrowser()
        self.grid.addWidget(self.openFileButton,1,0)
        self.grid.addWidget(self.br,2,0)
        self.grid.addWidget(self.FileHACK,4,0)
        self.files=list()
        self.dir=list()
        self.text=list()
        self.show()
        self.resize(740,480)
        self.setWindowTitle("FILEHACK")
    def getOpenFiles(self):
        self.br.clear()
        filenames,ok = QFileDialog.getOpenFileNames(self,
                             "Выберите несколько файлов",
                             "D:/",
                             "All Files(*.*)",)
        self.br.append("Ваши файлы:")
        for v in range(len(filenames)):            
            self.br.append(str(filenames[v]))
            self.files.append(str(filenames[v]))
    def fileHack(self):
        for v in range(len(self.files)):
            self.opened(str(self.files[v]))
            self.text.append("\n\n\n\n\n")
            self.br.append(str("Преобразован файл с номером : ")+str(v+1))
        self.deln()
        self.deleed(self.files)
        f=open("D:/FILIK.txt","w")
        for v in range(len(self.text)):
            f.write(self.text[v])
            f.write("\n")
            f.write("\n")
            f.write("\n")
        f.close()
        self.text.clear()
        self.br.clear()
        self.br.append("Файлы скомпанованы и находятся по пути: D:/FILIK.txt")
    def deleed(self,s):
        p=list()
        for v in range(len(s)):
            p.append(s[v])
        for v in range(len(p)):
            os.remove(p[v])
        p.clear()
        self.files.clear()
    def deln(self):
        for v in range(len(self.text)):
            r=self.text[v]
            r=str(r)
            r=r.replace("\n","")
            self.text[v]=r
    def opened(self,s):
        s=str(s)
        with open(s, "r") as file:
            try:
                for line in file:
                    self.text.append(str(line))
            except Exception:
                pass
    def dirHack(self):
        print("red")
    def closeEvent(self,event):
        reply = QMessageBox.question(self, "Внимание",
        "Вы хотите выйти из программы?",QMessageBox.Ok | QMessageBox.No,QMessageBox.No)
        if reply==QMessageBox.Ok:
            event.accept()
        else:
            event.ignore()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_()) 