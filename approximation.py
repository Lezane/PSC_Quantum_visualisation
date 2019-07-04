#!/usr/bin/env python
# coding: utf-8

# In[1]:


#We start by importing some useful packages.

import getpass, time
from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit
from qiskit import execute
from qiskit import IBMQ, Aer
import numpy as np
from numpy import binary_repr
import matplotlib.pyplot as plt
from cmath import *
from numpy import *

import math
from qiskit import execute, IBMQ

#we need to import ipyvolume to run these functions

import ipyvolume as ipv


# In[2]:


def convert_list_to_array(liste,a,b):
    tab= []
    for i in range(a):
        tab.append([])
        
    for i in range(a):
        for j in range(b):
            tab[i].append(liste[i*b+j])
    return np.asarray(tab)


# In[3]:


def convert_array_to_list(arr):
    a,b=arr.shape
    tab= []
    for i in range(a):
        for j in range(b):
            tab.append(arr[i][j])
    return tab


# In[4]:


def approximation_rank_1(liste,a,b):
    arr=convert_list_to_array(liste,a,b)
    u, s, vh = np.linalg.svd(arr, full_matrices=False)
    sbis = [0 for i in range(len(s))]
    sbis[0]=s[0]
    s0= np.diag(sbis)
    liste0= u@s0@vh
    return convert_array_to_list(liste0)


# In[5]:


def quantum_to_classic(qc):
    #we run a simulation of the quantum circuit and get the result
    backend = Aer.get_backend('statevector_simulator')
    job = execute(qc, backend)
    state_superposition = job.result().get_statevector(qc)
    return state_superposition


# In[6]:


def RCS(tab1,tab2):
    ## M : number total of bit
    #we will store all the points in these lists
    axeX,axeY,axeZ=[],[],[]
    
    #counter to know what sublot we are working on
    counter=0
    
    #the colors we use 
    listColors = ['red', 'blue']
    #list that will contain the points selected to be in a different color
    selected=[]
    
    #number of points to represent each state
    linePoints=1000
    for i in tab1:
        norm=(i.real**2)+(i.imag**2)
        
        for k in range(0,linePoints+1):
            axeX.append(0.5+np.sin(phase(i))*norm*k/linePoints)
            axeY.append(0.5+np.cos(phase(i))*norm*k/linePoints)
            #we put a state at each integer on the z axis
            #for no reason at all, it doesn't work when i only put "counter", i need to add the "k/(10000*Linepoints)" so the lines are not perfectly straight...
            axeZ.append(counter + k/(100000*linePoints))              
        counter+=1
    
    counter=0
    for i in tab2:
        norm=(i.real**2)+(i.imag**2)
        
        for k in range(0,linePoints+1):
            axeX.append(0.5+np.sin(phase(i))*norm*k/linePoints)
            axeY.append(0.5+np.cos(phase(i))*norm*k/linePoints)
            #we put a state at each integer on the z axis
            #for no reason at all, it doesn't work when i only put "counter", i need to add the "k/(10000*Linepoints)" so the lines are not perfectly straight...
            axeZ.append(counter + k/(100000*linePoints)) 
            selected.append(counter*linePoints + k)        
        counter+=1
    
    #we draw the z axis
    for k in range(linePoints):
        axeX.append(0.5)
        axeY.append(0.5)
        axeZ.append(k*counter/linePoints)
      
    ipv.quickscatter(array(axeX), array(axeY), array(axeZ), color='red', selected=selected,color_selected='blue', size_selected=1, size=1, marker="sphere")
    ipv.show()


# In[22]:


def distance(T0,T1):
    d=0
    for i in range(len(T0)):
        d+= (T0[i].real-T1[i].real)**2 + (T0[i].imag-T1[i].imag)**2
    return np.sqrt(d)* len(T1)


# In[40]:


# approximation_linear(data,  2^N) renvoie l'état séparable le plus proche avec N Qbits
def display(qc):
    T= quantum_to_classic(qc)
    print(len(T))
    T1= approximation_rank_1(T,2,len(T)//2)
    k,num,mind=1,1, distance(T,T1)
    while ( 2** k < len(T)-1):
        k+=1
        Tk = approximation_rank_1(T,(2**k),len(T)//(2**k))
        d= distance(T,Tk)
        if d < mind :
            num=k
            mind=d
    
    if (mind==0):
        print("separable state")
        print('first '+str(num)+' Q-Bits are separable from the rest')
    else:
        print("entangled state")
        print("here is its distance")
        print(mind)
        print("approximation supposing first "+str(num)+ " Q-Bits separable from the rest")
        
    Tbis= approximation_rank_1(T,2**num, len(T)//(2**num))
    RCS(T, Tbis)


# In[ ]:


print("finish importing approximation")

