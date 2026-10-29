import random
import string

print("===Strong Password Generator ===")
length = int(intput("Password Length?(e.g. 12):"))
chars = string.ascii_letters + string.digits + string.punctuation

password = "".join(random.choice(chars)for _ in range(length))
print(f"\nGenerated Password: {password}")
print("Strong password! Use it safely")
