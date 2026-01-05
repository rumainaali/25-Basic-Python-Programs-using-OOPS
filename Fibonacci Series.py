# Fibonacci Series - Way 1
class FibonacciSeries:
    def fiboSeries(self,num):
        result = []
        a,b = 0,1
        for i in range(1,num+1):
            result.append(a)
            a,b = b, a+b
        return result

obj = FibonacciSeries()
num = int(input("Enter the number of series:"))
fibo_series = obj.fiboSeries(num)
for i in fibo_series:
    print(i,end=" ")

"""
Input:Enter the number of series:5
Output: 0 1 1 2 3
"""

# Fibonacci Series - Way 2(Recursive Function)
class FibonacciSeries:
    def fibo(self, n):
        if n <= 1:
            return n
        return self.fibo(n-1) + self.fibo(n-2)

    def fiboSeries(self, num):
        result = []
        for i in range(num):
            result.append(self.fibo(i))
        return result


obj = FibonacciSeries()
num = int(input("Enter the number of series: "))
series = obj.fiboSeries(num)

for i in series:
    print(i, end=" ")


# Fibonacci Series - Way 3(Generator)
class FibonacciSeries:
    def fiboSeries(self,num):
        a,b = 0,1
        for _ in range(num):
            yield a
            a,b = b, a+b

obj = FibonacciSeries()
num = int(input("Enter the number of series:"))
fibo_series = obj.fiboSeries(num)
for i in fibo_series:
    print(i,end=" ")
