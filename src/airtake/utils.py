from time import time_ns
from random import random

alphabet = '_-0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def generate_id() -> str:
  alphabet_len = len(alphabet)

  id = ''
  for _ in range(32):
      id += alphabet[int(random() * alphabet_len) | 0]
  return id

def timestamp() -> int:
  return time_ns() // 1_000_000
