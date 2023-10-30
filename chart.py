import numpy as np
import matplotlib as mpl
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
import matplotlib.pyplot as plt
from analytical import solve_analytical
from explicit_scheme import solve_scheme


mpl.use('TkAgg')

def chart(coefs: list, window):
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
    if type_chart == 0:
        res_a = solve_analytical(coefs)
        res_s = solve_scheme(coefs)
        lin_t = [i * ht0 for i in range(K0 + 1)]
        lin_tetta = [i * htetta0 for i in range(I0 + 1)]
        plt0(window, lin_t, lin_tetta, si, sk, ht0, htetta0, res_a, res_s)
    elif type_chart == 1:
        I_factor = 2
        K_factor = 4
        K_arr = [K0]
        I_arr = [I0]
        for i in range(3):
            K_arr.append(K_arr[-1] * K_factor)
            I_arr.append(I_arr[-1] * I_factor)
        schema_solves = []
        for i in range(len(K_arr)):
            coefs[5] = K_arr[i]
            coefs[6] = I_arr[i]
            schema_solves.append(solve_scheme(coefs))
        res_a = solve_analytical(coefs)
        lin_t = []
        lin_tetta = []
        for i in range(len(K_arr)):
            ht_i = T / K_arr[i]
            htetta_i = np.pi / I_arr[i]
            lin_t.append([j * ht_i for j in range(K_arr[i] + 1)])
            lin_tetta.append([j * htetta_i for j in range(I_arr[i] + 1)])
        plt2(window, lin_t, lin_tetta, si, sk, ht0, htetta0, res_a, schema_solves, K_factor, I_factor, K_arr, I_arr)
    else:
        lin_t = [i * ht0 for i in range(K0 + 1)]
        lin_tetta = [i * htetta0 for i in range(I0 + 1)]
        res_s = solve_scheme(coefs)
        plt1(window, lin_t, lin_tetta, ht0, htetta0, res_s, I0, K0)


def plt0(window, lin_t, lin_tetta, si, sk, ht, htetta, res_a, res_s):
    fig = Figure(figsize=(10, 5), dpi=100)
    colors = ["red", "blue", "green", "pink", "olive", "lime", "black", "orange", "peru", "aqua"]
    plot1 = fig.add_subplot(1, 2, 1)
    plot2 = fig.add_subplot(1, 2, 2)
    max_e = abs(res_a - res_s).max()
    plot1.set_title(f'Погрешность = {max_e}')
    plot2.set_xlabel('t, с', fontsize=14)
    plot2.set_ylabel('Температура, °C', fontsize=14)
    plot1.set_xlabel('tetta, rad', fontsize=14)
    plot1.set_ylabel('Температура, °C', fontsize=14)
    plot2.plot(lin_t, res_a[:, si], color=colors[0], label=f'tetta={round(si * htetta, 2)}')
    plot1.plot(lin_tetta, res_a[sk, :], color=colors[0], label=f't={round(sk * ht, 2)}')
    plot2.plot(lin_t, res_s[:, si], color=colors[2], label=f'tetta={round(si * htetta, 2)} (S)')
    plot1.plot(lin_tetta, res_s[sk, :], color=colors[2], label=f't={round(sk * ht, 2)} (S)')
    plot1.legend(fontsize="small")
    plot2.legend(fontsize="small")

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()

    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()

    canvas.get_tk_widget().pack()


def plt1(window, lin_t, lin_tetta, ht, htetta, res_s, I, K):
    partition = [0, 0.01, 0.025, 0.1, 0.2, 0.375, 1]
    fig = Figure(figsize=(10, 5), dpi=100)
    colors = ["red", "blue", "green", "pink", "olive", "lime", "black", "orange", "peru", "aqua"]
    plot1 = fig.add_subplot(1, 2, 1)
    plot2 = fig.add_subplot(1, 2, 2)
    plot2.set_xlabel('t, с', fontsize=14)
    plot2.set_ylabel('Температура, °C', fontsize=14)
    plot1.set_xlabel('tetta, rad', fontsize=14)
    plot1.set_ylabel('Температура, °C', fontsize=14)
    i_part = I // 6
    for ind, i in enumerate(partition):
        cur_k = int(i * K)
        cur_i = ind * i_part
        if ind == 6:
            cur_i = I
        plot2.plot(lin_t, res_s[:, cur_i], color=colors[ind], label=f'tetta={round(cur_i * htetta, 2)} (i={cur_i})')
        plot1.plot(lin_tetta, res_s[cur_k, :], color=colors[ind], label=f't={round(cur_k * ht, 2)} (k={cur_k})')
    plot1.legend(fontsize="small")
    plot2.legend(fontsize="small")

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()

    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()

    canvas.get_tk_widget().pack()


def plt2(window, lin_t, lin_tetta, si, sk, ht, htetta, res_a, scheme_solves, K_factor, I_factor, K_arr, I_arr):
    fig = Figure(figsize=(10, 5), dpi=100)
    colors = ["red", "blue", "green", "pink", "olive", "lime", "black", "orange", "peru", "aqua"]
    plot1 = fig.add_subplot(1, 2, 1)
    plot2 = fig.add_subplot(1, 2, 2)
    plot2.set_xlabel('t, с', fontsize=14)
    plot2.set_ylabel('Температура, °C', fontsize=14)
    plot1.set_xlabel('tetta, rad', fontsize=14)
    plot1.set_ylabel('Температура, °C', fontsize=14)
    i_last = si * I_factor ** 3
    k_last = sk * K_factor ** 3
    plot2.plot(lin_t[-1], res_a[:, i_last], color=colors[0], label=f'tetta={round(si * htetta, 2)}')
    plot1.plot(lin_tetta[-1], res_a[k_last, :], color=colors[0], label=f't={round(sk * ht, 2)}')
    for i in range(len(lin_t)):
        plot2.plot(lin_t[i], scheme_solves[i][:, si * I_factor ** i], color=colors[i + 1], label=f'K={K_arr[i]}, I={I_arr[i]}')
        plot1.plot(lin_tetta[i], scheme_solves[i][sk * K_factor ** i, :], color=colors[i + 1], label=f'K={K_arr[i]}, I={I_arr[i]}')
    plot1.legend(fontsize="small")
    plot2.legend(fontsize="small")

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()

    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()

    canvas.get_tk_widget().pack()
