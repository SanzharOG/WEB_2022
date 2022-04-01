def sum67(nums):
  cnt = 0
  blocked = False
  
  for i in nums:
    if i == 6:
      blocked = True
      continue
    if i == 7 and blocked:
      blocked = False
      continue
    if not blocked:  
      cnt += i
  
  return cnt