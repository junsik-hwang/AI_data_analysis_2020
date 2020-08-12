import random
answer = random.randint(1,100)
guess = 0
count = 1
print("1부터 100 사이의 숫자를 맞추시오.")
guess = int(input("숫자를 입력하시오."))
for i in range(10):
    if(guess == answer):
        print("정답입니다! 시도 횟수 : ", count)
        break
    elif(guess != answer and i == 9):
        print("시도 횟수 초과! 답은 : ", answer)
        break
    elif(guess > answer):
        print("낮음!")
    else:
        print("높음!")
    guess = int(input("숫자를 입력하시오."))
    count += 1
