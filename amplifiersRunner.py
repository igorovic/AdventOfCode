import copy
from subprocess import Popen, PIPE
from IntcodeComputer import *


RAM = [3,8,1001,8,10,8,105,1,0,0,21,42,67,84,97,118,199,280,361,442,99999,3,9,101,4,9,9,102,5,9,9,101,2,9,9,1002,9,2,9,4,9,99,3,9,101,5,9,9,102,5,9,9,1001,9,5,9,102,3,9,9,1001,9,2,9,4,9,99,3,9,1001,9,5,9,1002,9,2,9,1001,9,5,9,4,9,99,3,9,1001,9,5,9,1002,9,3,9,4,9,99,3,9,102,4,9,9,101,4,9,9,102,2,9,9,101,3,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,99]

TEST1 = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
T1INPUTS = [4,3,2,1,0]

TEST2 = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
T2INPUTS = [0,1,2,3,4]

TEST3 = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
T3INPUTS = [1,0,4,3,2]

TESTB1 = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]

def genInputs():
    for A1 in list(range(5, 10)):
        for A2 in list(range(5, 10)):
            for A3 in list(range(5, 10)):
                for A4 in list(range(5, 10)):
                    for A5 in list(range(5, 10)):
                        yield [A1, A2, A3, A4, A5]

def filteredInputs():
    for I in genInputs():
        if any(I.count(x) > 1 for x in I):
            continue
        else:
            yield I


if __name__ == "__main__":
A1 = Popen(["python", "./Amplifier.py"], stdout=PIPE)
A2 = Popen(["python", "./Amplifier.py"], stdin=A1.stdout, stdout=PIPE)
A1.stdout.close()
output = A2.communicate()
    print(output)



    """ RESULTS = list()
    PROGRAMS = [
        copy.copy(TESTB1),
        copy.copy(TESTB1),
        copy.copy(TESTB1),
        copy.copy(TESTB1),
        copy.copy(TESTB1)]

    InitialSettings = [9,8,7,6,5]
    I = copy.copy(InitialSettings)
    Inext = []
    
    RET = [0]
    ITERCNT = 0
    MAXITER = 100
    RESULT = None

    while True:
        ITERCNT += 1
        execute(PROGRAMS[0], Uinput=[I[0], RET[-1]], ReturnDest=RET)
        Inext.append(RET[-1])
        execute(PROGRAMS[1], Uinput=[I[1], RET[-1]], ReturnDest=RET)
        Inext.append(RET[-1])
        execute(PROGRAMS[2], Uinput=[I[2], RET[-1]], ReturnDest=RET)
        Inext.append(RET[-1])
        execute(PROGRAMS[3], Uinput=[I[3], RET[-1]], ReturnDest=RET)
        Inext.append(RET[-1])
        execute(PROGRAMS[4], Uinput=[I[4], RET[-1]], ReturnDest=RET)
        Inext.insert(0, RET[-1])
        if RET[-1] == RESULT:
            print("RESULT", RESULT)
            print("Settings ", I)
            break
        I = copy.copy(Inext)
        RET = []

        if ITERCNT >= MAXITER:
            break """

