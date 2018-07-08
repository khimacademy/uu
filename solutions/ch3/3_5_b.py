'''
3-5. 손님 리스트 바꾸기
손님 중 한 명이 초대에 응할 수 없다고 말했으니 새 리스트를 만들어야 합니다. 초대할 다른 사람을 생각해 보세요.
- 연습문제 3-4에서 작성한 프로그램에 이어서 마지막에 print문을 추가해 불참한 손님의 이름을 출력하세요.
- 리스트를 수정해서 불참한 손님의 이름을 새 손님 이름으로 바꾸세요.
- 아직 리스트에 있는 각 손님 앞으로 초대 메시지를 출력하세요.

Output:
guido van rossum, please come to dinner.
jack turner, please come to dinner.
lynn hill, please come to dinner.

Sorry, jack turner can't make it to dinner.

guido van rossum, please come to dinner.
lynn hill, please come to dinner.
gary snyder, please come to dinner.
'''

# Invite some people to dinner.
guests = ['guido van rossum', 'jack turner', 'lynn hill']

name = guests[0]
print(name + ', please come to dinner.')

name = guests[1]
print(name + ', please come to dinner.')

name = guests[2]
print(name + ', please come to dinner.')

name = guests[1]
print('\nSorry, ' + name + " can't make it to dinner.")

# Jack can't make it! Let's invite Gary instead.
del guests[1]
guests.append('gary snyder')

# Print the invitations again.
name = guests[0]
print('\n' + name + ', please come to dinner.')

name = guests[1]
print(name + ', please come to dinner.')

name = guests[2]
print(name + ', please come to dinner.')

