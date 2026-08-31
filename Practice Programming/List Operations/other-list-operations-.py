
# Other list operations include:
# 1. append(item)
# 2. remove(item)
# 3. sort()
# 4. reverse()

box_items=["books","novels","stories","dialogues"]

# 1. Add "stationary" at the end.
box_items.append("stationary")
print("Added stationary and the end =",box_items)


# 2. Remove "dialogues" from the list.
box_items.remove("dialogues")
print("Removed dialogues from the list =", box_items)

# 3. Sort the list.
box_items.sort()
print("Sorted list =",box_items)

# 4. Reverese the sorted list.
box_items.reverse()
print("Unsorted list =",box_items)