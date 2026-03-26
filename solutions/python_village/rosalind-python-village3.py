#rosalind-python-village3

with open("data/rosalind_ini5.txt", "r") as file:
    with open("solutions/problem-5-solution.txt", "w") as outfile:
        i = 1
        for line in file:
            if i % 2 == 0:
                outfile.write(line)
            i += 1