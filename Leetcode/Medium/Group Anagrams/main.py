# https://leetcode.com/problems/group-anagrams/

def groupAnagrams(strs):
    records = {}
    
    # This code is grouping anagrams in a list of strings. It loops through each word in the input
    # list `strs`, sorts the letters in the word, and uses the sorted letters as a key in a dictionary
    # called `records`. If the sorted letters already exist as a key in the dictionary, the word is
    # appended to the list of words associated with that key. If the sorted letters do not exist as a
    # key in the dictionary, a new key is created with the sorted letters and the word is added to a
    # new list associated with that key. Finally, the function returns a list of the values in the
    # `records` dictionary, which are lists of anagrams.
    for word in strs:
        sorted_word = "".join(sorted(word))
        
        if sorted_word in records:
            records[sorted_word].append(word)
        else:
            records[sorted_word] = [word]
    
    # `return list(records.values())` is returning a list of the values in the `records` dictionary,
    # which are lists of anagrams. Each key in the `records` dictionary is a sorted string of letters
    # that represents a group of anagrams, and the corresponding value is a list of words that are
    # anagrams of each other. By calling `records.values()`, we get a list of all the values in the
    # dictionary (i.e. the lists of anagrams), and by wrapping that in `list()`, we convert the
    # dictionary view object to a list.
    return list(records.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))