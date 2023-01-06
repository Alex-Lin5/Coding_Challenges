def solution(pl: int, flowers: int) -> int:
  if(pl >= len(flowers)):    
    return sum(flowers)
  flowers.sort()
  # flowers.reverse()
  price = 0
  N = len(flowers)
  K = pl
  cof = 1          
  gpidx = 1
  for pflower in range(N-1, -1, -1):
  # for pflower in range(0, N):
    price += flowers[pflower]*cof
    gpidx += 1
    if(gpidx > K):
      gpidx = 1
      cof+=1
  print(price)
  return price
  
# def solution(k, c):
#     n = len(c)
#     c.sort(reverse=True)
#     cost = 0
#     previous_purchase = 0
#     for i in range(n):
#         cost += (previous_purchase +1) * c[i]
#         if (i+1)%k==0:
#             previous_purchase += 1
#     return cost


# ans = solution(3, [1,3,5,7,9])
# ans = solution(2, [2,5,6])

flowers1 = [120854, 100862, 523789, 849072, 23733, 355147, 660925, 59103, 801528, 607947, 51312, 754005, 823629, 876280, 23088, 668838, 214629, 641310, 66064, 541147, 97284, 579336, 319949, 193067, 35064, 227785, 376976, 146458, 258150, 551784, 961936, 189099, 552128, 318057, 39381, 41667, 316754, 680180, 681303, 7132, 472252, 791845, 540485, 464674, 336442, 572655, 724577, 627822, 553055, 986861, 944776, 588636, 966817, 892103, 737744, 478475, 668429, 809085, 362250, 597680]
res = solution(18, flowers1) # 46361218, len(flowers1) = 60
ans = 46361218
print(ans, res, ans-res)