# Sort Dictionary By Value
class SortDict:
    def sortDict(self,dict1):
        keys = list(dict1.keys())
        values = list(dict1.values())
        for i in range(len(values)):
            for j in range(i+1,len(values)):
                if values[i] > values[j]:
                    values[i],values[j] = values[j],values[i]
                    keys[i],keys[j] = keys[j],keys[i]
        
        sorted_dict = {}
        for i in range(len(keys)):
            sorted_dict[keys[i]] = values[i]
        return sorted_dict

obj = SortDict()
dict1 = {}
n = int(input("Enter the number of key and value pairs:"))
for _ in range(n):
    key = input("Enter the key:")
    value = int(input("Enter the value:"))
    dict1[key] = value
print(dict)
result = obj.sortDict(dict1)
print("Sorted by Value:",result)


"""
Input: Enter the number of key and value pairs: 2
Enter the key:a
Enter the value: 5
Enter the key: b
Enter the value: 1

Output: Sorted by Value: {'b':1,'a':5}
"""
            
