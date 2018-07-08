'''
3-6. 더 많은 손님
식당에서 예약 인원을 늘릴 수 있다 하여 손님을 더 초대할 수 있습니다. 저녁에 초대할 사람을 세 명 더 생각하세요.
- 연습문제 3-4나 3-5에서 프로그램을 시작하세요. 프로그램 마지막에 print문을 추가해 사람들에게 더 큰 저녁 식탁을 발견했다고 알리세요.
- insert()를 써서 새 손님 한 명을 리스트 맨 앞에 추가하세요.
- insert()를 써서 새 손님 한 명을 리스트 중간에 추가하세요.
- append()를 써서 새 손님 한 명을 리스트 마지막에 추가하세요.
- 리스트에 있는 각 손님 앞으로 새 초대 메시지를 출력하세요.

Output:
guido van rossum, please come to dinner.
jack turner, please come to dinner.
lynn hill, please come to dinner.

Sorry, jack turner can't make it to dinner.

guido van rossum, please come to dinner.
gary snyder, please come to dinner.
lynn hill, please come to dinner.

We got a bigger table!
frida kahlo, please come to dinner.
guido van rossum, please come to dinner.
reinhold messner, please come to dinner.
lynn hill, please come to dinner.
gary snyder, please come to dinner.
elizabeth peratrovich, please come to dinner.
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
guests.insert(1, 'gary snyder')

# Print the invitations again.
name = guests[0]
print('\n' + name + ', please come to dinner.')

name = guests[1]
print(name + ', please come to dinner.')

name = guests[2]
print(name + ', please come to dinner.')

# We got a bigger table, so let's add some more people to the list.
print('\nWe got a bigger table!')
guests.insert(0, 'frida kahlo')
guests.insert(2, 'reinhold messner')
guests.append('elizabeth peratrovich')

name = guests[0]
print(name + ', please come to dinner.')

name = guests[1]
print(name + ', please come to dinner.')

name = guests[2]
print(name + ', please come to dinner.')

name = guests[3]
print(name + ', please come to dinner.')

name = guests[4]
print(name + ', please come to dinner.')

name = guests[5]
print(name + ', please come to dinner.')

