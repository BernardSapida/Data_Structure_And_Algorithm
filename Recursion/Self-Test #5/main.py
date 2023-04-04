A = ['a', 'b', 'c']

def traverse_characters(characters, i = 0):
    # base case
    if i == len(characters):
        return
    
    # pair current char to all characters and print
    print_character_pairs(characters, i)

    # traverse to next character
    traverse_characters(characters, i+1)

def print_character_pairs(characters, charIndex, i = 0):
    # base case
    if i == len(characters):
        return
    
    if charIndex == i:
        # Go to next character
        print_character_pairs(characters, charIndex, i+1)
    else:
        # print current character and its pair
        print(characters[charIndex] + characters[i])

        # Go to next character
        print_character_pairs(characters, charIndex, i+1)

traverse_characters(A)