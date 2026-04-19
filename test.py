# Угадай число

import tkinter as tk
from tkinter import messagebox
import random

window = tk.Tk()
window.title("Угадай число")
window.geometry("400x350")
window.resizable(False, False)

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
            mesage_label.config(text="Больше!")
        elif guess > secret_number:
            mesage_label.config(text="Меньше!")
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

window.mainloop()
