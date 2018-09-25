import numpy as np
import matplotlib.pyplot as plt


def k_moment(data, k):
    moment = 0.0
    for elem in data:
        moment += elem ** k
    return moment / len(data)


def main():
    parameter = 10
    data_x = []
    data_y = []
    k_max = 100
    for k in range(1, k_max):
        mse = 0.0
        number_of_experiments = 100
        for i in range(0, number_of_experiments):
            sample = np.random.uniform(0, parameter, 1000)
            # get_parameter = lambda k, moment_value: ((k + 1) * moment_value) ** (1.0 / k)
            moment_value = k_moment(sample, k + 0.0)
            estimated_parameter = ((k + 1) * moment_value) ** (1.0 / k)
            mse += (estimated_parameter - parameter) ** 2
        mse /= number_of_experiments
        data_x.append(k)
        data_y.append(mse)
    plt.plot(data_x, data_y)
    plt.show()


if __name__ == "__main__":
    main()
