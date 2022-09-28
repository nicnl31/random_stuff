import numpy as np
from matplotlib import pyplot as plt


def create_data_points(time, zeta, omega_n, omega_d, initial, alpha):
    """
    Creates arrays of data points from solution.

    Parameters
    ----------
    time: array of time of interest
    zeta: damping ratio
    omega_n: natural frequency
    omega_d: damped frequency
    initial: initial condition, x_0
    alpha: phase lag

    Returns
    -------
    solution: solution behaviour from time 0.0 to 5.0

    """
    solution = initial * np.exp(-zeta * omega_n * time) * np.cos(omega_d * time - alpha)
    return solution


def plot(zeta, time, omega_n, initial, alpha):
    """
    Plot damped responses according to model specifications.
    Parameters
    ----------
    zeta: damping ratio
    time: array of time of interest
    omega_n: natural frequency
    initial: initial condition, x_0
    alpha: phase lag

    Returns
    -------
    Plots of solution behaviours according to model specifications.
    """
    fig, axs = plt.subplots(2)
    plt.subplots_adjust(hspace=.5)
    fig.suptitle('DAMPED RESPONSES')
    for i in range(len(zeta)):
        for j in range(len(omega_n)):
            omega_d = omega_n[j] * np.sqrt(1 - zeta[i] ** 2)
            axs[i].plot(
                time,
                create_data_points(time, zeta[i], omega_n[j], omega_d, initial, alpha),
                label=f'omega_n = {omega_n[j]}'
            )
        axs[i].legend(loc='upper right')
        axs[i].set_title(f'Damping ratio = {zeta[i]}')
        axs[i].set_xlabel('Time (sec)')
        axs[i].set_ylabel('Response (cm)')
    plt.show()


if __name__ == '__main__':
    time = np.arange(0, 5.05, 0.05)
    zeta = np.array([.1, .5])
    omega_n = np.array([10, 5])
    alpha = 0
    x_0 = 1.0
    plot(zeta, time, omega_n, x_0, alpha)
