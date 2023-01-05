import math
def solve(n, k, roads):
    # Write your code here
    gf = []
    hp = [] # cost, node index
    tb1 = []
    tb2 = []
    for fr in range(n):
        gf.append([]) # node, to, cost
        tb1.append([fr, -1, 2**31, False, -1, -1]) # node, from, cost, visited, heap index, originally from
        tb2.append([fr, -1, 2**31, False, -1, -1]) # node, from, cost, visited, heap index, originally from        
    for road in roads:
        src = road[0]-1
        dst = road[1]-1
        cost = road[2]
        gf[src].append([src, dst, cost])
        gf[dst].append([dst, src, cost])
    print(gf)

    nodep = roads[k-1][0]-1
    noden = roads[k-1][1]-1
    rddis = roads[k-1][2]
    print('p=', nodep, 'n=', noden, 'rdlen=', rddis)
    print('1...............')
    fromm = nodep
    tb1[nodep][1] = fromm
    tb1[nodep][5] = fromm
    tb1[nodep][2] = 0
    hp.append([0, nodep])
    tb1[nodep][4] = 0
    for i in range(n):
        if(i<nodep): tb1[i][4] = i+1
        elif(i==nodep): continue    
        elif(i>nodep): tb1[i][4] = i
        hp.append([2**31, i])
    # print(hp)
    dijkstra(hp, tb1, gf, nodep, noden)
    print('2....................')
    hp = []
    hp.append([0, noden])
    fromm = noden
    tb2[noden][1] = fromm
    tb2[noden][5] = fromm
    tb2[noden][2] = 0
    tb2[noden][4] = 0
    for i in range(n):
        if(i<noden): tb2[i][4] = i+1
        elif(i==noden): continue    
        elif(i>noden): tb2[i][4] = i
        hp.append([2**31, i])
    dijkstra(hp, tb2, gf, nodep, noden)

    posdis = 0
    negdis = 0
    # for it in tb1:
    #     if(it[2]>posdis and it[5]==nodep and it[1]!=nodep): posdis = it[2]
    # for it in tb2:
    #     if(it[2]>negdis and it[5]==noden and it[1]!=noden): negdis = it[2]
    for idx in range(n):
        if(tb1[idx][2]<tb2[idx][2] and tb1[idx][5]==nodep and idx!=nodep and posdis<tb1[idx][2]):
            posdis = tb1[idx][2]
        if(tb2[idx][2]<tb1[idx][2] and tb2[idx][5]==noden and idx!=noden and negdis<tb2[idx][2]):
            negdis = tb2[idx][2]
        
    mid = (posdis+negdis+rddis)/2
    print('posdis=', posdis, 'negdis=', negdis, 'rddis', rddis, 'mid=', mid)
    pos = mid-posdis
    maxdis = mid

    result = "%.5f %.5f"%(pos, maxdis)
    print(result)
    return result
    # return pos, maxdis

def dijkstra(hp, tb, gf, np, nn):
    while hp:
        node = hp[0][1]
        # print('node=', node)
        # print('table=', tb)
        # print('top hp=', hp)
        hp[0] = hp[-1]
        tb[node][4] = -1
        tb[hp[-1][1]][4] = 0
        del hp[-1]
        # heapify adjust down
        idx = 0
        while idx < len(hp):
            pt = hp[idx][0]
            if(2*idx+1 < len(hp)):
                lf = hp[2*idx+1][0]
            else:
                lf = 2**32
            if(2*idx+2 < len(hp)):
                rt = hp[2*idx+2][0]
            else:
                rt = 2**32            
            if(pt<=lf and pt<=rt): break
            elif(lf<pt and lf<=rt):
                hp[2*idx+1], hp[idx] = hp[idx], hp[2*idx+1]
                tb[hp[idx][1]][4] = 2*idx+1
                tb[hp[2*idx+1][1]][4] = idx
                idx = 2*idx+1
            elif(rt<pt and rt<=lf):
                hp[2*idx+2], hp[idx] = hp[idx], hp[2*idx+2]
                tb[hp[idx][1]][4] = 2*idx+2
                tb[hp[2*idx+2][1]][4] = idx
                idx = 2*idx+2
        if(tb[node][3] == False): tb[node][3] = True
        else: continue
        # update connection
        for path in gf[node]:
            # print('path=', path)
            dst = path[1]
            cst = path[2]
            if(tb[dst][3] == True): continue
            if(tb[dst][2] > tb[node][2]+cst):
                tb[dst][2] = tb[node][2]+cst
                tb[dst][1] = node
                # find original source
                if(node == nn and dst == np or 
                    node == np and tb[np][5] == np or
                    dst != nn and tb[node][5] == np):
                    tb[dst][5] = np
                elif(node == np and dst == nn or
                    node == nn and tb[nn][5] == nn or
                    dst != np and tb[node][5] == nn):
                    tb[dst][5] = nn
                # heapify adjust up
                up = tb[dst][4]
                hp[up][0] = tb[dst][2]
                while up >= 0:
                    # print('dst=', dst, 'upidx in hp=', up, 'up=', hp[up][0])
                    # print('hp=', hp)
                    ct = hp[up][0]
                    ptidx = math.floor((up-1)/2)
                    if(ptidx < 0): pt = -1
                    else: pt = hp[ptidx][0]
                    if(pt <= ct): break
                    else:
                        hp[up], hp[ptidx] = hp[ptidx], hp[up]
                        tb[hp[up][1]][4] = up
                        tb[hp[ptidx][1]][4] = ptidx
                        up = ptidx

n=4
k=1
# roads = [[1,2,10],[2,3,10],[3,4,1],[4,1,5]]
roads = [[1,2,10],[2,3,10],[3,4,1],[4,1,10]]
# roads = [[1,2,10],[2,3,20],[3,4,15],[4,1,17]]
solve(n, k, roads)
