# kolkata timestamp (24-hrs)
import time
# timestamp = int(time.strftime('%H'))
timestamp = int(input("Enter the Current Time: "))

if (timestamp > 0 and timestamp <=11):
    print("Good Morning Guys")

elif (timestamp >= 12 and timestamp <=16):
    print("Good Afternoon Guys")

elif (timestamp >= 17 and timestamp <=19):
    print("Good Evening Guys")

else:
    print("Good Night Guys")