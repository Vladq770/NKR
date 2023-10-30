import math
import numpy as np


def coefficient(n):
    if n == 0:
        return 10*np.sqrt(2)/3
    if n == 1:
        return 0
    if n == 2:
        return (20/3)*np.sqrt(2/5)


def func_lejandro(n, x):
    if n == 0:
        return 1
    if n == 1:
        return np.cos(x)
    if n == 2:
        return (1/2)*(3*(np.cos(x)**2)-1)


def solve_analytical(coefs):

    def sum_row(tetta, t):
        sum_rw = 0
        for i in range(3):
            sum_rw += coefficient(i) * np.exp(-(i * (i + 1) * kc * t) / (c * R ** 2)) * np.sqrt(
                (2 * i + 1) / 2) * func_lejandro(i, tetta)
        return sum_rw

    def create2(tetta, lin_t):
        w = []
        for i in lin_t:
            w.append(sum_row(tetta, i))
        return w

    def gr_tetta(t, lin_tetta):
        w = []
        for i in lin_tetta:
            w.append(sum_row(i, t))
        return w

    R = coefs[0]
    L = coefs[1]
    T = coefs[2]
    kc = coefs[3]
    c = coefs[4]
    K = coefs[5]
    I = coefs[6]
    sk = coefs[7]
    si = coefs[8]
    ht = T / K
    htetta = np.pi / I
    type_chart = coefs[9]
    lin_t = [i * ht for i in range(K + 1)]
    lin_tetta = [i * htetta for i in range(I + 1)]
    res_a = np.zeros((K + 1, I + 1))
    if type_chart == 1:
        sk *= 64
        row = np.array(gr_tetta(ht * sk, lin_tetta))
        res_a[sk, :] = row
        si *= 8
        col = np.array(create2(htetta * si, lin_t))
        res_a[:, si] = col
        return res_a
    for i in range(K + 1):
        row = np.array(gr_tetta(ht * i, lin_tetta))
        res_a[i, :] = row
    return res_a




