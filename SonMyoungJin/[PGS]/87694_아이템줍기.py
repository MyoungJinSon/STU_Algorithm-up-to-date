#03:00:00.00
from collections import deque

'''
여러 직사각형이 겹쳐져있을 때, 그 테두리 위를 따라 캐릭터가 이동하는데, 아이템까지의 최단경로거리 구하는 문제
=> 테두리를 표시하고, 테두리인지 아닌지 탐색하고 길을 지나가야하기 때문에 BFS로 풀이
* 중요 포인트
    직사각형들 겹치면서 내부는 2로 테두리는 1로 표시할 때,
    (3,5)가 1이고 (3,6)이 1인데, 둘이 연결되어있지 않은데, BFS는 갈 수 있는 길로 인식
        1. 변의 길이가 1인 직사각형은  테두리로만 이루어져있는데, 표시되어있는 내부는 없지만
            지나갈 수 없는 내부가 존재하는데, 여기를 뚫고 지나가버림.
        2. 직사각형들 겹치는데, 길이 1만큼 떨어져있는 경우, 지나갈 수 있다고 인식해버림.
    => 따라서 좌표를 2배확장해서, 테두리와 내부, 빈공간을 세밀하게 인식해야함. 마지막에 거리//2해서 리턴

1. 맵크기는 두배니까 max_size = 51*2하고, 각 위치 상태 표시할 grid 만듦
2. 직사각형 배열을 받아서 각 직사각형 그리기 위해 for문으로 각 좌표받아서 *2하고, 그 안에 for문 중첩시켜서
   내부였다가 테두리되는 경우는 없으므로, 내부라면 2 표시하고 2가 아니면 1로 테두리 표시
3. BFS로 아이템을 탐색할 거니까 캐릭터위치도 *2해주고 queue에 좌표넣고, 현재 거리도 표시할거니까 0으로 넣기
4. 방문한 곳 표시하기 위해 visited를 grid와 같은 크기로 만들고 모든곳을 False로하고 현재 캐릭터 위치만 True로 초기화
5. BFS 하는 중에 아이템좌표에 도달하면 거리 반환하고 끝내야하기 때문에, 아이템좌표*2해서 맞으면 dist//2해서 리턴
6. BFS 하기위해 queue가 있는 동안 while문 안에서 이동가능한 경우 상하좌우로 탐색하고, 경계 넘지 않는지 확인하고,
    테두리인 경우만 지나갈 수 있으니까 1인경우만 지나감.
        - 방문표시해주고, 거리+1해서 queue에 push
'''

def solution(rectangle, characterX, characterY, itemX, itemY):
    max_size = 51*2
    grid = [[0] * max_size for _ in range(max_size)]
    
    # 직사각형 그리기
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1*2, y1*2, x2*2, y2*2
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    # 내부는 2 표시
                    grid[i][j] = 2
                elif grid[i][j] != 2:
                    # 테두리는 1 표시
                    grid[i][j] = 1
    
    queue = deque([(characterX*2, characterY*2, 0)])
    visited = [[False] * max_size for _ in range(max_size)]
    visited[characterX*2][characterY*2] = True
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    while queue:
        x, y, dist = queue.popleft()
        
        # 아이템있는 곳 도착 시
        if x == itemX*2 and y == itemY*2:
            return dist//2
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < max_size and 0 <= ny < max_size:
                # 테두리만 이동 가능
                if not visited[nx][ny] and grid[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))
        
    
    return 0