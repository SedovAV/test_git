# Угадай число

import tkinter as tk
from tkinter import messagebox
import random

# Глобальные переменные
secret_number = 0
attempts = 0
max_attempts = 10

def new_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    attempts_label.config(text=f"Попыток: {attempts} из {max_attempts}")
    message_label.config(text="Я загадал число от 1 до 100")
    entry.delete(0, tk.END)
    guess_button.config(state=tk.NORMAL)
    entry.config(state=tk.NORMAL)

def check_guess():
    global attempts
    try:
        guess = int(entry.get())
        attempts += 1
        attempts_label.config(text=f"Попыток: {attempts} из {max_attempts}")

        if guess < secret_number:
            message_label.config(text="Больше!")
        elif guess > secret_number:
            message_label.config(text="Меньше!")
        else:
            messagebox.showinfo("Победа!", f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток")
            guess_button.config(state=tk.DISABLED)
            entry.config(state=tk.DISABLED)

        if attempts >= max_attempts:
            messagebox.showinfo("Поражение!", f"Попытки закончились! Было загадано число {secret_number}")
            guess_button.config(state=tk.DISABLED)
            entry.config(state=tk.DISABLED)
        else:
            entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите целое число!")
        entry.delete(0, tk.END)

# Создание главного окна
window = tk.Tk()
window.title("Угадай число")
window.geometry("400x350")
window.resizable(False, False)

# Заголовок
title_label = tk.Label(window, text="Игра 'Угадай число!'", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# Описание
desc_label = tk.Label(window, text="Компьютер загадал число от 1 до 100\nПопробуйте угадать это число\nУ вас есть 10 попыток\nУдачи!", font=("Arial", 10))
desc_label.pack(pady=5)

# Поле ввода
entry = tk.Entry(window, font=("Arial", 14), justify="center", width=10)
entry.pack(pady=10)

# Кнопка проверки
guess_button = tk.Button(window, text="Проверить", font=("Arial", 12), bg="green", fg="black", width=15, command=check_guess)
guess_button.pack(pady=5)

# Статусная информация
attempts_label = tk.Label(window, text=f"Попыток 0 из {max_attempts}", font=("Arial", 11))
attempts_label.pack(pady=10)

message_label = tk.Label(window, text="Нажми 'Новая игра', чтобы начать", font=("Arial", 10), fg="blue")
message_label.pack(pady=10)

# Кнопка новой игры
new_button = tk.Button(window, text="Новая игра", font=("Arial", 12), bg="blue", fg="black", width=15, command=new_game)
new_button.pack(pady=10)

window.mainloop()
