from stats import count_words, count_characters, sort_letters
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    content = get_book_text(filepath)
    total_words = count_words(content)
    sorted_lettercount = sort_letters(count_characters(content))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print(f"----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print(f"--------- Character Count -------")

    for letter in sorted_lettercount:
        print(f"{letter["char"]}: {letter["num"]}")

    print(f"============= END ===============")


main()