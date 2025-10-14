hight = float(input("키(cm) : "))
weight = float(input("몸무게(kg) : "))

bmi = weight / ((hight * 0.01) ** 2)

if bmi < 18.5 :
    print("저체중")
elif bmi < 23 : 
    print("정상")
elif bmi < 25 :
    print("과체중")
elif bmi < 30 :
    print("비만")
elif bmi < 35 :
    print("고도비만")
else :
    print("초고도비만")