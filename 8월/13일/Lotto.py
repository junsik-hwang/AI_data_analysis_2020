import random

all_num = list(range(1,46))

print("복권 번호 예측하기!")
while(1):
    start = input("Enter를 눌러주세요! (그만하려면 아무키 입력)")
    if(start == ''):
        for i in range(5):
            print(all_num.pop(all_num.index(random.choice(all_num))), end = ' ')
        print(all_num.pop(all_num.index(random.choice(all_num))))
        all_num = list(range(1,46))
    else:
        break
