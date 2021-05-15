
#Bài 2:
# Giai phương trình bậc 2 a*(x**2) + b*x + c = o
"""
import math
a = float(input(" nhập a = "))
b = float(input(" nhập b = "))
c = float(input(" nhập c = "))
if a == 0:
    if b == 0:
        print(" Phương trình vô nghiệm.")
    else:
        print(f"phương trình có một nghiệm x = {-c/ b}")
else:
    denta = b**2 - 4*a*c
    if denta == 0:
        print(f"phương trình có nghiệm kép x1 = x2 = {-b/(2*a)}")
    elif denta > 0:
        x1 = ((-b + math.sqrt(denta))/ (2 * a))
        x2 = ((-b - math.sqrt(denta))/(2 * a))
        print(f" Phương trình có 2 nghiêm x1 = {x1}, x2 = {x2}")
    else:
        j = math.sqrt(complex(-1))
        x1 = complex((-b + math.sqrt(-denta)*(j))/(2*a))
        x2 = complex((-b - math.sqrt(-denta)*j)/(2*a))
        print(f"phương trình có 2 nghiệm phức x1 = {x1}, x2 = {x2}")
"""
