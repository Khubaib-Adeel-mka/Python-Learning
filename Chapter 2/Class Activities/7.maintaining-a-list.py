
# Class Activity
# Imagine you are maintaining a list of your favourite books: ["To Kill a Mockingbird","1984","The Great Gatsby","Pride and Prejudice"].


books=["To Kill a Mockingbird","1984","The Great Gatsby","Pride and Prejudice"]

# Perform the following tasks using Python:
# Add a new book "Moby Dick" to the list
books.append("Moby Dick")

# Replace "1984" with "Brave New World"
books[1] = "Brave New World"

# Remove "The Great Gatsby" from the list
books.remove("The Great Gatsby")

# Merge this list with another list of books: ["War and Peace", "Hamlet"]
other_books=["War and Peace", "Hamlet"]
all_books=books + other_books

# Print the final list of books
print(all_books)