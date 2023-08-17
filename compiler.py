

a_file = open("programexample.ilham", "r")
compiledfile = open("programexample.ilhambin","a")
list_of_lists = [(line.strip()).split() for line in a_file]

a_file.close()

print(list_of_lists)

for i in range(len(list_of_lists)):
    listofline = len(list_of_lists[i])
    #ALU INSTRUCTIONS
    if(list_of_lists[i][0] == "AND"):
        rega = list_of_lists[i][1]
        regb = list_of_lists[i][2]
        filewrite = '1000' + rega + regb + "\n"
        compiledfile.write(filewrite)
    elif(list_of_lists[i][0] == "OR"):
        rega = list_of_lists[i][1]
        regb = list_of_lists[i][2]
        filewrite = '1001' + rega + regb+ "\n"
        compiledfile.write(filewrite)
    elif(list_of_lists[i][0] == "XOR"):
        rega = list_of_lists[i][1]
        regb = list_of_lists[i][2]
        filewrite = '1010' + rega + regb+ "\n"
        compiledfile.write(filewrite)
    elif(list_of_lists[i][0] == "NOT"):
        rega = list_of_lists[i][1]
        
        filewrite = '1011' + rega+ "00"
        compiledfile.write(filewrite)
    elif(list_of_lists[i][0] == "ADD"):
        rega = list_of_lists[i][1]
        regb = list_of_lists[i][2]
        filewrite = '1100' + rega + regb+ "\n"
        compiledfile.write(filewrite)
    elif(list_of_lists[i][0] == "SHR"):
        rega = list_of_lists[i][1]
        
        filewrite = '1101' + rega+ "00" "\n"
        compiledfile.write(filewrite)
    elif(list_of_lists[i][0] == "SHL"):
        rega = list_of_lists[i][1]
        
        filewrite = '1110' + rega+ "00" "\n"
        compiledfile.write(filewrite)
    elif(list_of_lists[i][0] == "SUB"):
        rega = list_of_lists[i][1]
        regb = list_of_lists[i][2]
        filewrite = '1111' + rega + regb+ "\n"
        compiledfile.write(filewrite)
    #ALU END
    #JUMP 
    elif(list_of_lists[i][0] == "JMP"):
        rega = list_of_lists[i][1]
        
        filewrite = '00000000' + "\n" +rega+ "\n"
        compiledfile.write(filewrite)
    elif(list_of_lists[i][0] == "JC"):
        rega = list_of_lists[i][1]
        
        filewrite = '000000100' +  "\n" +rega+ "\n"
        compiledfile.write(filewrite)
    elif(list_of_lists[i][0] == "JNC"):
        rega = list_of_lists[i][1]
        
        filewrite = '000001000' +  "\n" +rega+ "\n"
        compiledfile.write(filewrite)
    elif(list_of_lists[i][0] == "JP"):
        rega = list_of_lists[i][1]
        
        filewrite = '000001100' +  "\n" +rega+ "\n"
        compiledfile.write(filewrite)
    elif(list_of_lists[i][0] == "JN"):
        rega = list_of_lists[i][1]
        
        filewrite = '00010000' +  "\n" +rega+ "\n"
        compiledfile.write(filewrite)
    elif(list_of_lists[i][0] == "JE"):
        rega = list_of_lists[i][1]
        
        filewrite = '00010100' +  "\n" +rega+ "\n"
        compiledfile.write(filewrite)
    elif(list_of_lists[i][0] == "JNE"):
        rega = list_of_lists[i][1]
        
        filewrite = '00011000' +  "\n" +rega+ "\n"
        compiledfile.write(filewrite)
    elif(list_of_lists[i][0] == "JPE"):
        rega = list_of_lists[i][1]
        
        filewrite = '00011100' +  "\n" +rega+ "\n"
        compiledfile.write(filewrite)
    elif(list_of_lists[i][0] == "JPO"):
        rega = list_of_lists[i][1]
        
        filewrite = '00100000' +  "\n" +rega+ "\n"
        compiledfile.write(filewrite)
    elif(list_of_lists[i][0] == "LOAD"):
        rega = list_of_lists[i][1]
        regb = list_of_lists[i][2]
        filewrite = '011001' + rega + "\n" + regb+ "\n"
        compiledfile.write(filewrite)
    elif(list_of_lists[i][0] == "STR"):
        rega = list_of_lists[i][1]
        regb = list_of_lists[i][2]
        filewrite = '011010' + rega + "\n" + regb+ "\n"
        compiledfile.write(filewrite)
    elif(list_of_lists[i][0] == "PRINT"):
        rega = list_of_lists[i][1]
        
        
        filewrite = '011011' + rega+ "\n"
        compiledfile.write(filewrite)
    elif(list_of_lists[i][0] == "INP"):
        rega = list_of_lists[i][1]
        
        
        filewrite = '011100' + rega+ "\n"
        compiledfile.write(filewrite)
    elif(list_of_lists[i][0] == "CMP"):
        rega = list_of_lists[i][1]
        regb = list_of_lists[i][2]
        filewrite = '01111000' + "\n"+ rega  + regb+ "0000\n"
        compiledfile.write(filewrite)
    