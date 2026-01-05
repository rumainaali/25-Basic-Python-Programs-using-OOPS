# Check whether string is anagram or not
class Anagram:
    def isanagram(self,str1,str2):
        if len(str1)!=len(str2):
            return False
        str1 = str1.lower()
        str2 = str2.lower()
        for char in str1:
            if str1.count(char)!= str2.count(char):
                return False
        return True

obj = Anagram()
str1,str2 = input("Enter the string1:"), input("Enter the string2:")
result = obj.isanagram(str1,str2)
if result:
    print(f"{str1} is a Anagram")
else:
    print(f"{str1} is not a Anagram")

"""
Input: Enter the string1: listen
Enter the string2: silent
Output: listen is a Anagram
"""
