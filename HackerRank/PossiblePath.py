import sys
class point():
    type = 'cartesian coordinate'
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, point):
            return False
        return other.x == self.x and other.y == self.y
    def __hash__(self) -> int:
        return hash((self.x, self.y))
    def __str__(self) -> str:
        return f"{self.x, self.y} "

def solve(li) -> str:
    # print(str(input().strip()))
    # print(sys.argv[1])
    [a,b,x,y] = li
    mov = []
    start = point(a,b)
    end = point(x,y)
    if(x-a>=0): mov.append("RT")
    else: mov.append("LT")
    if(y-b>=0): mov.append("UP")
    else: mov.append("DN")
    if(sys.argv[1]=="-d"): print(start, end, mov)

    stack = [] # stack implementation using list
    stack.append(start)
    visited = set() # default python hash set implementation
    while(stack):
        now = stack[-1]
        if(sys.argv[1]=="-d"): print(now, end=' ')
        if(now == end): return "YES"
        if(mov[0]=="RT"):
            temp = now.x + now.y  
            if(temp <= end.x):
                new = point(temp, now.y)
                if(new not in visited):
                    visited.add(new)
                    stack.append(new)
                    if(sys.argv[1]=="-d"): print("->")
                    continue
        elif(mov[0]=="LT"):
            temp = now.x - now.y  
            if(temp >= end.x):
                new = point(temp, now.y)
                if(new not in visited):
                    visited.add(new)
                    stack.append(new)
                    if(sys.argv[1]=="-d"): print("<-")
                    continue
        if(mov[1]=="UP"):
            temp = now.y + now.x 
            if(temp <= end.y):
                new = point(now.x, temp)
                if(new not in visited):
                    visited.add(new)
                    stack.append(new)
                    if(sys.argv[1]=="-d"): print("^")
                    continue
        elif(mov[1]=="DN"):
            temp = now.y - now.x 
            if(temp >= end.y):
                new = point(now.x, temp)
                if(new not in visited):
                    visited.add(new)
                    stack.append(new)
                    if(sys.argv[1]=="-d"): print("V")
                    continue
        stack.pop()
        if(sys.argv[1]=="-d"): print("oO")
    return "NO"

# print(solve([1,1,5,2])) # true
# print(solve([1,2,3,6])) # false
# print(solve([1,4,5,9])) # true
print(solve([5564, 1059, 4129, 3475])) # true

input = [
    [3299, 7314, 6015, 6906],
    [2584, 2065, 5206, 6088],
    [968, 1238, 91, 9293],
    [7545, 2436, 3299, 4059],
    [5564, 1059, 4129, 3475], # YES
    [1595, 4472, 8536, 7035], # YES
    [3144, 2372, 1788, 1197],
    [3627, 4710, 9834, 6925],
    [8375, 5848, 182, 958],
    [7913, 5387, 3397, 8880], # YES
]
# NO
# NO
# NO
# NO
# YES
# YES
# NO
# NO
# NO
# YES

# for t in input:
#     print(solve(t))

# Solution
# if the greatest common divisor of (a,b) and (x,y) are same, 
# there is a path between 2 points, which they are eventually reachable to 
# point (N, N) where N = gcd(a,b)