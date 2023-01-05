def solution(pl: int, flowers: int[]) -> int:
  if(pl >= len(flowers)):    
    return sum(flowers)
  price = 0
  front = 0 
  back = len(flowers)-1
  avg = (back+1)/pl
  rem = (back+1)%pl
  for cus in range(pl):
    idx = 0
    cof = 0
      
    while idx < avg:
      
      idx+=1
    if(cus < rem):
      front+=1
      cof+=1
      price += flowers[front]*cof
  return price

ans = solution(3, [1,3,5,7,9])