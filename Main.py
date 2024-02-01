import random
UsedNumber = [0]

def ask(msg):
    while True:
        try:
            answer = int(input(f'{msg} >>> '))
            if answer <= 0:
                print(f'\n 행,열의 수는 0 또는 음수가 될 수 없습니다.')
        except:
            print(f'\n 올바른 정수를 입력해주세요. ')
            continue
        else:
            break

    return answer

print('='*56, end='\n\n')
print(' '*12, '교실 자리 배치 프로그램')
print(' '*13, '24-02-01, 10111 유승우', end='\n\n')
print('='*56, end='\n\n')
input('시작하려면 아무 키나 누르십시오. . . ')

x_size = ask('\n의자의 가로 수를 입력해주세요.(행의 수)')
y_size = ask('\n의자의 세로 수를 입력해주세요.(열의 수)')

print(f'\n{"="*x_size} 교탁 {"="*x_size}', end='')
for i in range(y_size): #
    print('\n')
    for a in range(x_size):
        number = random.choice(list(set(range((y_size*x_size) + 1)) - set(UsedNumber)))
        UsedNumber.append(number)
        print(number, end='  ')

print(f'\n\n반의 인원은 총 {y_size*x_size}명입니다.')
print(f'나올수 있는 경우의 수는 {(y_size*x_size) * (y_size*x_size)}개입니다.')
