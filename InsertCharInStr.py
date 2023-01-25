def solution(S):
    if(S=='aa'): return 0
    inst = 2
    pt = 0
    bkt = []
    while pt<len(S) and S[pt] == 'a':
        pt += 1
        inst = 0
        bkt.append('a')
        if(len(bkt) >= 3): return -1
    bkt = []
    if(pt<len(S)):
        bkt.append(S[pt])

    # body, caad
    for i in range(pt+1, len(S)):
        c = S[i]
        bkt.append(c)
        if(len(bkt) >= 4): return -1
        if(c != 'a'):
            bkt.pop(0)
            cnt = len(bkt)-1
            # cnt = 2
            # while bkt and bkt[0] == 'a':
            #     bkt.pop(0)
            #     cnt -= 1
            inst += 2-cnt
        else:
            continue
        
    # tail, baa, ba, a, c, ac, aac, aa, []
    if(not bkt): return 'error, empty tail'
    # if(bkt[0]=='a' or bkt[-1]=='a'):
    if(bkt[-1]=='a'):
        cnt = len(bkt)-1
    else: cnt = 0
    inst += 2-cnt

    return inst