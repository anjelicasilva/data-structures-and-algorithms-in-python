
# Implement a method to perform basic string compression using the counts of repeted characters.
# If the "compressed" string would not become smaller than the original string, 
# your method should return the original string.

# input: 'aabcccccaaa'
# output: 'a2b1c5a3'
# input: 'lmaooo'
#     -> 'l1m1a1o3'
# output: 'lmaooo'

def string_compression(string):
    #keep track with a letter_counter
    #new_string variable 
    #for loop and iterate through String
    #if char changes, restart my letter letter_counter

    #calculate length of the original and new string
    #return shortest length string

    current_letter = string[0]
    letter_counter = 0
    new_string_lst = []

    for idx, letter in enumerate(string):
        if letter == current_letter:
            letter_counter += 1

        else:
            new_string_lst.append(current_letter)
            new_string_lst.append(str(letter_counter))
            current_letter = string[idx]
            letter_counter = 1

        # if idx == len(string)-1:
        #     new_string_lst.append(current_letter)
        #     new_string_lst.append(str(letter_counter))

    new_string_lst.append(current_letter)
    new_string_lst.append(str(letter_counter))

    new_string = ''.join(new_string_lst)
    
    original_string_len = len(string)
    new_string_len = len(new_string_lst)

    if new_string_len >= original_string_len:
        return string
    return new_string


print(string_compression('aabcccccaaa'))
print(string_compression('lmaooo'))
print(string_compression('yoooooooab'))