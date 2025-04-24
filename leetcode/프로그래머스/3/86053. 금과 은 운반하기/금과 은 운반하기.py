def solution(a, b, g, s, w, t):
    total_g, total_s = 0, 0
    min_ellapsed_time, max_ellapsed_time = 0, 2 * (a + b) * max(t)
    # 각 도시의 모든 자원을 옮겼을 때의 최대 시간을 구한다.
    # for i in range(len(g)):
    #     _g, _s, _w, _t = g[i], s[i], w[i], t[i]
    #     total_rsc = _g + _s
    #     delivery_cnt = 2 * total_rsc // _w + (1 if total_rsc % _w else -1)
    #     cur_ellapsed_time = delivery_cnt * _t
    #     if max_ellapsed_time < cur_ellapsed_time:
    #         max_ellapsed_time = cur_ellapsed_time
            
    # 시간 계산법
    # 나눠 떨어짐 => 500 // 2 = 250, 500 % 2 = 0 => 2 * t *250 - t => (2 * 250 * - 1)t
    # 나눠 떨어지지 않음 => 499 // 2 = 249, 499 % 2 = 1 => 2 * t * 249 + t => (2 * 249 * + 1)t
    def can_delivery_in(time):
        total_rsc, total_g, total_s = 0, 0, 0
        for i in range(len(g)):
            # 10, 10
            # 100, 100, 7, 10
            _g, _s, _w, _t = g[i], s[i], w[i], t[i]
            cur_rsc = _g + _s # 200
            # time -> cnt, 주어진 시간에서 배달 횟수 구하는 법
            # 580 // 10 = 58 => 왕복 29번 => 29 * w
            # 579 // 10 = 57 => 왕복 28번, 편도 1 번 => 29(28 + 1) * w
            deliverable_cnt = time // _t
            deliverable_weight = (deliverable_cnt // 2 + (1 if deliverable_cnt % 2 else 0)) * _w
            total_rsc += min(cur_rsc, deliverable_weight) # (200, 101) (200, 21)
            total_g += min(_g, deliverable_weight) # (100, 101) (100, 21)
            total_s += min(_s, deliverable_weight) # (100, 101) (100, 21)
        
        # (101, 100, 100) (21, 21, 21)
        return total_rsc >= (a + b) and total_g >= a and total_s >= b
    
    # 최대 시간을 기준으로, 시간을 줄여가며(이분 탐색) a, b를 만족하는 최적의 시간을 찾는다.
    while min_ellapsed_time <= max_ellapsed_time:
        fastest_time = (min_ellapsed_time + max_ellapsed_time) // 2
        if can_delivery_in(fastest_time):
            max_ellapsed_time = fastest_time - 1
            continue
        min_ellapsed_time = fastest_time + 1
    return min_ellapsed_time