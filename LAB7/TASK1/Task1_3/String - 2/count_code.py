def count_code(str):
  cnt = 0
  i=0
  while "co" in str[i:]:
    if len(str[i+str[i:].index("co"):]) >= 4 and str[i+3+str[i:].index("co")] == "e":
      cnt += 1
    i += str[i:].index("co")+3
  return cnt