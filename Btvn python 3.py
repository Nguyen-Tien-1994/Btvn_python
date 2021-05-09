""" BÀI TẬP VỀ NHÀ
Bài 1. Code đoạn chương trình cho phép:
    1. Nhập vào bán kình r của hình tròn
    2. Tính diện tích hình tròn đó
    3. In kết quả ra màn hình "Dien tich hình tron la: <giá trị>"
Bài 2. Code đoạn chương trình để giải quyết các yêu cầu sau:
    1. Nhập 3 số thực x, y, z bất kì.
    2. Tính giá trị biểu thức F: F = (x+y+z)/(x^2+y^2+1) - |x-z*cos(y)|
    3. Đưa giá trị tính được của F ra màn hình dưới dạng: Gia tri cua F = <gia tri>
Bài 3. Xây dựng đoạn chương trình mô phỏng lại các phép toán học (càng nhiều càng tốt),
tối thiểu cần có: cộng, trừ, nhân, chia
"""
#Bài 1:
import math
r = 2
s = math.pi*(r**2)
print('Diện tích hình tròn là:',s)
print('----------------------------')
#Bài 2:
import math
x, y, z = 1, 2, 3
a = x + y + z
b = x**2 + y**2 + 1
c = x - z* math.cos(y)
F = a/b - c
print('Giá trị của F =', F)
print('--------------------------')
#bài 3:
print(3+5)
print(9-6)
print(5*6)
print(9/3)
print(9//3)
print(24%7)
print(4**3)
print('---------------------------')
x = 5
x +=5
x = x**2 + 3
print(x)
y = x//5
y %= 5
print(y)
z = 3
z **= 3
print(z)
print('--------------------------------')
x = 5
y =28% 3
print('x = y is',x == y)
print('x > y is', x > y)
print('x != y is', x !=y)
print('x < y is', x < y)
print('x >= y is', x >= y)
print('x <= y', x <= y)
print('----------------------------------')
x = True
y = False
print(x + y)
print(not x)
print(not y)
print(x and y)
print(x or y)
print('------------------------------')
x = 'hello world'
print('Hello in x is','Hello' in x)
print('hello in x is','hello' in x)
y = 'Hello world'
print('x is not y is', x is not y)
print('-------------------------------')
import math

a = 6.78945
print(math.floor(a))
print(math.ceil(a))
print(math.sqrt(a))
print(math.fabs(a))
a = math.floor(a)
print(math.factorial(a))
print(math.exp(a))
a = a**2
b = 45
print(math.gcd(a,b))

