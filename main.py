from stats import get_char_word_type
from stats import get_num_words
from stats import sort_char_num
import sys

def get_book_text (file):
	file_cont = file.read()
	return file_cont

def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
		return

	with open(sys.argv[1]) as f:
		text = get_book_text(f)
	char_count_type = get_char_word_type(text)
	word_count = get_num_words(text)
	print(f"Found {word_count} total words")
	sorted_char_list = sort_char_num(char_count_type)
	for char in sorted_char_list:
		if char.isalpha():
			print(f"{char}: {sorted_char_list[char]}")

main()
