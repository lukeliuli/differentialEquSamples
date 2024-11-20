'''
########################################################################################################
准备写的论文中，用python符号运算HJB公式计算双车微分博弈模型,结果失败

'''

from sympy import *

'''
x, y = symbols('x y')
expr = x**2 + y**2

# 求值
result = expr.evalf(subs={x: 3, y: 4})
print(result)  # 输出: 25.0000000000000


x, y = symbols('x y')
# 定义方程组
a = 4*x + 7 - y
b = 5*y - x + 6
# 求解方程组
solutions = solve((a, b), (x, y))
print(solutions)  # 输出: {x: 1, y: 3}
'''
x1_0, x1_T0 = symbols('x1_0 x1_T0')
y1_0, y1_T0 = symbols('y1_0 y1_T0')

x2_0, x2_T0 = symbols('x2_0 x2_T0')
y2_0, y2_T0 = symbols('y2_0 y2_T0')


a, b, c, d, T, theta, v,u = symbols('a b c d T theta v u')

func1  = x1_0+u*T-x1_T0
func2  = y1_0-y1_T0
func3 =  x2_0+v*cos(theta)*T-x2_T0
func4 =  y2_0+v*cos(theta)*T-y2_T0
vfunc = 2*c/d*(x1_T0-x2_T0)*cos(theta)-v
ufunc = -2*a/b*(x1_T0-x2_T0) -u

#solutions = solve((func1, func2,func3,func4,ufunc,vfunc), (x1_T0,x2_T0,y1_T0,y2_T0))
#print(solutions)  # 输出: {x: 1, y: 3}

solutions = solve((func2,vfunc,ufunc), (y1_T0,u,v))
print(solutions)  # 输出: {x: 1, y: 3}

solutions = solve((func2,vfunc,ufunc,func1), (y1_T0,u,v,x1_T0))
print(solutions)  # 输出: {x: 1, y: 3}



func1  = x1_0-2*a/b*(x1_T0-x2_T0)*T-x1_T0
func2  = x2_0+2*c/d*(x1_T0-x2_T0)*cos(theta)*T-x2_T0
solutions = solve((func1,func2), (x1_T0,x2_T0))
print(solutions)  # 输出: {x: 1, y: 3}

rvl1 = solutions[x1_T0]
rvl2 = solutions[x2_T0]
rvl1 = simplify(rvl1)
rvl2 = simplify(rvl2)
print(rvl1)
print(rvl2)

