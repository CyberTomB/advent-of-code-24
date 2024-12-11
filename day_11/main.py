sample = [0, 1, 10, 99, 999]
data = [4, 4841539, 66, 5279, 49207, 134, 609568, 0]

max_blinks = 25

def replace_0_with_1(num):
    if(num == 0):
        return 1
    else:
        return num
    
def split_evens(num):
    conversion = str(num)
    length_of_digits = len(conversion)
    if(not length_of_digits % 2 == 0):
        return num
    else:
        half = length_of_digits / 2
        return int(conversion[:half]), int(conversion[half:])


def main():
    print(split_evens(2024))

if __name__ == "__main__":
    main()