# Finding the Non Repeating Elements in the list  - Way 1
class NonRepeatingElements:
    def nonRepeatingElements(self, elements):
        freq = {}
        for char in elements:
            if char in freq:
                freq[char]+= 1
            else:
                freq[char] = 1
        
        non_repeating = []
        for key, value in freq.items():
            if value == 1:
                non_repeating.append(key)
        return non_repeating

obj = NonRepeatingElements()
elements = input("Enter the elements in the list:").split()
result = obj.nonRepeatingElements(elements)
print("Non Repeating Elements in the list:", result)


"""
Input: Enter the elements in the list:a cc c b d a bb
Output: Non Repeating Elements in the list: ['cc','c','b','d','bb']
"""


# Finding the Non Repeating Elements in the list - Way 2(Using Counter)
from collections import Counter
class NonRepeatingElements:
    def nonRepeatingElements(self, elements):
        freq = Counter(elements)
        
        non_repeating = []
        for key, value in freq.items():
            if value == 1:
                non_repeating.append(key)
        return non_repeating

obj = NonRepeatingElements()
elements = input("Enter the elements in the list:").split()
result = obj.nonRepeatingElements(elements)
print("Non Repeating Elements in the list:", result)
