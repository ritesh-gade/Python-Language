# readline():- 1) The readline() method reads a single line from the file & return them as a list of string. 
#              2) If we want to read multiple lines, we can use a loop. 


# readline Method:- 
f = open('3_Scripting_Concepts/myfile.txt','r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)


# writelines():- 1) The writeline() method in python write a sequence of string to a file. 
#                2) The sequence can be any iterable object, such as tuple or a list. 
#                3) Writeline() method does not add newline character between the string in sequence. 
#                4) If you want to add newline between string you ca use loop to write string separately.  

f = open('3_Scripting_Concepts/add.txt','w')
lines = ['line:- 1\n','line:- 2\n','line:- 3\n']

f.writelines(lines)
f.close()


# Using loop to add new line
f = open('3_Scripting_Concepts/add.txt','w')
lines = ['Newline:- 1','Newline:- 2','Newline:- 3']

for line in lines:
    f.writelines(line + '\n')
f.close()