# Check whether a number is Prime or Not
class PrimeNumber:
    def isPrime(self,n):
        if n<=1:
            return False
        else:
            for i in range(2,int(n**0.5)+1):
                if n % i == 0:
                    return False
                    break
            return True
               
obj = PrimeNumber()
number = int(input("Enter the number:"))
if obj.isPrime(number):
    print(f"{number} is a Prime Number")
else:
    print(f"{number} is not a Prime Number")

"""
Input : Enter the number:7
Output: 7 is a Prime Number
"""
