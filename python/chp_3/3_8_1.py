lst = input().split()
lst.append(True) if lst[0] != lst[-1] else lst.append(False)
# or
lst.append(lst[0] != lst[-1])
print(*lst)