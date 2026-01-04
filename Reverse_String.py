# Reverse the string - Way 1
class Reverse:
    def reverse_str(self,string):
        return string[::-1]

obj = Reverse()
result = obj.reverse_str(input("Enter the string:"))
if result is not None:
    print(result)
else:
    print("Invalid input")

"""
Input: Enter the string:Madam
Output: madaM
"""


# Reverse the string - Way 2
class Reverse:
    def reverse_str(self,string):
        rev_str=""
        for char in string:
            rev_str = char + rev_str
        return rev_str if rev_str else None

obj = Reverse()
result = obj.reverse_str(input("Enter the string:"))
if result is not None:
    print(result)
else:
    print("Invalid input")

