from stats import get_num_words, get_char_count, get_chars_sorted_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
     

def main():
    #filepath = 'books/frankenstein.txt'

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 

    filepath =  sys.argv[1]

    try:

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        book_contents = get_book_text(filepath)
        #print(book_contents)

        num_words = get_num_words(book_contents)
        print(f'Found {num_words} total words')
        print("--------- Character Count -------")
        char_counts = get_char_count(book_contents)
        sorted_char_list = get_chars_sorted_list(char_counts)
        
        for item in sorted_char_list:
            if (item['char']).isalpha():
                print(f"{item['char']}: {item['num']}")
        
        print("============= END ===============")
        
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        print("Please make sure the file exists in the correct directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()