# Find Repeating Elements in the list - Way 1
class RepeatingElements:
    def repeatingElements(self, elements):
        freq_elements = {}
        for char in elements:
            if char in freq_elements:
                freq_elements[char] += 1
            else:
                freq_elements[char] = 1
        
        repeating_elements = {}
        for key,value in freq_elements.items():
            if value > 1:
                repeating_elements[key] = value
        return repeating_elements
        
        # return {k:v for k,v in freq_elements.items() if v>1}

obj = RepeatingElements()
elements = input("Enter the elements in the list:").split()
result = obj.repeatingElements(elements)
print("Repeating elements in the list:",result)


"""
Input: Enter the elements in the list: 1 2 2 1 3 4
Output: Repeating elements in the list: {'1': 2, '2':2}
"""


# Find Repeating Elements in the list - Way 2(Using Counter)
from collections import Counter
class RepeatingElements:
    def repeatingElements(self, elements):
        freq_elements = Counter(elements)
        
        repeating_elements = {}
        for key,value in freq_elements.items():
            if value > 1:
                repeating_elements[key] = value
        return repeating_elements
        

obj = RepeatingElements()
elements = input("Enter the elements in the list:").split()
result = obj.repeatingElements(elements)
print("Repeating elements in the list:",result)
