from re import findall
EXAMPLE_DATA = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
MORE_EXAMPLE_DATA = "mul(4*|mul(6,9!?(12,34)mul ( 2, 4 )"
EXAMPLE_SOLUTION = 161

REGEX_MUL_EXPRESSION = r"(mul\(\d{1,3},\d{1,3}\))"

def find_real_muls(corrupted_string: str) -> list:
    return findall(REGEX_MUL_EXPRESSION, corrupted_string)

def process_mul(mul: str) -> int:
    values = findall(r"\d{1,3}", mul)
    return int(values[0]) * int(values[1])

def main():
    print("Running Day 3...")

    with open("data.txt") as f:
        corrupted_data = "".join(f.readlines())
    muls = find_real_muls(corrupted_data)
    sum = 0
    for m in muls:
        print(f">>> Processing {m}")
        sum += process_mul(m)
    print("Final Result: ", sum)


if __name__ == "__main__":
    main()