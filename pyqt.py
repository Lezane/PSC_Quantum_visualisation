#!/usr/bin/env python
# coding: utf-8

# # Vizualisation tools using PyQt5

# This notebook shows how to display a window with different vizualisation tools using PyQt5.

# In[1]:


import sys
import os
import random

import getpass, time
import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import BasicAer, execute
import pandas as pd
 
import numpy as np
from numpy import binary_repr
import matplotlib.pyplot as plt
from cmath import *
from math import *

from qiskit.tools.visualization import *

from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .circuit import ListSteps
from .colorBar import display as colorbar_display
from .dial_set import display as dial_set_display
from .dial_set_3d import display as dial_set_3d_display

# In[2]:


# Make sure that we are using QT5
import matplotlib
matplotlib.use('Qt5Agg')
progname=os.path.basename(sys.argv[0])
progversion = "0.1"


# We first define some useful functions.

# We define the classes that we use to diplay the matplotlib canvases.

# In[3]:


#Data processing for the entanglement canvas


# this is the case where the coefficients are complexe : coeff_1 + i* coeff_2
def createData(n,coeff_1, coeff_2):
    # number of states
    N = 2**n

    # name of qubits
    name = [str(x) for x in range(1,n+1)]   #1,2,3....n
    d = np.zeros((N,n))                     # data initialisation
    
    # initialise the indexes
    for j in range(N):
        binary_form = np.binary_repr(j,n)
        for i in range(n):
            d[j][i] = int(binary_form[i])        
     
    df = pd.DataFrame(d, columns = name).astype(int)
    # add real coeff
    df['coeff_1'] = coeff_1
    df['coeff_2'] = coeff_2
    df['state'] = [np.binary_repr(j,n) for j in range(N)]
    
    return df

def filter_data(data,n,i):
    t= len(n)
    j= np.binary_repr(i,t)
    for k in range(t):
        data = data[data[str(n[k])] != int(j[k])]
    return data


# In[4]:


#classes that we use to display the matplotlib canvases


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, circuit=None, width=5, height=4, dpi=100, m=None):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.qc = circuit
        self.m = m
        self.axes = fig.add_subplot(111)

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass




class DialSetMplCanvas(MyMplCanvas):
    
    def __init__(self,*args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        

    def compute_initial_figure(self):
        plt=dial_set_display(self.qc)
       

    
class DialSet3DMplCanvas(MyMplCanvas):
    
    def __init__(self,*args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        

    def compute_initial_figure(self):
        plt=dial_set_3d_display(self.qc)
    
            
class DialSetBarMplCanvas(MyMplCanvas):
    """Simple canvas with a sine plot."""
    
    def __init__(self,*args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        

    def compute_initial_figure(self):
        plt=colorbar_display(self.qc)


# This class displays the application window.

# In[5]:


#the class that display the application window

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self, qc):
        QtWidgets.QMainWindow.__init__(self)
        self.qc = qc
        
        #fenetre
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("Beautiful tools")
        
        

        self.file_menu = QtWidgets.QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)

        self.help_menu = QtWidgets.QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)

        self.help_menu.addAction('&About', self.about)
        self.help_menu.addAction('&Contact Us', self.contact)
        
        self.main_widget = QtWidgets.QWidget(self)
        
        self.layoutG = QtWidgets.QVBoxLayout(self.main_widget)
        layoutB = QtWidgets.QHBoxLayout(self.main_widget)
        
        #Title
        label = QtWidgets.QLabel(self)
        label.setText("Beautiful Tools Generator")
        label.setFont(QtGui.QFont('SansSerif', 20))
        self.layoutG.addWidget(label,  0, Qt.AlignCenter)
        
        #label.setAlignment(Qt.AlignCenter)
        
        #radio buttons
        layoutR = QtWidgets.QHBoxLayout(self.main_widget)
        self.b1 = QtWidgets.QRadioButton("2D Dial Set")
        self.b1.setChecked(True)
        layoutR.addWidget(self.b1, 0, Qt.AlignLeft )
        
        self.b2 = QtWidgets.QRadioButton("Color Bar")
        layoutR.addWidget(self.b2, 0, Qt.AlignCenter)
        
        self.b3 = QtWidgets.QRadioButton("3D Dial Set")
        layoutR.addWidget(self.b3, 0, Qt.AlignCenter)
        
        self.layoutG.addLayout(layoutR)
        
        #TextInput for entanglement
        self.EFrame = QtWidgets.QFrame()
        
        layoutE = QtWidgets.QHBoxLayout(self.main_widget)
            
        self.input1 = QtWidgets.QLineEdit(self)
        self.input1.setPlaceholderText("Input 1")
        self.input2 = QtWidgets.QLineEdit(self)
        self.input2.setPlaceholderText("Input 2")
        layoutE.addWidget(self.input1, 0, Qt.AlignLeft)
        layoutE.addWidget(self.input2, 0, Qt.AlignRight)
        
        self.EFrame.setLayout(layoutE)
        self.layoutG.addWidget(self.EFrame)
        self.EFrame.hide()
        
        
        
        #we first create the buttons
        listSteps = ListSteps(qc,0)
        button_number = len(listSteps)

        #on trouve la première étape
        firstStep = False
        firstStepNum = 0
        for i in range(button_number):
            if listSteps[i][:4]=='qc0.':
                if firstStep:
                    button = QtWidgets.QPushButton()
                    button.setText("Step "+str(i-firstStepNum+1))
                    #button.setText(listSteps[i])
                    button.setObjectName(str(i))
                    button.clicked.connect(self.on_button_clicked)
                    layoutB.addWidget(button)
                else :
                    firstStep = True
                    firstStepNum = i
                    button = QtWidgets.QPushButton()
                    button.setText("Step "+str(i-firstStepNum+1))
                    button.setObjectName(str(i))
                    button.clicked.connect(self.on_button_clicked)
                    layoutB.addWidget(button)
        
        layoutB.setContentsMargins(220, 0, 50, 0)
        self.layoutG.addLayout(layoutB)

        #we then display the circuit
        circuit_drawer(qc, scale=0.6 , output='mpl', filename='Circuit.jpg', interactive=False, justify='none')

        label = QtWidgets.QLabel(self)
        pixmap = QPixmap("Circuit.jpg")
        #pixmap2 = pixmap.scaledToWidth(64)
        label.setPixmap(pixmap)
        self.layoutG.addWidget(label)

        
        
        #sc = MyStaticMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        #dc = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        #layoutG.addWidget(sc)
        #layoutG.addWidget(dc)
        
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        

        self.statusBar().showMessage("All hail matplotlib!", 2000)
        
        #block window size
        self.setFixedSize(self.layoutG.sizeHint())
        
    def on_button_clicked(self):
        
        #get the id of the button 
        sending_button = self.main_widget.sender()
        i = int(sending_button.objectName())
        
        #get the corresponding qc0 Quantum circuit
        listSteps = ListSteps(self.qc,0)
        for j in range(i+1):
            print(listSteps[j])
            exec(listSteps[j])
        
        if(self.b1.isChecked()):
            #create a matplotlib class for visu
            exec('qc = DialSetMplCanvas(self.main_widget, circuit=qc0, width=5, height=4, dpi=100)')
            
        elif(self.b2.isChecked()):
            exec('qc = DialSetBarMplCanvas(self.main_widget, circuit=qc0, width=5, height=4, dpi=100)')
            
        else:
            exec('qc = DialSet3DMplCanvas(self.main_widget, circuit=qc0, width=5, height=4, dpi=100)')
        
        
    def on_radio_checked(self):
        if(self.b4.isChecked()):
            self.EFrame.show()
        else:
            self.EFrame.hide()
        
    def on_radio_unchecked(self):
        self.EFrame.hide()
        

    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()
        
    def contact(self):
        QtWidgets.QMessageBox.about(self, "Contact Us",
                                    """Feel free to contact us at : charles.gery@polytechnique.edu"""
                                )

    def about(self):
        QtWidgets.QMessageBox.about(self, "About",
                                    """Beautiful tools from Ecole Polytechnique"""
                                )


# In[6]:


def display(qc):
    qApp = QtWidgets.QApplication(sys.argv)
    aw = ApplicationWindow(qc)
    aw.setWindowTitle("%s" % progname)
    aw.show()
    sys.exit(qApp.exec_())
    #qApp.exec_()


# In[ ]:


print('finish importing pyqt')

