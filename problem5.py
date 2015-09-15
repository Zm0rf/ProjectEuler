

def evenDevided(maxDiv, maxNumber):
    for x in range(1, maxNumber):
        f = True
        for y in range(2, maxDiv):
            if x % y == 0:
                print x, " passes", y
            else:
                print x, " failed", y
                f = False        
                break
                

        if f:
            return x


print evenDevided(21, 100000)
