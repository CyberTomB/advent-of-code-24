def get_frequency_dictionary(list):
    frequency = {}
    for i in list:
        try:
            frequency[i] += 1
        except:
            frequency[i] = 1

    return frequency



def main():
    print("Executing...")

    input_list_1 = []
    input_list_2 = []
    with open("advent_01_input") as f:
        lines = f.readlines()
        
    for n in lines:
        nums = n.split("  ")
        input_list_1.append(int(nums[0]))
        input_list_2.append(int(nums[1]))

    # ex_list_1 = [3, 4, 2, 1, 3, 3]
    # ex_list_2 = [4, 3, 5, 3, 9, 3]

    freq_dict_1 = get_frequency_dictionary(input_list_1)
    freq_dict_2 = get_frequency_dictionary(input_list_2)

    similarity_score = 0

    for n in input_list_1:
        try: 
            print(n, freq_dict_2[n])
            similarity_score +=  n * freq_dict_2[n]
        except:
            similarity_score += 0

    print(similarity_score)

main()