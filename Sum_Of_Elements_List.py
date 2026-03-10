# Find the Sum of Elements in the List
class SumOfElements:
    def sumOfElements(self, num):
        sum_of_elements = 0
        
        if not num:
            return 0
            
        for i in num:
            sum_of_elements+= i
        return sum_of_elements

obj = SumOfElements()
num = list(map(int,input("Enter the numbers in the list:").split()))
result = obj.sumOfElements(num)

print("Sum of Elements in the list:", result)

"""
Input: Enter the numbers in the list: 1 2 3 4 5
Output: Sum of Elements in the list:15
"""
