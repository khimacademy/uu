'''
4-6. 홀수
range() 함수의 세 번째 매개변수를 써서 1부터 20까지의 홀수로 구성된 리스트를 만드세요. for 루프를 써서 각 숫자를 출력하세요.

Output:
1
3
5
7
9
11
13
15
17
19
'''

odds = list(range(1, 21, 2))

for odd in odds:
    print(odd)


