def dashboard():
    """Prints  
    40 '='
      📚  YOUR LIBRARY
    40 '='
    """
    # your code here
    print('=' * 40)
    print('  📚  YOUR LIBRARY')
    print('=' * 40)

def estimate_reading_time(pages):
    """Return estimated reading time in hours, assuming 40 pages/hour. 
    This number should be rounded to 1 decimal place"""
    reading_time = round(pages / 40, 1)
    return reading_time

def add_book(library):
    """
    This function takes in user input for title, author, and page count.
    Create a variable called hours that calls the function estimate_reading_time
    """
    # your code here
    book = {'title' : None, 'author' : None, 'pages' : None, 'hours' : None}
    library.append(book)
    book['title'] = input('Book title: ').title()
    book['author'] = input('Author: ')
    book['pages'] = int(input('Page count: '))
    book['hours'] = estimate_reading_time(book['pages'])
    print('Book added:')
    print(f'{book['title']} by {book['author']} -- approx. {book['hours']} hours to read')
    return library

def view_books(library):
    if not library:
        print("Your library is empty. Add a book first!")
    else:
        for index in range(len(library)):
            book = library[index]
            print(f"{str(index + 1)}. '{book['title']}' - {book['author']} ({book['pages']} pages - approx. {book['hours']} to read)")

def show_menu():
    print('''
    What would you like to do?

  1) View books
  2) Add a book

  q) Quit''')
    user_input = input('> ').strip().lower()
    return user_input

def main():
    library = []
    while True:
        user_input = show_menu()
        if user_input == '1':
            view_books(library)
        elif user_input == '2':
            library = add_book(library)
        elif user_input == 'q':
            print('Goodbye!')
            break
        else:
            print("Sorry, that option isn't available.") 

if __name__ == "__main__":
    main()