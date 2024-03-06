def update_stock(books, title, new_stock):
  if title in books:
    books[title] = new_stock
    print(f"Stock of '{title}' updated to {new_stock}.")
  else:
    print(f"Book '{title}' not found in the store.")

def add_book(books, title, stock):
  if title not in books:
    books[title] = stock
    print(f"Book '{title}' added to the store with {stock} stock.")
  else:
    print(f"Book '{title}' already exists in the store.")

def delete_book(books, title):
  if title in books:
    del books[title]
    print(f"Book '{title}' deleted from the store.")
  else:
    print(f"Book '{title}' not found in the store.")

def print_books(books):
  if not books:
    print("There are currently no books in the store.")
  else:
    print("\nCurrent book inventory:")
    for title, stock in books.items():
      print(f"- {title} ({stock} in stock)")

def main():
  books = {} 

  while True:
    print("\nBook Store Inventory Management")
    print("1. Update stock")
    print("2. Add book")
    print("3. Delete book")
    print("4. Print inventory")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
      title = input("Enter the title of the book: ")
      new_stock = int(input("Enter the new stock level: "))
      update_stock(books, title, new_stock)
    elif choice == '2':
      title = input("Enter the title of the book: ")
      stock = int(input("Enter the initial stock level: "))
      add_book(books, title, stock)
    elif choice == '3':
      title = input("Enter the title of the book to delete: ")
      delete_book(books, title)
    elif choice == '4':
      print_books(books)
    elif choice == '5':
      print("Exiting the program.")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
