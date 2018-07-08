'''
4-5. 백만까지 더하기
1부터 백만까지 숫자 리스트를 만들고, min()과 max()를 써서 리스트가 실제로 1에서 시작해 백만에서 끝났는지 확인하세요. 그리고 sum() 함수를 써서 백만 개까지의 합을 구하세요. 금방 계산할 겁니다.

Output:
1
1000000
500000500000
'''

numbers = list(range(1, 1000001))

print(min(numbers))
print(max(numbers))
print(sum(numbers))

