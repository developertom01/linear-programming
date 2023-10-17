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
# Coefficients of linear function
c = [-19, -15]

# Given that A_ub @ x <= b_ub

# A_ub - Coefficients of inequalities [[x,y]]
A_ub = [[-2, -10], [-16, 18], [-3, 3]]
# b_ab : Y intercepts of the inequalities [1,2,4]
b_ub = [40, 50, 80]

# Also Given that A_eq @ x == b_eq -
# Bounds for variables
x_bounds = (-10, 10)
y_bound = (-10, 10)
bounds = [x_bounds, y_bound]
optimal = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="highs")

if optimal.success:
    print(optimal.message)
    print("optimal objective function value ", optimal.fun ,)
    print("alues of the decision variables that minimizes the objective function while satisfying the constraints. ", optimal.x)

else:
    print("Iteration terminated with status", optimal.status, optimal.message)