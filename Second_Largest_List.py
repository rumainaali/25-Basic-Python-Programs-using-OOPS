# Second Largest Number in List
class SecondLargest:
    def secondLargest(self,num):
        largest_num = num[0]
        second_largest = -1
        for i in num:
            if i > largest_num:
                second_largest = largest_num
                largest_num = i
            elif  i!= largest_num and i > second_largest:
                second_largest = i
        return second_largest

obj = SecondLargest()
num = list(map(int,input("Enter the numbers:").split()))
result = obj.secondLargest(num)
print("Second Largest Element in List:",result)

"""
Input: Enter the numbers: 2 0 0 4
Output: Second Largest Element in List: 2
"""
