# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains at least 3 characters, remove the first letter and append it at the end
# now append three random characters at the starting and the end
# else:
# simply reverse the string


# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
# remove 3 random characters from start and end. Now remove the last letter a
# Your program should ask whether you want to code or decode

st = input("Enter Your Message: ")
words = st.split(" ")
# random character
r1 = "dsf"
r2 = "jkr"

coding = input("1 for Coding or 0 for Decoding: ")
coding = True if (coding=="1") else False
print(coding)

if(coding):                                 # Coding 
    nwords = []
    for word in words:
        if(len(word)>=3):
            stnew = r1 + word[1:] + word[0] + r2
            print(stnew)
            nwords.append(stnew)      # We can store in list nwords
        
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
        

else:                                       # Decoding
    nwords = []
    for word in words:
        if(len(word)>=3):
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
            print(stnew)

        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))