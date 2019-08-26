def findHighestFrequencyElement(input_list):
    result = None
    detail_dict = {}
    for i in input_list:
        detail_dict[i] = input_list.count(i)
    # print(detail_dict)
    sorted_dict = sorted(detail_dict.items(), key=lambda x: x[1])
    print(sorted_dict[-2][0])
    return sorted_dict[-2][1]

sample_input = [50, 30, 20, 0, "catch_me", 0, "you_got_me", "did_you_really_catch", 40, 50, "20", 0, 0, 0, 10]

findHighestFrequencyElement(sample_input)