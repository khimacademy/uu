'''
2-7. 이름에서 공백 제거
사람 이름을 변수에 저장하고 이름 주위에 공백 문자를 넣으세요. 그리고 문자 조합 '\t'와 '\n'을 최소한 한 번씩은 사용하세요. 이름 주위의 공백이 표시되도록 한 번 출력한 다음, 공백 제거 함수 lstrip()과 rstrip(), strip()을 한 번씩 써서 이름을 출력하세요. 다음과 같은 결과를 원합니다.

Output:
Unmodified:
    Eric Matthes

Using lstrip():
Eric Matthes

Using rstrip():
    Eric Matthes

Using strip():
Eric Matthes
'''

name = '\tEric Matthes\n'

print('Unmodified:')
print(name)

print('\nUsing lstrip():')
print(name.lstrip())

print('\nUsing rstrip():')
print(name.rstrip())

print('\nUsing strip():')
print(name.strip())

