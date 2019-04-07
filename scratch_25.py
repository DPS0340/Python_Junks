import random
import time

while True:
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    print("%d + %d =" % (x, y), end= " ")
    started = time.time()
    answer = int(input())
    elapsed = time.time() - started
    if answer == x + y and elapsed <= 5:
        print("잘했어요!!")
    elif answer == x + y and elapsed > 5:
        print("잘했지만, 늦었어요!")
    else:
        print("다음번에는 잘할 수 있죠?")