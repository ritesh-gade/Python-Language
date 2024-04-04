import os

if (not os.path.exists("data")):    # Given the function Condition. 
    os.mkdir("data")          #Directory will be formed. 

for i in range (0,100):
    os.mkdir(f"data/Day{i+1}")