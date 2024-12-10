import ast

# 참가자 수 읽기
n = int(input().strip())

# 참가자 정보 읽기
members = ""
for _ in range(n):
    members += input().strip()
participants = ast.literal_eval(members)

# 점수 내림차순, 이름 사전순으로 정렬
participants.sort(key=lambda x: (-x['score'], x['name']))

# 순위 계산
ranking = []
current_rank = 1
previous_score = None
same_rank_count = 0

for i, participant in enumerate(participants):
    name, score, is_hidden = participant['name'], participant['score'], participant['isHidden']

    if score == previous_score:
        # 동점자 처리: 이전 순위를 유지하고 카운트 증가
        same_rank_count += 1
    else:
        # 새로운 점수: 현재 순위에 동점자 수를 더해 갱신
        current_rank += same_rank_count
        same_rank_count = 1

    ranking.append((current_rank, name, score, is_hidden))
    previous_score = score

# 결과 출력 (isHidden == 0인 참가자만 출력)
for rank, name, score, is_hidden in ranking:
    if is_hidden == 0:
        print(rank, name, score)