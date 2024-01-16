N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())

M_numbers = list(map(int, input().split()))

def binary_search(x, M_numbers):
    def _binary_search(left, right):
        if left > right: return False

        mid = (left + right) // 2
        if M_numbers[mid] == x: return True
        if M_numbers[mid] < x:
            return _binary_search(mid + 1, right)
        elif M_numbers[mid] > x:
            return _binary_search(left, mid - 1)
    return _binary_search(0, len(M_numbers) - 1)

answer = [int(binary_search(M_numbers[i], A)) for i in range(M)]

print('\n'.join(map(str, answer)))