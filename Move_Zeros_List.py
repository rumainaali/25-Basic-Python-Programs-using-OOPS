# Move Zeros to the end of the list
class MoveZero:
    def moveZero(self, num):
        pos = 0
        for i in range(len(num)):
            if num[i]!=0:
                num[pos], num[i] = num[i], num[pos]
                pos+=1
        return num

obj = MoveZero()
num = list(map(int,input("Enter the numbers in the list:").split()))
result = obj.moveZero("List after moving zeros to end:", num)
print(result)

"""
Input: Enter the numbers in the list: 1 0 2 0 3 0
Output: List after moving zeros to end: [1,2,3,0,0,0]
"""
