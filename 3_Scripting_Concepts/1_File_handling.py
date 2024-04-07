# Opening a file: 1) Python provides the open() function to open the file.
#                 2) It takes two arguments: the name of the file and the mode in which the file should be opened. 
#                 3) The mode can be 'r' for reading, 'w' for writting, or 'a' for appending. 

# Modes in file:
# 1) read(r): This mode open the file for reading only and given an error if the file does not exist. This is default mode. 
# 2) write(w): This mode open the file for writing mode and creates a new file if the file is does not exist. 
# 3) append(a): This mode open the file for appending and creating file if does not exist. 
# 4) create(x): This mode craeting the file and give an error if the already exists. 
# 5) text(t): t mode used to handel as a text file not diff in 'r' & 'rt' or 'w' & 'wt'. 
# 6) binary(b): Used to handle binary file (Image,pdf,etc). 

# Reading a file
f = open('3_Scripting_Concepts/myfile.txt','r')

print(f)
text = f.read()
print(text)
f.close()

f = open('3_Scripting_Concepts/myfile2.txt','w')   # create the file at write mode 

# Writing a file
f = open('3_Scripting_Concepts/myfile2.txt', 'w')   # Write the data into file only one time
f.write('Hello, World!')
f.close()

# Append :
f = open('3_Scripting_Concepts/myfile.txt', 'a')    # Appending number of time at last at the number of running 
f.write('Hello, World!')
f.close()

# with satetment: 

with open('3_Scripting_Concepts/myfile3.txt', 'a') as f:
    f.write("Hey i am inside with")