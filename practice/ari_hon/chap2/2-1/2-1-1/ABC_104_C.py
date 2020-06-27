# -*- coding: utf-8 -*-
D, G = map(int, input().split())
p = []
c = []
for i in range(D):
    p_i,c_i = map(int, input().split())
    p.append(p_i)
    c.append(c_i)

min_problem = sum(p)
# コンプリートする・しないでbinary
for bit in range(2**D):
    base_score = 0
    base_problem = 0
    non_completed_index = []
    for shift in range(D):
        if (bit>>shift)&1:
            base_score += c[shift]
            base_score += 100*(shift+1)*p[shift]
            base_problem += p[shift]
        else:
            non_completed_index.append(shift)

    if base_score >= G:
        if base_problem < min_problem:
            min_problem = base_problem
    else:
        add_score = 0
        add_problem = 0
        # 上から順に埋めていく
        non_completed_index = non_completed_index[::-1]
        for idx in non_completed_index:
            max_add_score_idx = 100*(idx+1)*(p[idx]-1)
            if base_score+add_score+max_add_score_idx >= G:
                # 埋め終了
                if (G-base_score-add_score) % (100*(idx+1)) == 0:
                    idx_problem = int((G-base_score-add_score)/(100*(idx+1)))
                else:
                    idx_problem = int((G-base_score-add_score)/(100*(idx+1)))+1
                if idx_problem+add_problem+base_problem < min_problem:
                    min_problem = idx_problem+add_problem+base_problem
                break
            else:
                add_score += max_add_score_idx
                add_problem += p[idx]-1


print(min_problem)                    
        
