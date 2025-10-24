'''
양의 정수들의 덧셈을 수행하려한다.
- 더하고자 하는 숫자들을 입력
- 0이 입력되면 입력은 종료
- 앞서 입력한 숫자들을 더한 결과값 출력 프로그램 작성
( while을 활용하여 작성 )
'''

sum = 0

while (True) :
    num = int(input("더하고자 하는 숫자 입력 (종료 0) : "))
    if (num == 0) :
        break
    else : 
        sum += num
        
print(sum)