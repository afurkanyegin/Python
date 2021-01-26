print("Welcome to the Grade Sorter App")
grades=[]
for n in range(1,5):
      grades.append(int(input(f"Enter your {n}. score: ")))
print("Your grades "+f"{grades}")

grades.sort(reverse=True)
print("Your sorted grades "+f"{grades}")
print("Lowest two scores will be deleted")
removed_first_grade=grades.pop()
print(f"Removed grade {removed_first_grade}")
removed_second_grade=grades.pop()
print(f"Removed grade {removed_second_grade}")
print("Remaining grades"+f"{grades}")
print(f"Your highest score is {grades[0]}")
