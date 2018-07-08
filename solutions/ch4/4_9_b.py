'''
4-9. 세제곱 내포
리스트 내포를 사용해 1부터 10까지 정수의 세제곱으로 리스트를 만드세요.

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

cubes = [number**3 for number in range(1, 11)]

for cube in cubes:
    print(cube)



