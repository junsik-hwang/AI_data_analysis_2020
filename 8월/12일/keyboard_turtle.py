import turtle
t = turtle.Turtle()
t.shape("turtle")


while(1):
    keyboard = input("명령을 입력하세요").lower()
    if(keyboard == 'x' or keyboard == ''):
        t.reset()
        break
    elif(keyboard == 'l'):
        t.left(90)
        t.forward(100)
    elif(keyboard == 'r'):
        t.right(90)
        t.forward(100)
    else:
        print("L 또는 R 을 입력하세요! (끝내시려면 x 또는 공백)")
    
