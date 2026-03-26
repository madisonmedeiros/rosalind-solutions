'''
An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s

'''

# Open file

# Read in line


with open("data/rosalind_dna.txt", "r") as file:
    string = file.readline().strip()
    dic = {}
    for letter in string:
        if letter not in dic:
            dic[letter] = 1
        else:
            dic[letter] += 1
    
    print(f"{dic['A']} {dic['C']} {dic['G']} {dic['T']}")


