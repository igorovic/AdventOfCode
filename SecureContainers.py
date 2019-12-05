import copy
START = 235741
END = 706948


def NeverDecrease(value):
    digits = [int(x) for x in str(value)]
    for i in range(len(digits)):
        if i == 0:
            continue
        if digits[i] < digits[i-1]:
            return False
    return True

def DoublePresent(value):
    digits = [int(x) for x in str(value)]
    for i in range(len(digits)):
        if i == 0:
            continue
        if digits[i] == digits[i-1]:
            return True
    return False


def OnlyTwoDigitsDoubles(value):
    digits = [int(x) for x in str(value)]
    doubles = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

    for i in range(len(digits)):
        if i == 0:
            continue
        if digits[i] == digits[i-1]:
            doubles[digits[i]] += 1

    #del doubles[first]
    for k in copy.copy(doubles).keys():
        if doubles[k] == 0:
            del doubles[k]

    #if len(doubles.keys()) == 1 and list(doubles.values())[0] > 1:
    #    return False
    #else:
    for k in doubles.keys():
        hasDouble = False
        if doubles[k] == 1:
            hasDouble = True
            break
    if not hasDouble:
        print(value, " discarded")
        return False
    
    #print(value, doubles)
    return True

def display(R, R2):
    #print(R)
    print(len(R))
    print("======")
    #print(R2)
    print(len(R2))

def main():
    R = []
    R2 = []
    CURRENT = START
    while CURRENT < END:
        #while not NeverDecrease(CURRENT) or not DoublePresent(CURRENT):
        #    CURRENT += 1

        #if OnlyTwoDigitsDoubles(CURRENT):
        #    R.append(CURRENT)
        if NeverDecrease(CURRENT) and DoublePresent(CURRENT):
            R.append(CURRENT)
        CURRENT += 1

    for VAL in R:
        if OnlyTwoDigitsDoubles(VAL):
            R2.append(VAL)

    display(R, R2)

# 628 => WRONG 
# 670 => WRONG
# 598 => WRONG
# 445 => WRONG
# 781 => WRONG
if __name__ == "__main__":
    #T = [699999, 355577, 344466, 444445, 444499, 333999]
    #T = [577999]
    #for v in T:
    #    print(OnlyTwoDigitsDoubles(v))
    main()