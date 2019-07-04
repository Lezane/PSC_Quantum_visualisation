#!/usr/bin/env python
# coding: utf-8

# # Dial Set Visualization

# We start by importing some useful packages.

# In[1]:


import getpass, time
import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import BasicAer, execute
 
import numpy as np
from numpy import binary_repr
import matplotlib.pyplot as plt
from cmath import *
from math import *
from tkinter import * 
from PIL import Image, ImageTk
from .circuit import ListSteps


# We then write the dialSet() visualization function itself. It takes a quantum circuit as an argument.

# In[2]:


def display(qc):
    
    #we run a simulation of the quantum circuit and get the result
    backend = BasicAer.get_backend('statevector_simulator')
    job = execute(qc, backend)
    state_superposition = job.result().get_statevector(qc)

    #length of the string of bits
    n=len(binary_repr(len(state_superposition)))-1

    #creation of the subplots containing the dial sets
    fig, ax = plt.subplots(2**((n//2)+(n%2)),2**(n//2))
    fig.subplots_adjust(hspace=0.6, wspace=0.0)
    plt.axis('off')
    
    #creation of the dial set circle
    theta = np.linspace(0, 2*np.pi, 40)
    x = np.cos(theta)
    y = np.sin(theta)
    
    #counter to know what sublot we are working on
    counter=0

    #for each state we draw a dial set
    for i in state_superposition:
        
        #we first choose the coresponding subplot
        plt.subplot(2**((n//2)+(n%2)),2**(n//2),counter+1)

        title ="|"+binary_repr(counter,n)+">"

        plt.plot(x, y)
        plt.axis("equal")
        plt.axis('off')
        plt.title(title)
        
        
        #we draw the dial set 
        if i.imag==0 and i.real!=0:
            a = np.array([0, 0])
            b = np.array([0, i.real**2])
            plt.plot(a, b)

        elif i.imag!=0 and i.real==0:
            a = np.array([0, 0])
            b = np.array( [0, -(i.imag**2)])
            plt.plot(a, b)

        elif i.imag!=0: 
            a = np.array([0, ((i.real**2)+(i.imag**2))*np.sin(phase(i))])
            b = np.array([ 0, ((i.real**2)+(i.imag**2))*np.cos(phase(i))])
            plt.plot(a, b)

        counter+=1
    return plt


# In[3]:


def dialSetSave(qc, j):
    
    #we run a simulation of the quantum circuit and get the result
    backend = BasicAer.get_backend('statevector_simulator')
    job = execute(qc, backend)
    state_superposition = job.result().get_statevector(qc)

    #length of the string of bits
    n=len(binary_repr(len(state_superposition)))-1

    #creation of the subplots containing the dial sets
    fig, ax = plt.subplots(2**((n//2)+(n%2)),2**(n//2))
    fig.subplots_adjust(hspace=0.6, wspace=0.0)
    plt.axis('off')
    
    #creation of the dial set circle
    theta = np.linspace(0, 2*np.pi, 40)
    x = np.cos(theta)
    y = np.sin(theta)
    
    #counter to know what sublot we are working on
    counter=0

    #for each state we draw a dial set
    for i in state_superposition:
        
        #we first choose the coresponding subplot
        plt.subplot(2**((n//2)+(n%2)),2**(n//2),counter+1)

        title ="|"+binary_repr(counter,n)+">"

        plt.plot(x, y)
        plt.axis("equal")
        plt.axis('off')
        plt.title(title)
        
        
        #we draw the dial set 
        if i.imag==0 and i.real!=0:
            a = np.array([0, 0])
            b = np.array([0, i.real**2])
            plt.plot(a, b)

        elif i.imag!=0 and i.real==0:
            a = np.array([0, 0])
            b = np.array( [0, -(i.imag**2)])
            plt.plot(a, b)

        elif i.imag!=0: 
            a = np.array([0, ((i.real**2)+(i.imag**2))*np.sin(phase(i))])
            b = np.array([ 0, ((i.real**2)+(i.imag**2))*np.cos(phase(i))])
            plt.plot(a, b)

        counter+=1
        
    plt.savefig("foo"+str(j)+".jpg")


# Same thing but with an amplitude always equals to 1 (for clarity purposes)

# In[4]:


def dialSetNoAmp(qc):
    
    
    backend = BasicAer.get_backend('statevector_simulator')
    job = execute(qc, backend)
    state_superposition = job.result().get_statevector(qc)

    #length of the string of bits
    n=len(binary_repr(len(state_superposition)))-1

    #creation of the subplots containing the dial sets
    fig, ax = plt.subplots(2**((n//2)+(n%2)),2**(n//2))
    fig.subplots_adjust(hspace=0.6, wspace=0.0)
    plt.axis('off')
    
    #creation of the dial set circle
    theta = np.linspace(0, 2*np.pi, 40)
    x = np.cos(theta)
    y = np.sin(theta)
    
    #counter to know what sublot we are working on
    counter=0

    #for each state we draw a dial set
    for i in state_superposition:
        
        #we first choose the coresponding subplot
        plt.subplot(2**((n//2)+(n%2)),2**(n//2),counter+1)

        title ="|"+binary_repr(counter,n)+">"

        plt.plot(x, y)
        plt.axis("equal")
        plt.axis('off')
        plt.title(title)
        
        
        #we draw the dial set 
        if i.imag==0 and i.real!=0:
            a = np.array([0, 0])
            b = np.array([0, 1])
            plt.plot(a, b)

        elif i.imag!=0 and i.real==0:
            a = np.array([0, 0])
            b = np.array([0, -1])
            plt.plot(a, b)
        
        elif i.imag==0 and i.real==0:
            a = np.array([0, 0])
            b = np.array([0, 0])
            plt.plot(a, b)

        elif i.imag!=0: 
            a = np.array([0, np.sin(phase(i))])
            b = np.array([ 0, np.cos(phase(i))])
            plt.plot(a, b)

        counter+=1
    plt.show()  
    return plt


# Some examples :

# In[11]:


#displays each step, step by step
def stepbystep_dialSet(qc):
    
    # on récupère la liste des étapes
    listSteps = ListSteps(qc,0)
    
    #on boucle sur le nombre d'etapes
    for i in range(1,len(listSteps)+1) :
        
        #on recupere la liste des etapes
        listSteps = ListSteps(qc,i)
        
        #on execute les i premieres etapes
        for j in range(i):
            print(listSteps[j])
            exec(listSteps[j])
        #on affiche
        if listSteps[j][:3+len(str(i))]=='qc'+str(i)+'.':
            exec('dialSet(qc'+str(i)+')')
    


# In[6]:


def stepNumber_dialSet(qc, stepNumber):
    listSteps = ListSteps(qc,0)
    for j in range(stepNumber):
        print(listSteps[j])
        exec(listSteps[j])
    if listSteps[j][:4]=='qc0.':
        exec('dialSet(qc0)')


# In[7]:


def steps_dialSet(qc):
    listSteps = ListSteps(qc,0)
    for i in range(1,len(listSteps)+1) :
            stepNumber_dialSet(qc, i)


# In[8]:


def stepNumber_dialSetSave(qc, stepNumber):
    listSteps = ListSteps(qc,0)
    for j in range(stepNumber):
        print(listSteps[j])
        exec(listSteps[j])
    if listSteps[j][:4]=='qc0.':
        exec('dialSetSave(qc0,'+str(j)+')')

def steps_dialSetSave(qc):
    listSteps = ListSteps(qc,0)
    for i in range(1,len(listSteps)+1) :
            stepNumber_dialSetSave(qc, i)


# In[9]:


def create_step_qc(qc, stepNumber):
    listSteps = ListSteps(qc,0)
    for j in range(stepNumber):
        print(listSteps[j])
        exec(listSteps[j])

print('finish importing dial_set')