word_s = []
with open("./day4.txt") as file:
    for line in file:
        word_s.append(list(file.readline().strip()))


rows = len(word_s)
cols = len(word_s[0])

total_hits = 0
dirs = [(1, 0), (1, -1), (1, 1), (0, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]


def check_pos(row, col):
    hits = 0
    for dr, dc in dirs:
        if 0 <= (row + (dr * 3)) < rows and 0 <= (col + (dc * 3)) < cols:
            if (
                word_s[row + dr][col + dc] == "M"
                and word_s[row + (dr * 2)][col + (dc * 2)] == "A"
                and word_s[row + (dr * 3)][col + (dc * 3)] == "S"
            ):
                hits += 1
    return hits


for i in range(len(word_s)):
    for j in range(len(word_s[i])):
        if word_s[i][j] == "X":
            total_hits += check_pos(i, j)

print(total_hits)
