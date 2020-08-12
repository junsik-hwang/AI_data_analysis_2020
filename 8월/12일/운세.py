import random
number = random.randint(0,7)
answer = ["조금 더 노력해보세요",
          "지금 시작하세요",
          "주변 사람에게 도움을 청해보세요",
          "오늘은 힘들어요.",
          "당신 스스로 답을 이미 알고 있어요.",
          "의심할 여지가 없습니다.",
          "이게 질문인가요?",
          "기다리세요."]

while(1):
    name = input("(그만하려면 엔터) 이름 : ")
    if(name == ''):
        break
    question = input("무엇에 대하여 알고 싶은가요?")
    print(name,"님", question, "에 대하여 질문 주셨군요.")
    print("운명의 주사위를 굴려볼게요...")
    print(answer[number])
