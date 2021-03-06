import sys
sys.setrecursionlimit(10**6)

def printStar(l):
    if l == 1:
        return ['*']
    
    stars =  printStar(l//3)
    tmp = []
    for s in stars:
        tmp.append(s*3)
    for s in stars:
        tmp.append(s+' '*(l//3)+s)
    for s in stars:
        tmp.append(s*3)
    return tmp
        
n = int(input())
print('\n'.join(printStar(n)))