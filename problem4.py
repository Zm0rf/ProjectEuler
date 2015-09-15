
def findPalindromeProduct(max, min):
    ret = 0
    for x in range(max, min, -1):
        for y in range(max, min, -1):
            res = x * y
            if res > ret:
                if str(res) == str(res)[::-1]:
                    ret = res
    return ret

print findPalindromeProduct(999, 100)
