def first_word(string):
    words = string.split()
    return words[0]

input_string = input("Type a set if strings: ")
first_word = first_word(input_string)
print("First word:", first_word)



