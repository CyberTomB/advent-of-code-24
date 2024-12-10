from re import findall
EXAMPLE_DATA = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
MORE_EXAMPLE_DATA = "mul(4*|mul(6,9!?(12,34)mul ( 2, 4 )"
EXAMPLE_SOLUTION = 161

REGEX_MUL_EXPRESSION = r"(mul\(\d{1,3},\d{1,3}\))"
REGEX_MUL_EXPRESSION_WITH_LOGIC = r"(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))"

def find_real_muls(corrupted_string: str) -> list:
    return findall(REGEX_MUL_EXPRESSION, corrupted_string)

def find_muls_with_logic(corrupted_string: str) -> list:
    return findall(REGEX_MUL_EXPRESSION_WITH_LOGIC, corrupted_string)

def process_mul(mul: str) -> int:
    values = findall(r"\d{1,3}", mul)
    return int(values[0]) * int(values[1])

def process_all_muls_with_logic(muls):
    on = True
    sum = 0
    for (mul, do, donot) in muls:
        print(f">>>Mul processing is {'ON' if on else 'OFF'}: {f'the mul {mul} will be added' if (on and mul) else {f'the mul {mul} will not be added'} if ((not on) and mul) else ''}")
        if(not mul == '' and on):
            sum += process_mul(mul)
        elif(not do == ''):
            print(f">>Turning ON")
            on = True
        elif(not donot == ''):
            print(f">>Turning OFF")
            on = False
    return sum
        


def main():
    print("Running Day 3...")

    with open("data.txt") as f:
        corrupted_data = "".join(f.readlines())
    muls = find_muls_with_logic(corrupted_data)
    # sum = 0
    sum = process_all_muls_with_logic(muls)
    # for m in muls:
    #     print(f">>> Processing {m}")
    print("Final Result: ", sum)


if __name__ == "__main__":
    main()