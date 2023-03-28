import tkinter
from tkinter import *
import main


def windows():
    """Создает Окно с одним полем ввода, кнокой"""
    def button_click1():
        """Обработка нажатия кнопки
        Передаёт в MAIN PARSER url поиск-запрса"""
        url_click = url_entry.get()
        main.parser(url=url_click)

    """основное окно"""
    top = tkinter.Tk()
    top.resizable(False, False)
    top.title("AvitoParser")
    top.geometry("720x150")

    """Элементы при старте"""
    # Текст
    lbl1 = Label(top, text="Вставь ссылку", font=20)
    lbl1.grid(row=0, column=0)
    top.grid_columnconfigure(0, minsize=200)

    # Поле ввода
    url_entry = tkinter.Entry(top)
    url_entry.grid(row=0, column=1, sticky=EW, pady=10)
    top.grid_columnconfigure(1, minsize=400)

    # Кнопка
    btn_start = tkinter.Button(top, text="Start", command=button_click1)
    btn_start.grid(row=0, column=2, padx=5, sticky=EW)
    top.grid_columnconfigure(2, minsize=100)

    top.mainloop()



def result_price(average, fair):
    """Принимает значение из MAIN AVERAGE_PRICE
    Выводит в Label"""

    average_lbl = Label(text=f"{average} Средняя цена за м2 (весь рынок)", font=18)
    average_lbl.grid(row=1, column=1)

    fair_lbl = Label(text=f"{fair} Средневзвешенная цена за м2", font=18)
    fair_lbl.grid(row=2, column=1)


