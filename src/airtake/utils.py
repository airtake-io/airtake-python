from time import time_ns

def timestamp() -> int:
  return time_ns() // 1_000_000
