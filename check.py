student = {
   "name": "Sanawan Student",
   "grade": "A+",
   "skills": ["MS Office", "Python"]
}
def check_eligibility(s):
    if s["grade"] == "A+" and "Phython" in s["skills"}:
           return "Eligible for Outreachy"
  return "Need more skills"
  print(check_eligibility(student))
