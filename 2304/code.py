import sys
input = sys.stdin.readline

def area_calculate():	# 너비를 계산하는 함수
	global answer, dic	# answer에 너비의 합을 넣어줌, dic은 이 블록을 계산했는지 확인하기 위함(1이면 계산함)
	pre_length = -1	# 두 높이 간의 사이 값들을 채워주기 위한 이전 높이의 좌표 저장

	for b in block:	# 블록 for문
		l, h = b	# l에 좌표, h에 높이
		if dic[l] == 0:	# 0이라면 이 블록은 계산하지 않았다는 의미
			dic[l] = 1	# 1로 초기화시켜주기 -> 계산했다란 뜻
			answer += h	# answer에 h 더해줌 -> 결국 너비는 높이들의 합이기 때문

		if pre_length != -1 and abs(pre_length-l) != 1:	# pre_length가 -1이란 건 첫번째 블록이란 의미, 이전 높이와 현재 높이의 좌표간의 차가 1이 아니란 뜻은 그 사이에 채워줘야 할 좌표들이 있단 의미
			for i in range(min(pre_length,l)+1,max(pre_length,l)):	# 사이의 좌표들 for문
				if dic[i] == 0:	# 이미 계산한 좌표는 생략
					dic[i] = 1	# 계산했단 의미로 1로 초기화
					answer += h 	# 오목하게 안 만들고자 높이를 일정하게 h로 높여서 채워, 더해줌. 그래야 오목해지지 않음 

		pre_length = l	# pre_length는 현재의 좌표로 계속 갱신 초기화해줌

n = int(input())
block = []	# 블록들의 좌표와 높이를 튜플 형태로 저장할 리스트
max_length = 0	# 모든 블록을 포함한 창고를 만들었는지 확인하기 위한 범위 확인용 좌표상의 최대값
answer = 0	# 너비를 저장할 변수
dic = {}	# 확인한 블록들을 1로 초기화할 딕셔너리

for _ in range(n):	# 입력받을 때 좌표의 최대값 찾기
	l, h = tuple(map(int,input().split()))
	if l > max_length: max_length = l
	block.append((l-1,h))	# append 할때에는 tuple형태로 넣기

for i in range(max_length):	# 초기에는 0으로 초기화
	dic[i] = 0

block = sorted(block, key=lambda x : -x[1])	# 높이를 기준으로 내림차순 정렬

area_calculate()	# 너비 계산 함수 호출

print(answer)	# 정답 출력
