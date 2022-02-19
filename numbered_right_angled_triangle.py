"""
Author - Rakshit RK
Date - Feb 19, 2022
"""


def right_angled_triangle(number):
    all_nums = [num for num in range(number) if num != 0]
    all_nums.append(number)
    output_set = []
    iter_ = 1
    start = 2
    while True:
        if len([val for tup in output_set for val in tup]) == len(all_nums):
            break
        if not output_set:
            output_set.append([all_nums[0]])
        else:
            range_ = len([val for tup in output_set for val in tup]) + start
            last_idx = [ix for ix, val in enumerate(all_nums) if val == output_set[-1][-1]][0] + 1
            start += 1
            output_set.append(all_nums[last_idx:range_])
        iter_ += 1

    if len(output_set[-1]) < len(output_set[-2]):
        output_set[-2].extend(output_set[-1])
        output_set.pop()

    for ls in reversed(output_set):
        print_str = ''
        for val in ls:
            print_str = print_str + " " + str(val)
        print(print_str)


if __name__ == "__main__":
    print("Please enter a number in the below line")
    input_ = int(input())
    right_angled_triangle(input_)
