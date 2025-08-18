import sys
from stats import get_book_words, get_book_test,num_of_char_each,report
if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    sys.exit(1)
    
s= get_book_test(path)
yo = num_of_char_each(s)
print(yo)
report(path)