import random
import string

def generate_password(lenght=8):
    chars = string.ascii_ketters + string.digits
  password =".join(random.choice(chars)for _ in range(length)))
   return password

for i in range(3):
   print(f"Password {i+1}: {genetate_password(10)}"}
