import sys
input = sys.stdin.readline

def solution():
    G, P = int(input()), int(input()) 
    airplanes = [int(input()) for _ in range(P)]
    last_docked_table = [i for i in range(G + 1)]
    count = 0
    
    for arpn in airplanes:
        if last_docked_table[arpn] == arpn:
            count += 1
            last_docked_table[arpn] -= 1
        else:
            is_available = False
            for other_gate in range(last_docked_table[arpn], 0, -1):
                if last_docked_table[other_gate] == other_gate:
                    last_docked_table[other_gate] -= 1
                    last_docked_table[arpn] = other_gate
                    count += 1
                    is_available = True
                    break
            if not is_available:
                print(count)
                return
    print(count)
                
if __name__=="__main__":
    solution() 

