# Sort the first half in ascending order and other half in descending order - Way 1
class SortHalves:
    def sortHalves(self, num):
        mid = len(num) // 2
        
        # Sort the First half
        for i in range(mid):
            for j in range(i+1,mid):
                if num[i] > num[j]:
                    num[i], num[j] = num[j], num[i]
        
        # Sort the Second half
        for i in range(mid,len(num)):
            for j in range(i+1, len(num)):
                if num[i] < num[j]:
                    num[i], num[j] = num[j], num[i]
        return num

obj = SortHalves()
num = list(map(int,input("Enter the numbers in the list:").split()))
result = obj.sortHalves(num)
print("Sorted the first half in ascending order and other half in descending order:", result)
"""
Input: Enter the elements in the list: 8 7 6 5 4 3 2 1
Output: Sorted the first half in ascending order and other half in descending order: [5,6,7,8,4,3,2,1]
"""



# Sort the first half in ascending order and other half in descending order - Way 2
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
Input: Enter the elements in the list: 5 4 3 2 1
Output: Sorted the first half in ascending order and other half in descending order: [4,5,3,2,1]
"""
