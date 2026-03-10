# Find the first non-repeating element in the list - Way 1
class FirstNonRepeatingElement:
    def firstNonRepeatingElement(self, elements):
        freq = {}
        for char in elements:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1 
        
        for char in elements:
            if freq[char] == 1:
                return char
        return None

obj = FirstNonRepeatingElement()
elements = input("Enter the elements in the list:").split()
result = obj.firstNonRepeatingElement(elements)

if result is not None:
    print("First Non-Repeating element in the list:", result)
else:
    print("No non-repeating element found")


"""
Input: Enter the elements in the list: a b cc c a b m
Output: First Non-Repeating element in the list: cc
"""



# Find the first non-repeating element in the list - Way 2(Using Counter)
from collections import Counter
class FirstNonRepeatingElement:
    def firstNonRepeatingElement(self, elements):
        freq = Counter(elements)
        
        for char in elements:
            if freq[char] == 1:
                return char
        return None

obj = FirstNonRepeatingElement()
elements = input("Enter the elements in the list:").split()
result = obj.firstNonRepeatingElement(elements)

if result is not None:
    print("First Non-Repeating element:", result)
else:
    print("No non-repeating element found")
