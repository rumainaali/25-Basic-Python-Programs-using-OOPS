# Find the Smallest and Largest Element in the list - Way 1
class SmallestAndLargest:
    def smallestAndLargest(self, num):
        smallest = num[0]
        largest = num[0]
        
        for i in num[1:]: # To Avoid checking first number twice
            if i < smallest:
                smallest = i
            elif i > largest:
                largest = i
        return smallest, largest

obj = SmallestAndLargest()
num = list(map(int,input("Enter the numbers in the list:").split()))
smallest, largest = obj.smallestAndLargest(num)
print("Smallest Number in the List:", smallest)
print("Largest Number in the List:", largest)


"""
Input: Enter the numbers in the list: 10 9 7 8
Output: 
Smallest Number in the List: 7
Largest Number in the List: 10
"""



# Find the Smallest and Largest Element in the list - Way 2
class SmallestAndLargest:
    def smallestAndLargest(self, num):
        return min(num), max(num)

obj = SmallestAndLargest()
num = list(map(int,input("Enter the numbers in the list:").split()))
smallest, largest = obj.smallestAndLargest(num)
print("Smallest Number in the List:", smallest)
print("Largest Number in the List:", largest)
