sample_input = [50, 30, 20, 0, "catch_me", 0, "you_got_me", "did_you_really_catch", 40, 50, "20", 0, 0, 0, 10]
# expected_output = [100, 190, 200]

def get_cumulative_sum(input_list, split_val):
    result = []
    start_val = 0
    for i in range(0, len(input_list), split_val):
        cumulated_val = 0
        for j in input_list[i:i+split_val]:
            if isinstance(j, int):
                cumulated_val += j
        result.append(cumulated_val + start_val)
        start_val += cumulated_val
    return result

print(get_cumulative_sum(sample_input, 5))