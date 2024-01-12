import sys
sorted_dict_num = sorted({i : int(sys.stdin.readline()) for i in range(9)}.items(), key=lambda x:x[1])
print(sorted_dict_num[-1][1], sorted_dict_num[-1][0] + 1, sep="\n")