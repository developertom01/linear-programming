from scipy.optimize import linprog


""""
Get coefficients of inequalities Given that:
 maximize -19 * x + -15 * y 
 subject to: 
         -10 <= x <= 10 
         -10 <= y <= 10 
         -2 * x + -10 * y <= 40 
         -16 * x + 18 * y <= 50 
         -3 * x + 3 * y <= 80
"""
# Coefficients of the negative linear objective function (to maximize, we minimize the negative)
c = [19, 15]

# Coefficients of the inequality constraints: A_ub @ x <= b_ub
A_ub = [[-2, -10], [-16, 18], [-3, 3]]
b_ub = [40, 50, 80]

# Bounds for variables
x_bounds = (-10, 10)
y_bounds = (-10, 10)

# Solve the linear programming problem
optimal = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=[x_bounds, y_bounds], method="highs")

if optimal.success:
    # Print the optimal values and the actual objective function value (negative of what was minimized)
    print("Optimal values of x and y:", optimal.x[0], optimal.x[1])
    print("Maximized objective function value:", -optimal.fun)  # Negate to get the actual maximum value
else:
    print("Iteration terminated with status", optimal.status)


"""
The answers expected  are 
Optimal values of x and y: -6.224489795918367 -2.7551020408163267
Maximized objective function value: 159.59183673469389

"""