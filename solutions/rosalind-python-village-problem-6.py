#rosalind-python-village-problem-6

'''
Given: 
A string s of length at most 10000 letters.

Return: 
The number of occurrences of each word in s where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.
'''

word_counts = {}

with open("data/rosalind_ini6.txt", "r") as file:
    for line in file:
        parts = line.strip().split(" ")
        for word in parts:
            if word not in word_counts:
                word_counts[word] = 1
            else:
                word_counts[word] += 1
    
    for key, value in word_counts.items():
        print(f"{key} {value}")