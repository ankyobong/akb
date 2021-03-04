"""
a = 80
b = 75
c = 55

arg = (a+b+c)/3
print(arg)

a = int(input("숫자를 입력하세요: "))
a = a % 2
if 1 == a:
    print("홀수")
else:
    print("짝수")

pin = input("주민등록번호를 입력하세요: ")
yyyymmdd = pin[:6]
num = pin[7]
print(yyyymmdd)
if num == 1:
    print("남")
else:
    print("여")

"""
print("I eat {0} apples".format(3))
a = "ohmygot"
a.find('o')
a.index('o')
a = [1,2,3,4,5,6,7,8]
a.pop()
a
a.pop(4)
a