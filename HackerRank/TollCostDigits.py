def BFS(gf, tk, src, dst):
    que = []
    que.append(src)
    tb = [[i, -1, False] for i in range(len(gf))] # node, from, visited
    node = src
    tb[src][1] = node
    while que:
        node = que.pop()
        fm = tb[node][1]
        bsct = tk[src][node][fm][3]
        if(tb[node][2] == False): tb[node][2] = True
        else: continue
        for i in range(len(gf[node])):
            nb = gf[node][i][1]
            cst = gf[node][i][2]
            cap = gf[node][i][3] # from node to neighbor
            ttct = cst + bsct
            # if(tb[nb][2] == True): continue
            if(cap > 0): continue
            else:
                que.insert(0, nb)
                tb[nb][1] = node
                tk[src][nb][node][3] = ttct
                gf[node][i][3] = 1
                gf[nb][i][3] = -1
    if(tb[dst][1] == -1): return False
    else: return True
                
def EdmondsK(gf, tk, src, dst):
    while BFS(gf, tk, src, dst):
        pass
def resetGraph(gf):
    for node in range(len(gf)):
        for path in range(len(gf[node])):
            gf[node][path][3] = 0

def solve(roads):
    rdnum = len(roads[0])
    gf = [[] for _ in range(rdnum)] # source, destiny, cost, visited edge
    # [source[, destiny[, last visited node, cost
    tk = [[[[src, dst, lst, -1] for lst in range(rdnum)] for dst in range(rdnum)] for src in range(rdnum)] 
    for i in range(rdnum):
        src = roads[0][i]-1
        dst = roads[1][i]-1
        cst = roads[2][i]
        gf[src].append([src, dst, cst, 0])
        gf[dst].append([dst, src, 1000-cst, 0])
        tk[src][dst][src] = [src, dst, src, cst]
        tk[dst][src][dst] = [dst, src, dst, 1000-cst]
    for i in range(len(gf)):
        tk[i][i][i] = [i, i, i, 0]
    print('graph:', gf)
    print('track:', tk)

    for i in range(len(gf)):
        src = i
        for j in range(len(gf)):
            dst = j
            resetGraph(gf)
            EdmondsK(gf, tk, src, dst)
            resetGraph(gf)
            EdmondsK(gf, tk, dst, src)        
    
    result = [0 for _ in range(10)]
    for src in tk:
        for dst in src:
            tp = [0 for _ in range(10)]
            for lst in dst:
                cst = lst[3]
                if(cst == -1 or cst == 0): continue
                dig = cst%10
                if(tp[dig] == 0): tp[dig] = 1
            for i in range(10):
                result[i] += tp[i]
    print('result:', result)
    return result

rds = [[1,1,2],[3,2,3],[602,256,411]]
solve(rds)
ans = [0, 2, 1, 1, 2, 0, 2, 1, 1, 2]
print('answer:', ans)

