import numpy as np
from re import findall

SAMPLE_DATA = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

def vertical_transpose(rows):
    verticals = {}
    for i in range(0, len(rows)):
        for c in range(0, len(rows[i])):
            char = rows[i][c]
            try: 
                verticals[c] += char
            except:
                verticals[c] = char
    return list(verticals.values())

def diagonal_transpose(rows):
    matrix, maximum = convert_to_matrix(rows)
    diagonals = []


    for i in range(0, (maximum - 3)):
        top_row_diag = ''.join(np.diagonal(matrix, i))
        print(f"First row diagonal from position {i}: {top_row_diag}")
        diagonals.append(top_row_diag)

        sub_diag = ''.join(np.diagonal(matrix, -(i+1)))
        print(f"Subdiagonal from positon {i}: {sub_diag}")
        diagonals.append(sub_diag)

        anti_diag = ''.join(np.fliplr(matrix).diagonal(offset=i)) 
        print(f"Horizontal anti-diagonal from position {i}: {anti_diag}")
        diagonals.append(anti_diag)

        anti_sub_diag = ''.join(np.fliplr(matrix).diagonal(offset=-(i+1)))
        print(f"Vertial anti-sub-diagonal from position {i}: {anti_sub_diag}")
        diagonals.append(anti_sub_diag)

    return diagonals
        
def find_xmas(string) -> int:
   print(f">>>Trying to find XMAS in {string}")
   xmases = findall(r'(XMAS)', string)
   samxes = findall(r'(SAMX)', string)
   print(f">> FOUND {xmases} and {samxes}")
   return len(xmases) + len(samxes)

def convert_to_matrix(rows):
    matrix = []
    row_length = 0
    for row in rows:
        row_arr = []
        for char in row:
            if(not char == '\n'):
                row_arr.append(char)
        matrix.append(row_arr)
        row_length = len(row_arr)
    maximum = max(row_length, len(matrix))
    return matrix, maximum

def rolling_window(rows):
    matrix, maximum = convert_to_matrix(rows)

def find_crossmas(matrix):
    # Expect a matrix of 3x3 such as:
    # [M, A, S]
    # [X, A, S]
    # [M, S, S]
    # Output a 1 because MAS x MAS in the center
    top_left_bottom_right = ''.join(np.diagonal(matrix, 0))
    top_right_bottom_left = ''.join(np.fliplr(matrix).diagonal(offset=0))
    result = ((top_left_bottom_right == 'SAM' or top_left_bottom_right == 'MAS') and 
    (top_right_bottom_left == 'SAM' or top_right_bottom_left == 'MAS'))
    return int(result)

def part_one(input):
    lines = input
    verticals = vertical_transpose(input)
    diagonals = diagonal_transpose(input)

    vertical_total = 0
    for v in verticals:
        vertical_total += find_xmas(v)

    print(f">>> FOUND XMAS {vertical_total} times in vertical columns")

    lines_total = 0
    for l in lines:
        lines_total += find_xmas(l)
    
    print(f">>> FOUND XMAS {lines_total} times in horizontal rows")

    diags_total = 0
    for d in diagonals:
        diags_total += find_xmas(d)
    
    print(f">>> FOUND XMAS {diags_total} times in diagonal rows")

    print(f">>> GRAND TOTAL: {lines_total + diags_total + vertical_total}")


def main():
    with open('data.txt') as f:
        data = f.readlines()

    with open('sample.txt') as s:
        sample = s.readlines()

    input = data

    matrix, maximum = convert_to_matrix(input)

    window = np.lib.stride_tricks.sliding_window_view(matrix, (3, 3))
    count = 0
    for iteration in window:
        for submatrix in iteration:
            count += find_crossmas(submatrix)

    print(f"Found {count} total crossmasses")
            
    



if __name__ == "__main__":
    main()