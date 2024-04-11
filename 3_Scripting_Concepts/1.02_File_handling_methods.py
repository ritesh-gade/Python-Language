# seek() function:- 1)It is allow you to move the current position within a file to a specific point. 
#                   2)The position is specified in bytes & you can move ither forward or backward from the current position.

with open('3_Scripting_Concepts/myfile.txt','r') as f:
    
    f.seek(11)    # Move to the 11th byte in the file

    data = f.read(7)        # Read the next 7 bytes
    print(data)



# tell() function: 1) It return the current position within the file, in bytes. 
#                  2) This can be useful for keeping track of your location within the file or for seeking to specific position realative to the current position. 
with open('3_Scripting_Concepts/myfile.txt','r') as f:
    
    f.seek(11)    # Move to the 11th byte in the file

    print(f.tell())   # show the position

    data = f.read(7)        # Read the next 7 bytes
    print(data)


# truncate() function:- If you want to truncate the file to specific size, you can use the truncate function. 

with open('3_Scripting_Concepts/sample.txt','w') as f:
    f.write('Hello World!')
    f.truncate(5)

with open('3_Scripting_Concepts/sample.txt','r') as f:
    print(f.read()) 