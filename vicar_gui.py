import sys
from PyQt5 import QtWidgets,QtGui,QtCore

# import vicar_xpsf as vicar
import vicar as vicar

import numpy as np
import matplotlib.pyplot as plt
import os

# python D:/github.com/SETI/pds-tools/vicar_gui.py

plotLog = True # 是否对数尺度显示

class VicarGUI(QtWidgets.QWidget):
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv) #没了这句话，QtWidget的__init__()就不会被调用
        super(VicarGUI, self).__init__()
        
        self.init()

        self.show()
        sys.exit(app.exec_()) #没了这句话窗口就只能闪现一下

    def init(self):
        ''''''
        # 窗口的基本属性 ↓
        self.setGeometry(200,100,350,300)
        self.setWindowTitle('VICAR GUI')
        # 窗口的基本属性 ↑

        # 存储所有控件的字典
        self.widget_dict = {}

        openFileButton=QtWidgets.QPushButton(self)
        openFileButton.setGeometry(100,100,150,50) # 右下角(250,150)
        openFileButton.setText('打开文件')
        openFileButton.clicked.connect(self.openFile)
        self.widget_dict['openFileButton'] = openFileButton

        self.dir = 'D:/'

    def disable(self, widget_name:str):
        '''禁用某个控件'''
        self.widget_dict[widget_name].setDisabled(True)

    def enable(self, widget_name:str):
        '''启用某个控件'''
        self.widget_dict[widget_name].setEnabled(True)

    def disableAll(self):
        '''禁用所有控件'''
        for widget in list(self.widget_dict.values()):
            widget.setDisabled(True)

    def enableAll(self):
        '''禁用所有控件'''
        for widget in list(self.widget_dict.values()):
            widget.setEnabled(True)

    def openFile(self):
        '''Slot of clicked openFileButton: open and show VICAR.'''
        self.disableAll() # 禁用其它控件

        chosen,fileType=QtWidgets.QFileDialog.getOpenFileName(self, caption='选择图片', directory=self.dir, filter='VICAR (*.img, *.IMG)')
        if chosen!='':
            self.dir = os.path.dirname(chosen)
            self.vicar_image = vicar.VicarImage.from_file(chosen)
            self.image = self.vicar_image.data_2d
            self.showImage()

        self.enableAll()

    def showImage(self):
        '''Show image.'''
        if plotLog:
            plt.imshow(np.log(self.image), cmap='gray')
        else:
            plt.imshow(self.image, cmap='gray')
        plt.show()

if True:
    VicarGUI()

if False: # dict的使用
    d={'a':1, 'b':2}
    v = d.values()
    print(type(v))
    print(list(v))
