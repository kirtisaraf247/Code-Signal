def solution(a):
    a.reverse()                                   
    for i in range(len(a)):                       # This line reverses the order of rows in the input matrix 'a'.
        for j in range(i):                        # The inner loop iterates through the columns using the variable 'j'.
            a[i][j], a[j][i] = a[j][i],a[i][j]    # This line swaps the values of (i, j) and (j, i), effectively transposing them.
    return a                                      # Finally, after the loops have completed, the function returns the modified matrix 'a'.
