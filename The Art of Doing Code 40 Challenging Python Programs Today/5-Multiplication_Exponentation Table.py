print("Welcome to the Multiplication/Exponentation Table")
name=input("What is your name: ")
number=float(input("What number would like to work with: "))
print(f"\nMultiplication Table For {number}")
for n in range(1,10):
      result=round(number * n,2)
      print(f"\t{float(n)} * {number} = {result}")
print(f"\nExponent Table For {number}")
for m in range(1,10):
      result=round(number**m,4)
      print(f"\t{number} ** {m} = {result}")
titled_name=name.title().strip()
phrase=" Math is cool!"
print(f"{titled_name}" + f"{phrase.title()}")
print(f"{name}" + f"{phrase.lower()}")
print(f"\t{name.title()}" + f"{phrase.title()}")
print(f"\t\t{name.upper()}" + f"{phrase.upper()}")
