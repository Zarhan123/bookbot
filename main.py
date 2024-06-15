def main():
    
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = count_words(text)
    letter_counts = count_characters(text)
    letter_list = convert_to_list(letter_counts)
    #letter_list.sort(reverse=True, key=sort_on)
    #alpha_dictionary = only_alpha(letter_counts)

    #print(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"Total Word Count: {count}")
    for letter in letter_list:
        if not letter["letter"].isalpha():
                continue
        print(f"The '{letter['letter']}' letter was found {letter['num']} times")

    print("--- End report ---")
    #print("Letter Counts:")
    #print(letter_counts)
    #print(letter_list)
    #print("List of Letters")
    #print(alpha_dictionary)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(book_text):
    #count = 0
    #words = book_text.split()
    #for word in range(0, len(words)):
    #    count += 1
    #return count
    
    #their answer
    words = book_text.split()
    return len(words)

def count_characters(text):
    letter_dict = {}
    for letter in text:
        lower_book = letter.lower()
        if lower_book in letter_dict:
            letter_dict[lower_book] += 1
        else:
            letter_dict[lower_book] = 1
        #letter_dict.sort(reverse=True)
    return letter_dict


def convert_to_list(characters):
    sorted_list = []
    for letter in characters:
        sorted_list.append({"letter": letter, "num": characters[letter]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

    #dict_list = {}
    #dict_list.append(characters)
    #for letter in characters:
    #    letter_list = letter.split()
        
    #    dict_list[letter_list[0]] = letter_list[1]
    #for i in characters:
    #    letter_list.append(i)
    #    dict_list.append(characters[i])
    #    combined[{"letter": letter_list[i], "num": characters[i]}]
    #return dict_list
    
def sort_on(dict):
    return dict["num"]
    
    
    
    
    
    
    
    
    
    #for i in characters:
        #dict_list.append([{"name": i, "num": characters[i]}])
    #dict_list.sort()
    #return dict_list    
    letter_list = []
    combined = {}
    
    #dict_list.sort(reverse=True)
    #return combined

#def sort_letter_list(list):
#    list.sort(reverse=True, key=sort_on)


main()