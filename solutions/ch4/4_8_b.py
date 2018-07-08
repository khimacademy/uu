'''
4-8. 세제곱
세 번 제곱한 수를 세제곱이라 부릅니다. 파이썬에서는 2의 세제곱을 2**3으로 씁니다. 1부터 10까지 정수의 세제곱으로 리스트를 만들고, for 루프를 써서 각 값을 출력하세요.

Output:
1
8
27
64
125
216
343
512
729
1000
'''

cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)

for cube in cubes:
    print(cube)

