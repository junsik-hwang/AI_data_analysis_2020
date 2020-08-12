n = int(input("몇 단을 출력하시겠습니까?"))

for i in range(9,0,-1):
    print("%d * %d = %d" %(n, i, n*i))

