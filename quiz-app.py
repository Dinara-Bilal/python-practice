questions = [
  {"q": "Name Of Python Creater?","a": "Guido"},
  {"q": "2+2=?", "a": "4"},
  {"q": "Pakistan's Capital Name?", "a": "Islamabad"}
]
score=0
for i, ques in enumerate(questions,1):
   print(f"\nQ(i): {ques['q]}")
                    user_ans= ques['a']
                    print(f"Amswer: {user_ans}")

                    if user_ans.lower() == ques['a'].lower():
      print("Correct!")
      score += 1
      else:
print("Wrong!")
print(f"\nFinal Score: {score}/{len(questions)}")
