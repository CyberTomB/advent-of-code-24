sample = [0, 1, 10, 99, 999]
other_example = [125, 17]
data = [4, 4841539, 66, 5279, 49207, 134, 609568, 0]

from collections import defaultdict

max_blinks = 25


def process_input(arr):
    stone_dict = defaultdict(int)
    for stone in arr:
        stone_dict[stone] = 1
    return stone_dict

global stones
stones = process_input(data)


def replace_0_with_1(num):
    if(num == 0):
        return 1
    else:
        raise Exception(f"{num} is not 0")
    
def split_evens(num):
    conversion = str(num)
    length_of_digits = len(conversion)
    if(not length_of_digits % 2 == 0):
        raise Exception(f"{num} does not have an even number of digits")
    else:
        half = int(length_of_digits / 2)
        return int(conversion[:half]), int(conversion[half:])

def apply_rules(arr):
    new_arr = []
    hashmap = {}
    for elem in arr:
        try:
            new_arr.append(replace_0_with_1(elem))
        except:
            try:
                x, y = split_evens(elem)
                new_arr.append(x)
                new_arr.append(y)
            except:
                new_arr.append(elem * 2024)
    return new_arr

def blink_times(blink_count = 1):
    for i in range(0, blink_count):
        print(f">>> Step {i}")
        blink()

def blink():
    copy = dict(stones)
    for stone, count in copy.items():
        if count == 0:
            continue
        if stone == 0:
            stones[0] -= count
            stones[1] += count
        else:
            try:
                x, y = split_evens(stone)
                stones[x] += count
                stones[y] += count
                stones[stone] -= count
            except:
                stones[stone] -= count
                stones[stone * 2024] += count
    
    
# Probably best to develop an algorithm that will determine the number of stones Y based on the input X and N iterations
# The hard part is leading 0s. If a number like 306045 is split in half, the result will be 306 and 45, which will affect resulting iterations
# Maybe it can still be brute forced for single numbers, just to count the splits -- initial 0 and 1 will be predictable

# We know that an initial 0 will become 2, 0, 2, 4 when n = 3
# If this becomes mapped and iterates 3 more times, we know what the 0 will become, so we don't have to keep iterating on it
# We also know what the 2 will become, and can stop iterating

# What if we traverse the array, and if we hit a single digit, we discard that element and then save it with the # of remaining iterations?

# Ultimately, I had to concede that I lacked the necessary know-how to make this work. Thanks to the redditor who applied an excellent solution. I basically just stole it.
# I learned that if you need to iterate over a list, it's better to just create a map of things as you find them and add to their counts.
# The difference went from O(n^2) to O(n) as I understand it.

def main():
    # stones = process_input([0])
    print(f"Initial stones: {stones}")
    blink_count = 75
    blink_times(blink_count)
    print(f">>> Total stones is {sum(stones.values())}")

if __name__ == "__main__":
    main()