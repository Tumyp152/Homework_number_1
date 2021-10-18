def solution(A):
    sum = 0
    for i in range(2, A + 1):
        if((i % 3 == 0) or (i % 5 == 0)):
            sum += i
    return sum