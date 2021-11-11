import sys

result = 0

Temperature = int(input())

setNum = input().split()

for num in setNum:
    
    if int(num) < 0:
        result += 1
        
print (result)
