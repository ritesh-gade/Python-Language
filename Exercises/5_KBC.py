# Create the Program capable of displaying questions to the user like KBC. 
# user list data types to store the questions and thier correct answer. 
# Display the final amount the person is taking home after playing the KBC Game. 

questions = [
    ["Who is the Current CSK captain ?","M S Dhoni","Ravindra Jadeja","Ruturaj Gaikwad","Suresh Raina",3],
    ["which language was used to create FaceBook ?","Python","French","Javascripts","Php",4],
    ["Who is the Current CSK captain ?","M S Dhoni","Ravindra Jadeja","Ruturaj Gaikwad","Suresh Raina",3],
    ["Who is the Current CSK captain ?","M S Dhoni","Ravindra Jadeja","Ruturaj Gaikwad","Suresh Raina",3],
    ["which language was used to create FaceBook ?","Python","French","Javascripts","Php",4],
    ["Who is the Current CSK captain ?","M S Dhoni","Ravindra Jadeja","Ruturaj Gaikwad","Suresh Raina",3],
    ["Who is the Current CSK captain ?","M S Dhoni","Ravindra Jadeja","Ruturaj Gaikwad","Suresh Raina",3],
    ["Who is the Current CSK captain ?","M S Dhoni","Ravindra Jadeja","Ruturaj Gaikwad","Suresh Raina",3],
    ["Who is the Current CSK captain ?","M S Dhoni","Ravindra Jadeja","Ruturaj Gaikwad","Suresh Raina",3],
    ["Who is the Current CSK captain ?","M S Dhoni","Ravindra Jadeja","Ruturaj Gaikwad","Suresh Raina",3],
    ["Who is the Current CSK captain ?","M S Dhoni","Ravindra Jadeja","Ruturaj Gaikwad","Suresh Raina",3],
    ["Who is the Current CSK captain ?","M S Dhoni","Ravindra Jadeja","Ruturaj Gaikwad","Suresh Raina",3],
    ["Who is the Current CSK captain ?","M S Dhoni","Ravindra Jadeja","Ruturaj Gaikwad","Suresh Raina",3],
    ["Who is the Current CSK captain ?","M S Dhoni","Ravindra Jadeja","Ruturaj Gaikwad","Suresh Raina",3],
    ["Who is the Current CSK captain ?","M S Dhoni","Ravindra Jadeja","Ruturaj Gaikwad","Suresh Raina",3],

]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
money = 0

for i in range (0,len(questions)):
    question = questions[i]
    print("----------------------------------------------------------------------")
    print("----------------------------------------------------------------------\n")
    print(f"Next Question for Rs. {levels[i]}")
    print(f"Question No.:{i+1}) {question[0]}")
    print(f"a. {question[1]}                   b.{question[2]}")
    print(f"c. {question[3]}             d.{question[4]}")
    # print("\n")
    print("----------------------------------------------------------------------")
    reply = int(input("Enter Your Answer (1-4) or Quit(0): "))
    print("----------------------------------------------------------------------\n")


    if (reply == 0):
        money = levels[i-1]
        break
    if(reply == question[-1]):
        print(f"Your Answer is Correct, You have won Rs. {levels[i]}")
        if(i == 4):
            money = 10000
        elif(i == 7):
            money = 80000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money = 10000000
    else:
        print("Your Answer is Wrong!")
        break

print(f"Your Winneing Money is: {money}")


