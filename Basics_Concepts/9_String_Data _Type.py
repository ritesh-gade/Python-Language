# String:- Anythin inclose between in single or double quotation marks is consider a string.

name = "Ritesh"
friend = 'Raj'

apple = 'He said, "I want to eat Apple'
apple1 = "He said, \"I want to eat Apple"

print(apple)
print(apple1)

# Use triple single or Double Quote
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
# print(a)

b = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
# print(b)

# String Are Array:- WE can access parts of string by using its index which start from 0 and end with -1

A = "Ritesh"
print(A[0])
print(A[-1])

# Loop through a string
for character in apple:
    print(character)