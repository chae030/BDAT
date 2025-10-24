# 1이상의 정수를 입력하면 그 수의 약수를 출력해주는 프로그램 (for문 활용)

a = int(input("1 이상의 정수 입력 : "))

for i in range(1, a+1) :
    if (a % 1 == 0) :
        print(i)