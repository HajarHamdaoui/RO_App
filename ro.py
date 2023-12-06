from pulp import *
import matplotlib.pyplot as plt
import numpy as np

model = pulp.LpProblem('linear_programming', LpMaximize)

# get solver
solver = getSolver('PULP_CBC_CMD') #The CBC solver is an open-source tool for solving linear and mixed-integer programming problems.

# declare decision variables
x1 = LpVariable('x1', lowBound = 0, cat = 'continuous') #They are continuous variables (can take any real value) and have lower bounds of 0.
x2 = LpVariable('x2', lowBound = 0, cat = 'continuous')

# declare objective
z1 = int(input("z1 = "))
z2 = int(input("z2 = "))
# f.o. test case 1 
#model += 1*x1 + 1*x2
# f.o. original test case
#model += 5*x1 + 3*x2
model += z1*x1 + z2*x2
# f.o. test case 2 
# model += 2*x1 + 1*x2 

# declare constraints
a1 = int(input("a1 = "))
b1 = int(input("b1 = "))
c1 = int(input("c1 = "))

a2 = int(input("a2 = "))
b2 = int(input("b2 = "))
c2 = int(input("c2 = "))
# test case 1
""" model += 2*x1 + 1*x2 <= 2 
model += 3*x1 + 1*x2 <= 3 """
# original test case
#model += 3*x1 + 5*x2 <= 15 
#model += 5*x1 + 2*x2 <= 10
model += a1*x1 + b1*x2 <= c1 
model += a2*x1 + b2*x2 <= c2
# test case 2
""" model += 1*x2 <= 2 
model += 4*x1 + 2*x2 <= 8 """

# solve 
results = model.solve(solver=solver)

# print results
if LpStatus[results] == 'Optimal': print('The solution is optimal.')
print(f'Objective value: z* = {value(model.objective)}')
print(f'Solution: x1* = {value(x1)}, x2* = {value(x2)}')


# Plotting the feasible region and constraints
x_vals = np.linspace(0, 10, 400)
# test case 1
""" y1 = (2 - 2 * x_vals)  # Constraint 1: 2*x1 + x2 <= 2
y2 = (3 - 3 * x_vals)  # Constraint 2: 3*x1 + x2 <= 3 """
# original test case
#y1 = (15 - 3 * x_vals) / 5  
#y2 = (10 - 5 * x_vals) / 2
y1 = (c1 - a1 * x_vals) / b1  
y2 = (c2 - a2 * x_vals) / b2
# test case 2
""" y1 = 2 
y2 = (8 - 4 * x_vals) / 2 """ 

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y1, label=f'{a1}*x1 + {b1}*x2 <= {c1}')
plt.plot(x_vals, y2, label=f'{a2}*x1 + {b2}*x2 <= {c2}')
yy = np.minimum(y1, y2)
plt.fill_between(x_vals, 0, yy, alpha=0.2, color='gray', label='Feasible Region')
plt.plot(value(x1), value(x2), 'ro')  # Optimal solution point
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Feasible Region and Optimal Solution')
plt.legend()
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlim(0, 4)
plt.ylim(0, 4)
plt.show()