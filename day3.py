import re

running = 0

skip = False


def multiply(mul_str):
    comma_idx = mul_str.index(",")
    first_num = int(mul_str[4:comma_idx])
    second_num = int(mul_str[comma_idx + 1 : len(mul_str) - 1])
    return first_num * second_num


with open("./day3.txt") as file:
    file_str = file.read()
    matches = re.findall(r"(?:mul\(\s*\d+\s*,\s*\d+\s*\)|do\(\)|don't\(\))", file_str)
    for match in matches:
        if match == "do()":
            skip = False
        elif match == "don't()":
            skip = True
        elif not skip:
            running += multiply(match)

print(running)
