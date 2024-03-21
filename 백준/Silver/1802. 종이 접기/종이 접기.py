import sys
input = sys.stdin.readline

def solution():
    global available, paper
    T = int(input())
    
    def fold(left, right):
        global available, paper
        if (not available or left > right):
            return
        
        mid = (left + right) // 2
        _left, _right = mid - 1, mid + 1
        
        while (_left >= left and _right <= right):
            if paper[_left] == paper[_right]:
                available = False
                return
            _left -= 1
            _right += 1
            
        fold(left, mid - 1)
        fold(mid + 1, right)
        
    for _ in range(T):
        available = True
        paper = input()
        fold(0, len(paper) - 1)
        print("YES" if available else "NO")
    
if __name__=="__main__":
    solution() 