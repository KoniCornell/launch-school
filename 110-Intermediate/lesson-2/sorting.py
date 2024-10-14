# problem 1
'''
Sort the following list of numbers first in ascending numeric order, 
then in descending numeric order. 
Do not mutate the list.
'''

lst = [10, 9, -6, 11, 7, -16, 50, 8]

print(sorted(lst))                  # Ascending Sort
print(sorted(lst, reverse=True))    # Descending Sort

# Problem 2
'''
Perform the sort by mutating the list
'''
lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)

# problem 3
'''
Sort the list of dictionaries based on the year of
publication for each book
'''
books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]

def get_published_year(book):
    return int(book['published'])

# sorted_books = sorted(books, key=get_published_year)
sorted_books = sorted(books, key=lambda book: int(book['published']))
print(sorted_books) 
