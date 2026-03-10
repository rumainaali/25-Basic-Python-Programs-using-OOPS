# Sort the first half in ascending order and other half in descending order
class SortHalves:
    def sortHalves(self, num):
        mid = len(num) // 2
        first_half = num[:mid]
        second_half = num[mid:]
        first_half.sort()
        second_half.sort(reverse=True)
        return first_half + second_half

obj = SortHalves()
num = list(map(int,input("Enter the elements in the list:").split()))
result = obj.sortHalves(num)
print("Sorted the first half in ascending order and other half in descending order:", result)

"""
Input: Enter the elements in the list: 3 2 1 4 5 6
Output: Sorted the first half in ascending order and other half in descending order: [1,2,3,6,5,4]
"""
