import copy
import random
#MEMORY = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,19,5,23,1,13,23,27,1,27,6,31,2,31,6,35,2,6,35,39,1,39,5,43,1,13,43,47,1,6,47,51,2,13,51,55,1,10,55,59,1,59,5,63,1,10,63,67,1,67,5,71,1,71,10,75,1,9,75,79,2,13,79,83,1,9,83,87,2,87,13,91,1,10,91,95,1,95,9,99,1,13,99,103,2,103,13,107,1,107,10,111,2,10,111,115,1,115,9,119,2,119,6,123,1,5,123,127,1,5,127,131,1,10,131,135,1,135,6,139,1,10,139,143,1,143,6,147,2,147,13,151,1,5,151,155,1,155,5,159,1,159,2,163,1,163,9,0,99,2,14,0,0]
#second round
MEMORY = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,19,5,23,1,13,23,27,1,27,6,31,2,31,6,35,2,6,35,39,1,39,5,43,1,13,43,47,1,6,47,51,2,13,51,55,1,10,55,59,1,59,5,63,1,10,63,67,1,67,5,71,1,71,10,75,1,9,75,79,2,13,79,83,1,9,83,87,2,87,13,91,1,10,91,95,1,95,9,99,1,13,99,103,2,103,13,107,1,107,10,111,2,10,111,115,1,115,9,119,2,119,6,123,1,5,123,127,1,5,127,131,1,10,131,135,1,135,6,139,1,10,139,143,1,143,6,147,2,147,13,151,1,5,151,155,1,155,5,159,1,159,2,163,1,163,9,0,99,2,14,0,0]

#RAM = copy.copy(MEMORY)



def randomNun(nouns):
    return nouns.pop(random.randrange(len(nouns)))

def randomVerb(verbs):
    return verbs.pop(random.randrange(len(verbs)))

def phraseGenerator():
    SIZE = 100
    nouns = list(range(0, SIZE))
    while bool(len(nouns)):
        n = randomNun(nouns)
        verbs = list(range(0, SIZE))
        while bool(len(verbs)):
            v = randomVerb(verbs)
            yield (n,v)

def add(idx, RAM):
        resultIdx = RAM[idx+3]
        r = (RAM[RAM[idx+1]] + RAM[RAM[idx+2]])
        RAM.pop(resultIdx)
        RAM.insert(resultIdx, r)
    

def multiply(idx, RAM):
    resultIdx = RAM[idx+3]
    r = (RAM[RAM[idx+1]] * RAM[RAM[idx+2]])    
    RAM.pop(resultIdx)
    RAM.insert(resultIdx, r)
    

def inputs(idx):
    destination = RAM[idx+1]
    RAM[destination] = "T"

def outputs(idx):
    source = RAM[idx+1]
    print(RAM[source])

def paramMode(paramAdr, mode, RAM):
    val = None
    if mode == 1: # direct mode
        val = RAM[paramAdr]
    elif mode == 0:
        val = RAM[RAM[paramAdr]]
    else: 
        raise Exception("Unknown param mode")
    return val

def OPERATION(idx, RAM, Uinput=None, ReturnDest=None):
    OP = RAM[idx]
    #print("( ", idx, " - ", OP, ")")
    NEXT = -1

    modeA = 0
    modeB = 0
    modeC = 0
    opcode = 0
    A = 0
    B = 0
    destAdr = 0

    if OP == 99:
        return -1
    elif OP < 99:
        opcode = OP
        MODES = "000"
        """ if opcode == 3:
            destAdr = RAM[idx+1]
        elif opcode == 4:
            A = RAM[idx+1]
        else:
            A = RAM[RAM[idx+1]]
            B = RAM[RAM[idx+2]]
            destAdr = RAM[idx+3] """
    elif OP > 99:
        opcode = int(str(OP)[-2:])
        MODES = str(OP)[:-2].zfill(3)

    modeA = int(MODES[-1])
    modeB = int(MODES[-2])
    modeC = int(MODES[-3])

    if opcode == 3:
        destAdr = paramMode(idx+1, 1, RAM)
    elif opcode == 4:
        A = paramMode(idx+1, modeA, RAM)
    else:
        A = paramMode(idx+1, modeA, RAM)
        B = paramMode(idx+2, modeB, RAM)
        destAdr = paramMode(idx+3, 1, RAM)
        """ if modeC == 1: # this has no sense
            destAdr = RAM[idx+3]
            raise Exception("this should never happen")
        else:
            destAdr = RAM[idx+3]
    else:
        raise Exception("Unknown OPCODE", OP) """


    if opcode == 2:
        RAM[destAdr] = A * B
        NEXT = 4
    if opcode == 1:
        RAM[destAdr] = A + B
        NEXT = 4
    if opcode == 3:
        user_input = None
        if isinstance(Uinput, list):
            user_input = int(Uinput.pop(0))
        else:
            user_input = input("Enter a value: ")
        RAM[destAdr] = int(user_input)
        NEXT = 2
    if opcode == 4:
        if isinstance(Uinput, list):
            ReturnDest.append(A)
        else:
            print(A)
        NEXT = 2
    if opcode == 5:
        if A != 0:
            NEXT = (0,B)
        else:
            NEXT = 3
    if opcode == 6:
        if A == 0:
            NEXT = (0,B)
        else:
            NEXT = 3
    if opcode == 7:
        if A < B:
            RAM[destAdr] = 1
        else:
            RAM[destAdr] = 0
        NEXT = 4
    if opcode == 8:
        if A == B:
            RAM[destAdr] = 1
        else:
            RAM[destAdr] = 0
        NEXT = 4

    return NEXT

def execute(RAM, Uinput=None, ReturnDest=None):
    idx = 0

    while idx < len(RAM):
        NEXT = OPERATION(idx, RAM, Uinput, ReturnDest)
        if isinstance(NEXT, int):
            if NEXT < 0:
                break
            else:
                idx += NEXT
        else:
            idx = NEXT[1]


if __name__ == "__main__":
    """ for n,v in phraseGenerator():
        RAM = copy.copy(MEMORY)
        RAM[1] = n
        RAM[2] = v
        execute(RAM)
        if RAM[0] == 19690720:
            print("HAAAA ", RAM[0], n, v)
            print((100*n)+v)
            break """
    pass
        