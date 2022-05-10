백준 14906번 스러피
===================

### <https://www.acmicpc.net/problem/14906>
<img width="872" alt="image" src="https://user-images.githubusercontent.com/83554018/167604558-39388c18-8075-4016-aed9-a999974edacf.png">

<hr>

### 코드 설명
+ slimp : 문자열 길이가 2 미만일 때와 2일때, 3이상일 때로 나누어 계산한다. 
+ 2미만이라면 0을, 2라면 AH인지 검사한뒤 그 여부에 따라 1 또는 0을 리턴한다.
+ 3 이상이라면 A다음으로 B가 왔을 경우에는 B 이후에 slimp인지를 다시 확인하고(재귀), B가 안 왔을 경우에는 A 다음부터 slump인지를 확인한다.
+ slump : 가장 먼저 D 또는 E가 오는지 확인하고, 그 다음에는 F가 1개 이상 반복해서 와야 하며, 가장 마지막에는 G가 와야 한다.
+ 이와 같은 규칙을 지키지 않는다면 0을 리턴하고 반대라면 1을 리턴한다.
+ slurpy : slump를 먼저 확인한 뒤 slump가 slimp 뒤에 와야 하므로 slump가 시작한 위치를 찾아 그 위치를 기준으로 slimp를 확인한다.

### 소스코드
+ 메모리 : 33580 KB
+ 시간 : 136 ms
```python
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

```
