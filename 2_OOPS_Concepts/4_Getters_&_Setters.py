# Getters:- 1) Getter in python are methods that are used to access the values of an object's properties. 
#           2) They are used to return the value of a specific properties & typically using the @property decorator.   


class MyClass:
    def __init__(self, value):
        self._value = value 

    def show(self):
        print(f"Value is {self._value}")

# This is the Getter
    @property
    def ten_value(self):
        return 10 * self._value

obj = MyClass(10)
# obj.ten_value = 78   # It's not set the value So how to set the value by using setters
print(obj.ten_value)

obj.show()


# Setters:- 1) We can easly set/update the value by using setter. 
#           2) The getter do not take any parameters and we can not set the value through getter method. 
#           3) So we need to stter method which can be added by decorating method with @property_name.setter


class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

# This is the Getters:-
    @property
    def ten_value(self):
        return 10 * self._value

# This is the setters:-
    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value/10

obj = MyClass(10)
obj.ten_value = 78   # Now to use setter, we can easly set the value or update the value
print(obj.ten_value)

obj.show()