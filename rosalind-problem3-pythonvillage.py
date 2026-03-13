#rosalind-problem3-pythonvillage

'''
Problem
Given: Two positive integers a
 and b
 (a<b<10000
).

Return: The sum of all odd integers from a
 through b
, inclusively.
'''
with open("data/rosalind_ini4.txt", "r") as file:
    parts = file.readline().split(" ")
    a = int(parts[0])
    b = int(parts[1])

    count = 0
    for numbers in range(a, b+1):
        if numbers % 2 == 1:
            count += numbers
    
    print(count)
