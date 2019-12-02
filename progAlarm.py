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
    

def execute(RAM):
    idx = 0

    def add(idx):
        #before = RAM[RAM[idx+3]]
        resultIdx = RAM[idx+3]

        r = (RAM[RAM[idx+1]] + RAM[RAM[idx+2]])
        
        RAM.pop(resultIdx)
        RAM.insert(resultIdx, r)
        #print(RAM[RAM[idx+1]], " + ", RAM[RAM[idx+2]], " = ", RAM[resultIdx], "( ", before, " )")
    

    def multiply(idx):
        #before = RAM[RAM[idx+3]]
        resultIdx = RAM[idx+3]
        r = (RAM[RAM[idx+1]] * RAM[RAM[idx+2]])    
        RAM.pop(resultIdx)
        RAM.insert(resultIdx, r)
        #print(RAM[RAM[idx+1]], " * ", RAM[RAM[idx+2]], " = ", RAM[resultIdx], "( ", before, " )")

    while idx < len(RAM):
        #print(idx)
        if(RAM[idx] == 99):
            break

        if(RAM[idx] == 2):
            multiply(idx)
            idx += 4
            continue
        if(RAM[idx] == 1):
            add(idx)
            idx += 4
            continue

if __name__ == "__main__":
    for n,v in phraseGenerator():
        RAM = copy.copy(MEMORY)
        RAM[1] = n
        RAM[2] = v
        execute(RAM)
        if RAM[0] == 19690720:
            print("HAAAA ", RAM[0], n, v)
            print((100*n)+v)
            break
        