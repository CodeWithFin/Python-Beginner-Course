numbers = [2,2,4,6,3,4,6,1]
numbers_list = []

numbers.sort()
for number in numbers:
    if number not in numbers_list:
        numbers_list.append(number)
   
print(numbers_list)