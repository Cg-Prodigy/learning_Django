import re
with open('bestseller.txt', 'r') as file:
    book_data = [i.strip('\n').split('\t') for i in file.readlines()]

# constants
ALL_YEARS = [int(i[3].split('/')[-1]) for i in book_data]
ALL_MONTHS = [int(i[3].split('/')[0]) for i in book_data]
#  fucntions to process each of the promts


def by_range(s_year, e_year):
    s_year = int(s_year)
    e_year = int(e_year)
    result = []
    upper = max(ALL_YEARS)
    lower = min(ALL_YEARS)
    if (s_year < lower or s_year > upper) or (e_year > upper or e_year < lower):
        print(
            f'Invalid year passed. Range should stay between {lower} and {upper}')
        return False
    for i in book_data:
        index_year = int(i[3].split('/')[-1])
        if index_year >= s_year and index_year <= e_year:
            result.append(i)
    print()
    print(f'All Titles between {s_year} and {e_year}')
    for i in result:
        print(f'\t{i[0]}, by {i[2]} {i[3]}')

    return True


def by_month_year(m, y):
    m = int(m)
    y = int(y)
    u_m = max(ALL_MONTHS)
    l_m = min(ALL_MONTHS)
    u_y = max(ALL_YEARS)
    l_y = min(ALL_YEARS)
    result = []
    if (m < l_m or m > u_m):
        print(f'Invalid year passed. Range should stay between {1} and {12}')
        return False
    if (y < l_y or y > u_y):
        print(
            f'Invalid year passed. Range should stay between {l_y} and {u_y}')
        return False
    for i in book_data:
        i_month = int(i[3].split('/')[0])
        i_year = int(i[3].split('/')[-1])
        if m == i_month and y == i_year:
            result.append(i)
    print(f'All titles in the month {m} of {y}')
    print_results(result)

def by_author(u_str):
    regex = re.compile(u_str, re.IGNORECASE)
    result = []
    for i in book_data:
        author=i[1]
        if regex.search(author):
            result.append(i)
    if not result:
        print(f'{u_str} Not found. Use another string or substring')
    else:
        print_results(result)


def by_title(u_title):
    regex = re.compile(u_title, re.IGNORECASE)
    result = []
    for i in book_data:
        title = i[0]
        if regex.search(title):
            result.append(i)
    if not result:
        print(f'{u_title} Not found. Use another string or substring')
    else:
        print_results(result)


def print_results(lst):
    for i in lst:
        print(f'\t{i[0]}, by {i[1]} {i[3]}')

#  process user inputdef process_input(u_input):


def process_input(u_input):
    if u_input == '1':
        s_year = input('Enter beginning year: ')
        e_year = input('Enter for year: ')
        by_range(s_year, e_year)
    elif u_input == '2':
        u_month = input('Enter month (as a number, 1-12): ')
        u_year = input('Enter year: ')
        by_month_year(u_month, u_year)
    elif u_input == '3':
        author_name = input("Enter an author's name (or part of name): ")
        by_author(author_name)
    elif u_input == '4':
        title = input('Enter title (or part of a title): ')
        by_title(title)
    else:
        print('Invalid input.')
# recieve user input
while True:
    u_input = input('\
What would you like to do?\n\
1. Look up year range\n\
2. Look up month/year\n\
3. Search by author\n\
4. Search by title\n\
Q. Quit\n\
>')
    if u_input == 'Q' or u_input == 'q':
        break
    process_input(u_input)
