#00:29:12.48

'''
정르별로 가장 많이 재생된 노래를 두 개씩 모아 그 리스트를 출력하는 문제
- 속한 노래가 많이 재생된 장르 > 장르 내에서 많이 재생된 노래 > 고유번호 낮은 노래
1. 장르와 재생횟수가 각각 배열로 주어지기 때문에 고유번호까지 인덱스로 접근하기 위해 songs_info라는 배열 만듦
2. 많이 재생된 장르부터 들어가야하기 때문에 각 장르의 재생횟수 합의 리스트 필요하기 때문에 total_plays_genres 딕셔너리 만듦
    - 주어진 배열 genres길이 이용해 for문으로 인덱스기반으로 배열접근해서 songs_info 만들고
    - genres[i]가 total 딕셔너리에 있으면 plays[i]를 더하고 없으면 key에 추가
3. 우선순위에 맞게 출력하기 위해 songs_info와 total_plays_genres를 정렬
    - songs_info는 많이 재생된 순 > 고유번호 낮은 순으로 정렬하기 위해 sort사용해서 key는 lambda x로 우선순위 정렬
    - total_plays_genres는 dict니까 정렬하기 위해 total_plays_genres.items()해서 리스트로 만들고,
        많이 재생된 순이니까 reverse=True해주고, sorted로 리턴해줌
4. 맞게 출력하기 위해 total에 있는 장르가 songs_info에 있으면 answer에 고유번호만 append하고 select+=1,
    select가 2개이상이면 못넣으니까 break
'''

def solution(genres, plays):
    answer = []
    songs_info = []
    total_plays_genres = {}
    
    for i in range(len(genres)):
        songs_info.append([genres[i], plays[i], i])
        if genres[i] not in total_plays_genres:
            total_plays_genres[genres[i]] = plays[i]
        else:
            total_plays_genres[genres[i]] += plays[i]
    
    songs_info.sort(key = lambda x: (-x[1], x[-1]))
    total_plays_genres = sorted(total_plays_genres.items(), reverse = True)
    
    for genre, total_plays in total_plays_genres:
        select = 0
        for g, p, i in songs_info:
            if genre == g:
                answer.append(i)
                select += 1
            if select >= 2:
                break
                
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))