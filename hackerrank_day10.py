# Given a base-10 integer, n, convert it to binary (base-2).
# Then find and print the base-10 integer denoting the maximum number of consecutive 1 s in n's binary representation.

n = int(input("n = "))

# transform the base10 integer into a binary number and then into a string, to get each element and put it into a list
binary_n_string = str(bin(n))
digit_list = []

for d in range(2, len(binary_n_string)):
    digit_list.append(binary_n_string[d])

print(digit_list)

count = 0
consecutive_1_list = []


for digit in digit_list:
    if digit == "0":
        count = 0
    elif digit == "1":
        count = count + 1
        consecutive_1_list.append(count)


# print(consecutive_1_list)
reverse_consecutive_1_list = sorted(consecutive_1_list, reverse = True)
print(reverse_consecutive_1_list[0])




