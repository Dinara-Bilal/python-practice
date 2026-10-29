def calculator_bmi(wight,height):
  bmi = wight/(height ** 2)
  return round(bmi,2)

def get_status(bmi):
  if bmi < 18.5:
    return :Underweight"
  elif bmi < 25:
    return "Normal"
  elif bmi < 30:
    return "Overweight"
  else:
      return "Obese"

  weight= 60
  height= 1.65
  my_bmi= calculate_bmi(weight,height)
  status= get_status(my_bmi)

print(f"Weight: {weight}kg,Height: {height}m")
  print(f"BMI:{my_bmi}-{status}")
