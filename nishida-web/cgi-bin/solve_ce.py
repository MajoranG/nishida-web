#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import sys
import math
import cgitb

def solve1(a, b):
    if a != 0:
        x = [complex(0, 0)]
        x[0] = complex(-b/a, 0)
        return x

def solve2(a, b, c):
    if a != 0:
        x = [complex(0, 0)] * 2
        D = b**2 - 4*a*c
        if D >= 0:
            x[0] = complex((-b + math.sqrt(D))/(2*a), 0)
            x[1] = complex((-b - math.sqrt(D))/(2*a), 0)
        elif D < 0:
            x[0] = complex(-b/(2*a), math.sqrt(-D)/(2*a))
            x[1] = complex(-b/(2*a), -math.sqrt(-D)/(2*a))
        return x

def f3(a, b, c, d, x):
    return a*x**3 + b*x**2 + c*x + d

def d1f3(a, b, c, d, x):
    return 3*a*x**2 + 2*b*x + c

def d2f3(a, b, c, d, x):
    return 6*a*x + 2*b

def d3f3(a, b, c, d, x):
    return 6*a

def newton3(a, b, c, d, x0):
    if a != 0:
        x1 = 0
        e = 1e-22
        c = 0
        C = int(math.pow(10, 10))
        for i in range(C):
            x1 = (2*a*x0**3+b*x0**2-d)/(3*a*x0**2+2*b*x0+c)
            if abs(x0 - x1) <= e:
                break
            if c > 10000:
                exit()
            x0 = x1
            c = c + 1
        return x1

def solve3(a, b, c, d):
    if a != 0:
        x = [complex(0, 0)] * 3
        da = 3*a
        db = 2*b
        dc = c

        D3 = db**2 - 4*da*dc
        if D3 > 0:
            x_tmp = solve2(da, db, dc)
            p = x_tmp[0].real
            q = x_tmp[1].real
            if f3(a, b, c, d, p) * f3(a, b, c, d, q) < 0:
                x[0] = complex(newton3(a, b, c, d, p-1), 0)
                x[1] = complex(newton3(a, b, c, d, (p+q)/2), 0)
                x[2] = complex(newton3(a, b, c, d, p+1), 0)
            else:
                if d1f3(a, b, c, d, 1) != 0:
                    x[0] = complex(newton3(a, b, c, d, 1), 0)
                else:
                    x[0] = complex(newton3(a, b, c, d, 2), 0)
                ca = 8*a**2
                cb = 8*a*b
                cc = 2*(b**2+a*c)
                cd = b*c - a*d
                p = newton3(ca, cb, cc, cd, 1)
                q = math.sqrt(6*d1f3(a, b, c, d, p)/d3f3(a, b, c, d, p))
                x[1] = complex(p, q)
                x[2] = complex(p, -q)
        else:
            if d1f3(a, b, c, d, 1) != 0:
                x[0] = complex(newton3(a, b, c, d, 1), 0)
            else:
                x[0] = complex(newton3(a, b, c, d, 2), 0)
            ca = 8*a**2
            cb = 8*a*b
            cc = 2*(b**2+a*c)
            cd = b*c - a*d
            p = newton3(ca, cb, cc, cd, 1)
            q = math.sqrt(6*d1f3(a, b, c, d, p)/d3f3(a, b, c, d, p))
            x[1] = complex(p, q)
            x[2] = complex(p, -q)
        return x

#cgitb.enable()

form = cgi.FieldStorage() # フォームデータを取得する

print("Content-Type: text/html; charset=UTF-8") # HTMLを記述するためのヘッダ
print("")
print('<body bgcolor="#FFC7AF" text="#000000">')
print('<a href="/"><img src="/img/top.png" alt="トップ"></a><br />')

# フォームのデータが入力されていない場合
a = 0
b = 0
c = 0
d = 0
try:
    if "a" in form:
        a = int(form.getvalue("a"))
    if "b" in form:
        b = int(form.getvalue("b"))
    if "c" in form:
        c = int(form.getvalue("c"))
    if "d" in form:
        d = int(form.getvalue("d"))
except ValueError:
    print("バカタレ")
    exit(0)

print(a, "x^3 + ", b, "x^2 + ", c, "x + ", d, " = 0<br />")
x = []
if a != 0:
    x = solve3(a, b, c, d)
elif b != 0:
    x = solve2(b, c, d)
elif c != 0:
    x = solve1(c, d)
elif d != 0:
    print(d, "= 0なわけないだろバカタレ")
    exit(0)
else:
    print("0 = 0に決まっているだろバカタレ")
    exit(0)
for i in x:
    print("x =", i, "<br />")
    #print(f3(a, b, c, d, i), "<br />")


print('</body>')
