#returns the liste of steps in a list
def ListSteps(qc,l):
    
    #chaine qasm du circuit
    chain = qc.qasm()
    
    #on divise la chaine a chaque espace et on supprime les termes inutiles
    mod = chain.split('\n')
    del mod[0:2]
    i=0
    
    
    a=mod[i].split(' ')
    registerList =[]
    
    #liste contenant les etapes a executer une par une
    listSteps=[]


    # tant qu'il reste des termes et que le premier terme crée un registre
    while (i<len(mod)) and ((a[0]=="creg") or (a[0]=="qreg")) :

        op = a[0]

        if op == 'creg' : 
            bra1 = a[1].find('[')
            bra2 = a[1].find(']')
            listSteps.append(a[1][0:bra1] + '= ClassicalRegister(' + a[1][bra1+1:bra2] + ', "' + a[1][0:bra1] +'")')
            registerList.append(a[1][0:bra1])

        elif op == 'qreg' :
            bra1 = a[1].find('[')
            bra2 = a[1].find(']')
            listSteps.append(a[1][0:bra1] + '= QuantumRegister(' + a[1][bra1+1:bra2] + ', "' + a[1][0:bra1] +'")')
            registerList.append(a[1][0:bra1])

        i+=1
        a=mod[i].split()

    #creation du quantumCircuit, on lui donne le numero l
    Qc = 'qc'
    Qc+=str(l)
    Qc+='=QuantumCircuit('
    for j in registerList :
        Qc+=j
        Qc+=', '
    Qc+='name="qc'
    Qc+=str(l)
    Qc+='")'
    listSteps.append(Qc)
    name='qc'+str(l)

    
    #on code les operations
    a=mod[i].split()

    while i<len(mod)-1:

        op = a[0]

        if op[0] == 'u' and op[1] == '3' :
            bra1 = a[0].find(')')
            debut = a[0][:bra1]
            a[0] = debut + ','

            bra2 = a[1].find(';')
            a[1]=a[1][:bra2]

            a[0]+=a[1]
            a[0]+=')'
            listSteps.append(name+'.'+a[0])

        elif op =='z' :
            bra2 = a[1].find(';')
            a[1]=a[1][:bra2]
            listSteps.append(name+'.'+a[0]+'('+a[1]+')')

        elif op =='y' :
            bra2 = a[1].find(';')
            a[1]=a[1][:bra2]
            listSteps.append(name+'.'+a[0]+'('+a[1]+')')

        elif op =='x' :
            bra2 = a[1].find(';')
            a[1]=a[1][:bra2]
            listSteps.append(name+'.'+a[0]+'('+a[1]+')')

        elif op == 'h' :
            bra2 = a[1].find(';')
            a[1]=a[1][:bra2]
            listSteps.append(name+'.'+a[0]+'('+a[1]+')')

        elif op == 'cx' :
            bra2 = a[1].find(';')
            a[1]=a[1][:bra2]
            listSteps.append(name+'.'+a[0]+'('+a[1]+')')

        elif op == 'barrier' :
            bra2 = a[1].find(';')
            a[1]=a[1][:bra2]
            listSteps.append(name+'.'+a[0]+'('+a[1]+')')
            
        else :
            bra2 = a[1].find(';')
            a[1]=a[1][:bra2]
            listSteps.append(name+'.'+a[0]+'('+a[1]+')')

        i+=1  
        a=mod[i].split()

    return listSteps