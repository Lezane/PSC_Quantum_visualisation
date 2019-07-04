#!/usr/bin/env python
# coding: utf-8

# In[1]:


import getpass, time
from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit
from qiskit import BasicAer, execute
import numpy as np
from numpy import binary_repr
import matplotlib.pyplot as plt
from cmath import *


# In[7]:


# Each color correspond to a phase
def indicator():
    plt.rcParams['figure.figsize'] = [3, 3]
    theta = np.linspace(0, 2*np.pi, 300)
    x = np.cos(theta)
    y = np.sin(theta)
    Scolor=theta/(2*np.pi)
    plt.text(1, 0, 0, ha='center', fontsize=10)
    plt.text(0, -1, 'pi/2', ha='center', fontsize=10)
    plt.text(-1, 0, 'pi', ha='center', fontsize=10)
    plt.text(0, 1, '3*pi/2', ha='center', fontsize=10)
    plt.axis("equal")
    legend1 = plt.scatter(x, y, s=300, c = Scolor, cmap=plt.get_cmap("hsv"))
    return legend1


# In[10]:


#draw color bar for a quantum circuit
def display(qc):

    backend = BasicAer.get_backend('statevector_simulator')
    job = execute(qc, backend)
    state_superposition = job.result().get_statevector(qc)

    #length of the string of bits
    n=len(binary_repr(len(state_superposition)))-1
    
    plt.rcParams['figure.figsize'] = [n*3, 5]

    fig, ax = plt.subplots()
    ind = np.arange(1, len(state_superposition)+1)

    x = []
    statePhase = []
    barX = 3*n*ind
    titleList=[]
    
    counter=0
    cmap=plt.get_cmap("hsv")
    
    for i in state_superposition:
        title ="|"+binary_repr(counter,n)+">"
        titleList.append(title)
        x.append((i.real**2)+(i.imag**2))
        statePhase.append(cmap(phase(i)/(2*np.pi)))
        counter+=1
    
    bars = plt.bar(barX, x, width = n, color = statePhase)
    
    for i in range(len(state_superposition)):
        bars[i].set_height(x[i])
        if x[i]!=0:
            ax.text(barX[i], 1.05*x[i], '%.3f' % float(x[i]), ha='center', va='bottom', fontsize=8)
    
    
    ax.set_xticks(barX)
    ax.set_ylim([0., min([1.2, max([1.2 * val for val in x])])])
    ax.set_xticklabels(titleList, fontsize=12, rotation=70)
    ax.set_xlabel('State')
    ax.set_ylabel('Amplitude')
    ax.set_title('Color Bar')
    #plt.legend(legend1, 'phase')
    return plt


# In[14]:


print('finish importing colorBar')

