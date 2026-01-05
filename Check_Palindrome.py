# Check whether a string is palindrome or not - Way 1
class Palindrome:
    def palindrome(self,string):
        return string.lower() == string[::-1].lower()

obj = Palindrome()
string = input("Enter the string:")
if obj.palindrome(string):
    print(f"{string} is a Palindrome")
else:
    print(f"{string} is not a Palindrome")
  
"""
Input: Enter the string:
Output: Madam is a Palindrome
"""



# Check whether a string is palindrome or not - Way 2(isalnum())
class Palindrome:
    def palindrome(self, string):
        cleaned = ""
        for ch in string:
            if ch.isalnum():
                cleaned += ch.lower()
        return cleaned == cleaned[::-1]


obj = Palindrome()
string = input("Enter the string: ")

if obj.palindrome(string):
    print(f'"{string}" is a Palindrome')
else:
    print(f'"{string}" is not a Palindrome')


"""
Input:A man, a plan, a canal: Panama
Output: A man, a plan, a canal: Panama is a Palindrome
"""
