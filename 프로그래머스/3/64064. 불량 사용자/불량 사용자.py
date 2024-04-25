def solution(user_id, banned_id):
    answer = 0
    # user_id에서 banned_id 갯수만큼 경우의 수를 구한다 (순서 x, 조합)
    # 해당 경우가 banned_id와 일치하는지를 본다.
    r = len(banned_id)
    answer_set = set()
    visited = [False] * len(user_id)
    def is_banned(buf):
        match_count = 0
        is_contain = [False] * r
        for user in buf:
            for b_idx, ban in enumerate(banned_id):
                if len(user) != len(ban) or is_contain[b_idx]:
                    continue
                matched = True
                for i in range(len(user)):
                    if ban[i] != '*' and user[i] != ban[i]:
                        matched = False
                if matched:
                    is_contain[b_idx] = True
                    match_count += 1
                    break;
        return match_count == len(banned_id)
    
    def comb(buffer, users):
        if len(buffer) == r:
            if is_banned(buffer):
                answer_set.add(tuple(sorted(buffer)))
            return
        for i in range(len(users)):
            if not visited[i]:
                buffer.append(users[i])
                visited[i] = True
                comb(buffer[:], users)
                visited[i] = False
                buffer.pop()
            
    comb([], user_id)
    answer = len(answer_set)
    return answer