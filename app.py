from flask import Flask, render_template, request
from pulp import *
import io
import base64
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    model = pulp.LpProblem('linear_programming', LpMaximize)
    solver = getSolver('PULP_CBC_CMD') 
    x1 = LpVariable('x1', lowBound = 0, cat = 'continuous') 
    x2 = LpVariable('x2', lowBound = 0, cat = 'continuous')

    z1 = int(request.form['z1'])
    z2 = int(request.form['z2'])
    a1 = int(request.form['a1'])
    b1 = int(request.form['b1'])
    c1 = int(request.form['c1'])
    a2 = int(request.form['a2'])
    b2 = int(request.form['b2'])
    c2 = int(request.form['c2'])
    model += z1*x1 + z2*x2
    model += a1*x1 + b1*x2 <= c1 
    model += a2*x1 + b2*x2 <= c2
    results = model.solve(solver=solver)
    if LpStatus[results] == 'Optimal': print('The solution is optimal.')
    print(f'Objective value: z* = {value(model.objective)}')
    print(f'Solution: x1* = {value(x1)}, x2* = {value(x2)}')
    # Plotting the feasible region and constraints
    x_vals = np.linspace(0, 10, 400)
    y1 = (c1 - a1 * x_vals) / b1  
    y2 = (c2 - a2 * x_vals) / b2
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

    # Save the plot as a PNG image
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    img.close()

    

    
    return render_template('result.html', plot_url=plot_url)  # Return the result to be displayed

if __name__ == "__main__":
    app.run(debug=True)
