SAMPLE_DATA = [[7,6,4,2,1],
                [1,2,7,8,9],
                 [9,7,6,2,1],
                  [1,3,2,4,5],
                   [8,6,4,4,1],
                    [1,3,6,7,9]]

SAMPLE_SOLUTION = [True, False, False, False, False, True]

def normalize_file(path = "data.txt"):
    f = open(path)
    records = []
    for line in f:
        record = [int(x) for x in line.split(" ")]
        records.append(record)
    return records

def is_record_safe(record: list) -> list[bool]:
    initial_diff = record[0] - record[1]
    if(initial_diff == 0):
        return False
    is_increasing = initial_diff < 0
    prior_level = None

    for level in record:
        if(prior_level == None):
            prior_level = level
            continue

        diff = prior_level - level
        prior_level = level

        if((abs(diff) > 3) or diff == 0):
            return False
        
        pattern_maintained = is_increasing == (diff < 0)
        if(not pattern_maintained):
            return False
        
    return True



def main():
    print("Running...")
    data = normalize_file()
    safe_count = 0
    
    for record in data:
        print(f">>> RECORD {record} is {'safe' if is_record_safe(record) else 'unsafe'}")
        if(is_record_safe(record)):
            safe_count += 1

    print("Total safe records: ", safe_count)
        


if __name__ == "__main__":
    main()