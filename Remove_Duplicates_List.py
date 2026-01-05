# Remove Duplicates from List
class RemoveDuplicate:
    def removeDup(self,num):
        unique = []
        for i in num:
            if i not in unique:
                unique.append(i)
        return unique

obj = RemoveDuplicate()
num = list(map(int,input("Enter the numbers:").split()))
result = obj.removeDup(num)
print(result)
"""
Input: Enter the numbers: 1 2 3 4 2
Output:[1,2,3,4]
"""
