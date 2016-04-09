def findProductForPythagoreanTriplet(maxValue):
    ret = 0

    for a in range(1, maxValue*2):
        for b in range(1, maxValue*2):
            for c in range(1, maxValue*2):
                if a+b+c == maxValue:
                    #print "Found:", str(a), " - ", str(b), " - ", str(c), " = ", str(a+b+c)
                    #print str(a*a), " - ", str(b*b), " - ", str(c*c)
                    if a*a + b*b == c*c:
                        #print "Found pytheagorean", str(a), " - ", str(b), " - ", str(c)
                        return a*b*c
                    


    return ret



print findProductForPythagoreanTriplet(1000)
