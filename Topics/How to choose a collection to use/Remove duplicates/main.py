names = input().split()

l1 = list()

no_dup = set()

l1.append(names)
for name in names:
    no_dup.add(name)

no_dup_sort = sorted(no_dup)

for i in no_dup_sort:
    print(i)
