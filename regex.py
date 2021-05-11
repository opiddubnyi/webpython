import re
import timeit

pattern = str(input('Enter regexp pattern you want to search for: '))


def testing_speed():
    count = 0
    sum = 0
    with open('mbox.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if re.findall(pattern, line):
                sum += int(re.findall(pattern, line)[0])
                count += 1
    print(f'Found {count} match(es), avg = {sum/count}')


elapsed_time = timeit.timeit(testing_speed, number=1)
print(elapsed_time)


