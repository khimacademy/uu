'''
3-7. 손님 리스트 줄이기
식당에서 예약에 혼선이 있었다며 연락이 왔습니다. 두 자리만 예약할 수 있다고 합니다.
- 연습문제 3-6에서 프로그램을 시작하세요. 새 행을 추가해 저녁 식사에 손님을 두 명밖에 초대할 수 없다는 메시지를 출력하세요.
- 리스트에 두 명만 남을 때까지 pop()을 써서 한 번에 손님 이름 하나씩 리스트에서 제거하세요. 리스트에서 손님 이름을 꺼낼 때마다 저녁에 초대하지 못해 미안하다는 메시지를 출력하세요.
- 여전히 리스트에 아직 남아 있는 손님들에게 저녁 약속이 유효하다는 메시지를 출력하세요.
- del을 써서 리스트의 마지막 두 이름을 제거해 빈 리스트를 만드세요. 프로그램 마지막에 리스트를 출력해 실제 빈 리스트가 남아 있음을 확인하세요.

Output:
guido van rossum, please come to dinner.
jack turner, please come to dinner.
lynn hill, please come to dinner.

Sorry, jack turner can't make it to dinner.

guido van rossum, please come to dinner.
lynn hill, please come to dinner.
gary snyder, please come to dinner.

We got a bigger table!
frida kahlo, please come to dinner.
guido van rossum, please come to dinner.
reinhold messner, please come to dinner.
lynn hill, please come to dinner.
gary snyder, please come to dinner.
elizabeth peratrovich, please come to dinner.

Sorry, we can only invite two people to dinner.
Sorry, elizabeth peratrovich there's no room at the table.
Sorry, gary snyder there's no room at the table.
Sorry, lynn hill there's no room at the table.
Sorry, reinhold messner there's no room at the table.
frida kahlo, please come to dinner.
guido van rossum, please come to dinner.
[]
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

# Oh no, the table won't arrive on time!
print('\nSorry, we can only invite two people to dinner.')

name = guests.pop()
print('Sorry, ' + name + " there's no room at the table.")

name = guests.pop()
print('Sorry, ' + name + " there's no room at the table.")

name = guests.pop()
print('Sorry, ' + name + " there's no room at the table.")

name = guests.pop()
print('Sorry, ' + name + " there's no room at the table.")

# There should be two people left. Let's invite them.
name = guests[0]
print(name + ', please come to dinner.')

name = guests[1]
print(name + ', please come to dinner.')

# Empty out the list.
del guests[0]
del guests[0]

# Prove the list is empty.
print(guests)

