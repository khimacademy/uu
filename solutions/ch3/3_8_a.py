'''
3-8. 세계 둘러보기
세계에서 가보고 싶은 장소를 최소한 다섯 곳 이상 생각하세요.
- 리스트에 다섯 장소를 저장하세요. 순서는 상관없습니다.
- 리스트를 원래 순서대로 출력하세요. 출력 형식에는 신경 쓰지 말고 파이썬이 리스트를 출력하는 기본값대로 출력하세요.
- 실제 리스트를 수정하지 말고 sorted()를 써서 리스트를 알파벳 순서로 출력하세요.
힌트: sort()와 sorted() 사용방법은 조금 다릅니다. 헷갈리지 마세요.
- 리스트를 다시 출력해서 여전히 원래 순서임을 확인하세요.
- 리스트의 원래 순서를 바꾸지 말고 sorted()를 써서 알파벳 반대 순서로 출력하세요.
- 리스트를 다시 출력해서 여전히 원래 순서임을 확인하세요.
- reverse()를 써서 리스트 순서를 바꾸세요. 리스트를 출력해서 순서가 바뀐 것을 확인하세요.
- reverse()를 써서 리스트 순서를 다시 바꾸세요. 리스트를 출력해서 순서가 원래대로 돌아온 것을 확인하세요.
- sort()를 써서 리스트를 알파벳 순서로 저장하세요. 리스트를 출력해서 순서가 바뀐 것을 확인하세요.
- sort()를 써서 리스트를 알파벳 반대 순서로 저장하세요. 리스트를 출력해서 순서가 바뀐 것을 확인해보세요.

Output:
Original order:
['himalaya', 'andes', 'tierra del fuego', 'labrador', 'guam']

Alphabetical:
['andes', 'guam', 'himalaya', 'labrador', 'tierra del fuego']

Original order:
['himalaya', 'andes', 'tierra del fuego', 'labrador', 'guam']

Reverse alphabetical:
['tierra del fuego', 'labrador', 'himalaya', 'guam', 'andes']

Original order:
['himalaya', 'andes', 'tierra del fuego', 'labrador', 'guam']

Reversed:
['guam', 'labrador', 'tierra del fuego', 'andes', 'himalaya']

Original order:
['himalaya', 'andes', 'tierra del fuego', 'labrador', 'guam']

Alphabetical
['andes', 'guam', 'himalaya', 'labrador', 'tierra del fuego']

Reverse alphabetical
['tierra del fuego', 'labrador', 'himalaya', 'guam', 'andes']
'''

locations = ['himalaya', 'andes', 'tierra del fuego', 'labrador', 'guam']

print('Original order:')
print(locations)

print('\nAlphabetical:')
print(sorted(locations))

print('\nOriginal order:')
print(locations)

print('\nReverse alphabetical:')
print(sorted(locations, reverse=True))

print('\nOriginal order:')
print(locations)

print('\nReversed:')
locations.reverse()
print(locations)

print('\nOriginal order:')
locations.reverse()
print(locations)

print('\nAlphabetical')
locations.sort()
print(locations)

print('\nReverse alphabetical')
locations.sort(reverse=True)
print(locations)

