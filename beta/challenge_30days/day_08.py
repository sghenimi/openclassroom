n = int(input())
name_phones = [input().split() for _ in range(n)]
book = {k: v for k,v in name_phones}
print(book)

def is_here(name):
    if name in book:
        print(f'{name}={book.get(name)}')
    else:
        print('Not fount')

while True:
        is_here(input())