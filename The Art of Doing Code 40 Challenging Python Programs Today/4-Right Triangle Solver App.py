import math
print("Welcome to the Right Triangle Solver App")
leg_one=float(input("First leg of right triangle: "))
leg_two=float(input("Second leg of right triangle: "))
#leg_three=math.sqrt(leg_one**2 + leg_two**2)
leg_three=(leg_one**2 + leg_two**2)**(0.5)
right_triangle_area=leg_one*leg_two*0.5
print(f"For a triangle with legs of {leg_one} and {leg_two} the hypotenus is {round(leg_three,3)}")
print(f"For a triangle with legs of {leg_one} and {leg_two} the area is {round(right_triangle_area,3)}")
