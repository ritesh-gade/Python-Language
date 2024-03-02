# String are immutable

a = "Ritesh"

# 1) Find the length of String:
print(len(a))

# 2) String are convert into Upper case:
print(a.upper())

# 3) String are Convert into Lower case:
print(a.lower())

# 4) Remove the All strip part
b = "!!!Gade!!!!!!!"
print(b.strip("!"))
c = "@@@Ritesh@@@"
print(c.strip("@"))

# 5) Remove the End strip part(Trailing Strip)
d = "!!!Ritesh!!!!!!!"
print(d.rstrip("!"))

# 6) Replace any one to other 
print(d.replace("Ritesh","Vipul"))
print(d.replace("!","#"))

# 7) Create the list using split method:
e = "Ritesh Kedar Raj Krushna Akshay"
print(e.split(" "))

# 8) First letter capital letter using capitalize Method:
cap = "hello, Good Morning"
print(cap.capitalize())

# 9) Aligned to the Center add the spaces:
str1 = "Welcome to the Podcast"
print(len(str1))
print(str1.center(50))
print(len(str1.center(50)))

# 10) Count the Word, letter & symbols
str2 = '''P1: Hello Good Morning,
P2: Good Morning
P1: What's Going on? 
P2: Nothing Special @@@ !!!
    '''
print(str2)
print(str2.count("Good"))
print(str2.count("P"))
print(str2.count("@"))

# 11) Endwith use by Boolen Output True/False:
str3 = "Welcome to the World !!!!"
print(str3.endswith("!"))
print(str3.endswith("to",4,10))

# 12) Find use the search and given output in index place:
str3 = "Hey, What are you doing? "
print(str3.find("you"))
print(str3.find("cat"))  # cat not in string showing -1

# 13) Index method use is same as find only the word is not in string it's show the Value Error:
str3 = "Hey, What are you doing? "
print(str3.index("you"))
# print(str3.index("cat"))  # cat not in string showing Value Error

# 14) isalnum method return True if string is Under A-Z,a-z,0-9 otherwise it's shows False
str1 = "WelcomeToTheWorld10"
print(str1.isalnum())
str2 = "WelcomeToTheWorld!!!"
print(str2.isalnum())

# 15) isalpha is same as isalnum only Numberic Value is not Present here(i.e:A-Z,a-z)
str1 = "WelcomeToTheWorld"
print(str1.isalpha())
str2 = "WelcomeToTheWorld34"
print(str2.isalpha())

# 16) islower is return True if the all alphabates in lower case othewise return False
str4 = "hello i am ritesh"
print(str4.islower())
str4 = "Hello I am Ritesh"
print(str4.islower())

# 17) isprintable method returns true if all the value within the give string are printable if not, return False
str1 = "Hii, How are You?"
print(str1.isprintable())
str1 = "Hii, How are You?\n"  # this is not printable
print(str1.isprintable())

# 18) isspace method is return True only and only string contains white space:
str1 = "        "
print(str1.isspace())

# 19) istitle if each world of First letter is capitalized return Ture otherwise return false:
str2 = "Hii, Who Are You?"
print(str2.istitle()) 

str2 = "Hii, Who are you?"
print(str2.istitle()) 

# 20) isupper method use to if the all character is capital return True otherwise Flase:
str2 = "HII, GOOD MORNING"
print(str2.isupper())

str2 = "Hii, Good Morning"
print(str2.isupper())

# 21) strtwith return ture/false:
str3 = "Hello I am Working on Jenkins"
print(str3.startswith("Hello"))
print(str3.startswith("Hii"))

# 22) swapcase method use to convert upper case to lower case & vise-versa
str3 = "Hello I am Working on Jenkins"
print(str3.swapcase())

# 23) title method use to correct the string in title form(First letter capital)
str4 = "introduction to python"
print(str4.title())