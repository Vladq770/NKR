import tkinter
import tkinter.messagebox as mb

from chart import chart


type_chart = {'Погрешность': 0, 'Увеличение K, I': 1, 'Разные слои': 2}
def enter(frames: list, root):
    coefficients = []
    for i in range(len(frames) - 1):
        try:
            x = float(frames[i].get())
            print(x, type(x))
        except ValueError:
            msg = f'Неверный ввод в строке {i + 1}'
            mb.showerror("Ошибка", msg)
            return
        coefficients.append(x)
    coefficients.append(type_chart[frames[9].get()])
    print('TYPE CHART', coefficients[9])
    for i in range(len(coefficients)):
        if i in (0, 1, 3, 4, 5, 6, 7, 8) and coefficients[i] < 0:
            msg = f'Неверный ввод в строке {i + 1} (необходимо положительное число)'
            mb.showerror("Ошибка", msg)
            return
    for i in range(5, 9):
        coefficients[i] = int(coefficients[i])
    newWindow = tkinter.Toplevel(root)
    newWindow.grab_set()
    chart(coefficients, newWindow)
