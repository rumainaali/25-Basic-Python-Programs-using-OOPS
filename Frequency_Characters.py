# Find the Frequency of Characters
class FrequencyCharacter:
    def freqChar(self,string):
        freq = {}
        for char in string:
            if char == " ":
                continue
            if char in freq:
                freq[char]+=1
            else:
                freq[char]=1
        return freq

obj = FrequencyCharacter()
string = input("Enter the string:")
result = obj.freqChar(string)
print("Frequency of Characters:",result)

"""
Input: Enter the string:madam
Output: Frequency of Characters:{'m':2,'a':2,'d':1}
"""
