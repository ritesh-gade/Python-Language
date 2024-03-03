a=int(input("Enter the First value:"))
b=int(input("Enter the Second value:"))
operator=input("Select the Operator: (+,-,*,/,%,**,//):-")

if operator == "+":
    print("Addition of A & B is: ",a+b)

elif operator == "-":
    print("Subtraction of A & B is:",a-b)

elif operator == "*":
    print("Multiplication of A & B is:",a*b)

elif operator == "/":
    print("Division of A & B is:",a/b)

elif operator == "%":
    print("Modulus of A & B is:",a%b)

elif operator == "**":
    print("Exponentiation of A & B is:",a**b)

elif operator == "//":
    print("Floor Division of A & B is:",a//b)

else :
    print("-----------> This operator is not present Here <-------------------------")