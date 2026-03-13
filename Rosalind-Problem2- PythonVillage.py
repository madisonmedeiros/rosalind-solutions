# Rosalind Problem 2 - Python Village

with open("data/rosalind_ini3.txt", "r") as file:
    string = file.readline().strip()
    nums = file.readline().strip()
    a,b,c,d= map(int,nums.split())
    print(f"string: {string}")
    print(f"a:{a} b:{b} c:{c} d:{d}")
    print(f"{string[a:b+1]} {string[c:d+1]}")
