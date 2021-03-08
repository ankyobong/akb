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
a = "a:b:c:d"
a=a.replace(":", "#")
a
a=[1,3,5,4,2]
a.reverse()
a
a = ['Life', 'is', 'too', 'short']
a= ' '.join(a)
a
a = (1, 2, 3)
a= a + (4,)
a = dict()
a
a[250] ='python'
#a[[1]] = 'python' #딕셔너리의 Key로 쓸 수 있느냐 없느냐는 Key가 변하는 값인지 변하지 않는 값인지에 달려 있다. 리스트는 그 값이 변할 수 있기 때문에 Key로 쓸 수 없다. 다음 예처럼 리스트를 Key로 설정하면 리스트를 키 값으로 사용할 수 없다는 오류가 발생한다.
a = dict()
a={'A':90, 'B':80, 'C':70}
a.pop('B')
a = b = [1, 2, 3]
a[1] = 4
b


##################################################################3장연습문제

a
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

a: print("shirt")

if "python" in a and "you" not in a: print("python")
a=0
sum=0
while a <= 1000:
    a = a+1
    if a%3 == 0: sum = a+ sum


print(sum)
i=1
while i <6:
   print('*'* i)
   i += 1
i=1
for i in range(1, 101) :
    print(i)

a=[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum=0
i=0
for i in a:
    sum += i

score =sum/len(a)
print(score)
i=0
numbers = [1, 2, 3, 4, 5]
result = [i*2 for i in numbers if i%2 == 1]
result

##################################################################4장연습문제
def boolean(a):
    if a%2 ==0:c ="짝수입니다."
    else: c = "홀수입니다."
    return print(c)
boolean(1)
boolean(2)

def arg(a):
    sum = 0
    for i in a:
        sum+=i
    arg = sum / len(a)
    return arg

arg([1,2,35,54])

print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python") #이거만 띄어쓰기됨
print("".join(["you", "need", "python"]))
"""
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()
f2 = open("test.txt", 'r')
print(f2.read())
f2.close()

user_input = input("저장할 내용을 입력하세요:")
f = open('test.txt', 'a')
f.write("\n")
f.write(user_input)
f.close()

f = open('test.txt', 'r')
body = f.read()
f.close()

body = body.replace('java', 'python')

f = open('test.txt', 'w')
f.write(body)
f.close()

f = open('test.txt'.r)
print(f.read())
"""
##################################################################5장연습문제

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
     def minus(self, val):
         self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value >100:
            self.value =100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)

all([1, 2, abs(-3)-3])
chr(ord('a')) == 'a'

a = range(4)
list(a)