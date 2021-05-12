import random

tries = 10000
in_count = 0
out_count = 0
for i in range(1, tries):
    x = random.uniform(0,1)
    y = random.uniform(0,1)

    c = x**2 + y**2

    if c <= 1:
        in_count += 1
    else:
        out_count += 1

print('pi is around ~', 4 * in_count/(out_count + in_count))

