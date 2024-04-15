def solution(routes):
    sorted_routes = sorted(routes, key=lambda x:x[1])
    answer = 1
    prev_route = sorted_routes[0]
    for i in range(1, len(sorted_routes)):
        next_route = sorted_routes[i]
        if prev_route[1] >= next_route[0]:
            continue
        prev_route = next_route
        answer += 1
    
    return answer