import numpy as np


def solve_scheme(coefs):
    def psi(teta):
        return 10 * np.cos(teta) ** 2

    def scheme(K, I, ht, hteta):
        res = np.zeros((K + 1, I + 1))
        for i in range(I + 1):
            res[0, i] = psi(i * hteta)
        for k in range(K):
            for i in range(1, I):
                res[k + 1, i] = res[k, i] + kc * ht / (R ** 2 * c) * (
                            (res[k, i - 1] - 2 * res[k, i] + res[k, i + 1]) / hteta ** 2 + (
                                res[k, i + 1] - res[k, i - 1]) / (np.tan(i * hteta) * hteta * 2))
            res[k + 1, 0] = res[k, 0] + 4 * kc * ht / (R ** 2 * c) * ((res[k, 1] - res[k, 0]) / hteta ** 2)
            res[k + 1, I] = res[k, I] + 4 * kc * ht / (R ** 2 * c) * ((res[k, I - 1] - res[k, I]) / hteta ** 2)
        return res
    R = coefs[0]
    L = coefs[1]
    T = coefs[2]
    kc = coefs[3]
    c = coefs[4]
    K0 = coefs[5]
    I0 = coefs[6]
    sk = coefs[7]
    si = coefs[8]
    type_chart = coefs[9]
    ht0 = T / K0
    htetta0 = np.pi / I0
    return scheme(K0, I0, ht0, htetta0)
