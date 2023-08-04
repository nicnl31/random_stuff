import numpy as np


def gradient_vector(
        X: np.ndarray,
        mu: float=0.1
) -> np.ndarray:
    """
    Calculates the gradient vector based on a function.
    Parameters
    ----------
    X: array of length (N, )
    mu: regularisation parameter

    Returns
    -------
    The gradient vector.
    """
    # Get the dimension of X
    dimension = len(X)

    # Initiate an empty gradient vector with the same length as X
    grad_X = np.zeros(shape=dimension)

    # Update the gradient vector according to f(X)
    grad_X[0] = 1/16 * (2 * X[0] + 2 * (X[0] - X[1]) - 2) + mu * np.linalg.norm(X, ord=1) * X[0]/abs(X[0])
    print(grad_X[0])
    grad_X[-1] = 1/16 * (-2 * (X[-2] - X[-1])) + mu * np.linalg.norm(X, ord=1) * X[-1]/abs(X[-1])
    print(grad_X[-1])
    for i in range(1, dimension-1):
        grad_X[i] = -2 * (X[i-1] - X[i]) + 2 * (X[i] - X[i+1]) + mu * np.linalg.norm(X, ord=1) * X[i]/abs(X[i])

    return grad_X


def run_gradient_descent(
        X: np.ndarray,
        alpha: float=.5,
        n: int=50,
        mu: float=.1
) -> np.ndarray:
    """
    Runs the gradient descent algorithm.
    Parameters
    ----------
    X: the input vector
    alpha: learning rate
    n: number of iterations
    mu: regularisation parameter

    Returns
    -------
    The updated vector.

    """
    for i in range(n):
        X -= alpha * gradient_vector(X, mu)
    return X


vec = 5 * np.ones(50)
print(run_gradient_descent(vec))

# Result:
# [ 1.72584348e+24 -6.02780114e+24  7.77201481e+24 -8.47880688e+24
#   8.76358632e+24 -8.87451943e+24  8.90940276e+24 -8.90105200e+24
#   8.84571438e+24 -8.69930408e+24  8.33823736e+24 -7.45081142e+24
#   5.26446163e+24  1.29111961e+23  2.19545174e+24  1.36960195e+24
#   1.69596724e+24  1.56921379e+24  1.61723303e+24  1.59963617e+24
#   1.60582128e+24  1.60375155e+24  1.60440766e+24  1.60421071e+24
#   1.60426706e+24  1.60425146e+24  1.60425573e+24  1.60425455e+24
#   1.60425488e+24  1.60425479e+24  1.60425482e+24  1.60425481e+24
#   1.60425481e+24  1.60425481e+24  1.60425481e+24  1.60425481e+24
#   1.60425481e+24  1.60425481e+24  1.60425481e+24  1.60425481e+24
#   1.60425481e+24  1.60425481e+24  1.60425481e+24  1.60425481e+24
#   1.60425481e+24  1.60425481e+24  1.60425481e+24  1.60425481e+24
#   1.60425481e+24  1.60425481e+24]
