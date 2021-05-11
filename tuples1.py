import timeit

def stupid():
    name = "data.txt"
    count = 0
    sample = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    with open('data.txt', 'r', encoding='utf-8') as file:

        for line in file.readlines():
            line = line.lower()
            for char in line:
                if char in sample:
                    count += 1


def code_to_test():
    name = "data.txt"
    count = {}
    total = 0
    sample = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    with open('data.txt', 'r', encoding='utf-8') as file:

        for line in file.readlines():
            line = line.lower()
            for char in line:
                if char in sample:
                    total += 1
                    if char in count.keys():
                        count[char] += 1
                    elif char not in count.keys():
                        count[char] = 1

    maximum = 0
    for k, v in sorted(count.items()):
        tmp = v
        if maximum < tmp:
            maximum, user = v, k

    for k, v in sorted(count.items()):
        return(k, v, 'percentage = ', round(v / total * 100, 3), '%')

    print('max used = ', user, maximum)


elapsed_time = timeit.timeit(code_to_test, number=10) / 10
print(elapsed_time)


