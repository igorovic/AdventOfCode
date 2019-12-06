import collections
from anytree import Node, RenderTree
from anytree.exporter import DotExporter
from anytree.dotexport import RenderTreeGraph
from anytree.util import commonancestors



def ShowTree(T):
    for pre, fill, node in RenderTree(T):
        print("%s%s" % (pre, node.name))


def constructTree(sourceFile):
    #COM = Node("COM")
    TREE = collections.OrderedDict()
    #TREE["root"] = COM

    with open(sourceFile, "r") as SOURCE:
        for line in SOURCE:
            nodes = line.split(")")
            A, B = nodes
            B = B.rstrip('\n')
            if not A in TREE.keys():
                TREE[A] = Node(A)
            if not B in TREE.keys():
                TREE[B] = Node(B)
            
            TREE[B].parent = TREE[A]
            
 
    return (TREE['COM'], TREE)
    
def calculateOrbits(TREE):
    TOTAL = 0
    for K in TREE.keys():
        TOTAL += len(TREE[K].anchestors)
    print(TOTAL)


ROOT, TREE = constructTree("orbits2.txt")
FIRST_COMMON_ANCESTOR = commonancestors(TREE["YOU"], TREE["SAN"])[-1]

def distanceToTargetNode(Node, Target):
    DISTANCE = 0 
    ANCH = list(Node.anchestors)
    ANCH.reverse()
    for A in ANCH:
        if A == Target:
            break
        else:
            DISTANCE += 1
    #print(DISTANCE)
    return DISTANCE

# 122782 => RIGHT answer

# 63 => WRONG
if __name__ == "__main__":
    
    D1 = distanceToTargetNode(TREE["YOU"], FIRST_COMMON_ANCESTOR)
    D2 = distanceToTargetNode(TREE["SAN"], FIRST_COMMON_ANCESTOR)
    print( D1 + D2)
    print(FIRST_COMMON_ANCESTOR)
    DotExporter(ROOT).to_dotfile("tree.dot")
    #DotExporter(FIRST_COMMON_ANCESTOR).to_dotfile("tree.dot")
    