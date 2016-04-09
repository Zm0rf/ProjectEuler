import math

def calculateSquareOfNaturalNumbers():
    i = 0
    for x in range(1, 101):
        i = i + x

    print "First:", i*i
    return i*i


def calculateSquareOfIndividualNaturalNumbers():
    ret = 0
    for x in range(1, 101):
        ret = ret + x*x

    print "Second:", ret
    return ret


print calculateSquareOfIndividualNaturalNumbers() - calculateSquareOfNaturalNumbers()
