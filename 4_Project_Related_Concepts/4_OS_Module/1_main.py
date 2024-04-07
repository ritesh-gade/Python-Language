import os

# if (not os.path.exists("data")):    # Given the function Condition. 
#     os.mkdir("data")          #Directory will be formed. 

# for i in range (0,100):
#     os.mkdir(f"data/Day{i+1}")   # Create the folders in(data) range of Day1 to Day100 in friction of Second.(Time saving)


# Methods:- 
cmd = 'date'
os.system(cmd)         # using os.system() method to get current date of computer

print(os.getcwd())  #  says this is the directory you are working in

os.chdir("4_Project_Related_Concepts/")
print(os.getcwd())