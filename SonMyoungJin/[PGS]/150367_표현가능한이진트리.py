#01:31:45.45
'''
완전이진트리로 십진수를 이진수로 표현가능한지 여부를 확인하는 문제
- 더미노드(0)아래에는 실제노드(1)이 올 수 없고, 완전이진트리는 가운데 인덱스가 항상 루트이므로
    제약을 검증하려면 좌측트리와 우측트리를 재귀적으로 확인해야함
    
1. 해당 이진수를 수용할 수 있는 최소 완전이진트리의 높이를 찾기위해
    - 입력받은 숫자의 이진수 길이를 len(binary)로 찾아
    - 완전이진트리 크기 = 2**hight -1이니까 while  사용해 맞는 높이 high 찾음
2. 완전이진트리의 크기보다 이진수길이가 작으면 앞의 더미노드들 붙여줘서 확인해야하니까 앞에 0붙여줌
3. 표현가능 여부를 확인하기 위해 can_represent_tree(binary, 0, len(binary) - 1) 함수
    - 노드1개이거나 빈 노드는 유효한 노드니까 start >= end 이면
        재귀종료조건이기도 하고 return True
    - 루트가 0이면 더미노드 아래 모든 노드가 더미이므로 모두 맞으면 True
    - 0이 아니면, 재귀적으로 좌측트리를 확인하기위해 start부터 mid-1까지로 범위 줄여서 확인
                        우측트리 확인하기 위해 mid+1부터 end까지로 범위 줄여서 확인
'''

def solution(numbers):
    def can_represent_tree(binary, start, end):
        if start >= end:
            return True
        
        mid = (start + end) // 2
        root = binary[mid]
        
        if root == '0':
            # 더미노드 아래 모든 노드가 더미
            return all(binary[i] == '0' for i in range(start, end + 1))
                
        else:
            # 실제 노드: 좌우 서브트리 재귀 검증
            left_valid = can_represent_tree(binary, start, mid - 1)
            right_valid = can_represent_tree(binary, mid + 1, end)
            return left_valid and right_valid
    
    answer = []
    # 십진수 -> 이진수
    for num in numbers:
        binary = bin(num)[2:] # 앞에 0b떼고
        
        # 완전 이진트리 크기로 패딩
        length = len(binary)
        high = 1
        while (2**high - 1) < length:
            high += 1
        
        target_length = 2**high - 1
        binary = '0' * (target_length - length) + binary # 부족한길이만큼 앞에 0붙임
        if can_represent_tree(binary, 0, len(binary) - 1):
            answer.append(1)
        else:
            answer.append(0)
    
    return answer