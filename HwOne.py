import math
def bisection(f, a, b, tol=1e-6, max_iter=100):
    for _ in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    raise ValueError("Bisection method did not converge")

def equation_a(x):
    return x**3 - 3*x**2 + 3*x - 1

root_a_bisection = bisection(equation_a, 1, 3)
print("Root (Bisection):", root_a_bisection)

def newton(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise ValueError("Newton's method did not converge")

def equation_a(x):
    return x**3 - 3*x**2 + 3*x - 1

def equation_a_derivative(x):
    return 3*x**2 - 6*x + 3


root_a_newton = newton(equation_a, equation_a_derivative, 2)
print("Root (Newton):", root_a_newton)
def secant(f, x0, x1, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if abs(x2 - x1) < tol:
            return x2
        x0, x1 = x1, x2
    raise ValueError("Secant method did not converge")
def equation_a(x):
    return x**3 - 3*x**2 + 3*x - 1
root_a_secant = secant(equation_a, 1, 3)
print("Root (Secant):", root_a_secant)


# a. x^3 - 2x - 5 = 0 deriv: 3x^2 - 2
# Root (Bisection): 2.0945515632629395
# Root (Newton): 2.0945514815423265
# Root (Secant): 2.094551481542313 

# b. -math.exp(-x) - 1 deriv:-math.exp(-x) - 1
#Root (Bisection): 0.567143440246582
#Root (Newton): 0.5671432904097811
#Root (Secant): 0.567143290409603

#c. x * math.sin(x) - 1 deriv:math.sin(x) + x * math.cos(x)
# Root (Bisection): 1.1141571998596191
# Root (Newton): 1.1141571408717905
# Root (Secant): 1.1141571408718775

# d. x**3 - 3*x**2 + 3*x - 1 deriv: 3*x**2 - 6*x + 3
# Root (Bisection): 0.9999990463256836
# Root (Newton): 1.0
# Root (Secant): 1.0

