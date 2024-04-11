# Lambda Function:-1) lambda function is a small anonymous function without a def name. It is defined using the lambda keyword.
#                      syntax:- lambda arguments: expression
#                  2) Lambda function are often used in situations where a small function is requried for a short period of time. 
#                  3) They are commonly used as arguments to high-order function, such as map, filter & reduce.  

# Normal Function:-
# def cube(x):
#     return x*x*x


# Lambda Function:- 

cube = lambda x: x*x*x
print(cube(5))

avg = lambda x,y: (x+y)/2
print(avg(3,9))



def appl(fx, value):
    return fx(value)

print(appl(lambda x: x * x , 2))