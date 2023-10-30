def solution(a):
    b = [0] * 100001      # Initializes a list 'b' with 100001 elements, all of which are initialized to 0.
    for i in a:           # The code then iterates through each element 'i' in the input list 'a' using a 'for' loop.
        if b[i] == 1:     # Checks whether the element 'i' has already been encountered in the input list. If b[i] is equal to 1, it means that 'i' has been encountered before, and the code immediately returns 'i' as the first duplicate element found.
            return i      # The code immediately returns 'i' as the first duplicate element found.
        else:
            b[i] = 1      # The code sets b[i] = 1 to mark that num has been encountered.
    return -1             # If the loop completes without finding a duplicate element, the function returns -1, indicating that there are no duplicate elements in the input list.
