'''
수를 입력받아 그 수가 소수인지 판별하는 프로그램 작성
- 0을 입력하면 Exit 출력하고 프로그램 종료
( while문과 break 문 활용하여 작성 )
'''

while(True) :
    prime = 1
    p = int(input("수 입력 : "))
    if (p == 0) :
        print("Exit")
        break
    for i in range(2, p) :
        if (p % i == 0) :
            prime = 0
            break
    if (prime) :
        print("소수입니다.")
    else :
        print("소수가 아닙니다.")