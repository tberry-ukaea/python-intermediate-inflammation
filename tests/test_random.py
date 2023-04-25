from random import normalvariate
import numpy as np


def test_normalvariate():
    mu = 0.0
    sigma = 1.0
    samples = 1000000
    np.testing.assert_almost_equal(normalvariate(mu, sigma)/samples, mu,
                                   decimal=2)


def test_np_random():
    mu = 0.0
    sigma = 1.0
    samples = 1000000
    np.testing.assert_almost_equal(np.mean(np.random.normal(mu, sigma,
                                                            samples)),
                                   mu, decimal=2)
