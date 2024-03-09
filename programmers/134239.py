"""
[134239] 우박수열 정적분
https://school.programmers.co.kr/learn/courses/30/lessons/134239

"""
def solution(k, ranges):
    answer = []
    areas = [0.0]
    
    while k > 1:
        # 우박수열 계산
        if k%2==0: newK=k//2
        else: newK = k*3+1

        # 정적분 넓이 계산
        minY, maxY = min(k, newK), max(k, newK)
        areas.append(areas[-1] + (minY+ 0.5*(maxY - minY)))

        k = newK

    n = len(areas)
    for a, b in ranges:
        if n + (b-1) >= a: 
            answer.append(areas[b-1] - areas[a])
        else: 
            answer.append(-1)
        
    return answer