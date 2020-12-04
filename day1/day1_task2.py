from day1 import measure
with open("input") as input:
    input_list = [int(x) for x in input.read().split()]

@measure
def find_combination(number_to_find=2020, input_list=input_list):
    ans = None
    for number in input_list:
        difference = number_to_find - number
        available_options = [x for x in input_list if x<difference]
        for i in available_options:
            diff = difference - i
            if diff in available_options:
                ans = number*i*diff
                print(ans)
                break
        if ans != None:
            break

find_combination()
