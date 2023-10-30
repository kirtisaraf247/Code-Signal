def solution(inputString):
    rev = reversed(inputString)
    if list(rev) == list(inputString):
        return True
    return False
