import numpy as np
from sklearn.neighbors import KernelDensity


def _calculate_quasi_potential(z):
    return -np.log(z)


def kde2D(x, y, bandwidth, xbins=80j, ybins=80j, **kwargs):
    # create grid of sample locations (default: 100x100)
    xx, yy = np.mgrid[x.min():x.max():xbins,
             y.min():y.max():ybins]

    xy_sample = np.vstack([yy.ravel(), xx.ravel()]).T
    xy_train = np.vstack([y, x]).T

    kde_skl = KernelDensity(bandwidth=bandwidth, **kwargs)
    kde_skl.fit(xy_train)

    # score_samples() returns the log-likelihood of the samples
    z = np.exp(kde_skl.score_samples(xy_sample))
    qp = _calculate_quasi_potential(z)
    return xx, yy, np.reshape(z, xx.shape), np.reshape(qp, xx.shape)
