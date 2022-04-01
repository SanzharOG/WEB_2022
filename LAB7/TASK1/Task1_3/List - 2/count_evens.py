def count_evens(nums):
  cnt = 0
  for i in nums:
    cnt -= i % 2 - 1
  return cnt