#count even and odd
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = 0
odd = 0
for i in numbers:
    if i % 2 == 0:
        even += 1
    elif i % 2 != 0:
        odd += 1

print(f'the number of even numbers is: {even}')
print(f'the number of even numbers is: {odd}')


    
