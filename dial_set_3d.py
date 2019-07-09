#!/usr/bin/env python
# coding: utf-8

# In[2]:

%matplotlib widget
import getpass, time
from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit
from qiskit import BasicAer, execute
from qiskit.quantum_info import Pauli, state_fidelity, basis_state, process_fidelity
import numpy as np
from numpy import binary_repr
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from cmath import *
from numpy import *


# In[3]:


def display(qc):
    
    #we will store all the points in these lists
    axeX,axeY,axeZ=[],[],[]
    
    #we run a simulation of the quantum circuit and get the result
    backend = BasicAer.get_backend('statevector_simulator')
    job = execute(qc, backend)
    state_superposition = job.result().get_statevector(qc)

    #length of the string of bits
    n=len(binary_repr(len(state_superposition)))-1
    
    #counter to know what sublot we are working on
    counter=0
    
    #number of states we want in one color (the others will automaticly be in an another color)
    nstate=0
    #the colors we use 
    listColors = ['red', 'blue']
    #list that will contain the points selected to be in a different color
    selected=[]
    
    #number of points to represent each state
    linePoints=1000
    
    #for each state we draw a vector
    for i in state_superposition:
        
        norm=(i.real**2)+(i.imag**2)
        
        for k in range(0,linePoints+1):
            axeX.append(0.5+np.sin(phase(i))*norm*k/linePoints)
            axeY.append(0.5+np.cos(phase(i))*norm*k/linePoints)
            
            #we put a state at each integer on the z axis
            #for no reason at all, it doesn't work when i only put "counter", i need to add the "k/(10000*Linepoints)" so the lines are not perfectly straight...
            axeZ.append(counter) 
            
            #if this is a state we want to have in a different color, we add it to the selected list
            if counter < nstate:
                selected.append(counter*linePoints + k)
        
            axeX.append(0.5)
            axeY.append(0.5)
            axeZ.append(counter) 
        counter+=1
    
    #we draw the z axis
    for k in range(linePoints):
        axeX.append(0.5)
        axeY.append(0.5)
        axeZ.append(0)
    
    
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(axeX, axeY, axeZ)
    
    return plt

print("finish importing dial_set_3d")

