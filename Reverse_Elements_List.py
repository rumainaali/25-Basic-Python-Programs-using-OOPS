# Reverse the List - Way 1(Slicing)
class ReverseList:
    def revList(self, num):
        return num[::-1]

obj = ReverseList()
num = list(map(int,input("Enter the elements in the list:").split()))
result = obj.revList(num)

print("Reversed List:", result)

"""
Input: Enter the elements in the list: 1 2 3 -1 2
Output: Reversed List: [2,-1,3,2,1]
"""


# Reverse the List - Way 2(Using For loop)
class ReverseList:
    def revList(self, num):
        rev_list = []
        for i in num:
            rev_list = [i] + rev_list
        return rev_list   

obj = ReverseList()
num = list(map(int,input("Enter the numbers in the list:").split()))
result = obj.revList(num)

print("Reversed List:", result)

"""
Input: Enter the elements in the list: 0 1 2 3 4
Output: Reversed List: [4,3,2,1,0]
"""




# Reverse the List - Way 3(reverse function[in place modification])
class ReverseList:
    def revList(self, num):
        num.reverse()
        return num

obj = ReverseList()
num = list(map(int,input("Enter the numbers in the list:").split()))
result = obj.revList(num)

print("Reversed List:", result)

"""
Input: Enter the elements in the list: 1 2 3 4 5
Output: Reversed List: [5,4,3,2,1]
"""



# Reverse the List - Way 4(reversed function[returns a reverse iterator, which can be converted into a list using list()])
class ReverseList:
    def revList(self, num):
        return list(reversed(num))

obj = ReverseList()
num = list(map(int,input("Enter the numbers in the list:").split()))
result = obj.revList(num)

print("Reversed List:", result)

"""
Input: Enter the elements in the list: 5 4 3 2 1
Output: Reversed List: [1,2,3,4,5]
"""
