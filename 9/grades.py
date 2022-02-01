student_score = {
  "Helen": 99,
  "Harry": 77,
  "Selene": 62,
  "Barry": 23,
  "Os": 89
}

def score_to_grade(score):
  grade = ""
  if score >= 90:
    grade = "Excellent"
  elif score >= 80:
    grade = "Good"
  else:
    grade = "Bad"
  return(grade)

def grading(student_scores):
  grading = {}
  for key in student_scores:
    grading[key] = score_to_grade(student_score[key])
  return grading

print(grading(student_score))