tal1 = 1
tal2 = 2
sum = 0

while tal2 < 4000000:
    #check tal 2
    if tal2 % 2 == 0:
        sum = sum + tal2
    #calculate new tal 2
    tmp = tal1
    tal1 = tal2
    tal2 = tmp + tal1


print sum
