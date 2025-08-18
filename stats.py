
def get_book_test(pa):
    with open(pa,'r') as f:
        file_contents = f.read()
    return file_contents

def get_book_words(u):
        j = u.split()
        print(f"{len(j)} words were found in the document")
 
def num_of_char_each(u):
    d = {}
    m = u.lower()
    for char in m:
        if char.isalpha():
            if char in d:
                d[char] +=1
            else :
                d[char] =1
    m = sorted(d.items(), key = lambda item: item[1],reverse=True)
    return m

def report(path):
    print(f"============ BOOKBOT ============\nAnalyzing book found at {path}\n----------- Word Count ----------\nFound {get_book_words(path)} total words\n--------- Character Count -------")
    for i in num_of_char_each(get_book_test(path)):
        print(i)
    print("============= END ===============")
