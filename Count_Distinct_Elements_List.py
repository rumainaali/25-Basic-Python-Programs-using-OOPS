# Counting the distinct elements in list - Way 1(set())
class CountDistinctElement:
    def countDistinctElement(self, elements):
        return len(set(elements))

obj = CountDistinctElement()
elements = input("Enter the elements in the list: ").split()
result = obj.countDistinctElement(elements)
print("Count of distinct elements in the list:", result)

"""
Input: Enter the elements in the list: 1 2 3 4 1
Output: Count of distinct elements in the list: 4
"""



# Counting the distinct elements in list - Way 2(Using loop)
class CountDistinctElement:
    def countDistinctElement(self, elements):
        distinct_elements = set()
        for i in elements:
            distinct_elements.add(i)
        return len(distinct_elements)

obj = CountDistinctElement()
elements = input("Enter the elements in the list: ").split()
result = obj.countDistinctElement(elements)
print("Count of distinct elements in the list:", result)


"""
Input: Enter the elements in the list: a aa b c bc a
Output: Count of distinct elements in the list: 5
"""
