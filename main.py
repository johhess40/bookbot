def main():
    book_path = input("Enter the path to the book: ")
    book_text = read_book_text(book_path)
    print(f"--- Book stats for {book_path}  ---")
    print("Word count: ", word_count(book_text))
    book_dictionary = create_word_count_dict(book_text)
    for key, value in book_dictionary.items():
        print(f"{key} was found {value} times in the book.")
    print("--- End of book stats ---")
        
def read_book_text(path):
    with open(path) as f:
        return f.read()
        
def read_book_text_as_lines(path):
    with open(path) as f:
        return f.readlines()

def word_count(text):
    return len(text.split())

def create_word_count_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        stripped = lowered.strip()
        if stripped in chars and stripped.isalnum() and stripped.isdigit() == False:
            chars[stripped] += 1
        elif stripped.isalnum() and stripped.isdigit() == False:
            chars[stripped] = 1
    return chars


    
if __name__ == "__main__":
    main()