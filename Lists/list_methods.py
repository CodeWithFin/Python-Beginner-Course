numbers = [5,2,1,7,4]
numbers.insert(2,56)#inserts a number into a list at a particular index
numbers.pop()#removes the last number in the list
numbers.index(2)#displays the index of the number that you have entered
numbers.remove(5)#removes the number you have entered from the list 
print(56 in numbers)#looks if the number you have entered is in the list and outputs either true or false
print(numbers.count(5))#tells you how many times a number has appeared in your list
numbers.sort()#sorts list in ascending order
numbers2 = numbers.copy()#cpies list into a new variable
numbers.reverse()#sort list in descending order
numbers.append(13)#adds a number to the last index ofthe list
numbers.clear()#clears a list and lets it be empty

print(numbers)
