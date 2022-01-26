student_heights = input("Input a list of student heights: ").split()

height_sum = 0

for i in range (0, len(student_heights)):
  student_heights[i] = int(student_heights[i])
  height_sum += student_heights[i]

average = round(height_sum / len(student_heights))

print(average)
