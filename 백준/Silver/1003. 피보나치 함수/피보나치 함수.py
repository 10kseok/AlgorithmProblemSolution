
n = int(input())
call_num = []

for _ in range(n):
    call_num.append(int(input()))

fivonacci_dict = {0 : 0, 1 : 1 }

def fivonacci(n):
    if n < 0:
        return 1

    if n not in fivonacci_dict.keys():
        fivonacci_dict[n] = fivonacci(n-1) + fivonacci(n-2)

    return fivonacci_dict[n]

for num in call_num:
    print(fivonacci(num-1), fivonacci(num))