import numpy as np
import pandas as pd

def composite_trapezoid_rule(func, a, b, h):
    """
    Numerical approximation of an integral using Composite Trapezoid Rule.

    Parameters:
        func (function): The integrand function.
        a (float): Lower limit of integration.
        b (float): Upper limit of integration.
        h (float): Step size.

    Returns:
        float: Approximation of the integral.
    """
    n = int((b - a) / h)
    x = np.linspace(a, b, n+1)
    y = func(x)
    return h * (0.5*y[0] + 0.5*y[-1] + np.sum(y[1:-1]))

def composite_simpsons_rule(func, a, b, h):
    """
    Numerical approximation of an integral using Composite Simpson's Rule.

    Parameters:
        func (function): The integrand function.
        a (float): Lower limit of integration.
        b (float): Upper limit of integration.
        h (float): Step size.

    Returns:
        float: Approximation of the integral.
    """
    n = int((b - a) / h)
    if n % 2 != 0:
        n += 1  # Ensure even number of subintervals
    x = np.linspace(a, b, n+1)
    y = func(x)
    return h / 3 * (y[0] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-2:2]) + y[-1])

def composite_gaussian_quadrature(func, a, b):
    """
    Numerical approximation of an integral using Composite Gaussian Quadrature Rule with two points.

    Parameters:
        func (function): The integrand function.
        a (float): Lower limit of integration.
        b (float): Upper limit of integration.

    Returns:
        float: Approximation of the integral.
    """
    x1 = -np.sqrt(1/3)
    x2 = np.sqrt(1/3)
    x_values = [(b - a) / 2 * x1 + (a + b) / 2, (b - a) / 2 * x2 + (a + b) / 2]
    w1 = w2 = 1

    integral_approx = ((b - a) / 2) * (w1 * func(x_values[0]) + w2 * func(x_values[1]))
    return integral_approx

# Integration limits
a = 0
b = 1

# Step size
h = 0.05

# Function 

def func(x):
    return x * np.exp(-x)

# Approximate the integral using Composite Trapezoid Rule
approx_trapezoid = composite_trapezoid_rule(func, a, b, h)
print("Approximation using Composite Trapezoid Rule:", approx_trapezoid)

# Approximate the integral using Composite Simpson's Rule
approx_simpson = composite_simpsons_rule(func, a, b, h)
print("Approximation using Composite Simpson's Rule:", approx_simpson)

# Approximate the integral using Composite Gaussian Quadrature Rule with two points
approx_gaussian = composite_gaussian_quadrature(func, a, b)
print("Approximation using Composite Gaussian Quadrature Rule:", approx_gaussian)

# Exact integral calculation

exact_integral = -2 * np.exp(-1) + 1 #exact integral is -2e^-1 + 1
print("Exact integral:", exact_integral)

#to find which algorithm has worst estimate and which algorithm has best estimate, sort |exact - estimate|

error_trapezoid = abs(approx_trapezoid - exact_integral)
error_simpson = abs(approx_simpson - exact_integral)
error_gaussian = abs(approx_gaussian - exact_integral)

print("Absolute error for Composite Trapezoid Rule:", error_trapezoid)
print("Absolute error for Composite Simpson's Rule:", error_simpson)
print("Absolute error for Composite Gaussian Quadrature Rule:", error_gaussian)

estimates = [approx_trapezoid, approx_simpson, approx_gaussian]
errors = [error_trapezoid, error_simpson, error_gaussian]
method_names = ['Composite Trapezoid Rule', 'Composite Simpson\'s Rule', 'Composite Gaussian Quadrature Rule']

# Create DataFrame
df = pd.DataFrame({
    'Method': method_names,
    'Estimate': estimates,
    'Absolute Error': errors
})

# Print the DataFrame
df_sorted = df.sort_values(by='Absolute Error')

print(df_sorted)

best_estimate = df_sorted.head(1)
worst_estimate = df_sorted.tail(1)

print("The best estimate is " + best_estimate['Method'].values[0] + " with an absolute error of " + str(best_estimate['Absolute Error'].values[0]))
print("The worst estimate is " + worst_estimate['Method'].values[0] + " with an absolute error of " + str(worst_estimate['Absolute Error'].values[0]))
