import csv

def dashboard():
    """Prints
    40 '='
      📚  YOUR LIBRARY
    40 '='
    """
    print('=' * 40)
    print('  📚  YOUR LIBRARY')
    print('=' * 40)


def estimate_reading_time(pages):
    """Return estimated reading time in hours, assuming 40 pages pr hour"""
    reading_time = round(pages / 40, 1)
    return reading_time


def add_book(library):
    """
    Get the book details from user, save it to the csv
    """
    title = input('Book title: ').title()
    author = input('Author: ')
    pages = int(input('Page count: '))
    hours = estimate_reading_time(pages)
    book = {'title': title, 'author': author, 'pages': pages, 'hours': hours}
    library.append(book)

    with open('books.csv', 'a') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'author', 'pages', 'hours'])
        writer.writerow(book)

    print('\nBook added:\n')
    print(f"  '{book['title']}' by {book['author']} -- approx. {book['hours']} hours to read")
    return library


def load_books():
    """
    Read every book saved in books.csv and return them as a list of dictionaries
    """
    library = []
    with open('books.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            book = {
                'title': row['title'],
                'author': row['author'],
                'pages': int(row['pages']),
                'hours': float(row['hours']),
            }
            library.append(book)
    return library


def format_book(book, number):
    """
    Return one book as a numbered line of text
    """
    return (f"{number}. '{book['title']}' - {book['author']} "
            f"({book['pages']} pages - approx. {book['hours']} hours to read)")


def view_books(library):
    """Print every book in library with a number in front"""
    if not library:
        print("Your library is empty. Add a book first!")
    else:
        for i in range(len(library)):
            print(format_book(library[i], i + 1))


def show_menu():
    print('''
  What would you like to do?

  1) View books
  2) Add a book

  q) Quit
''')
    user_input = input('> ').strip().lower()
    return user_input


def main():
    library = load_books()
    dashboard()
    while True:
        user_input = show_menu()
        if user_input == '1':
            view_books(library)
        elif user_input == '2':
            library = add_book(library)
        elif user_input in ('q', 'quit', 'exit'):
            print('Goodbye!')
            break
        else:
            print("Sorry, that option isn't available.")

if __name__ == "__main__":
    main()