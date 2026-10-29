def get_grade(marks):
  if marks>=90:
    return "A+"
  elif marks>= 80:
    return "A"
  elif marks>= 70:
    return "B"
  elif marks>=60:
    return "C"
  else:
    return "Fail"
    sudents_marks=[95,85,72,55]

for marks in students_marks:
     grade = get_grade(marks)
    print(f"Marks: {marks}-> Grade:{grade}")
