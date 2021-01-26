print("Welcome to the Basketball Roster App")
players=[]
for n in range (1,6):
      players.append(str(input(f"Who is player{n} : ")))
print("\n")
for n in range(len(players)):
      print(f"Player{n+1}:\t {players[n]}")

print("\n")
print(f"{players[3]} is injured.")
players.remove(players[3])
print("\n")

for n in range(len(players)):
      print(f"Player{n+1}:\t {players[n]}")
      
print(f"You have {len(players)} players left.")
players.insert(3,str(input("Add new player: ")))

for n in range(len(players)):
      print(f"Player{n+1}:\t {players[n]}")
