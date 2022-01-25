import random

TAILS = 0
HEADS = 1

coin_side = random.randint(0, 1);

if coin_side == TAILS:
  print("tails")
if coin_side == HEADS:
  print("heads")