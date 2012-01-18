def abs(dif):
  if dif > 0:
    return dif
  else:
    return -dif

def diff21(n):
  if n <= 21:
    return abs(n-21)
  else:
    return 2 * abs(n-21)