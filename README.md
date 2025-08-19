
# BookBot

BookBot is a simple Python tool for analyzing text files (such as books). It provides word and character frequency statistics to help you understand the contents of your text documents.

## Features
- Counts total words in a text file
- Counts frequency of each character (case-insensitive)
- Prints a detailed report with sorted character frequencies

## Installation
1. Clone this repository:
	```sh
	git clone https://github.com/Ojasvi-Poonia/bookbot.git
	```
2. Navigate to the project directory:
	```sh
	cd bookbot
	```

## Usage
Run the following command, replacing `<path-to-your-book-or-text-file>` with the path to your text file:

```sh
python main.py <path-to-your-book-or-text-file>
```

## Example Output
```
============ BOOKBOT ============
Analyzing book found at <your-file-path>
----------- Word Count ----------
Found 12345 total words
--------- Character Count -------
('e', 2345)
('t', 2100)
('a', 1900)
...
============= END ===============
```

## File Structure
- `main.py` - Entry point; handles command-line arguments and prints the report
- `stats.py` - Functions for reading files, counting words, and character frequencies
- `README.md` - Project documentation

## Contributing

## License
