scores = input("Type list of scores: ").split()
for i in range(0, len(scores)):
  scores[i] = int(scores[i])

if len(scores) > 1:
  max_score = scores[0]

  for score in scores:
    if score > max_score:
      max_score = score
  
  print(f"Max value is: {max_score}")
else:
  print("Score list is empty")



