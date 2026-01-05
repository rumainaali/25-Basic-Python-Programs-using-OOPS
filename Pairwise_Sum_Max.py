# Pairwise Sum and find the max, Sort the list, pairwise sum and find max
class PairSum:
    def bubbleSort(self,num):
        for i in range(len(num)):
            for j in range(0,len(num)-i-1):
                if num[j] > num[j+1]:
                    num[j], num[j+1] = num[j+1], num[j]
        return num
    
    def pairSum1(self,num):
        max_sum1 = num[0] + num[1]
        for i in range(0,len(num)-1,2):
            pair_sum = num[i] + num[i+1]
            if pair_sum > max_sum1:
                max_sum1 = pair_sum
        return max_sum1
    
    def pairSum2(self,num):
        number = num.copy()
        self.bubbleSort(number)
        max_sum2 = number[0] + number[1]
        for i in range(0,len(number)-1,2):
            pair_sum = number[i] + number[i+1]
            if pair_sum > max_sum2:
                max_sum2 = pair_sum
        return max_sum2

obj = PairSum()
num = list(map(int,input("Enter the numbers:").split()))
result1 = obj.pairSum1(num)
result2 = obj.pairSum2(num)
print("Max after first grouping:",result1)
print("Max after second grouping:",result2)

"""
Input: Enter the numbers: -5 -3 -2 -4
Output: Max after first grouping: -6
Max after second grouping: -5
"""


# Way 2
class PairSum:
    def pairSum1(self, num):
        max_sum1 = num[0] + num[1]
        for i in range(0, len(num) - 1, 2):
            pair_sum = num[i] + num[i + 1]
            if pair_sum > max_sum1:
                max_sum1 = pair_sum
        return max_sum1

    def pairSum2(self, num):
        largest = second_largest = float('-inf')

        for i in num:
            if i > largest:
                second_largest = largest
                largest = i
            elif i > second_largest:
                second_largest = i

        return largest + second_largest


obj = PairSum()
num = list(map(int, input("Enter the numbers: ").split()))

print("Max after first grouping:", obj.pairSum1(num))
print("Max after second grouping:", obj.pairSum2(num))
