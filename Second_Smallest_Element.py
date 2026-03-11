# Find Second Smallest Element in list
class SecondSmallest:
    def secondSmallest(self, num):
        smallest_num = num[0]
        second_smallest = float('inf')
        
        for i in num:
            if i < smallest_num:
                second_smallest = smallest_num
                smallest_num = i
            elif i!= smallest_num and i < second_smallest:
                second_smallest = i
        return second_smallest

obj = SecondSmallest()
num = list(map(int,input("Enter the numbers in the list:").split()))
result = obj.secondSmallest(num)
print("Second Smallest Element in the List:", result)

  
"""
Input: Enter the numbers in the list: 0 0 4 2
Output: Second Smallest Element in the List: 2
"""
