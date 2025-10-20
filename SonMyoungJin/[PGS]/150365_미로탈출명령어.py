#02:00:00.00
'''
탈출조건에 맞게 미로를 탈출하는데, 사전순으로 최소로 탈출하는 문제
- 사전순으로 최우선을 선택(지역 최적해 -> 전역 최적해)해야하기 때문에 그리디 문제
- 사전순 : d < l < r < u

1. 방향 접근을 위해 direction 배열을 각 방향을 나타내는 좌표와 char를 묶어서 만듦
2. 격자안에서의 최단거리를 계산하기 위해 x좌표끼리, y좌표끼리 빼서 절댓값의 합을 최단거리로 사용(맨해튼거리)
3. 최단거리 > K, (k - 최단거리)가 홀수인 경우 불가능하기 떄문에 if문으로 확인해서 'impossible' 리턴
4. k만큼 이동해야하니까 for문사용해서 k만큼 이동할 수 있도록
    - 현재 좌표를 cx, cy로 받고 for문으로 각 방향을 사전순으로 접근하여 다음좌표 nx, ny계산
    - 계산된 다음 좌표가 경계 안에 있는지 확인하고 있으면, 이 방향으로 이동가능한지 확인
        - 불가능 조건을 현재 좌표로 계산해서 이동가능여부 확인
    - 이동가능하면, 결과출력을 위한 배열result에 direction을 append
    - 계산된 다음좌표를 cx, cy에 저장하고, 남은 거리를 저장하는 remaining_k -= 1
    - break해서 방향탐색은 중지하고 남은 k-1번째 진행 
'''

def solution(n, m, x, y, r, c, k):
    directions = [(1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u')]
    
    # 최단거리
    min_dist = abs(x - r) + abs(y - c)
    
    # 불가능한 경우
    if min_dist > k or (k - min_dist) % 2 != 0:
        return 'impossible'
    
    cx, cy = x, y
    result = []
    remaining_k = k
    
    for _ in range(k):
        # 사전순으로 방향탐색
        for dx, dy, direction in directions:
            nx = cx + dx
            ny = cy + dy
            if not(1 <= nx <= n and 1 <= ny <= m):
                continue # 경계넘어가면 다음 index로
            
            # 이 방향으로 이동했을 떄 목표 도달가능한지 확인
            n_k = remaining_k - 1
            n_min_dist = abs(nx - r) + abs(ny - c)
            if n_min_dist <= n_k and (n_k - n_min_dist) % 2 == 0:
                result.append(direction)
                cx, cy = nx, ny
                remaining_k -= 1
                break 
            
    return ''.join(result)