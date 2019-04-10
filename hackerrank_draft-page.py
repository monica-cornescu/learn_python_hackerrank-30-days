import random


a = [100, 72, 4, 39, 1234, 15, 28]


def random_list_generator(start, end, num):
    random_list = []
    for j in range(num):
        random_list.append(random.randint(start, end))
    return random_list


b = random_list_generator(3, 1500, 10)

print(b)
print(min(b))
print(max(b))


