with open("input") as input:
    input_list = [int(x) for x in input.read().split()]
for numbah in input_list:
    difference = 2020 - numbah
    if difference in input_list:
        break

print(difference * numbah)
