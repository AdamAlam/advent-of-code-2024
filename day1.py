l1 = []
l2 = []
with open("day1.txt") as file:
    for line in file:
        left, right = line.split("   ")
        l1.append(int(left))
        l2.append(int(right))
l1.sort()
l2.sort()
# part 1
cur_sum = 0
for i in range(len(l1)):
    cur_sum += abs(l1[i] - l2[i])
print("Part 1", cur_sum)

# part 2
count = {}
for val in l2:
    count[val] = 1 + count.get(val, 0)

cur_sim = 0
for val in l1:
    if val in count:
        cur_sim += val * count.get(val)
print("Part 2", cur_sim)
