# Python 1
# Basic Data Types

h = "hello"
w = "world"

print(h,w)
print(h+w)

n1 = 5
n2 = 4
print(h+str(n1))

multilinestring = """
    str() - cast to string
    int() - cast to integer
    float() - cast to float
"""

# Formatted strings
n1 = 5
n2 = 3
res = n1 + n2
out = f'{n1} + {n2} = {res}'
print(out)

# Logical operators
# Code block
n1 = 5
n1 = 3

if n1 < n2:
    print("Lesser")
    print("<" * 6)
elif n1==n2:
    print("Equal")
    print("=====")
else:
    print("Greater")
    print(">" * len("Greater"))

# blocks in python use indentation
# used in if statements / function def

f = 17.4
print(type(f))