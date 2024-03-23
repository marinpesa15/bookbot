def main():
    # open the file and read it
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    # count occurences of all characters in the file and sort it from most occurences to least
    counter = {}
    word = "".join(file_contents)
    for i in word.lower():
            counter[i] = counter.get(i, 0) + 1

    sorted_counter = sorted(counter.items(), key=lambda x:x[1], reverse=True)
    converted_dict = dict(sorted_counter)
    
    # count occurences of only letters in the file
    letter_counts = {}
    for char, count in converted_dict.items():
         if char.isalpha():
              letter_counts[char] = file_contents.count(char)

    # Print the Report
              
    print("--- Begin report of books/frankenstein.txt ---")

    # print number of words in the file
    total_words = len(file_contents.split())
    print(f"{total_words} words found in the document\n")

    # print letter counts
    for char, count in letter_counts.items():
         print(f"The '{char}' character was found {count} times")
    
    # Print End of report
    print("--- End of Report ---")


main()
