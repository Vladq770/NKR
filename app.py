from tkinter import *
from tkinter import ttk
from label_frame import LabelFr
from func_buttons import enter


root = Tk(baseName="123")
root.title("Явная схема")
root.configure(bg='palegreen')
font = ('Times 14')
s = ttk.Style()
s.configure('My.TFrame', background='palegreen')
frm = ttk.Frame(root, padding=10, style='My.TFrame')
frm.grid(column=0, row=0)
frm_buttons = ttk.Frame(root, padding=10)
frm_buttons.grid(column=1, row=0, rowspan=2)
label_R = LabelFr("R", frm, 0, 0, font, 6)
label_L = LabelFr("L", frm, 0, 1, font, 0.1)
label_T = LabelFr("T", frm, 0, 4, font, 200)
label_k = LabelFr("k", frm, 0, 5, font, 0.59)
label_c = LabelFr("c", frm, 0, 6, font, 1.65)
label_K = LabelFr("K", frm, 0, 9, font, 1000)
label_I = LabelFr("I", frm, 0, 10, font, 20)
label_hrk = LabelFr("Слой k", frm, 0, 11, font, 1)
label_hti = LabelFr("Слой i", frm, 0, 12, font, 1)
Button(frm, text="Построить", font=font, command=lambda : enter(labels_fr, root)).grid(column=0, row=15)
label_frame_chart = LabelFrame(frm)
label_chart = Label(label_frame_chart, text="Тип графика", width=15, font=('Times 14'))
label_chart.grid(column=0, row=0)
label_frame_chart.grid(column=0, row=14, pady=5, padx=10)
type_chart = ('Погрешность', 'Увеличение K, I', 'Разные слои')
var_chart = StringVar(value=type_chart[0])
combobox_chart = ttk.Combobox(label_frame_chart, textvariable=var_chart)
combobox_chart['values'] = type_chart
combobox_chart['state'] = 'readonly'
combobox_chart.grid(column=1, row=0, padx=5)

labels_fr = [label_R, label_L, label_T, label_k, label_c, label_K, label_I,
             label_hrk, label_hti, combobox_chart]

root.mainloop()
