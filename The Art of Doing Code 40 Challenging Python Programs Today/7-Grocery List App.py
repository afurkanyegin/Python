import datetime
print("Welcome to the Grocery List App")

print(f"Current Day and Time: {datetime.datetime.now().month}/{datetime.datetime.now().day}  {datetime.datetime.now().hour}:{datetime.datetime.now().minute}")

grocery_list=["Meat","Cheese"]

print(f"You are currently have {grocery_list[0]} and {grocery_list[1]} in the list. ")

grocery_list.append(str(input("the food that will be added to the grocery list: ")).title())
grocery_list.append(str(input("the food that will be added to the grocery list: ")).title())
grocery_list.append(str(input("the food that will be added to the grocery list: ")).title())

print("Grocery List:")
print(grocery_list)

grocery_list.sort()

print(f"Sorted grocery list:\n{grocery_list}")



for n in range(1,4):
      print(f"Grocery List has: {len(grocery_list)} items")
      latest_bought_item=str(input("Latest bought item: ")).title()
      print(f"Removing {latest_bought_item.title()} from the list\n")

      grocery_list.remove(latest_bought_item)

      print(grocery_list)

grocery_list[0]=str(input(f"The {grocery_list[0]} in the list doesn't available at the moment. What would you want to buy instead:  ")).title()

print(grocery_list)


