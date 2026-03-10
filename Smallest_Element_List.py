# Smallest Element in the List
class SmallestNumber:
    def smallestNum(self,num):
        smallest_num = num[0]
        
        if not num:
            return None
            
        for i in num:
            if i < smallest_num:
                smallest_num = i
        return smallest_num

obj = SmallestNumber()
num = list(map(int,input("Enter the numbers in the list:").split()))
result = obj.smallestNum(num)

if result is not None:
    print("Smallest Number in the list:", result)
else:
    print("List is Empty")

"""
Input: Enter the numbers in the list: 0 9 -1 8
Output: Smallest Number in the list: -1
"""
