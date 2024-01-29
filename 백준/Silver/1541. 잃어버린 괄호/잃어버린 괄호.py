import sys

expr_without_sub = sys.stdin.readline().split("-")
total = sum(map(int, expr_without_sub[0].split("+")))

for expr in expr_without_sub[1:]:
    total -= sum(map(int, expr.split("+")))

print(total)