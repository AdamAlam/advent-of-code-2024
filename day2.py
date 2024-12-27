def validate(numbers: list[int]) -> bool:
    if len(numbers) == 1:
        return True

    increasing = numbers[1] > numbers[0]

    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i - 1]

        if (increasing and (diff <= 0 or abs(diff) > 3)) or (
            not increasing and (diff >= 0 or abs(diff) > 3)
        ):
            return False

    return True

# function for part 2
def validate_with_removal(numbers: list[int]) -> bool:
    for i in range(len(numbers)):
        if validate(numbers[:i] + numbers[i+1:]):
            return True
    return False
                        

def count_valid_lines(file_path: str) -> int:
    valid_count = 0

    with open(file_path) as file:
        for line in file:
            nums = [int(num) for num in line.strip().split()]
            if validate(nums) or validate_with_removal(nums):
                valid_count += 1
    return valid_count


if __name__ == "__main__":
    file_path = "day2.txt"
    result = count_valid_lines(file_path)
    print(result)
