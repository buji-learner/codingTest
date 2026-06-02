numbers = [1,2,3,4,6,7,8,0]
full_numbers = [i for i in range(10)]
# print(full_numbers)

for num in numbers:
    full_numbers.remove(num)

print(full_numbers)

print(sum(full_numbers))


