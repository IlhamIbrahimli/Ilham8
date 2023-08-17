filename = input("Enter Filename:")
file = open(filename,'r')

ram = file.read().splitlines() 
rega = ''
regb = ''
regc = 0
regd = 0
regir = 0
regiar = 0
addreg = 0

haltCPU = False
Equal = False
answer = ['','','',False, Equal]
def binaryToDecimal(n):
    return int(n,2)
def FindReg(reg1,reg2):
    reg1answer = 0
    reg2answer = 0
    if reg1 == "00":
        reg1answer = rega
    elif reg1 == "01":
        reg1answer = regb
    elif reg1 == "10":
        reg1answer = regc
    elif reg1 == "11":
        reg1answer = regd
    if reg2 == "00":
        reg2answer = rega
    elif reg2 == "01":
        reg2answer = regb
    elif reg2 == "10":
        reg2answer = regc
    elif reg2 == "11":
        reg2answer = regd
    return [reg1answer,reg2answer]
def ALU(opcode,reg1,reg2):
    global Equal
    answer = ''
    negative = '0'
   
    if opcode == "000":
        for i in range(8):
            if reg1[i] == reg2[i]:
                answer = answer + '1'
            else:
                answer = answer + '0'
    elif opcode == "001":
        for i in range(8):
            if reg1[i] ==1 or reg2[i] == 1:
                answer = answer + '1'
            else:
                answer = answer + '0'
    elif opcode == "010":
        for i in range(8):
            if reg1[i] ==1 or reg2[i] == 1:
                if reg1[i] == 1 and reg2[i] == 1:
                    answer = answer + "0"
                else:
                    answer = answer + '1'
            else:
                answer = answer + '0'
    elif opcode == "011":
        for i in range(8):
            if reg1[i] ==1:
                answer = answer + '0'
            else:
                answer = answer + '1'
    elif opcode == '100':
        carrybit = '0'
        
        for i in range(7,-1,-1):
            if reg1[i] == "0" and reg2[i] == '0':
                if carrybit == '1':
                    answer = '1' + answer
                    carrybit = '0'
                else:

                    answer = '0' + answer
            elif reg1[i] == '1' and reg2[i] == '0':
                if carrybit == '1':
                    answer = '0' + answer
                    carrybit = '1'
                else:
                    answer = '1' + answer
            elif reg1[i] == '0' and reg2[i] == '1':
                if carrybit == '1':
                    answer = '0' + answer
                    carrybit = '1'
                else:

                    answer = '1' + answer
            elif reg1[i] == '1' and reg2[i] == '1':
                if carrybit == '1':
                    answer = '1' + answer
                    carrybit = '1'
                else:

                    answer = '0' + answer
                    carrybit = '1'     
    elif opcode == '101':
        carrybit = reg1[-1]
        answer = "0"+ reg1[:-1]
    elif opcode == '110':
        carrybit = reg1[1]
        answer = reg1[1:] + "0"
    elif opcode == '111':
        negative = '0'
        currnegative = '0'
        for i in range(7,-1,-1):
            if reg1[i] == "0" and reg2[i] == '0':
                answer = '0' + answer
            elif reg1[i] == '1' and reg2[i] == '0':
                answer = '1' + answer
            elif reg1[i] == '0' and reg2[i] == '1':
                j = 1
                while reg1[i-j] != '1':
                    if i-j == 0:
                        
                        currnegative = '1'
                        break
                    j+=1
                if currnegative == '0':
                    reg1[i-j] = '0'
                    answer = '0'+answer
                else:
                    negative = '1'
                currnegative = '0'

                
                
            elif reg1[i] == '1' and reg2[i] == '1':
                answer = '0' + answer
    #Calculating FLAGS
    if answer[:-1] =="0":
        even = True
    else:
        even = False

    
    
    
    return [answer,carrybit,negative,even,Equal]
def FindCond(condtofind):
    cond = ""
    if condtofind == "0000":
        cond = "JMP"
    elif condtofind == "0001":
        cond = "C"
    elif condtofind == "0010":
        cond = "NC"
    elif condtofind == "0011":
        cond = "P"
    elif condtofind == "0100":
        cond = "N"
    elif condtofind == "0101":
        cond = "E"
    elif condtofind == "0110":
        cond = "NE"
    elif condtofind == "0111":
        cond = "PE"
    elif condtofind == "1000":
        cond = "PO"
    return cond



while haltCPU == False:
    for i in range(4):
        if(i == 0):
            regir = ram[regiar]
        elif(i==1):
            
            if regir == "00000000" or  regir == "000000100" or  regir == "000001000"or  regir == "000001100" or  regir == "00010000" or  regir == "00010100" or  regir == "00011000" or  regir ==  "00100000" or  regir == "00011100" or regir ==  "00100000" or regir ==  "01111000" :
                try:
                    addreg = ram[regiar+1]
                except:
                    haltCPU = True
                    #print("ENDOFFILE")
            elif regir[0:5] == "011001" or regir[0:5] =="011010":
                try:
                    addreg = ram[regiar+1]
                except:
                    haltCPU = True
                    #print("ENDOFFILE")
        elif i == 2:
           
            if regir[0] == '1':
                #ALU INSTRUCTION
                registers = FindReg(regir[4:6],regir[6:])
                answer = ALU(regir[1:4],registers[0],registers[1])
                if regir[4:6] == "00":
                    rega = answer[0]
                elif regir[4:6] == "01":
                    regb = answer[0]
                elif regir[4:6] == "10":
                    regc = answer[0]
                elif regir[4:6] == "11":
                    regd = answer[0]

            else:
                #JUMPORLOADINSTR
                if regir[1] == "0":
                    
                    condition = FindCond(regir[2:6])
                    if condition == "JMP":
                        binnum = binaryToDecimal(addreg)
                        regiar = binnum
                        addreg = ''
                        break
                    elif condition == "C" and answer[1] == '1':
                        binnum = binaryToDecimal(addreg)
                        regiar = binnum
                        addreg = ''
                        break
                    elif condition == "NC" and answer[1] == '0':
                        binnum = binaryToDecimal(addreg)
                        regiar = binnum
                        addreg = ''
                        break
                    elif condition == "N" and answer[2] == '1':
                        binnum = binaryToDecimal(addreg)
                        regiar = binnum
                        addreg = ''
                        break
                    elif condition == "P" and answer[2] == '0':
                        binnum = binaryToDecimal(addreg)
                        regiar = binnum
                        addreg = ''
                        break
                    elif condition == "PO" and answer[3] == False:
                        binnum = binaryToDecimal(addreg)
                        regiar = binnum
                        addreg = ''
                        break
                    elif condition == "PE" and answer[3] == True:
                        binnum = binaryToDecimal(addreg)
                        regiar = binnum
                        addreg = ''
                        break
                    elif condition == "E" and answer[4] == True:
                        binnum = binaryToDecimal(addreg)
                        regiar = binnum
                        addreg = ''
                        break
                    elif condition == "NE" and answer[4] == False:
                        binnum = binaryToDecimal(addreg)
                        regiar = binnum
                        addreg = ''
                        break
                    else:
                        regiar += 2
                        break
                    
                else:
                    #LOAD INSTR
                    if regir[0:6] == "011001":
                        
                        if regir[6:] == "00":
                            rega = addreg
                        elif regir[6:] == "01":
                            regb = addreg
                        elif regir[6:] == "10":
                            regc = addreg
                        elif regir[6:] == "11":
                            regd = addreg
                        addreg = ''
                        regiar += 1
                    elif regir[0:6] == "011010":
                        ramSpace = binaryToDecimal(addreg)
                        if regir[6:] == "00":
                            ram[ramSpace] = rega
                        elif regir[6:] == "01":
                            ram[ramSpace] = regb
                        elif regir[6:] == "10":
                            ram[ramSpace] = regc
                        elif regir[6:] == "11":
                            ram[ramSpace] = regd
                        addreg = ''
                        regiar += 1
                    elif regir[0:6] == "011011":
                        if regir[6:] == "00":
                            print(rega)
                        elif regir[6:] == "01":
                            print(regb)
                        elif regir[6:] == "10":
                            print(regc)
                        elif regir[6:] == "11":
                            print(regd)
                    elif regir[0:6] == "011100":
                        
                        if regir[6:] == "00":
                            rega = input("Enter Bin Num:")
                        elif regir[6:] == "01":
                            regb = input("Enter Bin Num:")
                        elif regir[6:] == "10":
                            regc = input("Enter Bin Num:")
                        elif regir[6:] == "11":
                            regd = input("Enter Bin Num:")
                    elif regir == "01111000":
                        registers2 = FindReg(addreg[0:2],addreg[2:4])
                        if registers2[0] == registers2[1]:
                            Equal = True
                            answer[4] = Equal
                        else:
                            Equal = False
                            answer[4] = Equal
                        regiar += 1
   
        elif i == 3:
            regiar +=1
            if regiar == len(ram):
                haltCPU = True
            
                        
                        
                            



                    
                
        

        
            
