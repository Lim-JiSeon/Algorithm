import sys, re
input = sys.stdin.readline

def slimp(s):
    if len(s) < 2:
        return 0
    elif len(s) == 2 and s == 'AH':
        return 1
    elif s[0] == 'A' and s[-1] == 'C':
        if s[1] == 'B':
            return slimp(s[2:-1])
        else:
            return slump(s[1:-1])
    else:
        return 0
    
def slump(s):
    if re.search('((D|E)F+)+G$',s):
        return 1
    else:
        return 0

def slurpy(s):
    slump = re.search('((D|E)F+)+G$',s)
    if slump and slump.span()[0] > 1 and slimp(s[:slump.span()[0]]):
        return 1
    return 0

n = int(input())
print("SLURPYS OUTPUT")
while n:
    n -= 1
    s = input()
    if slurpy(s):
        print("YES")
    else:
        print("NO")
    
print("END OF OUTPUT")
