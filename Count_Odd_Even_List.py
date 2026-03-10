# Counting the number of odd and even elements in the list - Way 1
class CountOddAndEvenElements:
    def countOddAndEvenElements(self, num):
        count_odd = 0
        count_even = 0 
        for i in num:
            if i % 2 == 0:
                count_even+= 1
            else:
                count_odd+= 1
        return count_odd, count_even

obj = CountOddAndEvenElements()
num = list(map(int,input("Enter the elements in the list:").split()))
odd,even = obj.countOddAndEvenElements(num)
print("Count of odd numbers in the list:", odd)
print("Count of even numbers in the list:", even)

"""
Input: Enter the elements in the list: 2 3 4 5 1 6 1
Output: Count of odd numbers in the list: 4
Count of even numbers in the list: 3
"""


# Counting the number of odd and even elements in the list - Way 2(Using sum())
class CountOddAndEvenElements:
    def countOddAndEvenElements(self, num):
        count_even = sum(1 for i in num if i % 2 == 0)
        count_odd = len(num) - count_even
        return count_odd, count_even

obj = CountOddAndEvenElements()
num = list(map(int,input("Enter the elements in the list:").split()))
odd,even = obj.countOddAndEvenElements(num)
print("Count of odd numbers in the list:", odd)
print("Count of even numbers in the list:", even)
