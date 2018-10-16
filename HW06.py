import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sc

gamma = 0.9


def confidenceIntervalLength1st(sample_size):
    sample = np.random.standard_normal(sample_size)
    sum_of_squares = sum(map(lambda x: x * x, sample))
    greater_quantile = sc.chi2.ppf((1 + gamma) / 2, sample_size)
    less_quantile = sc.chi2.ppf((1 - gamma) / 2, sample_size)
    return sum_of_squares * (1 / less_quantile - 1 / greater_quantile)


def conductFirstExperiment():
    data_x = []
    data_y = []
    max_sample_size = 1000
    for sample_size in range(100, max_sample_size):
        data_x.append(sample_size)
        data_y.append(confidenceIntervalLength1st(sample_size))
    plt.subplot(211)
    plt.title("First Statistics")
    plt.plot(data_x, data_y)
    plt.ylabel("Confidence Interval Length")
    plt.xlabel("Sample Size")


def confidenceIntervalLength2st(sample_size):
    sample = np.random.standard_normal(sample_size)
    square_of_sum = (sum(sample) / sample_size)**2
    greater_quantile = sc.norm.ppf((3 + gamma) / 4)**2
    less_quantile = sc.norm.ppf((3 - gamma) / 4)**2
    return sample_size * square_of_sum * (1 / less_quantile - 1 / greater_quantile)


def conductSecondExperiment():
    data_x = []
    data_y = []
    max_sample_size = 1000
    for sample_size in range(100, max_sample_size):
        data_x.append(sample_size)
        data_y.append(confidenceIntervalLength2st(sample_size))
    plt.subplot(212)
    plt.title("Second Statistics")
    plt.plot(data_x, data_y)
    plt.ylabel("Confidence Interval Length")
    plt.xlabel("Sample Size")


def main():
    plt.figure(1)
    conductFirstExperiment()
    conductSecondExperiment()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
