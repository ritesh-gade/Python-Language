# Typecasting: The conversion of one Data type into the other Data type is called casting.
#  1) Explicit Typecasting: Done via developer or programmer's intervention or manullay as per the requirement.
#       such as: int(), float(), hex(), oct(), str(), etc

#  2) Implicit Typecasting: One data type convert into other by the python interpreter itself(Automatically).
#       such as python convert automatically lower data type into higher data type.


# 1) Explicit Typecasting:
# a) Conversion of String into integer:
string1 = "2"
string2 = "4"
number = 9

conv1=int(string1)
conv2=int(string2)

print("Addition of all these number are:",int(string1) + int(string2) + number)
print("Addition of all these number are:",conv1 + conv2 + number)

# b) Conversion of integer into string:
int1 = 3
k = str(int1)
print("Conversion of Integer into string: ",k ,"--Now the Data type is: ",type(k))

# c) Conversion of float into integer
flaot1 = 2.8
float2 = 4.9
print("Addition of Two Numbers:", int(flaot1) + int(float2))

# d) Conversion of integer into float
int1 = 12
v = float(int1)
print("Conversion of Interger into string:",str(v), "--Now the Data Type is:",type(v))


# 2) Implicit Typecasting:
I = 9
print(type(I))

P = 2.8
print(type(P))

T =  I + P
print("Impicit Type:",T)
print(type(T))
