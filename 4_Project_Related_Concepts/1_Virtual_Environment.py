# Virtual Environment: 1) A virtual Environmnet is an tool used to isolate specific python environment on a single machine(Separate your python environment). 
#                      2) Allowing you to work on multiple projects with different depencies and packages without conflicts. 
#                      3) This can be especillay useful when working on project that have conflicting package version or packges that are not compatible with each other. 


# 1) Create a Virtual Environment:-(Command)
# ===>   python3 -m venv myenv

# 2) a) Activate the Virtual Environment(Linux):-
# ===>   source myenv/bin/activate

# ----->> output:-  (myenv) ritesh@ritesh-VirtualBox:~/Desktop/Python_Language/4_Project_Related_Concepts/Python_Env$  --->  pip3 install pandas==1.4.4
#                                                                                                                      --->  python3
#                                                                                                                      >>>>  import pandas as pd
#                                                                                                                      >>>>  pd.__version__
#                                                                                                                      >>>>  exit()

#    b) Activate the Virtual Environment(Windows):-
# ===>   myenv\Scripts\active.bat 

#    c) Activate the Virtual Environment(Powershell):-
# ===>   myenv\Scripts\active.ps1

#  3) How to see All install pacakages versions
# ===>  pip freeze

# Requirements.txt file :- You can already installed packages list with version put into txt file. This file can be used to easily install all the required packages in a new environment. 
#  4) List of installed packages and their version to a file
# --->>  (myenv) ritesh@ritesh-VirtualBox:~/Desktop/Python_Language/4_Project_Related_Concepts/Python_Env$ ====>  pip freeze > requirements.txt

#  5) How to install and setup on a new machine by using txt file:-
# ===>  pip install -r requirements.txt

#  6) How to deactivate virtual Env:
# --->>  (myenv) ritesh@ritesh-VirtualBox:~/Desktop/Python_Language/4_Project_Related_Concepts/Python_Env$  ====>  deactivate



import pandas as pd
print(pd.__version__)
