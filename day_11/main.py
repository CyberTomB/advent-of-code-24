sample = [0, 1, 10, 99, 999]
other_example = [125, 17]
data = [4, 4841539, 66, 5279, 49207, 134, 609568, 0]

max_blinks = 25

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
        
# def flatten(arr):
#     new_arr = []
#     for elem in arr:
#         if(not type(elem) == int):
#             new_arr.append(elem[0])
#             new_arr.append(elem[1])
#         else:
#             new_arr.append(elem)
#     return new_arr

def blink(input, blink_count = 1):
    output = input
    for i in range(0, blink_count):
        output = apply_rules(output)
    return output
    



def main():
    input = data
    blink_count = 26
    print(f">>> Iterating {blink_count} times over {input}")
    output = blink(input, blink_count)
    print(f">>> Final output has {len(output)} stones")

if __name__ == "__main__":
    main()