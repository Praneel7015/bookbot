path = "/Users/ojasvipoonia/Documents/bookbot/books/frankenstein.txt"
def get_book_test(pa):
    with open(pa,'r') as f:
        file_contents = f.read()
    return file_contents
m= get_book_test(path)
def get_book_words(u):
        j = u.split()
        print(f"{len(j)} words were found in the document")
 
def num_of_char_each(u):
    d = {}
    m = u.lower()
    for char in m:
        if 'a' <= char <= 'z':
            if char in d:
                d[char] +=1
            else :
                d[char] =1
    m = sorted(d.items(), key = lambda item: item[1],reverse=True)
    return m

def report():
    print(f"============ BOOKBOT ============\nAnalyzing book found at {path}\n----------- Word Count ----------\nFound {get_book_words(m)} total words\n--------- Character Count -------")
    for i in num_of_char_each(m):
        print(i)
