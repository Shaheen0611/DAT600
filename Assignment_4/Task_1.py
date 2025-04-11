from scipy.optimize import linprog

# Coefficients of the objective function (negated for maximization)
c = [-168.35, -256.70]

# Coefficients of the inequality constraints (Ax <= b)
A = [
    [15, 20], # Machine time
    [20, 30], # Craftsman time
    [-1, 0] # x >= 10 → -x <= -10
]
b = [2400, 2100, -10]

# Bounds for x and y: x >= 0, y >= 0
x_bounds = (0, None)
y_bounds = (0, None)

# Solve the LP
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Output the results
if result.success:
    x_opt, y_opt = result.x
    max_profit = -result.fun
    print(f"Optimal production:\n - Product X: {x_opt:.2f} units\n - Product Y: {y_opt:.2f} units")
    print(f"Maximum weekly profit: £{max_profit:.2f}")
else:
    print("Optimization failed:", result.message)
