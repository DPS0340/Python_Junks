import random

rsp = ["가위", "바위", "보"]

print("가위바위보 게임")
print("=" * 20)

while True:
    my_choice = int(input('''1.가위
2.바위
3.보'''))
    my_choice -= 1
    bots_choice = random.randint(0,2)
    print("내 선택:", rsp[my_choice])
    print("봇의 선택:", rsp[bots_choice])
    if my_choice == bots_choice:
        print("비겼습니다!")
    elif my_choice == (bots_choice + 1) % 3:
        print("이겼습니다!")
    else:
        print("졌습니다!")