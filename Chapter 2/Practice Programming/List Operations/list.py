

from styling import styles


print("")
print(styles())
print("")

# Creating A List
fruits=["Mango","Apple","Banana"]
print("List of Some Fruits =",fruits)

# Accessing List Items
print("Second fruit in the list =",fruits[1])

# Modifying A List
fruits[1]="Grapes"
print("List After Replacing Apple with Grapes =",fruits)

# Adding "Pomegranates" at the End of List
fruits.append("Pomegranate")
print("List After adding Pomegranate at the End =",fruits)

print("Length of the list =",(len(fruits)))

print("")
print(styles())
print("")