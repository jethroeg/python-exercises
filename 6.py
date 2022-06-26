#write a for loop that has the same functionality as the following while loop
# integerList = [1, 2, 3, 4, 5, 6]
# i = 0
# multiplierVariable = 1
# while i < len(integerList):
#   multiplierVariable = multiplierVariable * integerList[i]
#   i += 1
# print(f"The product of all the items in the list is {multiplierVariable}")

integerList = [1, 2, 3, 4, 5, 6]
multiplierVariable = 1
for number in integerList:
    multiplierVariable = multiplierVariable * number

print(f"The product of all the items in the list is {multiplierVariable}")
