SAMPLE_DATA = [
[7,6,4,2,1], # safe
[1,2,7,8,9], # unsafe
[9,7,6,2,1], # unsafe
[1,3,2,4,5], # safe after removing index 2
[8,6,4,4,1], # safe after removing index 2 or 3
[1,3,6,7,9], # safe
[1,6,4,5,6,7], # safe
[1,3,6,5,6,9], # safe after removing index 2
[59,62,61,58,57,54], # safe after removing index 0
[62,61,58,57,79], # safe after removing index 4
[2, 3, 5, 6, 8, 7, 8, 9], # safe after removing index 5
[8, 7, 6, 7, 4, 3], # safe after removing index 3
[8, 2, 5, 7, 9] #safe after removing index 0
]

SAMPLE_SOLUTION = [True, False, False, False, False, True]

def normalize_file(path = "data.txt") -> list[list[int]]:
    f = open(path)
    records = []
    for line in f:
        record = [int(x) for x in line.split(" ")]
        records.append(record)
    return records

def is_record_safe(record: list) -> tuple[bool, int]:
    initial_diff = record[0] - record[1]
    if(initial_diff == 0):
        return False, 0
    for i in range(1, len(record)):
        diff = record[i - 1] - record[i]
        try:
            next_diff = record[i] - record[i + 1]
        except:
            next_diff = diff

        if((abs(diff) > 3) or diff == 0):
            print("Failed absolute diff")
            return False, i
        
        will_ascend = next_diff < 0
        is_ascending = diff < 0
        if(not (will_ascend) == (is_ascending)):
            return False, i
        
    return True, i

def handle_out_of_bounds(arr, index, modifier):
    pass




def main():
    print("Running...")
    data = normalize_file("data.txt")
    safe_count = 0
    
    for record in data:
        print("-----")
        print(f">>> TESTING RECORD {record}")
        safe, fail_index = is_record_safe(record)
        if(safe):
            print(f">>> It's safe, First Try!")
            safe_count += 1
            continue
        else:
            print(f">> RECORD FAILED ON INDEX: {fail_index}")
            print(f">> TRYING AGAIN REMOVING INDEX {fail_index}")
            copy = record.copy()
            copy.pop(fail_index)
            safe, other_index = is_record_safe(copy)
            if(safe):
                safe_count += 1
                print(f">>> NEW RECORD {copy} WAS SAFE")
                continue
            print(f">> TRYING AGAIN REMOVING INDEX (-1) {fail_index - 1}")
            copy = record.copy()
            copy.pop(fail_index - 1)
            safe, other_index = is_record_safe(copy)
            if(safe):
                safe_count += 1
                print(f">>> NEW RECORD {copy} WAS SAFE")
                continue
            else:
                print(f">> TRYING AGAIN REMOVING INDEX (+1) {fail_index + 1}")
                copy = record.copy()
                try:
                    copy.pop(fail_index + 1)
                    safe, fail_index = is_record_safe(copy)
                    if(safe):
                        safe_count += 1
                        print(f">>> NEW RECORD {copy} WAS SAFE")
                        continue
                    else:
                        print(f">>> RECORD IS NOT SAFE")
                except:
                    print(f">>> RECORD IS NOT SAFE")

        

    print("Total safe records: ", safe_count)
        


if __name__ == "__main__":
    main()