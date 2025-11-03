#00:59:39.31
import sys

#sys.stdin = open('input.txt', 'r')

def input():
    return sys.stdin.readline().rstrip()

'''
블록이 쌓여있는 2차원 세계에 고이는 빗물 계산하는 문제
- 물은 가장 높은 높이의 블록에서 낮은 높이의 블록 기준으로 고이니까 블록의 높이를 찾아서 빗물을 계산해야함
- 어떤 칸 i에 고일 수 있는 물의 양은 min(왼쪽 최고 높이, 오른쪽 최고 높이) - 현재 i의 블록 높이이니까
    각 칸 i를 기준으로 왼쪽, 오른쪽 최고 높이 구해야함.

1. 각 칸 i를 기준으로 왼쪽 최고 높이 구하기 위해 
    - left_max배열을 [0]*W으로 초기화
    - left_max[0]은 당연히 블록 중 첫번쨰높이 일테니까 block[0]으로 초기화
    - left_max[i]는 이전블록과 현재블록을 비교해서 더 높은 것이므로 max(left_max[i-1], blocks[i])
2. 각 칸 i를 기준으로 오른쪽 최고 높이 구하기 위해
    - right_max배열을 [0]*W으로 초기화
    - right_max[-1]은 당연히 블록 중 마지막높이 일테니까 block[-1]로 초기화
    - right_max[i]는 현재블록과 현재의 오른쪽 블록 비교해서 더 높은 것이므로 뒤쪽에서부터 접근해 
        max(right_max[i+1], blocks[i])
3. 빗물은 양쪽 벽중 더 낮은 쪽의 높이까지만 찰 수 있으니까
    현재 칸 i에 대해서 min(left_max[i], right_max[i]) - blocks[i]인데, 
    음수가 나오는경우 물이 안고이니까 max(0, min(left_max[i], right_max[i]) - blocks[i])
'''

H, W = map(int, input().split())
blocks = list(map(int, input().split()))

# i번째에서 왼쪽 최고높이, 오른쪽 최고 높이
left_max = [0] * W
right_max = [0] * W

# 왼쪽 최고 높이 계산
left_max[0] = blocks[0]
for i in range(1, W):
    left_max[i] = max(left_max[i-1], blocks[i])
    
# 오른쪽 최고 높이 계산
right_max[-1] = blocks[-1]
for i in range(W-2, -1, -1):
    right_max[i] = max(right_max[i+1], blocks[i])

# 빗물 계산
water = 0
for i in range(W):
    water += max(0, min(left_max[i], right_max[i]) - blocks[i])

print(water)

