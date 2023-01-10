# numbers = [2,3,1,6,5,7,9,10]

# numbers.append(13)                      #adding 13 to the end of list
# print(numbers)                          

# numbers.insert(2,20)                    #.insert(index,value)
# print(numbers)

# numbers.remove(1)                       #Will remove 1 from list
# #numbers.clear()                        #Will clear the list completely
# numbers.pop()                           #Will also remove numbers but by default, it'll be from the last
# print(numbers)

# print(numbers.index(5))                 #Will Print index of 5
# print(50 in numbers)                    #Will return True if 50 is in the list or False if 50 is not in the list

# numbers.sort()                          #Will Sort the list
# print(numbers)

# numbers.reverse()                       #Reversing the current list
# print(numbers)

# numbers2 = numbers.copy()               #Copies list to new list
# print(numbers2)

#Write a program to remove the duplicates in a list

numbers = [1,2,7,3,2,4,9,1]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
