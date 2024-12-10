import numpy as np

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

SAMPLE_AS_LIST = SAMPLE_DATA.split("\n")

def split_text(lines):
    counter = 0
    diagonals = {}
    print(diagonal_transpose(lines))

def vertical_transpose(rows):
    verticals = {}
    for i in range(0, len(rows)):
        for c in range(0, len(rows[i])):
            char = rows[i][c]
            try: 
                verticals[c] += char
            except:
                verticals[c] = char
    return verticals

def diagonal_transpose(rows):
    matrix = []
    for row in rows:
        row_arr = []
        for char in row:
            row_arr.append(char)
        matrix.append(row_arr)

    for i in range(0, 7):
        print(f"First row diagonal from position {i}: {''.join(np.diagonal(matrix, i))}")
        print(f"Subdiagonal from positon {i}: {''.join(np.diagonal(matrix, -i))}")
        print(f"Horizontal anti-diagonal from position {i}: {''.join(np.fliplr(matrix).diagonal(offset=-i))}")
        print(f"Vertial anti-diagonal from position {i}: {''.join(np.flipud(matrix).diagonal(offset=i))}")
        



def find_xmas(iterable) -> int:
        counter = 0
        current_match = ""  
        # iterate over every character
        for c in iterable:
            if(c == 'S' and current_match == 'XMA'):
                counter += 1
                current_match = ""
                print(f">> Found XMAS! Current count: {counter}")
            elif(c == 'A' and current_match == 'XM'):
                current_match = "XMA"
            elif(c == 'M' and current_match == 'X'):
                current_match = "XM"
            elif(c == 'X' and current_match == ''):
                current_match = 'X'
            print(f">> Char {c} found {current_match} so far")
        return counter
        


def main():
    with open('data.txt') as f:
        input = f.readlines()

    split_text(SAMPLE_AS_LIST)

if __name__ == "__main__":
    main()