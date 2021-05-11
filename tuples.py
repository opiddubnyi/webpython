name = "data.txt"

# sorted hourly track
count = {}
with open('data.txt', 'r', encoding='utf-8') as file:

    for line in file.readlines():
        if line.count('2008') == 1 and line.count('From'):
            hour = line.split(':')[0].split()[-1]

            if hour in count.keys():
                count[hour] += 1
            elif hour not in count.keys():
                count[hour] = 1

for k, v in sorted(count.items()):
    print(k, v)

# most messages
# with open('data.txt', 'r', encoding='utf-8') as file:
#
#     for line in file.readlines():
#         if line.count('2008') == 1 and line.count('From'):
#             sender = line.split()[1]
#
#             if sender in count.keys():
#                 count[sender] += 1
#             elif sender not in count.keys():
#                 count[sender] = 1
#
# maxim = 0
# for k, v in sorted(count.items()):
#     tmp = v
#     if maxim < tmp:
#         maxim, user = v, k
#
# print(user, maxim)







