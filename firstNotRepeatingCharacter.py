def solution(s):
    # This line initializes an empty dictionary 'c'. This dictionary will be used to store the frequency of each character in the input string 's'.
    c = {}                        
    # The code then iterates through each character 'i' in the input string 's' using 'a' for loop.
    for i in s:
        # 'get' method updates the dictionary 'c'. 'c.get(i, 0)' retrieves the current count of character 'i' in the dictionary. If the character has not been encountered before,
        # it defaults to 0. The code then adds 1 to this count, effectively incrementing the count for the character 'i'.
        c[i] = c.get(i, 0) + 1
    # 'i for i in s', generator expression will produce characters from the string one by one. 
    # if 'c[i] == 1'. This condition checks whether the character 'i' has a frequency of 1 in the dictionary 'c'.
    # If the loop completes without finding a non-repeated character, the code returns '_'.
    return next((i for i in s if c[i] == 1), '_')
