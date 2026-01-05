# Find the largest element in the list
class LargestElement:
    def largestElementList(self,num):
        if not num:
            return None
        max_num = num[0]
        for i in num:
            if i > max_num:
                max_num = i
        return max_num

obj = LargestElement()
num = list(map(int,input("Enter the numbers:").split()))
result = obj.largestElementList(num)
if result is not None:
    print("Largest Number in the given list:",result)
else:
    print("List is empty")

"""
Input: Enter the numbers: 1 9 2 4
Output: Largest Number in the given list: 9
"""
