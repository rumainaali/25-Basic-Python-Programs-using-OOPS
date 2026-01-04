# Check whether a year is Leap year or not - Way 1
class LeapYear:
    def isLeapYear(self,year):
        if year < 1900:
            return None
        return year % 400 ==0 or (year % 4 == 0 and year % 100!=0)

obj = LeapYear()
year = int(input("Enter the year:"))
result = obj.isLeapYear(year)

if result is None:
    print("Please enter a year greater than or equal to 1900")
elif result:
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")

"""
Input: Enter the year:2000
Output: 2000 is a Leap Year

Input: Enter the year:1899
Output: Please enter a year greater than or equal to 1900
"""


# Checks a list of years whether it is Leap year or not - Way 2
class LeapYear:
    def isLeapYear(self,years_list):
        result = []
        for year in years_list:
            if year < 1900:
                continue
            if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
                result.append(f"{year} Leap Year")
            else:
                result.append(f"{year} Not a Leap Year")
        return result

obj = LeapYear()
years_list = list(map(int,input("Enter the years:").split()))
output = obj.isLeapYear(years_list)

for year in output:
    print(year, end = "  ")

"""
Input: Enter the years: 2004 2000 1900 1899 2005
Output: 2004 Leap Year  2000 Leap Year  1900 Leap Year  2005 Not a Leap Year
"""
