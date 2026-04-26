Chores = ["Clean", "Wipe", "Remove.Trash"]
Chores.append("Wipe.Windows")
print(Chores)

Chores.insert(2, "Swipe.Floor")
print(Chores)

Chores.remove("Remove.Trash")
Chores.insert(2, "Wipe.Table")
print (Chores)

Chores.remove("Clean")
Chores.insert(0,"Deepclean")
print(Chores)

Chores.clear()
print(Chores)
