import tkinter as tk


def 홀짝():
    result = int(entry.get()) % 2
    if result:
        result = "홀"
    else:
        result = "짝"
    result_label.configure(text=result)


win = tk.Tk()

input_label = tk.Label(win, text="숫자를 입력하세요.")
input_label.grid(row=0, column=0)

entry = tk.Entry(win)
entry.grid(row=1, column=0)

button = tk.Button(win, text="클릭", command=홀짝)
button.grid(row=2, column=0)

result_label = tk.Label(win, text="")
result_label.grid(row=3, column=0)

win.mainloop()